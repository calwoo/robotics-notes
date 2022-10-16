//#include <stdint.h>
#include "tm4c_cmsis.h"
#include "delay.h"

#define SYS_CLOCK_HZ 16000000U

#define LED_RED (1U << 1)
#define LED_BLUE (1U << 2)
#define LED_GREEN (1U << 3)

int main() {
    SYSCTL->RCGC2 |= (1U << 5); // turn on clock for GPIOF
//    SYSCTL->GPIOHSCTL |= (1U << 5); // enable AHB for GPIOF
    GPIOF->DIR |= (LED_RED | LED_BLUE | LED_GREEN); /* set pins 1, 2, 3 as outputs */
    GPIOF->DEN |= (LED_RED | LED_BLUE | LED_GREEN); // set pins 1, 2, 3 as digital

//    SysTick->LOAD = SYS_CLOCK_HZ / 2U - 1U;
//    SysTick->VAL = 0U;
//    SysTick->CTRL = (1U << 2) | (1U << 1) | 1U;

    GPIOF->DATA_Bits[LED_BLUE] = LED_BLUE;
    while (1) {
        GPIOF->DATA_Bits[LED_RED] ^= LED_RED;
        delay(1000000);
    }
	return 0;
}
