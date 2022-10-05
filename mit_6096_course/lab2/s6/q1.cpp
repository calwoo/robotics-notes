#include <iostream>

void printArray(int arr[], int len)
{
    for (int i = 0; i < len - 1; i++)
    {
        std::cout << arr[i] << ", ";
    }
    std::cout << arr[len - 1] << std::endl;
}

int main()
{
    int arr[5] = {1, 1, 2, 3, 5};
    printArray(arr, 5);

    return 0;
}