import sys

from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

import DataBaseFile
import GenerationQuestionFile
import InformationWindow
import StatisticsWindow
import MoveFunction


# Класс главного окна
class MainQuestionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\MainQuestionWindow.ui', self)
        self.setWindowTitle('Системы счисления')
        # Передвижение на центр экрана
        MoveFunction.move_to_senter(self)

        self.initUi()
        # Получение настроек
        a = DataBaseFile.find('''SELECT * FROM QuestionSettings''')
        b = []
        self.difficulty = a[0]
        if a[1] == 'True':
            b.append(1)
        if a[2] == 'True':
            b.append(2)
        self.types = b

    def initUi(self):
        self.settingsButton.clicked.connect(self.settings)
        self.exitButton.clicked.connect(self.close_window)
        self.statisticsButton.clicked.connect(self.statistics)
        self.nextButton.clicked.connect(self.next)
        self.answerButton.clicked.connect(self.answer)
        self.returnButton.clicked.connect(self.return_back)

        self.questionEdit.setReadOnly(True)

    def close_window(self):
        self.close()

    def settings(self):
        sw.show()

    def return_back(self):
        self.close()
        cw.show()

    def statistics(self):
        statw.show()

    def answer(self):
        # Проверка ответа
        if self.answerEdit.text() == str(self.answer):
            self.answerLabel.setText('Верно')
            # Запись правильно решённой задачи
            DataBaseFile.insert('True')
        else:
            self.answerLabel.setText('Неверно')

    def next(self):
        # Запись неправильно решённой задачи
        if self.answerLabel.text() != 'Верно':
            DataBaseFile.insert('False')
        self.nextButton.setEnabled(False)
        # Генерация задачи
        n = GenerationQuestionFile.print_question(self.difficulty, self.types)
        self.answer = n[1]
        self.questionEdit.setText(n[0])
        self.answerLabel.setText('')
        self.answerEdit.setText('')
        self.nextButton.setEnabled(True)

    def first_question(self):
        # Первая генерация задачи
        self.nextButton.setEnabled(False)
        n = GenerationQuestionFile.print_question(self.difficulty, self.types)
        self.answer = n[1]
        self.questionEdit.setText(n[0])
        self.answerLabel.setText('')
        self.answerEdit.setText('')
        self.nextButton.setEnabled(True)


class MainProgrammingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\MainProgrammingWindow.ui', self)
        self.setWindowTitle('Программирование')
        self.initUi()

    def initUi(self):
        self.checkButton.clicked.connect(self.check)
        self.exitButton.clicked.connect(self.exit)
        self.returnButton.clicked.connect(self.return_back)
        self.settingsButton.clicked.connect(self.settings)

    def check(self):
        pass

    def return_back(self):
        self.close()
        cw.show()

    def settings(self):
        spw.show()

    def exit(self):
        self.close()


class AnswerProgrammingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\AnswerProgrammingWindow.ui', self)
        self.setWindowTitle('Ответ')
        self.initUi()

    def initUi(self):
        self.retryButton.clicked.connect(self.retry)
        self.nextButton.clicked.connect(self.next)

    def answer(self, text):
        pass

    def retry(self):
        self.close()

    def next(self):
        pass


# Окно выбора задач на программирование или на системы счисления
class ChoiceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\ChoiceWindow.ui', self)
        self.setWindowTitle('Выбор задач')
        MoveFunction.move_to_senter(self)
        self.quest = False
        self.prog = False
        self.initUi()

    def initUi(self):
        self.confirmButton.clicked.connect(self.confirm)
        self.programmButton.clicked.connect(self.programming)
        self.questionButton.clicked.connect(self.question)

    def confirm(self):
        if self.prog:
            self.close()
            mpw.show()
        elif self.quest:
            self.close()
            mqw.show()

    def programming(self):
        self.prog = True
        self.quest = False

    def question(self):
        self.quest = True
        self.prog = False


# Приветственное окно
class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\HelloWindow.ui', self)
        self.setWindowTitle('Приветствие')
        self.startWorkButton.clicked.connect(self.start)
        self.pixmap = QPixmap('files\HelloImage.jpg')
        self.image.setPixmap(self.pixmap)

        # Передвижение на центр экрана
        MoveFunction.move_to_senter(self)

    def start(self):
        self.close()
        cw.show()


class SettingsProgrammingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\SettingsProgrammingWindow.ui', self)
        self.setWindowTitle('Настройки')
        self.setWindowTitle('Настройки')
        self.initUi()

    def initUi(self):
        pass


# Окно настроек задач на системы счисления
class SettingsQuestionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\SettingsWindow.ui', self)
        self.setWindowTitle('Настройки')
        # Показывание окна поверх главного
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        # Передвижение на центр экрана
        MoveFunction.move_to_senter(self)
        self.initUi()

    def initUi(self):
        self.cancelButton.clicked.connect(self.close_window)
        self.acceptButton.clicked.connect(self.save)
        self.informationButton.clicked.connect(self.show_information)
        self.typesBox.clicked.connect(self.choice_type)
        self.easyButton.clicked.connect(self.easy)
        self.normalButton.clicked.connect(self.normal)
        self.hardButton.clicked.connect(self.hard)
        self.clearStatisticsButton.clicked.connect(DataBaseFile.delete)
        self.normalButton.setChecked(True)
        # Получение настроек при запуске
        a = DataBaseFile.find('''SELECT * FROM QuestionSettings''')

        self.type1Box.setEnabled(False)
        self.type2Box.setEnabled(False)
        self.difficulty = a[0]
        if a[1] == 'True':
            self.type1Box.setChecked(True)
        else:
            self.type1Box.setChecked(False)
        if a[2] == 'True':
            self.type2Box.setChecked(True)
        else:
            self.type2Box.setChecked(False)

    def close_window(self):
        # Закрытие и возвращение изменений
        self.errorLabel.setText('')
        a = DataBaseFile.find('''SELECT * FROM QuestionSettings''')
        self.difficulty = a[0]
        if self.difficulty == 1:
            self.easyButton.setChecked(True)
        elif self.difficulty == 2:
            self.normalButton.setChecked(True)
        elif self.difficulty == 3:
            self.hardButton.setChecked(True)
        if a[1] == 'True':
            self.type1Box.setChecked(True)
        else:
            self.type1Box.setChecked(False)
        if a[2] == 'True':
            self.type2Box.setChecked(True)
        else:
            self.type2Box.setChecked(False)
        self.close()

    def show_information(self):
        iw.show()

    def easy(self):
        self.difficulty = 1

    def normal(self):
        self.difficulty = 2

    def hard(self):
        self.difficulty = 3

    def save(self):
        # Проверка на наличие хотя бы 1 типа в генерации
        if not (self.type1Box.isChecked() or self.type2Box.isChecked()):
            self.errorLabel.setText('Вы не выбрали тип задач.')
        else:
            self.errorLabel.setText('')
            # Закрытие и сохранение изменений
            types = [self.type1Box.isChecked(), self.type2Box.isChecked()]
            DataBaseFile.update(self.difficulty, types)
            a = DataBaseFile.find('''SELECT * FROM QuestionSettings''')
            b = []
            mqw.difficulty = a[0]
            if a[1] == 'True':
                b.append(1)
            if a[2] == 'True':
                b.append(2)
            mqw.types = b
            self.close()

    def choice_type(self):
        # Вкл-выкл выбора типов задач(пользователем)
        if self.typesBox.isChecked():
            self.type1Box.setEnabled(True)
            self.type2Box.setEnabled(True)
        else:
            self.type1Box.setEnabled(False)
            self.type2Box.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mqw = MainQuestionWindow()
    mqw.first_question()
    mpw = MainProgrammingWindow()
    # mpw.first_question()
    apw = AnswerProgrammingWindow()
    spw = SettingsProgrammingWindow()
    cw = ChoiceWindow()
    sw = SettingsQuestionWindow()
    statw = StatisticsWindow.StatisticsWindow()
    iw = InformationWindow.InformationWindow()
    hw = HelloWindow()
    hw.show()
    sys.exit(app.exec_())
