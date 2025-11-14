#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int count = 200;
    int min = 7;
    int max = 100000000;
    int values[count];

    srand(time(NULL));

    values[0] = min;

    for (int i = 1; i < count; i++) {
        // small step: between 3 and 10000
        int step = 3 + rand() % 50;
        values[i] = values[i - 1] + step;

        if (values[i] > max)
            values[i] = max;
    }

    for (int i = 0; i < count; i++)
        printf("%d\n", values[i]);

    return 0;
}

