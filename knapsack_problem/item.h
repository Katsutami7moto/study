#ifndef ITEM_H
#define ITEM_H

#include <iostream>
#include <QString>
using namespace std;

class Item
{
public:
    Item(string n, int p, int c);
    ~Item();

    void setpacked();
    void setunpacked();
    string getname();
    int getweight();
    int getvalue();
    double getspecific();
    bool getpacked();
    QString getinfo();
private:
    string name;
    int weight;
    int value;
    double specific;
    bool packed;
};

#endif // ITEM_H
