#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <pthread.h>

void break_here() {}

int main() {
    void* allocs[6] = {0};

    allocs[0] = malloc(10);
    allocs[1] = malloc(10);

    break_here();

    allocs[2] = malloc(40);

    break_here();

    free(allocs[1]);

    break_here();

    allocs[3] = malloc(0x1000);
    allocs[4] = malloc(0x2000);
    free(allocs[3]);

    break_here();
No specific changes are needed in the provided code snippet as it seems to be part of a C source file with heap manipulation and a comment about CI test pass requirements.
