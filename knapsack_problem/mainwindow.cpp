#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "cipherwndow.h"
#include "decipherwindow.h"
#include "knapsackwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushKnapsack_clicked()
{
    KnapsackWindow *k1 = new KnapsackWindow();
    k1->show();
}

void MainWindow::on_pushKnapsack_2_clicked()
{
    CipherWndow *c1 = new CipherWndow();
    c1->show();
}

void MainWindow::on_pushKnapsack_3_clicked()
{
    DecipherWindow *d1 = new DecipherWindow();
    d1->show();
}
