import user
from games import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QMainWindow, QMenuBar, \
     QSpinBox, QTableWidget, QAction
from PyQt5.QtGui import QFont

main_win = ""
users = []
us = ""
bet = 1


def gui_kostky():
    pass


def gui_ruleta():
    pass


def set_main_menu():
    global main_win

    # if widget was not set dont try to delete it
    widget_to_delete = main_win.centralWidget()
    try:
        widget_to_delete.destroy()
    except:
        pass

    widget = QWidget()
    widget.setGeometry(0, 0, main_win.width(), main_win.height())

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

    main_win.setCentralWidget(widget)
    main_win.update()


def automat_set_bet(value):
    global bet
    bet = value
    return


def action_automat():
    global us
    global bet
    numb = Automat(us, bet)
    print(numb, bet)
    return


def gui_automat():
    global main_win
    global widget
    global us

    widget_to_delete = main_win.centralWidget()
    try:
        widget_to_delete.destroy()
    except:
        pass

    # new widget to replace main menu
    aut_wid = QWidget()
    aut_wid.setStyleSheet("background-color: red ")
    aut_wid.setGeometry(0, 0, main_win.width(), main_win.height())

    # main grid
    layout2 = QGridLayout(aut_wid)
    # grid for 3 Slots
    layout = QGridLayout(aut_wid)
    # grid for buttons and bet
    layout3 = QGridLayout(aut_wid)

    # set layout as main layout
    aut_wid.setLayout(layout2)

    # dummy = QSpacerItem(0,0,QSizePolicy.Ignored,QSizePolicy.Ignored)
    # layout2.addItem(dummy, 1, 1)

    # set layout for slots view
    layout2.addLayout(layout, 2, 2)
    # set layout for control bar
    layout2.addLayout(layout3, 3, 3)

    # set table with prices
    table = QTableWidget(10, 2, aut_wid)
    table.setHorizontalHeaderLabels(["Sign", "Win"])
    Wins = []
    Signs = []
    table.setFixedSize(204, 360)
    table.verticalHeader().hide()
    layout2.addWidget(table, 2, 3)

    Slot1 = QWidget(aut_wid)
    Slot1.setGeometry(0, 0, 150, 150)
    # Slot1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    Slot1.setStyleSheet('.QWidget { border: 2px solid black; background-color: white } ')
    layout.addWidget(Slot1, 1, 1)

    Slot2 = QWidget(aut_wid)
    Slot2.setGeometry(0, 0, 150, 150)
    Slot2.setStyleSheet(".QWidget { border: 2px solid black; background-color: white } ")
    layout.addWidget(Slot2, 1, 2)

    Slot3 = QWidget(aut_wid)
    Slot3.setGeometry(0, 0, 150, 150)
    Slot3.setStyleSheet(".QWidget { border: 2px solid black; background-color: white } ")
    layout.addWidget(Slot3, 1, 3)

    btn = QPushButton(aut_wid)
    btn.clicked.connect(action_automat)
    btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn.setGeometry(0, 0, 70, 40)
    layout3.addWidget(btn, 1, 1)

    bet = QSpinBox(aut_wid)
    bet.setValue(1)
    bet.setMaximum(1000)
    bet.valueChanged.connect(automat_set_bet)
    layout3.addWidget(bet, 1, 3)

    bet_text = QLabel(aut_wid)
    bet_text.setText("bet:")
    layout3.addWidget(bet_text, 1, 2)

    main_win.setCentralWidget(aut_wid)
    main_win.update()
    return


def main():
    # GUI

    global main_win
    global widget
    global users
    global us

    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setWindowTitle("Casino Royale")
    main_win.setGeometry(0, 0, 1000, 1000)

    menubar = QMenuBar(main_win)
    main_win.setMenuBar(menubar)

    menu_layout = QGridLayout(main_win)
    menu_layout.setContentsMargins(0, 0, 0, 0)

    menubar.setLayout(menu_layout)
    # dummy to show grid
    dummy_for_grid = QAction("dummy")
    menubar.addAction(dummy_for_grid)

    btn_menu = QPushButton(main_win)
    btn_menu.setText("Back to menu")
    btn_menu.clicked.connect(set_main_menu)
    menu_layout.addWidget(btn_menu, 1, 1)

    btn_menu2 = QPushButton(main_win)
    btn_menu2.setText("Change user")
    menu_layout.addWidget(btn_menu2, 1, 2)

    btn_menu3 = QPushButton(main_win)
    btn_menu3.setText("Help")
    menu_layout.addWidget(btn_menu3, 1, 3)

    set_main_menu()

    main_win.show()

    # load saved users
    users = user.get_users()
    # list is empty
    if not users:
        users.append(user.User('Pepa'))
    us = users[0]

    return app.exec_()


numb = main()
for i in users:
    i.save()
    print(i.get_balance())
exit(numb)
