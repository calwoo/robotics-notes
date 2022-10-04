#include <iostream>
using namespace std;

int main()
{
    int n, min, max;
    int sum = 0;
    cout << "input number of ints: ";
    cin >> n;

    int next_num;
    for (int i = 0; i < n; i++) {
        // accept number
        cin >> next_num;
        if (i == 0)
        {
            min = next_num;
            max = next_num;
        }

        sum += next_num;
        if (next_num < min)
        {
            min = next_num;
        }
        else if (next_num > max)
        {
            max = next_num;
        }
    }

    int avg = sum / float(n);
    cout << "mean: " << avg << "\n";
    cout << "max: " << max << "\n";
    cout << "min: " << min << "\n";
    cout << "range: " << max - min << "\n";
    return 0;
}