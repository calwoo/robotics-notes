#include <iostream>
using namespace std;

int main()
{
    int n, output;
    while (true)
    {
        cout << "value: ";
        cin >> n;

        if (n < 0)
        {
            cout << "goodbye!\n";
            break;
        }

        output = ((n > 0) && (n % 5 == 0)) ? (n / 5) : -1;

        if (output == -1)
        {
            continue;
        }

        cout << "out: " << output << "\n";
    }

    return 0;
}