#include <iostream>
using namespace std;

int sum(const int x, const int y)
{
    return x + y;
}

double sum(const double x, const double y)
{
    return x + y;
}

int main()
{
    cout << sum(1, 2) << endl;
    cout << sum(1.0, 2.0) << endl;
    // cout << sum(1.0, 2) << endl;
    return 0;
}