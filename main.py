import user
import automat
import time
import ruleta
import pickle
import dice
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QLineEdit, QMainWindow
from PyQt5.QtGui import QFont

main_win = ""
widget = ""
users = []
us = ""


def gui_kostky():
    print("hello")
    pass

def gui_ruleta():
    pass

def action_automat():
    global us
    automat.automat(us,10)
    return

def gui_automat():

    global main_win
    global widget
    global us

    aut_wid = QWidget(main_win)
    aut_wid.setStyleSheet("background-color: red ")
    layout2 = QGridLayout(aut_wid)
    layout = QGridLayout(aut_wid)

    aut_wid.setLayout(layout2)
    layout2.addLayout(layout, 2, 2)
    aut_wid.setGeometry(500, 500, main_win.width(), main_win.height())
    Slot1 = QWidget(aut_wid)
    layout.addWidget(Slot1, 1, 1)
    Slot2 = QWidget(aut_wid)
    layout.addWidget(Slot2, 2, 1)
    Slot3 = QWidget(aut_wid)
    layout.addWidget(Slot3, 3, 1)
    btn = QPushButton(aut_wid)
    btn.clicked.connect(action_automat)
    layout2.addWidget(btn, 1, 2)


    widget.hide()
    aut_wid.show()
    Slot1.setStyleSheet("background-color: red")
    main_win.setCentralWidget(aut_wid)
    main_win.update()
    print("hello2")
    return



def main():
    # GUI

    global main_win
    global widget
    global users
    global us

    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setGeometry(0, 0, 1000, 1000)


    widget = QWidget()
    main_win.setCentralWidget(widget)
    widget.setGeometry(500, 500, 1000, 1000)
    main_win.setWindowTitle("Casino Royale")
    widget.setStyleSheet(".QWidget{ border-image: url(./SKINS/main_menu.jpg)}")

    layout = QGridLayout(widget)
    widget.setLayout(layout)

    grid_games = QGridLayout(widget)
    layout.addLayout(grid_games, 2, 1)

    title = QLabel(widget)
    title.setFont(QFont('Arial', 50))
    title.setText("Casino Royale")
    title.setStyleSheet("border-image: none; color: white")
    layout.addWidget(title, 1, 1)

    # RULETA
    btn_ruleta = QPushButton(widget)
    btn_ruleta.setText("Ruleta")
    btn_ruleta.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn_ruleta.setFixedSize(250, 250)
    btn_ruleta.setStyleSheet("background-color: green")
    btn_ruleta.clicked.connect(gui_ruleta)
    grid_games.addWidget(btn_ruleta, 1, 1)

    # KOSTKY
    btn_kostky = QPushButton(widget)
    btn_kostky.setText("Kostky")
    btn_kostky.setFixedSize(250, 250)
    btn_kostky.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn_kostky.setStyleSheet("background-color: yellow")
    btn_kostky.clicked.connect(gui_kostky)
    grid_games.addWidget(btn_kostky, 1, 2)

    # AUTOMAT
    btn_automat = QPushButton(widget)
    btn_automat.setText("Automat")
    btn_automat.setFixedSize(250, 250)
    btn_automat.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn_automat.setStyleSheet("background-color: red")
    btn_automat.clicked.connect(gui_automat)
    grid_games.addWidget(btn_automat, 1, 3)

    main_win.show()
    widget.show()




    # load saved users
    users = user.get_users()
    # list is empty
    if not users:
        users.append(user.User('Pepa'))
    # us = user.User("novak")
    us = users[0]
    return app.exec_()
exit(main())
