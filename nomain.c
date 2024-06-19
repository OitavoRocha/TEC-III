#include <stdio.h>
#include <stdlib.h>

int notMain();

void _start() {
    notMain();
    exit(0);
}

int notMain() {
    printf("Aqui é a função principal\n");
    return 0;
}