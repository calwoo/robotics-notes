#include "i2c.h"
#include <sam.h>


void i2c_init(void) {
  /* Configure and enable the SERCOM I2C peripheral to communicate in master mode, 
     at a standard BAUD RATE (e.g., 400 kHz or less). This also should configure the 
     appropriate pins on the MCU so they are connected to the correct I2C peripheral 
     rather than operating as GPIO pins. */

  // enable clocks
  GCLK->CLKCTRL.reg = (GCLK_CLKCTRL_ID(GCM_SERCOM3_CORE) | GCLK_CLKCTRL_ID (SERCOM3_GCLK_ID_SLOW) | GCLK_CLKCTRL_GEN_GCLK0 | GCLK_CLKCTRL_CLKEN);
  while (GCLK->STATUS.reg & GCLK_STATUS_SYNCBUSY);

  // set up pins
  PORT->Group[0].PINCFG[22].reg |= (PORT_PINCFG_PMUXEN | PORT_PINCFG_INEN | PORT_PINCFG_PULLEN);
  PORT->Group[0].PINCFG[23].reg |= (PORT_PINCFG_PMUXEN | PORT_PINCFG_INEN | PORT_PINCFG_PULLEN);
  PORT->Group[0].PMUX[11].reg |= (PORT_PMUX_PMUXE_C | PORT_PMUX_PMUXO_C);

  // enable interrupts
  NVIC_EnableIRQ(SERCOM3_IRQn);
  NVIC_SetPriority(SERCOM3_IRQn, SERCOM_NVIC_PRIORITY);

  // reset i2c registers
  SERCOM3->I2CM.CTRLA.bit.SWRST = 1;
  while (SERCOM3->I2CM.CTRLA.bit.SWRST || SERCOM3->I2CM.SYNCBUSY.bit.SWRST);

  // initialize i2c
  SERCOM3->I2CM.CTRLA.reg = SERCOM_I2CM_CTRLA_MODE(I2C_MASTER_OPERATION);
  SERCOM3->I2CM.BAUD.reg = SERCOM_I2CM_BAUD_BAUD(48);

  // enable i2c
  SERCOM3->I2CM.CTRLA.bit.ENABLE = 1;
  while (SERCOM3->I2CM.SYNCBUSY.bit.ENABLE != 0);
  SERCOM3->I2CM.STATUS.bit.BUSSTATE = 1;
  while (SERCOM3->I2CM.SYNCBUSY.bit.SYSOP != 0);
  // now bus is in idle state
}

uint8_t i2c_transaction(uint8_t address, uint8_t dir, uint8_t* data, uint8_t len) {
  /* Perform a transaction to Write/Read bytes to/from the I2C peripheral to a slave 
     with the address specified as a parameter. If the dir parameter is 0 it is 
     writing to a slave,  if it is 1 it is reading from the slave. This is a blocking 
     function, in that it should return only when the entire transaction has completed. */

  // why not 0x18???
  uint8_t addr = (0x19 << 1) | dir;
  // write address
  SERCOM3->I2CM.ADDR.reg = addr;

  if (dir == 0) { // write mode
    // wait for acknowledgment from slave
    while (0 == (SERCOM3->I2CM.INTFLAG.reg & SERCOM_I2CM_INTFLAG_MB));
    if (SERCOM3->I2CM.STATUS.reg & SERCOM_I2CM_STATUS_RXNACK) {
        SerialUSB.println("RXNACK received during address write!");
        // issue stop condition
        SERCOM3->I2CM.CTRLB.reg |= SERCOM_I2CM_CTRLB_CMD(3);
        return 0;
      }

    for (int i = 0; i < len; i++) {
      SERCOM3->I2CM.DATA.bit.DATA = data[i];

      while (0 == (SERCOM3->I2CM.INTFLAG.reg & SERCOM_I2CM_INTFLAG_MB));
      // check for RXNACK failure
      if (SERCOM3->I2CM.STATUS.reg & SERCOM_I2CM_STATUS_RXNACK) {
        SerialUSB.println("RXNACK received during data write!");
        // issue stop condition
        SERCOM3->I2CM.CTRLB.reg |= SERCOM_I2CM_CTRLB_CMD(3);
        return 0;
      }
    }

    // issue stop condition
    SERCOM3->I2CM.CTRLB.reg |= SERCOM_I2CM_CTRLB_CMD(3);
  } 
  else { // read mode
    // wait for acknowledgment from slave
    while (0 == (SERCOM3->I2CM.INTFLAG.reg & SERCOM_I2CM_INTFLAG_SB));
    if (SERCOM3->I2CM.STATUS.reg & SERCOM_I2CM_STATUS_RXNACK) {
      SerialUSB.println("RXNACK received during read address!");
      // issue stop condition
      SERCOM3->I2CM.CTRLB.reg |= SERCOM_I2CM_CTRLB_CMD(3);
      return 0;
    }

    // set CTRLB.ACKACT to 0 (send ACK)
    SERCOM3->I2CM.CTRLB.reg &= ~SERCOM_I2CM_CTRLB_ACKACT;

    for (int i = 0; i < len - 1; i++) {
      data[i] = SERCOM3->I2CM.DATA.reg;
      while (0 == (SERCOM3->I2CM.INTFLAG.reg & SERCOM_I2CM_INTFLAG_SB));
    }

    if (len > 0) {
      // on last bit, send NACK after data is sent
      SERCOM3->I2CM.CTRLB.reg |= SERCOM_I2CM_CTRLB_ACKACT;
      SERCOM3->I2CM.CTRLB.reg |= SERCOM_I2CM_CTRLB_CMD(3);
      data[len - 1] = SERCOM3->I2CM.DATA.reg;
    }
  }

  return 1;
}
