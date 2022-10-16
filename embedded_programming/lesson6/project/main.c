#include "lm4f120h5qr.h"

#define LED_RED (1U << 1)
#define LED_BLUE (1U << 2)
#define LED_GREEN (1U << 3)

int main() {
    SYSCTL_RCGCGPIO_R = 0x20U; // turn on clock for GPIOF
    GPIO_PORTF_DIR_R = 0x0EU; /* set pins 1, 2, 3 as outputs */
    GPIO_PORTF_DEN_R = 0x0EU; // set pins 1, 2, 3 as digital

    GPIO_PORTF_DATA_R = LED_BLUE;
    while (1) {
        GPIO_PORTF_DATA_R |= LED_RED; // turn on pins 2, 3

        int volatile counter = 0;
        while (counter < 1000000) {
            ++counter;
        }

        GPIO_PORTF_DATA_R &= ~LED_RED; // turn off pins in GPIOF
        counter = 0;
        while (counter < 1000000) {
            ++counter;
        }
    }
	return 0;
}
