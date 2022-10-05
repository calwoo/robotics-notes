#include <iostream>
using namespace std;

void swap(int &a, int &b)
{
    int tmp = b;
    b = a;
    a = tmp;
}

int main()
{
    int x = 2;
    int y = 5;
    cout << x << y << endl;
    swap(x, y);
    cout << x << y << endl;
    return 0;
}
