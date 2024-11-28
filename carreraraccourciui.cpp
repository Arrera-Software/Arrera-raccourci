#include "carreraraccourciui.h"
#include "ui_carreraraccourciui.h"

CArreraRaccourciUI::CArreraRaccourciUI(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::CArreraRaccourciUI)
{
    ui->setupUi(this);
}

CArreraRaccourciUI::~CArreraRaccourciUI()
{
    delete ui;
}
