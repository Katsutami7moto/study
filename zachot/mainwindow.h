#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "number.h"
#include <QString>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_sumButton_clicked();
    void on_subtrButton_clicked();
    void on_multButton_clicked();
    void on_divButton_clicked();
    void on_lenButtonA_clicked();
    void on_lenButtonB_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
