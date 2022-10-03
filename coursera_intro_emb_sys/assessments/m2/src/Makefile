#******************************************************************************
# Copyright (C) 2017 by Alex Fosdick - University of Colorado
#
# Redistribution, modification or use of this software in source or binary
# forms is permitted as long as the files maintain this copyright. Users are 
# permitted to modify this and use it to learn about the field of embedded
# software. Alex Fosdick and the University of Colorado are not liable for any
# misuse of this material. 
#
#*****************************************************************************

include sources.mk

TARGET = c1m2

ifeq ($(PLATFORM),HOST)
	CPU = x86_64

else
	LINKER_FILE = -T ../msp432p401r.lds
	CPU = cortex-m4
	ARCH = armv7e-m
	SPECS = nosys.specs

endif

ifeq ($(PLATFORM),HOST)
	CC = gcc
	LDFLAGS = -Wl,-Map=$(TARGET).map
	CFLAGS = -Wall -Werror -O0 -g -std=c99
	CPPFLAGS = -M -MF test.d
	DEFINEFLAG = -DHOST

else
	CC = arm-none-eabi-gcc
	LD = arm-none-eabi-ld
	LDFLAGS = -Wl,-Map=$(TARGET).map $(LINKER_FILE)
	CFLAGS = -mcpu=$(CPU) -march=$(ARCH) --specs=$(SPECS) -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 -Wall -Werror -O0 -g -std=c99
	CPPFLAGS = -M -MF test.d
	DEFINEFLAG = -DMSP432

endif

OBJECTS = $(SOURCES:.c=.o)
ASMS = $(SOURCES:.c=.s)
PPS = $(SOURCES:.c=.i)
MAPS = $(SOURCES:.c=.map)
OUTPUTS = $(SOURCES:.c=.out)

%.i: %.c
	$(CC) $(CPPFLAGS) $(DEFINEFLAG) $<
	$(CC) $(DEFINEFLAG) -E -o $@ $<

%.o: %.c
	$(CC) $(DEFINEFLAG) $(CFLAGS) -c $<

.PHONY: compile-all
compile-all: $(SOURCES)
	$(CC) $(DEFINEFLAG) $(CFLAGS) -c $(SOURCES)

.PHONY: build
build: $(OUTPUTS)
$(OUTPUTS): $(SOURCES)
	$(CC) $(DEFINEFLAG) $(CFLAGS) $(LDFLAGS) $(INCLUDES) -o c1m2.out $^
	size c1m2.out

.PHONY: clean
clean:
	rm -f *.i *.d *.map *.s *.out *.o
