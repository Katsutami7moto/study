#ifndef DECIPHER
#define DECIPHER

#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>
using namespace std;

map<string, char> binabchashmap;
string abc1 = "abcdefghijklmnopqrstuvwxyz ";
string abcbin1[27] = {"01100001", "01100010", "01100011", "01100100", "01100101", "01100110",
                         "01100111", "01101000", "01101001", "01101010", "01101011", "01101100",
                         "01101101", "01101110", "01101111", "01110000", "01110001", "01110010",
                         "01110011", "01110100", "01110101", "01110110", "01110111", "01111000",
                         "01111001", "01111010", "00100000"};
void init_bahm()
{
    for (int i = 0; i < 27; i++)
    {
        binabchashmap.insert( pair<string, char>(abcbin1[i], abc1[i]) );
    }
}

int modinv(int a, int b)
{
    int b0 = b, t, q;
    int x0 = 0, x1 = 1;
    if (b == 1) return 1;
    while (a > 1)
    {
        q = a / b;
        t = b, b = a % b, a = t;
        t = x0, x0 = x1 - q * x0, x1 = t;
    }
    if (x1 < 0) x1 += b0;
    return x1;
}

string knapsack(int w[], int x)
{
    string s = "00000000";
    int m = x;

    for (int i = 7; i >= 0; i--)
    {
        while (m > 0 && m >= w[i])
        {
            s[i] = '1';
            m = m - w[i];
            break;
        }
    }
    return s;
}

char deconvert(string s)
{
    return binabchashmap[s];
}

#endif // DECIPHER
