#include <iostream>
using namespace std;

int strlen(char *str)
{
    int len = 0;
    while (*(str + len)) {
        len += 1;
    }
    return len;
}

int main()
{
    char str[] = "whattaboutit";
    cout << strlen(str) << endl;
    return 0;
}