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
 * @file stats.c
 * @author calvin d. woo
 * @date 10.2.2022
 *
 */


#include <stdio.h>
#include "stats.h"

/* Size of the Data Set */
#define SIZE (40)

void main() {

    unsigned char test[SIZE] = { 34, 201, 190, 154,   8, 194,   2,   6,
                                114, 88,   45,  76, 123,  87,  25,  23,
                                200, 122, 150, 90,   92,  87, 177, 244,
                                201,   6,  12,  60,   8,   2,   5,  67,
                                7,  87, 250, 230,  99,   3, 100,  90};

    /* Other Variable Declarations Go Here */
    /* Statistics and Printing Functions Go Here */
    print_statistics(test, SIZE);
}

/* Add other Implementation File Code Here */
void print_statistics(unsigned char *arr, unsigned int size) {
    printf("array:\n");
    print_array(arr, size);
    printf("sorted:\n");
    sort_array(arr, size);
    print_array(arr, size);
    printf("median: %d\n", find_median(arr, size));
    printf("mean: %d\n", find_mean(arr, size));
    printf("max: %d\n", find_maximum(arr, size));
    printf("min: %d\n", find_minimum(arr, size));
}

void print_array(unsigned char *arr, unsigned int size) {
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

unsigned int find_median(unsigned char *arr, unsigned int size) {
    sort_array(arr, size);
    if (size % 2 == 0) {
        int mid = size / 2;
        return (arr[mid - 1] + arr[mid]) / 2;
    } else {
        int mid = (size - 1) / 2;
        return arr[mid];
    }
}

unsigned int find_mean(unsigned char *arr, unsigned int size) {
    int sum = 0;
    for (int i = 0; i < size; i++ ) {
        sum += arr[i];
    }
    return sum / size;
}

unsigned int find_maximum(unsigned char *arr, unsigned int size) {
    sort_array(arr, size);
    return arr[0];
}

unsigned int find_minimum(unsigned char *arr, unsigned int size) {
    sort_array(arr, size);
    return arr[size - 1];
}

// https://stackoverflow.com/a/6567846/13191956
void sort_array(unsigned char *arr, unsigned int size) {
    // standard insertion sort
    for (int i = 0; i < size - 1; i++)
    {
        int max_so_far = arr[i];
        int max_idx = i;
        for (int j = i + 1; j < size; j++) {
            if (arr[j] > max_so_far) {
                max_so_far = arr[j];
                max_idx = j;
            }
        }

        // max value is found, swap
        int temp = arr[i];
        arr[i] = max_so_far;
        arr[max_idx] = temp;
    }
}