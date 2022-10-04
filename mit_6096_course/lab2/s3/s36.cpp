#include <iostream>
const int ARRAY_LEN = 10;

int main() {
    int arr[ARRAY_LEN] = {10};

    int *xPtr = arr; 
    int *yPtr = arr + ARRAY_LEN - 1;
    std::cout << *xPtr << ' ' << *yPtr;
    return 0;
}