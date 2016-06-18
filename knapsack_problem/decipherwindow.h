#ifndef DECIPHERWINDOW_H
#define DECIPHERWINDOW_H

#include <QWidget>

namespace Ui {
class DecipherWindow;
}

class DecipherWindow : public QWidget
{
    Q_OBJECT

public:
    explicit DecipherWindow(QWidget *parent = 0);
    ~DecipherWindow();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

private:
    Ui::DecipherWindow *ui;
};

#endif // DECIPHERWINDOW_H
