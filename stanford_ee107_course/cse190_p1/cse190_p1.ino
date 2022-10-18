#include <sam.h>

#include "ledcircle.h"

/* === DO NOT REMOVE: Initialize C library === */
extern "C" void __libc_init_array(void);

int main(void) {  
  /* ==== DO NOT REMOVE: USB configuration ==== */
  init();
  __libc_init_array();
  USBDevice.init();
  USBDevice.attach();
  /* =========================================== */

  /* === Init Drivers === */
  ledcircle_select(0);

  int num_leds = 16;
  
  /* === Main Loop === */
  while (1) {
    // TODO Your implementation here
    for (int i = 0; i < num_leds; i++) {
      ledcircle_select(i);
      delay(100);
    }
    for (int i = num_leds - 1; i > 0; i--) {
      ledcircle_select(i);
      delay(100);
    }
  }
  
  return 0;
}
