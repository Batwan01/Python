#include <stdio.h>

int main() {
    int a, b=1;

    for (a = 1; a < 4; a += 2) {
        KKK:
        for (; b < 4; b++) {
            if (a < b) { continue; }
            else if (a == b) { break; }
            else {
                b++;
                goto KKK;
            }
        }
        
    }
    printf("%d\n",a * b);
}