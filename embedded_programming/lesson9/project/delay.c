void delay(int iter) {
    int volatile counter = 0;
    while (counter < 1000000) {
        ++counter;
    }
}
