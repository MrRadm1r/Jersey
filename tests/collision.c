#include <stdio.h>

void main() {
    int result;
    for (int i =1; i<2073600; i++){
        result = i / 9000 * 1000;
        printf("%d", i);
    }
    printf("done");
}
