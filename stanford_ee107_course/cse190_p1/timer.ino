#include <sam.h>
#include "timer.h"


void timer3_init() {
  // disable, reset TC3 if on
  TC3->COUNT16.CTRLA.reg &= ~TC_CTRLA_ENABLE;
  TC3->COUNT16.CTRLA.reg = TC_CTRLA_SWRST;

  // prep for enabling
  GCLK->CLKCTRL.reg = (uint16_t) (GCLK_CLKCTRL_CLKEN | GCLK_CLKCTRL_GEN_GCLK0 | GCLK_CLKCTRL_ID(GCM_TCC2_TC3));
  while (GCLK->STATUS.bit.SYNCBUSY);

  TC3->COUNT16.CTRLA.reg |= TC_CTRLA_MODE_COUNT16;
  TC3->COUNT16.CTRLA.reg |= TC_CTRLA_WAVEGEN_MFRQ;
  TC3->COUNT16.CTRLA.reg |= TC_CTRLA_PRESCALER_DIV1024 | TC_CTRLA_ENABLE;

  // enable interrupts
  NVIC_DisableIRQ(TC3_IRQn);
  NVIC_ClearPendingIRQ(TC3_IRQn);
  NVIC_SetPriority(TC3_IRQn, 0);
  NVIC_EnableIRQ(TC3_IRQn);

  // enable the TC3 interrupt request
  TC3->COUNT16.INTENSET.bit.MC0 = 1;
}

void timer3_reset() {
  TC3->COUNT16.CTRLA.reg = TC_CTRLA_SWRST;
}

void timer3_set(uint16_t period_ms) {
  timer3_reset();
  TC3->COUNT16.CC[0].reg = (uint16_t) (SystemCoreClock / period_ms);
  TC3->COUNT16.CTRLA.reg = TC_CTRLA_ENABLE;
  while (TC3->COUNT16.STATUS.reg & TC_STATUS_SYNCBUSY);
  while (TC3->COUNT16.COUNT.reg > 0);
}
