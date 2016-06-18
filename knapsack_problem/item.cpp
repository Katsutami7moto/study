#include "item.h"

Item::Item(string n, int p, int c)
{
    name = n;
    weight = p;
    value = c;
    specific = double(c) / double(p);
    packed = false;
}

Item::~Item()
{

}

void Item::setpacked()
{
    packed = true;
}

void Item::setunpacked()
{
    packed = false;
}

string Item::getname()
{
    return name;
}

int Item::getweight()
{
    return weight;
}

int Item::getvalue()
{
    return value;
}

double Item::getspecific()
{
    return specific;
}

bool Item::getpacked()
{
    return packed;
}

QString Item::getinfo()
{
    QString temp;
    temp = "Item: " + QString::fromStdString(getname()) + "; Weight: " + QString::number(getweight()) +
            "; Value: " + QString::number(getvalue()) + ".";
    return temp;
}
