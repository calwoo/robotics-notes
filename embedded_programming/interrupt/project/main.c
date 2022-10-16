#include <stdint.h>
#include "tm4c_cmsis.h"
#include "delay.h"

#define SYS_CLOCK_HZ 16000000

#define BUTTON1 (1U << 0)
#define LED_RED (1U << 1)
#define LED_BLUE (1U << 2)
#define LED_GREEN (1U << 3)
#define BUTTON2 (1U << 4)

int main(void)
{
    SYSCTL->RCGC2 |= (1 << 5); // enable GPIOF clock

    GPIOF->LOCK = 0x4C4F434B; // unlock GPIOCR register
    GPIOF->CR = 0x01;
    GPIOF->LOCK = 0;

    GPIOF->PUR |= (BUTTON1 | BUTTON2);
    GPIOF->DIR |= (LED_RED | LED_BLUE | LED_GREEN); // turn led pins to output
    GPIOF->DEN |= (LED_RED | LED_BLUE | LED_GREEN | BUTTON1 | BUTTON2);

    // enable interrupts
    NVIC->ISER[0] |= (1 << 30); // enable GPIOF interrupts
    GPIOF->IM |= (BUTTON1 | BUTTON2);

    GPIOF->IS  &= (~BUTTON1 | ~BUTTON2);        /* make bit 4, 0 edge sensitive */
    GPIOF->IBE &= (~BUTTON1 | ~BUTTON2);        /* trigger is controlled by IEV */
    GPIOF->IEV &= (~BUTTON1 | ~BUTTON2);        /* falling edge trigger */
    GPIOF->ICR |= (BUTTON1 | BUTTON2);          /* clear any prior interrupt */

    while (1) {
        GPIOF->DATA_Bits[LED_RED] = LED_RED;
    }
	return 0;
}

void GPIOPortF_IRQHandler(void) {
    if (GPIOF->MIS & BUTTON2) {
        GPIOF->DATA_Bits[LED_GREEN] ^= LED_GREEN;
        GPIOF->ICR |= BUTTON2;
    }
    else if (GPIOF->MIS & BUTTON1) {
        GPIOF->DATA_Bits[LED_BLUE] ^= LED_BLUE;
        GPIOF->ICR |= BUTTON1;
    }
}
