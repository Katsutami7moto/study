#ifndef CIPHER
#define CIPHER

#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>
#include <QDebug>
using namespace std;

map<char, string> abcbinhashmap;
string abc = "abcdefghijklmnopqrstuvwxyz ";
string abcbin[27] = {"01100001", "01100010", "01100011", "01100100", "01100101", "01100110",
                         "01100111", "01101000", "01101001", "01101010", "01101011", "01101100",
                         "01101101", "01101110", "01101111", "01110000", "01110001", "01110010",
                         "01110011", "01110100", "01110101", "01110110", "01110111", "01111000",
                         "01111001", "01111010", "00100000"};
void init_abhm()
{
    for (int i = 0; i < 27; i++)
    {
        abcbinhashmap.insert( pair<char, string>(abc[i], abcbin[i]) );
    }
}

vector<int> gen_open_key(int w[], int r, int q)
{
    vector<int> beta(8);
    for (int i = 0; i < 8; i++)
    {
        beta[i] = (w[i] * r % q);
    }
    return beta;
}

vector<string> convert(string s)
{
    int sz = s.length();
    vector<string> temp(sz);
    for (int i = 0; i < sz; i++)
    {
        temp[i] = abcbinhashmap[s[i]];
    }
    return temp;
}

vector<int> ciphering(vector<int> key, vector<string> conv)
{
    int s = 0;
    vector<int> sl(conv.size());

    for (int i = 0; i < conv.size(); i++)
    {
        for (int j = 0; j < conv[i].length(); j++)
        {
            if (conv[i][j] == '1')
            {
                s += key[j];
            }
        }
        sl[i] = s;
        s = 0;
    }
    return sl;
}

vector<int> run_cipher(string texty)
{
    int wtest[8] = {2, 3, 9, 23, 42, 86, 174, 346};
    vector<int> ktest = gen_open_key(wtest, 113, 971);
    vector<string> ctest = convert(texty);
    vector<int> shiffre = ciphering(ktest, ctest);
    return shiffre;
}

#endif // CIPHER
