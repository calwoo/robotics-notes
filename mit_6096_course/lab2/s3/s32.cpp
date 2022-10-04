#include <iostream>

void printNum();
int number = 35;

int main() {
    printNum();
    return 0;
}

void printNum() { std::cout << number; }