#include <iostream>

void printArray(int arr[], int len)
{
    for (int i = 0; i < len - 1; i++)
    {
        std::cout << arr[i] << ", ";
    }
    std::cout << arr[len - 1] << std::endl;
}

void reverse(int arr[], int len)
{
    for (int i = 0; i < len / 2; i++)
    {
        int tmp = arr[i];
        int end_idx = len - 1 - i;
        arr[i] = arr[end_idx];
        arr[end_idx] = tmp;
    }
}

int main()
{
    int arr[5] = {1, 1, 2, 3, 5};
    printArray(arr, 5);
    reverse(arr, 5);
    printArray(arr, 5);

    return 0;
}
