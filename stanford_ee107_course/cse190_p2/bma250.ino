#include "bma250.h"
#include "i2c.h"
#include <sam.h>


void bma250_init(void) {
  // Configure and enable the BMA250 

  uint8_t reg = BMA250_REG_G_RANGE_SEL;
  uint8_t val = BMA250_G_RANGE_PM2;
  i2c_transaction(BMA250_I2C_ADDR, 0, &reg, (uint8_t) 1);
  i2c_transaction(BMA250_I2C_ADDR, 0, &val, (uint8_t) 1);

  reg = BMA250_REG_BANDWIDTH;
  val = BMA250_BANDWITH_MID;
  i2c_transaction(BMA250_I2C_ADDR, 0, &reg, (uint8_t) 1);
  i2c_transaction(BMA250_I2C_ADDR, 0, &val, (uint8_t) 1);
}

void bma250_read_xyz(int16_t* x, int16_t* y, int16_t* z) {
  int16_t _x = 0;
  int16_t _y = 0;
  int16_t _z = 0;

  // x accel
  uint8_t x_reg = BMA250_REG_ACCEL_X_LSB;
  i2c_transaction(BMA250_I2C_ADDR, 0, &x_reg, (uint8_t) 1);

  uint8_t return_data = 0;
  i2c_transaction(BMA250_I2C_ADDR, 1, &return_data, (uint8_t) 1);

  _x = (int16_t) return_data;

  x_reg = BMA250_REG_ACCEL_X_MSB;
  i2c_transaction(BMA250_I2C_ADDR, 0, &x_reg, (uint8_t) 1);

  return_data = 0;
  i2c_transaction(BMA250_I2C_ADDR, 1, &return_data, (uint8_t) 1);

  _x |= (return_data << 8);
  _x >>= 6;
  *x = _x;

  // y accel
  uint8_t y_reg = BMA250_REG_ACCEL_Y_LSB;
  i2c_transaction(BMA250_I2C_ADDR, 0, &y_reg, (uint8_t) 1);

  return_data = 0;
  i2c_transaction(BMA250_I2C_ADDR, 1, &return_data, (uint8_t) 1);

  _y = (int16_t) return_data;

  y_reg = BMA250_REG_ACCEL_Y_MSB;
  i2c_transaction(BMA250_I2C_ADDR, 0, &y_reg, (uint8_t) 1);

  return_data = 0;
  i2c_transaction(BMA250_I2C_ADDR, 1, &return_data, (uint8_t) 1);

  _y |= (return_data << 8);
  _y >>= 6;
  *y = _y;

  // z accel
  uint8_t z_reg = BMA250_REG_ACCEL_Z_LSB;
  i2c_transaction(BMA250_I2C_ADDR, 0, &z_reg, (uint8_t) 1);

  return_data = 0;
  i2c_transaction(BMA250_I2C_ADDR, 1, &return_data, (uint8_t) 1);

  _z = (int16_t) return_data;

  z_reg = BMA250_REG_ACCEL_Z_MSB;
  i2c_transaction(BMA250_I2C_ADDR, 0, &z_reg, (uint8_t) 1);

  return_data = 0;
  i2c_transaction(BMA250_I2C_ADDR, 1, &return_data, (uint8_t) 1);

  _z |= (return_data << 8);
  _z >>= 6;
  *z = _z;
}