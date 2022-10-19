#include <sam.h>

#include "ledcircle.h"
#include "timer.h"

/* === DO NOT REMOVE: Initialize C library === */
extern "C" void __libc_init_array(void);

void TC3_Handler(void) {
  timer3_reset();
  TC3->COUNT16.INTFLAG.bit.MC0 = 1;
}

int main(void) {  
  /* ==== DO NOT REMOVE: USB configuration ==== */
  init();
  __libc_init_array();
  USBDevice.init();
  USBDevice.attach();
  /* =========================================== */

  /* === Init Drivers === */
  timer3_init();
  ledcircle_select(0);

  int num_leds = 16;
  int led = 0;
  
  /* === Main Loop === */
  while (1) {
    for (int i = 0; i < num_leds; i++) {
      ledcircle_select(i);
      timer3_set(100);
    }
    for (int i = num_leds - 1; i > 0; i--) {
      ledcircle_select(i);
      timer3_set(100);
    }
  }
  
  return 0;
}


