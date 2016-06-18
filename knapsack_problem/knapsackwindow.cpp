#include "knapsackwindow.h"
#include "ui_knapsackwindow.h"
#include <ctime>

KnapsackWindow::KnapsackWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::KnapsackWindow)
{
    ui->setupUi(this);
}

KnapsackWindow::~KnapsackWindow()
{
    delete ui;
}

void KnapsackWindow::on_addItemButton_clicked()
{
    items2pack.insert(items2pack.end(), 1,
                      Item(ui->itemEdit->text().toStdString(),ui->weightEdit->text().toInt(),
                           ui->valueEdit->text().toInt()));
    ui->itemEdit->clear();
    ui->weightEdit->clear();
    ui->valueEdit->clear();
    ui->itemsList->append(items2pack.back().getinfo());
}

int KnapsackWindow::getcap()
{
    return capacity;
}

void KnapsackWindow::setcap(int x)
{
    capacity = x;
    ui->labelCapacity->setText(QString::number(capacity));
}

void KnapsackWindow::deccap(int x)
{
    capacity = capacity - x;
    ui->labelCapacity->setText(QString::number(capacity));
}

bool sortbyspec(Item i1, Item i2)
{
    return i1.getspecific() > i2.getspecific();
}

void KnapsackWindow::greedy()
{
    sort(items2pack.begin(), items2pack.end(), sortbyspec);
    for (int i = 0; i < items2pack.size(); i++)
    {
        if (items2pack[i].getweight() <= capacity)
        {
            items2pack[i].setpacked();
            deccap(items2pack[i].getweight());
        }
    }
    ui->labelDone->setText(QString("Выполнен"));
}

void KnapsackWindow::branchbound()
{
    solutions = vector<int>(items2pack.size());
    soltemp = vector<int>(items2pack.size());
    sort(items2pack.begin(), items2pack.end(), sortbyspec);
    items2pack.insert(items2pack.begin(), 1, Item("Sentinel", 0, 0));
    solutionValue = -1;
    currWeight = 0;
    currValue = 0;
    newWeight = 0;
    newValue = 0;
    k = 0;
    partItem = 0;
    BBknapsack();

    for (int i = 1; i < solutions.size(); i++)
    {
        if (solutions[i] != 0)
        {
            items2pack[i].setpacked();
        }
    }
    ui->labelDone->setText(QString("Выполнен"));
}

void KnapsackWindow::BBknapsack()
{
    int n = items2pack.size();
    do
    {
        while (bound() <= solutionValue)
        {
            while (k != 0 && soltemp[k] != 1)
                k--;
            if (k == 0)
                return;
            soltemp[k] = 0;
            currWeight -= items2pack[k].getweight();
            currValue -= items2pack[k].getvalue();
        }
        currWeight = newWeight;
        currValue = newValue;
        k = partItem;
        if (k == n)
        {
            solutionValue = currValue;
            solutions = vector<int>(soltemp);
            k = n - 1;
        }
        else
            soltemp[k] = 0;
    }
    while (true);
}

int KnapsackWindow::bound()
{
    bool found = false;
    double boundVal = -1;
    int n = items2pack.size();
    newWeight = currWeight;
    newValue = currValue;
    partItem = k + 1;
    while (partItem < n && !found)
    {
        if (newWeight + items2pack[partItem].getweight() <= capacity)
        {
            newWeight += items2pack[partItem].getweight();
            newValue += items2pack[partItem].getvalue();
            soltemp[partItem] = 1;
        }
        else
        {
            boundVal = newValue + (capacity - newWeight) *
                    items2pack[partItem].getvalue() / items2pack[partItem].getweight();
            found = true;
        }
        partItem++;
    }
    if (found)
    {
        partItem--;
        return boundVal;
    }
    else
    {
        return newValue;
    }
}

void KnapsackWindow::on_pushButton_clicked()
{
    ui->itemsKnapsack->clear();
    on_pushButton_2_clicked();
    on_fileLoadButton_clicked();
    setcap(ui->capacityEdit->text().toInt());
    ui->labelDone->clear();
    ui->labelPushed->clear();
    ui->labelSumW->clear();
    ui->labelSumV->clear();
    ui->labelTime->clear();
    optimal = 0;
    optsel.clear();
}

void KnapsackWindow::on_fileLoadButton_clicked()
{
    QFile file("file.txt");
    QByteArray item, weight, value;
    if (!file.open(QIODevice::ReadOnly)) return;
    items2pack.clear();
    ui->itemsList->clear();
    while (!file.atEnd())
    {
        item = file.readLine();
        weight = file.readLine();
        value = file.readLine();
        items2pack.insert(items2pack.end(), 1,
                          Item(item.toStdString(), QString(weight).toInt(), QString(value).toInt()));
        ui->itemsList->append(items2pack.back().getinfo());
    }
}

void KnapsackWindow::on_pushButton_2_clicked()
{
    items2pack.clear();
    ui->itemsList->clear();
}

void KnapsackWindow::on_pushAlgorithm_clicked()
{
    ui->itemsKnapsack->clear();
    unsigned int start_time =  clock();
    if (ui->radioGreedy->isChecked())
    {
        greedy();
    }
    if (ui->radioMethod->isChecked())
    {
        branchbound();
    }
    unsigned int end_time = clock();
    unsigned int search_time = end_time - start_time;
    ui->labelTime->setText(QString::number(search_time));
}

void KnapsackWindow::on_pushItems_clicked()
{
    bool check = false;
    int sw = 0, sv = 0;
    for (int i = 0; i < items2pack.size(); i++)
    {
        if (items2pack[i].getpacked())
        {
            ui->itemsKnapsack->append(items2pack[i].getinfo());
            sw += items2pack[i].getweight();
            sv += items2pack[i].getvalue();
            check = true;
        }
    }
    if (check)
    {
        ui->labelPushed->setText(QString("Наполнен"));
        ui->labelSumW->setText(QString::number(sw));
        ui->labelSumV->setText(QString::number(sv));
    }
}
