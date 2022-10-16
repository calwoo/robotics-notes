#include <stdint.h>
#include "tm4c_cmsis.h"
#include "delay.h"

#define SYS_CLOCK_HZ 16000000

#define LED_RED (1U << 1)
#define LED_BLUE (1U << 2)
#define LED_GREEN (1U << 3)
#define BUTTON (1U << 4)

int main(void)
{
    unsigned int state;

    SYSCTL->RCGC2 |= (1 << 5); // enable GPIOF clock
    GPIOF->LOCK = 0x4C4F434B; // unlock GPIOCR register
    GPIOF->CR = 0x01;
    GPIOF->PUR |= BUTTON;
    GPIOF->DIR |= (LED_RED | LED_BLUE | LED_GREEN); // turn led pins to output
    GPIOF->DEN |= (LED_RED | LED_BLUE | LED_GREEN | BUTTON);

//    SysTick->LOAD = SYS_CLOCK_HZ / 2U - 1U;
//    SysTick->VAL = 0U;
//    SysTick->CTRL = (1U << 2) | (1U << 1) | 1U;

    GPIOF->DATA_Bits[LED_BLUE] = LED_BLUE;
    while (1) {
        state = GPIOF->DATA & BUTTON;
        GPIOF->DATA_Bits[LED_RED] = (~state >> 3);
    }
	return 0;
}
