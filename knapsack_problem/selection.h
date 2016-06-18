#ifndef SELECTION_H
#define SELECTION_H

#include <set>
using namespace std;

class Selection
{
public:
    Selection(int number, int w, int v);
    Selection(Selection *selcp);
    ~Selection();

    void add(int number, int w, int v);
    set<int> getnumber();
    int getweight();
    int getvalue();
private:
    set<int> select_number;
    int sum_weight;
    int sum_value;
};

#endif // SELECTION_H
