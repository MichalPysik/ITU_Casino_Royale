import user
import automat
import ruleta
import dice
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QMainWindow, QMenuBar, \
    QMenu, QSpinBox, QTableWidget, QTableView
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

    #new widget to replace main menu
    aut_wid = QWidget(main_win)
    aut_wid.setStyleSheet("background-color: red ")
    aut_wid.setGeometry(0, 0, main_win.width(), main_win.height())

    #main grid
    layout2 = QGridLayout(aut_wid)
    #grid for 3 Slots
    layout = QGridLayout()
    #grid for buttons and bet
    layout3 = QGridLayout()

    #set layout as main layout
    aut_wid.setLayout(layout2)

    #set layout for slots view
    layout2.addLayout(layout, 2, 1)
    #set layout for control bar
    layout2.addLayout(layout3,3,2)

    #set table with prices
    table = QTableWidget(10, 2, aut_wid)
    table.setHorizontalHeaderLabels(["Sign", "Win"])
    Wins = []
    Signs = []
    table.setFixedSize(204,360)
    table.verticalHeader().hide()
    layout2.addWidget(table, 2, 2)





    Slot1 = QWidget(aut_wid)
    #Slot1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    Slot1.setGeometry(0, 0, 80, 80)
    Slot1.setStyleSheet(".QWidget { background-color: black} ")
    layout.addWidget(Slot1, 1, 1)

    Slot2 = QWidget(aut_wid)
    Slot2.setGeometry(0,0,80,80)
    Slot2.setStyleSheet(".QWidget { border: 2px solid black } ")
    layout.addWidget(Slot2, 1, 2)

    Slot3 = QWidget(aut_wid)
    Slot3.setGeometry(0,0,80,80)
    Slot3.setStyleSheet(".QWidget { border: 2px solid black } ")
    layout.addWidget(Slot3, 1, 3)

    btn = QPushButton(aut_wid)
    btn.clicked.connect(action_automat)
    #btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn.setGeometry(0,0,70,40)
    layout3.addWidget(btn, 1, 1)

    bet = QSpinBox(aut_wid)
    layout3.addWidget(bet, 1, 3)

    bet_text = QLabel(aut_wid)
    bet_text.setText("bet:")
    layout3.addWidget(bet_text, 1,2)


    #widget.hide()
    #aut_wid.show()
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

    menubar = QMenuBar(main_win)
    menu = QMenu("Change user")
    menu2 = QMenu("Menu")
    menu3 = QMenu("Help")


    menubar.addMenu(menu2)
    menubar.addMenu(menu)
    menubar.addMenu(menu3)


    main_win.setMenuBar(menubar)

    widget = QWidget()
    main_win.setCentralWidget(widget)
    widget.setGeometry(500, 500, 1000, 1000)
    main_win.setWindowTitle("Casino Royale")
    widget.setStyleSheet(".QWidget{ border-image: url(./SKINS/main_menu.jpg)}")

    layout = QGridLayout(widget)
    widget.setLayout(layout)

    grid_games = QGridLayout()
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

    # load saved users
    users = user.get_users()
    # list is empty
    if not users:
        users.append(user.User('Pepa'))
    # us = user.User("novak")
    us = users[0]
    return app.exec_()
exit(main())
