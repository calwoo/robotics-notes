#include <iostream>
using namespace std;

int sum(const int x, const int y, const int z = 0, const int w = 0)
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
