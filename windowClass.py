from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self, title):
        super().__init__()
        self.add_new_student_button = QPushButton(self)
        self.initUI(title, 4000, 1980)
        self.label = QLabel(self)
        self.add_new_student()
        # self.add_picture()

    def initUI(self, title, length, width):
        self.setWindowTitle(title)
        self.setStyleSheet('background-color:white')
        self.resize(length, width)
        self.showMaximized()

    # TODO after click on "Add New" button, will bring up another screen and start to create a new student
    def add_new_student(self):
        # self.add_new_student_button = QPushButton()
        # TODO Add font to it
        self.add_new_student_button.setText("Add New")
        self.add_new_student_button.setStyleSheet('font: 80px; background-color: yellow')
        self.add_new_student_button.adjustSize()
        self.add_new_student_button.move(550, 550)
        self.add_new_student_button.show()


    # def add_picture(self):
    #     plus_image = QLabel(self)
    #     plus_image.setText("")
    #     plus_image.setPixmap(QPixmap("plus.png"))
    #     plus_image.show()
    #     plus_image.mousePressEvent = self.add_student

    # @staticmethod
    # def add_student(event):
    #     print('clicked')
