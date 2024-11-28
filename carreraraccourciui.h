#ifndef CARRERARACCOURCIUI_H
#define CARRERARACCOURCIUI_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class CArreraRaccourciUI;
}
QT_END_NAMESPACE

class CArreraRaccourciUI : public QMainWindow
{
    Q_OBJECT

public:
    CArreraRaccourciUI(QWidget *parent = nullptr);
    ~CArreraRaccourciUI();

private:
    Ui::CArreraRaccourciUI *ui;
};
#endif // CARRERARACCOURCIUI_H
