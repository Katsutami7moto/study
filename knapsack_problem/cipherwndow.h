#ifndef CIPHERWNDOW_H
#define CIPHERWNDOW_H

#include <QWidget>

namespace Ui {
class CipherWndow;
}

class CipherWndow : public QWidget
{
    Q_OBJECT

public:
    explicit CipherWndow(QWidget *parent = 0);
    ~CipherWndow();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_4_clicked();

private:
    Ui::CipherWndow *ui;
};

#endif // CIPHERWNDOW_H
