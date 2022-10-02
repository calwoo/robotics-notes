/******************************************************************************
 * Copyright (C) 2017 by Alex Fosdick - University of Colorado
 *
 * Redistribution, modification or use of this software in source or binary
 * forms is permitted as long as the files maintain this copyright. Users are 
 * permitted to modify this and use it to learn about the field of embedded
 * software. Alex Fosdick and the University of Colorado are not liable for any
 * misuse of this material. 
 *
 *****************************************************************************/
/**
 * @file stats.h
 * @author calvin d. woo
 * @date 10.2.2022
 *
 */


#ifndef __STATS_H__
#define __STATS_H__

/* Add Your Declarations and Function Comments here */ 
void print_statistics(unsigned char *arr, unsigned int size);
void print_array(unsigned char *arr, unsigned int size);
unsigned int find_median(unsigned char *arr, unsigned int size);
unsigned int find_mean(unsigned char *arr, unsigned int size);
unsigned int find_maximum(unsigned char *arr, unsigned int size);
unsigned int find_minimum(unsigned char *arr, unsigned int size);
void sort_array(unsigned char *arr, unsigned int size);

#endif
