#include "cipherwndow.h"
#include "ui_cipherwndow.h"
#include "cipher.h"
#include <ctime>

CipherWndow::CipherWndow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::CipherWndow)
{
    ui->setupUi(this);
    init_abhm();
}

CipherWndow::~CipherWndow()
{
    delete ui;
}

void CipherWndow::on_pushButton_clicked()
{
    string strtemp = ui->textBeforeC->toPlainText().toLower().toStdString();
    vector<int> temp = run_cipher(strtemp);
    for (int i = 0; i < temp.size(); i++)
    {
        ui->textAfterC->append(QString::number(temp[i]));
    }
}

void CipherWndow::on_pushButton_3_clicked()
{
    ui->textAfterC->clear();
}

void CipherWndow::on_pushButton_2_clicked()
{
    ui->textAfterC->selectAll();
    ui->textAfterC->copy();
}

void CipherWndow::on_pushButton_4_clicked()
{
    ui->textBeforeC->clear();
}
