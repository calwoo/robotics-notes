#include <iostream>
using namespace std;\

// doesn't compile; arg1 declared twice

int main()
{
    int arg1;
    arg1 = -1;
    int x, y, z;
    char myDouble = '5';
    char arg1 = 'A';
    cout << arg1 << "\n";
    return 0;
}