#ifndef KNAPSACKWINDOW_H
#define KNAPSACKWINDOW_H

#include <QWidget>
#include "item.h"
#include <ctime>
#include <QFile>
#include <QByteArray>
#include "selection.h"
using namespace std;

namespace Ui {
class KnapsackWindow;
}

class KnapsackWindow : public QWidget
{
    Q_OBJECT

public:
    explicit KnapsackWindow(QWidget *parent = 0);

    int getcap();
    void setcap(int x);
    void deccap(int x);

    void greedy();

    void branchbound();
    void BBknapsack();
    int bound();

    ~KnapsackWindow();

private slots:
    void on_addItemButton_clicked();

    void on_pushItems_clicked();

    void on_pushButton_clicked();

    void on_fileLoadButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushAlgorithm_clicked();

private:
    Ui::KnapsackWindow *ui;

    int capacity;
    vector<Item> items2pack;

    int optimal;
    set<int> optsel;

    vector<int> solutions;
    vector<int> soltemp;
    int solutionValue;
    int currWeight;
    int currValue;
    int newWeight;
    int newValue;
    int k;
    int partItem;
};

bool sortbyspec(Item i1, Item i2);

#endif // KNAPSACKWINDOW_H
