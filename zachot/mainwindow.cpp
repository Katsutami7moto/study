#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->labelResult->setText("");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_sumButton_clicked()
{
    ComplexNumber complexNumber1;
    ComplexNumber complexNumber2;

    complexNumber1.real = ui->lineEdit->text().toDouble();
    complexNumber1.imaginary = ui->lineEdit_2->text().toDouble();

    complexNumber2.real = ui->lineEdit_3->text().toDouble();
    complexNumber2.imaginary = ui->lineEdit_4->text().toDouble();

    complexNumber1 = complexNumber1 + complexNumber2;

    if (complexNumber1.imaginary == 0)
        ui->labelResult->setText(QString::number(complexNumber1.real));
    else
        ui->labelResult->setText(QString::number(complexNumber1.real) +
                                 "+ i * (" + QString::number(complexNumber1.imaginary) + ")");
}

void MainWindow::on_subtrButton_clicked()
{
    ComplexNumber complexNumber1;
    ComplexNumber complexNumber2;

    complexNumber1.real = ui->lineEdit->text().toDouble();
    complexNumber1.imaginary = ui->lineEdit_2->text().toDouble();

    complexNumber2.real = ui->lineEdit_3->text().toDouble();
    complexNumber2.imaginary = ui->lineEdit_4->text().toDouble();

    complexNumber1 = complexNumber1 - complexNumber2;

    if (complexNumber1.imaginary == 0)
        ui->labelResult->setText(QString::number(complexNumber1.real));
    else
        ui->labelResult->setText(QString::number(complexNumber1.real) +
                                 "+ i * (" + QString::number(complexNumber1.imaginary) + ")");
}

void MainWindow::on_multButton_clicked()
{
    ComplexNumber complexNumber1;
    ComplexNumber complexNumber2;

    complexNumber1.real = ui->lineEdit->text().toDouble();
    complexNumber1.imaginary = ui->lineEdit_2->text().toDouble();

    complexNumber2.real = ui->lineEdit_3->text().toDouble();
    complexNumber2.imaginary = ui->lineEdit_4->text().toDouble();

    complexNumber1 = complexNumber1 * complexNumber2;

    if (complexNumber1.imaginary == 0)
        ui->labelResult->setText(QString::number(complexNumber1.real));
    else
        ui->labelResult->setText(QString::number(complexNumber1.real) +
                                 "+ i * (" + QString::number(complexNumber1.imaginary) + ")");
}

void MainWindow::on_divButton_clicked()
{
    ComplexNumber complexNumber1;
    ComplexNumber complexNumber2;

    complexNumber1.real = ui->lineEdit->text().toDouble();
    complexNumber1.imaginary = ui->lineEdit_2->text().toDouble();

    complexNumber2.real = ui->lineEdit_3->text().toDouble();
    complexNumber2.imaginary = ui->lineEdit_4->text().toDouble();

    complexNumber1 = complexNumber1 / complexNumber2;

    if (complexNumber1.imaginary == 0)
        ui->labelResult->setText(QString::number(complexNumber1.real));
    else
        ui->labelResult->setText(QString::number(complexNumber1.real) +
                                 "+ i * (" + QString::number(complexNumber1.imaginary) + ")");
}

void MainWindow::on_lenButtonA_clicked()
{
    ComplexNumber complexNumber;

    complexNumber.real = ui->lineEdit->text().toDouble();
    complexNumber.imaginary = ui->lineEdit_2->text().toDouble();

    ui->labelLengthA->setText(QString::number(complexNumber.getLength()));
}

void MainWindow::on_lenButtonB_clicked()
{
    ComplexNumber complexNumber;

    complexNumber.real = ui->lineEdit_3->text().toDouble();
    complexNumber.imaginary = ui->lineEdit_4->text().toDouble();

    ui->labelLengthB->setText(QString::number(complexNumber.getLength()));
}
