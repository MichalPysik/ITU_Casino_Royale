from random import choice
import user
from games import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QMainWindow, QMenuBar, \
    QSpinBox, QTableWidget, QAction, QTableWidgetItem, QLineEdit, QComboBox, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QFont

main_win = ""
users = []
us = ""
bet = 1
choice = 0
slots = []
Alert = []
balance = ""
username = ""
result_int = 4
cervena = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
cerna = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
nOfDice = 1
throwTable = 0
DiePlayer = 0
DieEnemy = 0

def update_menu(user):
    global balance
    global username
    balance.setText(str(user.get_balance()))
    username.setText(user.get_name())

def help():
    global Alert

    okno = QWidget()
    Alert.append(okno)

    layout = QGridLayout()
    okno.setLayout(layout)

    text = QLabel(okno)
    text.setText("Help")
    layout.addWidget(text, 1, 1)

    okno.show()
    okno.update()

def delete_user(dropbox):
    global us
    global users
    global Alert

    users2 = []
    users3 = users.copy()
    for i in range(0,len(users)):
        if users3[i].get_name() != dropbox.itemText(dropbox.currentIndex()):
            users2.append(users3[i])
        else:
            users3[i].delete()

    users = users2
    if len(users2) == 0:
        new_user("NEW USER")
    else:
        us = users[0]
        update_menu(us)
        Alert.clear()



def new_user(text):
    global users
    global Alert
    global us

    for i in users:
        try:
            if i.get_name() == text.text():
                return
        except:
            if i.get_name() == text:
                return
    try:
        us = user.User(text.text())
    except: us = user.User(text)
    users.append(us)
    update_menu(us)
    Alert.clear()

def create_user():
    global users
    global us
    global Alert

    okno = QWidget()
    Alert.clear()
    Alert.append(okno)
    okno.setFixedSize(300, 150)
    okno.setWindowTitle("New user")

    layout = QGridLayout()
    okno.setLayout(layout)

    text2 = QLabel(okno)
    text2.setText("Input your username")
    layout.addWidget(text2, 1, 1)

    text = QLineEdit(okno)
    layout.addWidget(text, 2, 1)

    btn = QPushButton()
    btn.setText("Okey")
    btn.clicked.connect(lambda: new_user(text))
    layout.addWidget(btn, 3, 1)

    okno.show()
    okno.update()

def user_update(dropbox):
    global Alert
    global us
    global users

    for i in users:
        if i.get_name() == dropbox.itemText(dropbox.currentIndex()):
            us = i

    update_menu(us)
    Alert.clear()
    return

def change_user():
    global users
    global us
    global Alert

    okno = QWidget()
    okno.setFixedSize(300, 200)
    Alert.append(okno)

    okno.setWindowTitle("Change user")

    layout = QGridLayout()
    okno.setLayout(layout)

    dropbox = QComboBox(okno)
    dropbox.addItem(us.get_name())
    for user in users :
        if us is user:
            continue
        dropbox.addItem(user.get_name())

    text = QLabel(okno)
    text.setText("Choose user:")
    layout.addWidget(text, 2, 1)

    layout.addWidget(dropbox, 2, 2)

    btn = QPushButton(okno)
    btn.setText("Okey")
    btn.clicked.connect(lambda: user_update(dropbox))
    layout.addWidget(btn, 4, 1, 4, 2)

    btn2 = QPushButton(okno)
    btn2.setText("Create user")
    btn2.clicked.connect(create_user)
    layout.addWidget(btn2, 1, 1)

    btn3 = QPushButton(okno)
    btn3.setText("Delete user")
    btn3.clicked.connect(lambda: delete_user(dropbox))
    layout.addWidget(btn3, 1, 2)

    okno.show()
    okno.update()



def alert(bet, balance):
    global Alert
    new_win = QWidget()
    Alert.append(new_win)
    new_win.setFixedSize(300, 120)
    new_win.setWindowTitle("ERROR MESSAGE")
    text = QLabel("LOW BALANCE:\nBalance: " + str(balance) + "\nBet: " + str(bet))
    layout = QGridLayout()
    layout.addWidget(text, 1, 1)
    new_win.setLayout(layout)
    new_win.show()
    btn = QPushButton(new_win)
    btn.setText("Okey")
    btn.clicked.connect(new_win.close)
    layout.addWidget(btn, 2, 1)
    new_win.update()
    return

def dice_set_bet(value):
    global bet
    bet = value
    return

def change_nod(text):
    global nOfDice
    nOfDice = int(text[0])
    return

def roll_dice():
    global main_win
    global us
    global bet
    global nOfDice
    global throwTable
    global DiePlayer
    global DieEnemy

    if us.get_balance() < bet:
        alert(bet, us.get_balance())
        return

    for j in range (7):
        Item1 = QTableWidgetItem("")
        Item2 = QTableWidgetItem("")
        throwTable.setItem(j, 0, Item1)
        throwTable.setItem(j, 1, Item2)

    pT = []
    eT = []
    gS, pS, eS, pT, eT = Dice(us, bet, nOfDice)
    #print("hodnoty jsou" + str(gS) + "  " + str(pS) + "  " + str(eS))

    for i in range (nOfDice):
        Item1 = QTableWidgetItem(str(pT[i]))
        Item2 = QTableWidgetItem(str(eT[i]))
        Item1.setTextAlignment(Qt.AlignCenter)
        Item2.setTextAlignment(Qt.AlignCenter)
        throwTable.setItem(i, 0, Item1)
        throwTable.setItem(i, 1, Item2)

    Item1 = QTableWidgetItem(str(pS))
    Item2 = QTableWidgetItem(str(eS))
    Item1.setTextAlignment(Qt.AlignCenter)
    Item2.setTextAlignment(Qt.AlignCenter)
    throwTable.setItem(6, 0, Item1)
    throwTable.setItem(6, 1, Item2)

    if pT[nOfDice-1] == 1:
        DiePlayer.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/1yellow.png") } ')
    elif pT[nOfDice-1] == 2:
        DiePlayer.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/2yellow.png") } ')
    elif pT[nOfDice-1] == 3:
        DiePlayer.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/3yellow.png") } ')
    elif pT[nOfDice-1] == 4:
        DiePlayer.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/4yellow.png") } ')
    elif pT[nOfDice-1] == 5:
        DiePlayer.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/5yellow.png") } ')
    else:
        DiePlayer.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/6yellow.png") } ')

    if eT[nOfDice-1] == 1:
        DieEnemy.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/1red.png") } ')
    elif eT[nOfDice-1] == 2:
        DieEnemy.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/2red.png") } ')
    elif eT[nOfDice-1] == 3:
        DieEnemy.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/3red.png") } ')
    elif eT[nOfDice-1] == 4:
        DieEnemy.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/4red.png") } ')
    elif eT[nOfDice-1] == 5:
        DieEnemy.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/5red.png") } ')
    else:
        DieEnemy.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/6red.png") } ')

    update_menu(us)

    msgBox = QMessageBox(main_win)
    msgBox.setIcon(QMessageBox.Information)
    resText = ""
    if gS == 0:
        resText = us.get_name() + ", you have won " + str(bet) + " credit(s)"
    elif gS == 1:
        resText = us.get_name() + ", you have lost " + str(bet) + " credit(s)"
    else:
        resText = "It's a draw"
    msgBox.setText(resText)
    msgBox.setWindowTitle("Game Results")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.show()

    return


def gui_kostky():
    global main_win
    global widget
    global us
    global nOfDice
    global throwTable
    global DiePlayer
    global DieEnemy

    nOfDice = 1

    widget_to_delete = main_win.centralWidget()
    try:
        widget_to_delete.destroy()
    except:
        pass

    # new widget to replace main menu
    dice_wid = QWidget()
    dice_wid.setStyleSheet(".QWidget { border-image: url(./SKINS/DICE/DarkWood.jpg) } ")
    dice_wid.setGeometry(0, 0, main_win.width(), main_win.height())

    # main grid
    layout1 = QGridLayout(dice_wid)
    # grid for num of dice and ROLL button
    layout2 = QGridLayout(dice_wid)
    # grid for dice and rolled nums
    layout3 = QGridLayout(dice_wid)

    # set layout as main layout
    dice_wid.setLayout(layout1)

    # set layout for number of dice and roll button
    layout1.addLayout(layout2, 1, 1)
    # set layout for viewing dice and the numbers rolled in each turn
    layout1.addLayout(layout3, 2, 1)

    DiePlayer = QWidget(dice_wid)
    DiePlayer.setFixedSize(280, 300)
    DiePlayer.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/1yellow.png") } ')
    layout3.addWidget(DiePlayer, 2, 1)

    DieEnemy = QWidget(dice_wid)
    DieEnemy.setFixedSize(280, 300)
    DieEnemy.setStyleSheet('.QWidget { margin: 50px; border-image: url("SKINS/DICE/2red.png") } ')
    layout3.addWidget(DieEnemy, 2, 2)

    textPlayer = QLabel(dice_wid)
    textPlayer.setText(us.get_name())
    textPlayer.setFixedSize(280,50)
    textPlayer.setAlignment(Qt.AlignCenter)
    textPlayer.setStyleSheet(".QLabel { color: yellow; font: bold 28px }")
    layout3.addWidget(textPlayer, 1, 1)

    textEnemy = QLabel(dice_wid)
    textEnemy.setText("Enemy")
    textEnemy.setFixedSize(280,50)
    textEnemy.setAlignment(Qt.AlignCenter)
    textEnemy.setStyleSheet(".QLabel { color: red; font: bold 28px}")
    layout3.addWidget(textEnemy, 1, 2)

    rollBtn = QPushButton(dice_wid)
    rollBtn.setFixedSize(150, 100)
    rollBtn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    rollBtn.setStyleSheet("QPushButton { border-image: url(./SKINS/DICE/Roll.png) } QPushButton:hover { border-image: url(./SKINS/DICE/Roll_hover.png)} ")
    rollBtn.clicked.connect(roll_dice)
    layout2.addWidget(rollBtn, 1, 1)

    selectBox = QComboBox(dice_wid)
    selectBox.addItem("1 die")
    for i in range (5):
        selectBox.addItem(str(i+2)+" dice")
    selectBox.setFixedSize(90, 30)
    selectBox.activated[str].connect(change_nod)
    layout2.addWidget(selectBox, 1, 2)

    spacer1 = QLabel(dice_wid)
    layout2.addWidget(spacer1, 1, 3)
    spacer2 = QLabel(dice_wid)
    layout2.addWidget(spacer2, 1, 4)

    bet_text = QLabel(dice_wid)
    bet_text.setText("Bet amount:")
    bet_text.setAlignment(Qt.AlignCenter)
    bet_text.setStyleSheet(".QLabel { color: white; font: bold 18px}")
    layout2.addWidget(bet_text, 1, 5)

    bet = QSpinBox(dice_wid)
    bet.setFixedSize(90, 30)
    bet.setValue(1)
    bet.setMinimum(1)
    bet.setMaximum(1000)
    bet.valueChanged.connect(dice_set_bet)
    layout2.addWidget(bet, 1, 6)

    throwTable = QTableWidget(7, 2, dice_wid)
    throwTable.setHorizontalHeaderLabels([us.get_name(), "Enemy"])
    throwTable.setVerticalHeaderLabels(["1", "2", "3", "4", "5", "6", "="])
    #Wins = [20,40,80,80,80,150,300,300,800,800]
    #Signs = [1,2,3,4,5,6,7,8,9,0]
    #for pos in range(0,10):
    #    Item1 = QTableWidgetItem(str(Signs[pos]))
    #    Item1.setTextAlignment(Qt.AlignHCenter)
    #    Item2 = QTableWidgetItem(str(Wins[pos]))
    #    Item2.setTextAlignment(Qt.AlignHCenter)
    #    table.setItem(pos, 0, Item1)
    #    table.setItem(pos, 1, Item2)
    throwTable.setFixedSize(225, 240)
    throwTable.setStyleSheet("background-color: yellow; text-align: center")
    layout3.addWidget(throwTable, 2, 3)

    main_win.setCentralWidget(dice_wid)
    main_win.update()
    return

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
    btn_ruleta.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn_ruleta.setFixedSize(250, 250)
    btn_ruleta.setStyleSheet("QPushButton { border-image: url(./SKINS/ruleta_icona.png) } QPushButton:hover { border-image: url(./SKINS/ruleta_icona_hover.png)} ")
    btn_ruleta.clicked.connect(gui_ruleta)
    grid_games.addWidget(btn_ruleta, 1, 1)

    # KOSTKY
    btn_kostky = QPushButton(widget)
    btn_kostky.setFixedSize(250, 250)
    btn_kostky.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn_kostky.setStyleSheet("QPushButton { border-image: url(./SKINS/dices_icona.png) } QPushButton:hover { border-image: url(./SKINS/dices_icona_hover.png)} ")
    btn_kostky.clicked.connect(gui_kostky)
    grid_games.addWidget(btn_kostky, 1, 2)

    # AUTOMAT
    btn_automat = QPushButton(widget)
    btn_automat.setFixedSize(250, 250)
    btn_automat.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn_automat.setStyleSheet("QPushButton { border-image: url(./SKINS/slots_icona.png) } QPushButton:hover { border-image: url(./SKINS/slots_icona_hover.png)} ")
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
    global slots
    numb = Automat(us, bet)
    if type(numb) == bool:
        print("balance")
        alert(bet, us.get_balance())
        return
    if numb[0] == numb[1] and numb[0] == numb[2]:
        you_won()
    slots[0].setStyleSheet('.QWidget { border: 3px double rgba(126,26,27,1); background-image: url("SKINS/' + str(numb[0]) + '.png") } ')
    slots[1].setStyleSheet('.QWidget { border: 3px double rgba(126,26,27,1); background-image: url("SKINS/' + str(numb[1]) + '.png") } ')
    slots[2].setStyleSheet('.QWidget { border: 3px double rgba(126,26,27,1); background-image: url("SKINS/' + str(numb[2]) + '.png") } ')
    update_menu(us)
    return


def you_won():
    global Alert

    Alert.clear()
    alert = QWidget()
    Alert.append(alert)
    alert.setFixedSize(220, 150)
    layout = QGridLayout()
    label = QLabel(alert)
    label.setFont(QFont("Times", 30, QFont.Bold))
    label.setText("YOU WON")
    alert.setLayout(layout)
    layout.addWidget(label, 1, 1)
    btn = QPushButton(alert)
    btn.setText("Close")
    btn.clicked.connect(alert.close)
    layout.addWidget(btn, 2, 1)
    alert.show()
    alert.update()

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
    aut_wid.setStyleSheet(".QWidget { border-image: url('SKINS/automat_background.jpg') } ")

    aut_wid.setGeometry(0, 0, main_win.width(), main_win.height())

    # main grid
    layout2 = QGridLayout(aut_wid)
    # grid for 3 Slots
    layout = QGridLayout(aut_wid)
    # grid for buttons and bet
    layout3 = QGridLayout(aut_wid)

    # set layout as main layout
    aut_wid.setLayout(layout2)

    middle_widget = QWidget(aut_wid)
    middle_widget.setStyleSheet(".QWidget { background-color: rgba(255,215,0,0.85); border: 10px solid black; border-image: none } ")
    middle_widget.setFixedWidth(900)

    layout_for_middle = QGridLayout(middle_widget)
    middle_widget.setContentsMargins(20,30,20,20)
    middle_widget.setLayout(layout_for_middle)
    middle_widget.show()
    middle_widget.update()

    layout2.addWidget(middle_widget, 2, 2, 3, 2, Qt.AlignHCenter)

    right_menu = QWidget(aut_wid)
    right_menu.setLayout(layout3)
    right_menu.setFixedWidth(214)
    right_menu.setStyleSheet(".QWidget { background-color: rgba(255,215,0,0.8); border: 6px solid black; border-image: none  } ")
    right_menu.show()
    right_menu.update()

    layout2.addWidget(right_menu, 1, 1, 3, 1)

    # set table with prices
    table = QTableWidget(10, 2, right_menu)
    header = QHeaderView(Qt.Horizontal)
    header.setStyleSheet("background-color: rgba(0,0,0,0.1)")
    table.setHorizontalHeader(header)
    table.setHorizontalHeaderLabels(["Sign", "Win"])
    Wins = [20,40,80,80,80,150,300,300,800,800]
    Signs = [1,2,3,4,5,6,7,8,9,0]
    for pos in range(0,10):
        Item1 = QTableWidgetItem(str(Signs[pos]))
        Item1.setTextAlignment(Qt.AlignHCenter)
        Item1.setFlags(Qt.ItemIsEnabled)
        Item2 = QTableWidgetItem(str(Wins[pos]) + " x BET")
        Item2.setTextAlignment(Qt.AlignHCenter)
        Item2.setFlags(Qt.ItemIsEnabled)
        table.setShowGrid(False)
        table.setItem(pos, 0, Item1)
        table.setItem(pos, 1, Item2)
    table.setFixedSize(204, 330)
    table.verticalHeader().hide()
    table.setStyleSheet(".QTableWidget { background-color: rgba(0,0,0,0.3) ; border-bottom: 5px solid black }")
    layout3.addWidget(table, 1, 1, Qt.AlignTop)

    Slot = QWidget(aut_wid)
    Slot.setFixedSize(820, 440)
    Slot.setLayout(layout)
    Slot.setStyleSheet('.QWidget { border: 5px double rgba(126,26,27,1); background-color: rgba(165,125,0,0.7) }')
    Slot.show()
    Slot.update()
    # set layout for slots view
    layout_for_middle.addWidget(Slot, 1, 1, Qt.AlignTop)

    Slot1 = QWidget(Slot)
    Slot1.setFixedSize(250, 400)
    Slot1.setStyleSheet('.QWidget { border: 3px double rgba(126,26,27,1); background-image: url("SKINS/7.png") } ')
    layout.addWidget(Slot1, 1, 1)

    Slot2 = QWidget(Slot)
    Slot2.setFixedSize(250, 400)
    Slot2.setStyleSheet('.QWidget { border: 3px double rgba(126,26,27,1); background-image: url("SKINS/7.png") } ')
    layout.addWidget(Slot2, 1, 2)

    Slot3 = QWidget(Slot)
    Slot3.setFixedSize(250, 400)
    Slot3.setStyleSheet('.QWidget { border: 3px double rgba(126,26,27,1); background-image: url("SKINS/7.png") } ')
    layout.addWidget(Slot3, 1, 3)

    slots.clear()
    slots.append(Slot1)
    slots.append(Slot2)
    slots.append(Slot3)

    layout4 = QGridLayout(middle_widget)

    bet_text = QLabel(right_menu)
    bet_text.setText("BET:")
    bet_text.setFont(QFont("Times", 16, QFont.Bold))
    layout4.addWidget(bet_text, 2, 1, Qt.AlignRight)

    bet = QSpinBox(right_menu)
    bet.setValue(1)
    bet.setMinimum(1)
    bet.setMaximum(1000)
    bet.valueChanged.connect(automat_set_bet)
    bet.setStyleSheet("background-color: rgba(0,0,0,0.25)")
    bet.setFixedWidth(150)
    layout4.addWidget(bet, 2, 2, Qt.AlignLeft)

    btn = QPushButton(right_menu)
    btn.clicked.connect(action_automat)
    btn.setFixedSize(400, 40)
    btn.setText("PLAY")
    btn.setFont(QFont("Times",20,QFont.Bold))
    btn.setStyleSheet(".QPushButton { background-color: rgba(0,0,0,0.6) } ")
    layout4.addWidget(btn, 3, 1, 3, 2, Qt.AlignTop)
    layout_for_middle.addLayout(layout4, 2, 1, 2, 2,Qt.AlignCenter)

    btn_back = QPushButton(aut_wid)
    btn_back.setText("Back")
    btn_back.clicked.connect(set_main_menu)

    main_win.setCentralWidget(aut_wid)
    main_win.update()
    return

def ruleta_set_bet(value):
    global bet
    bet = value
    return

def ruleta_set_choice(value):
    global choice
    choice = value
    return

def action_ruleta():
    global us
    global bet
    global choice
    global result_int

    num = Ruleta(us, bet, choice)
    #if bet is larger than balance, alert
    if type(num) == bool:
        print("balance")
        alert(bet, us.get_balance())
        return
    result_int = (num)
    label_color()
    update_menu(us)
    return

# change label background based on number
def label_color():
    if result_int in cervena :
        result.setStyleSheet("QLabel{background-color: rgba(204, 0, 0, 1); border-radius: 10px}")
    elif result_int in cerna:
        result.setStyleSheet("QLabel{background-color: rgba(64, 64, 64, 1); border-radius: 10px}")
    else:
        result.setStyleSheet("QLabel{background-color: rgba(0, 153, 0, 1); border-radius: 10px}")
    return

def gui_ruleta():
    global main_win
    global widget
    global us

    widget_to_delete = main_win.centralWidget()
    try:
        widget_to_delete.destroy()
    except:
        pass

    # new widget to replace main menu
    rul_wid = QWidget()
    rul_wid.setStyleSheet(".QWidget { background-color: green } ")
    rul_wid.setGeometry(0, 0, main_win.width(), main_win.height())

    # main layout
    layout = QGridLayout(rul_wid)

    layout2 = QGridLayout(rul_wid)
    layout3 = QGridLayout(rul_wid)
    layout4 = QGridLayout(rul_wid)


    # set layout as main layout
    rul_wid.setLayout(layout)

    layout.addLayout(layout2, 0, 0)
    layout.addLayout(layout3, 4, 8)
    layout.addLayout(layout4, 2, 2)

    # button back to main menu
    btn_back = QPushButton(rul_wid)
    btn_back.setText("Back")
    btn_back.clicked.connect(set_main_menu)
    btn_back.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    layout2.addWidget(btn_back, 0, 0)

    # Bet button.
    # actualize balance label
    # actualize result label
    btn_bet = QPushButton(rul_wid)
    btn_bet.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn_bet.setText("Bet")
    btn_bet.clicked.connect(action_ruleta)
    btn_bet.clicked.connect(lambda: balance.setNum(us.get_balance()))
    btn_bet.clicked.connect(lambda: result.setNum(result_int))
    layout3.addWidget(btn_bet, 1, 2)

    # show balance of user
    balance = QLabel(rul_wid)
    balance.setNum(us.get_balance())
    balance.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    layout2.addWidget(balance, 0, 2)
    label1 = QLabel(rul_wid)
    label1.setText("Balance:")
    label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    layout2.addWidget(label1, 0, 1)
    

    # Bet label
    bet_label = QLabel(rul_wid)
    bet_label.setText("Bet: ")
    bet_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    layout3.addWidget(bet_label, 1, 0)

    # bet amount
    bet = QSpinBox(rul_wid)
    bet.setValue(1)
    bet.setMinimum(1)
    bet.setMaximum(100000)
    bet.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    bet.valueChanged.connect(ruleta_set_bet)
    layout3.addWidget(bet, 1, 1)

    # choice label
    choice_label = QLabel(rul_wid)
    choice_label.setText("Choice: ")
    choice_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    layout3.addWidget(choice_label, 0, 0)

    # Bet choice
    choice = QSpinBox(rul_wid)
    choice.setMinimum(0)
    choice.setMaximum(36)
    choice.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    choice.valueChanged.connect(ruleta_set_choice)
    layout3.addWidget(choice, 0, 1)

    # result label
    global result
    result = QLabel(rul_wid)
    result.setNum(result_int)
    result.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    result.setFixedSize(50, 50)
    result.setAlignment(Qt.AlignCenter)
    #number on color
    if result_int in cervena :
        result.setStyleSheet("QLabel{background-color: rgba(204, 0, 0, 1); border-radius: 10px}")
    elif result_int in cerna:
        result.setStyleSheet("QLabel{background-color: rgba(64, 64, 64, 1); border-radius: 10px}")
    else:
        result.setStyleSheet("QLabel{background-color: rgba(0, 153, 0, 1); border-radius: 10px}")
    layout4.addWidget(result, 1, 1)

    # update window
    main_win.setCentralWidget(rul_wid)
    main_win.update()

def main():
    # GUI

    global main_win
    global widget
    global users
    global us
    global username
    global balance

    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setWindowTitle("Casino Royale")
    main_win.setGeometry(0, 0, 1000, 1000)

    menubar = QMenuBar(main_win)
    menubar.setFixedHeight(50)
    main_win.setMenuBar(menubar)

    menu_layout = QGridLayout(main_win)
    menu_layout.setContentsMargins(0, 0, 0, 0)

    menubar.setLayout(menu_layout)
    # dummy to show grid
    dummy_for_grid = QAction("")
    menubar.addAction(dummy_for_grid)

    btn_menu = QPushButton(main_win)
    btn_menu.setText("Back to menu")
    btn_menu.clicked.connect(set_main_menu)
    menu_layout.addWidget(btn_menu, 1, 1)

    btn_menu2 = QPushButton(main_win)
    btn_menu2.setText("Change user")
    btn_menu2.clicked.connect(change_user)
    menu_layout.addWidget(btn_menu2, 1, 2)

    btn_menu3 = QPushButton(main_win)
    btn_menu3.setText("Help")
    btn_menu3.clicked.connect(help)
    menu_layout.addWidget(btn_menu3, 1, 3)

    menu_sub_layout = QGridLayout(main_win)
    menu_layout.addLayout(menu_sub_layout, 2, 1)

    user_menu = QLabel(main_win)
    user_menu.setText("User:")
    user_menu.setStyleSheet("background-color: yellow")
    user_menu.setFont(QFont("Arial", 12, QFont.Bold))
    menu_sub_layout.addWidget(user_menu, 2, 1, Qt.AlignRight)

    balance = QLabel(main_win)
    menu_sub_layout.addWidget(balance, 2, 4, Qt.AlignLeft)

    double_dot = QLabel(main_win)
    double_dot.setText("Balance:")
    double_dot.setFont(QFont("Arial", 12, QFont.Bold))
    menu_sub_layout.addWidget(double_dot, 2, 3, Qt.AlignRight)


    username = QLabel(main_win)
    menu_sub_layout.addWidget(username, 2, 2, Qt.AlignLeft)

    set_main_menu()

    main_win.show()

    # load saved users
    users = user.get_users()
    # list is empty
    if not users:
        users.append(user.User('Pepa'))
    us = users[0]

    balance.setText(str(us.get_balance()))
    username.setText(us.get_name())
    return app.exec_()


numb = main()
for i in users:
    i.save()
    print(i.get_balance())
exit(numb)
