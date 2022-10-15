#include "lm4f120h5qr.h"
#include "delay.h"

#define LED_RED (1U << 1)
#define LED_BLUE (1U << 2)
#define LED_GREEN (1U << 3)

int main() {
    SYSCTL_RCGCGPIO_R |= (1U << 5); // turn on clock for GPIOF
    SYSCTL_GPIOHBCTL_R |= (1U << 5); // enable AHB for GPIOF
    GPIO_PORTF_AHB_DIR_R |= (LED_RED | LED_BLUE | LED_GREEN); /* set pins 1, 2, 3 as outputs */
    GPIO_PORTF_AHB_DEN_R |= (LED_RED | LED_BLUE | LED_GREEN); // set pins 1, 2, 3 as digital

    GPIO_PORTF_AHB_DATA_R = LED_BLUE;
    while (1) {
        GPIO_PORTF_AHB_DATA_BITS_R[LED_RED] = LED_RED;
        delay(1000000);

        GPIO_PORTF_AHB_DATA_BITS_R[LED_RED] = 0; // turn off pins in GPIOF
        delay(500000);
    }
	return 0;
}
