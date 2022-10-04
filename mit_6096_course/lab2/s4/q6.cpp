#include <iostream>
using namespace std;

int sum(const int numbers[], const int len)
{
    if (len == 0)
    {
        return *numbers;
    }

    return *numbers + sum(numbers + 1, len - 1);
}

int main()
{
    int test[4] = {1, 2, 3, 4};
    cout << sum(test, 4) << endl;
    return 0;
}
