#include <iostream>
using namespace std;

void swap(int **a, int **b)
{
    int *tmp = *b;
    *b = *a;
    *a = tmp;
}

int main()
{
    int x = 5;
    int y = 6;
    cout << x << y << endl;

    int *ptr1 = &x, *ptr2 = &y;
    swap(&ptr1, &ptr2);

    cout << x << y << endl;
    cout << *ptr1 << ' ' << *ptr2 << endl;
    return 0;
}
