#include "decipherwindow.h"
#include "ui_decipherwindow.h"
#include "decipher.h"
#include <ctime>

DecipherWindow::DecipherWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::DecipherWindow)
{
    ui->setupUi(this);
    init_bahm();
}

DecipherWindow::~DecipherWindow()
{
    delete ui;
}

void DecipherWindow::on_pushButton_clicked()
{
    vector<QString> vtemp = ui->textBeforeD->toPlainText().split("\n").toVector().toStdVector();
    int sz = vtemp.size();
    int itemp[sz];
    QString stemp;
    for (int i = 0; i < sz; i++)
    {
        stemp = vtemp[i];
        itemp[i] = stemp.toInt();
    }
    int wtest[8] = {2, 3, 9, 23, 42, 86, 174, 346};
    int mr = modinv(113, 971);
    int s[sz];
    string rs[sz];
    char result[sz];

    for (int i = 0; i < sz; i++)
    {
        s[i] = itemp[i] * mr % 971;
    }
    for (int i = 0; i < sz; i++)
    {
        rs[i] = knapsack(wtest, s[i]);
    }
    for (int i = 0; i < sz; i++)
    {
        result[i] = deconvert(rs[i]);
    }
    ui->textAfterD->append(QString::fromStdString(result));
}

void DecipherWindow::on_pushButton_2_clicked()
{
    ui->textBeforeD->clear();
}

void DecipherWindow::on_pushButton_3_clicked()
{
    ui->textAfterD->clear();
}

void DecipherWindow::on_pushButton_4_clicked()
{
    ui->textAfterD->selectAll();
    ui->textAfterD->copy();
}
