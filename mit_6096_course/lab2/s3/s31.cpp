#include <iostream>

// should be declared here, as opposed to bottom of file
void printNum(int number) { std::cout << number; }

int main() {
    printNum(35);
    return 0;
}
