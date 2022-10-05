#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;

double randUni()
{
    // random number in 0-1
    return rand() / (double)RAND_MAX;
}

double computePi(int n)
{
    // initialize random seed
    srand(time(0));

    double x, y, d;
    int darts_in_circle = 0;

    for (int i = 0; i < n; i++)
    {
        // dart coordinates
        x = randUni();
        y = randUni();

        // compute distance from center
        d = sqrt(x * x + y * y);

        // check if in circle
        if (d <= 1) {
            darts_in_circle += 1;
        }
    }

    double ratio = darts_in_circle / static_cast<double>(n);
    return ratio * 4;
}

int main()
{
    cout << computePi(5000000) << endl;
    return 0;
}
