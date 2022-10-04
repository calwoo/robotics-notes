#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    srand(time(0));

    int rand_num = rand();
    std::cout << "a random number: " << rand_num << std::endl;
    return 0;
}