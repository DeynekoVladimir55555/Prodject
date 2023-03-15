import DataBaseFile

import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

import MoveFunction

#Окно статистики решений
class StatisticsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\StatisticsWindow.ui', self)
        self.setWindowTitle('Статистика')
        self.closeButton.clicked.connect(self.close_window)
        self.updateButton.clicked.connect(self.update)
        #Показывание окна поверх главного
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        #Передвижение на центр экрана
        MoveFunction.move_to_senter(self)

    def update(self):
        #Получение статистики и её вывод
        a = DataBaseFile.statistics()
        self.trueLabel.setText('Решено верно:   ' + a[0])
        self.falseLabel.setText('Решено неверно:   ' + a[1])

    def close_window(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    statw = StatisticsWindow()
    statw.show()
    sys.exit(app.exec_())
