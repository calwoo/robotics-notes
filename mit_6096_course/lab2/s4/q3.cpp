#include <iostream>
using namespace std;

int sum(const int x, const int y)
{
    return x + y;
}

int sum(const int x, const int y, const int z)
{
    return x + y + z;
}

int sum(const int x, const int y, const int z, const int w)
{
    return x + y + z + w;
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
    cout << sum(1, 2, 3) << endl;
    cout << sum(1, 2, 3, 4) << endl;
    return 0;
}
