from PyQt5.QtWidgets import QApplication


def move_to_senter(object):
    # Передвижение окна на центр экрана
    desktop = QApplication.desktop()
    x = (desktop.width() - object.width()) // 2
    y = (desktop.height() - object.height()) // 2
    object.move(x, y)
