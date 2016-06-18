#include "selection.h"

Selection::Selection(int number, int w, int v)
{
    select_number.insert(number);
    sum_weight = w;
    sum_value = v;
}

Selection::Selection(Selection *selcp)
{
    select_number = selcp->getnumber();
    sum_weight = selcp->getweight();
    sum_value = selcp->getvalue();
}

Selection::~Selection()
{

}

void Selection::add(int number, int w, int v)
{
    select_number.insert(number);
    sum_weight += w;
    sum_value += v;
}

std::set<int> Selection::getnumber()
{
    return select_number;
}

int Selection::getweight()
{
    return sum_weight;
}

int Selection::getvalue()
{
    return sum_value;
}
