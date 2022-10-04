#include <iostream>

int sum(const int x, const int y, const int z) {
    return x + y + z;
}

int main() {
    std::cout << sum(1, 2, 3);
    return 0;
}
