#include "TM4C123GH6PM.h"

//#define RCGCGPIO (*((unsigned int *)0x400FE608U))
//#define GPIOF_BASE 0x40025000U
//#define GPIOF_DIR (*((unsigned int *)(GPIOF_BASE + 0x400U)))
//#define GPIOF_DEN (*((unsigned int *)(GPIOF_BASE + 0x51CU)))
//#define GPIOF_DATA (*((unsigned int *)(GPIOF_BASE + 0x3FCU)))

int main() {
    RCGCGPIO = 0x20U; // turn on clock for GPIOF
    GPIOF->DIR = 0x0EU; /* set pins 1, 2, 3 as outputs */
    GPIOF_DEN = 0x0EU; // set pins 1, 2, 3 as digital

    while (1) {
        GPIOF_DATA = 0x0CU; // turn on pins 2, 3

        volatile int counter = 0;
        while (counter < 1000000) {
            ++counter;
        }

        GPIOF_DATA = 0x00U; // turn off pins in GPIOF
        counter = 0;
        while (counter < 1000000) {
            ++counter;
        }
    }
	return 0;
}
