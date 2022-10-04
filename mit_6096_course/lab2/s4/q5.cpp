#include <iostream>
using namespace std;

int sum(const int numbers[], const int len)
{
    int acc = 0;
    for (int i = 0; i < len; i++)
    {
        acc += numbers[i];
    }
    return acc;
}

int main()
{
    int test[4] = {1, 2, 3, 4};
    cout << sum(test, 4) << endl;
    return 0;
}
