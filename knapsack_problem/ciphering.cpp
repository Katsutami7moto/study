#include <iostream>
#include <stdlib.h>
using namespace std;

int* gen_open_key(int* w, int r, int q) {
    int* beta;
    int end = _countof(w);
    for (i = 0; i < end; i++) {
        beta[i] = (w[i] * r % q);
    }
    return beta;
}
