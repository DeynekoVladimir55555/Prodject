import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

import MoveFunction

#Окно с дополнительной информацией о типах задач(для пользователя)
class InformationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\InformationWindow.ui', self)
        self.setWindowTitle('Информация о типах задач')
        self.closeButton.clicked.connect(self.close_window)
        #Показывание окна поверх главного
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        #Передвижение на центр экрана
        MoveFunction.move_to_senter(self)

    def close_window(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    iw = InformationWindow()
    iw.show()
    sys.exit(app.exec_())
