#ifndef __BMA_250_H_
#define __BMA_250_H_

// default i2c address: 0011000b (0x18)
#define BMA250_I2C_ADDR 0x18
#define BMA250_REG_ACCEL_X_LSB 0x02
#define BMA250_REG_ACCEL_X_MSB 0x03
#define BMA250_REG_ACCEL_Y_LSB 0x04
#define BMA250_REG_ACCEL_Y_MSB 0x05
#define BMA250_REG_ACCEL_Z_LSB 0x06
#define BMA250_REG_ACCEL_Z_MSB 0x07
#define BMA250_REG_G_RANGE_SEL 0x0F
#define BMA250_REG_BANDWIDTH 0x10

#define BMA250_G_RANGE_PM2 0x03
#define BMA250_BANDWITH_MID 0x08

void bma250_init();
void bma250_read_xyz(int16_t* x, int16_t* y, int16_t* z);

#endif
