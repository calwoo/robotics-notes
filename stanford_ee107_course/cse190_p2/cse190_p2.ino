#include <sam.h>
// #include "bma250.h"
// #include "i2c.h"


/* === DO NOT REMOVE: Initialize C library === */
extern "C" void __libc_init_array(void);

extern "C" {
  int _write(int fd, const void *buf, size_t count) {
    // STDOUT
    if (fd == 1)
      SerialUSB.write((char*)buf, count);
    return 0;
  }
}

int main(void) {  
  /* ==== DO NOT REMOVE: USB configuration ==== */
  init();
  __libc_init_array();
  USBDevice.init();
  USBDevice.attach();
  /* =========================================== */

  i2c_init();
  bma250_init();

  int16_t acc_x = 0;
  int16_t acc_y = 0;
  int16_t acc_z = 0;
  
  /* === Main Loop === */
  while (1) {
    bma250_read_xyz(&acc_x, &acc_y, &acc_z);

    SerialUSB.print("acc_x: ");
    SerialUSB.print(acc_x);
    SerialUSB.print(" - acc_y: ");
    SerialUSB.print(acc_y);
    SerialUSB.print(" - acc_z: ");
    SerialUSB.print(acc_z);
    SerialUSB.print("\n");
    delay(1000);
  }
  
  return 0;
}
