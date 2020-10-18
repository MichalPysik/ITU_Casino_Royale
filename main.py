import user
import automat
import time
import ruleta
import pickle
import dice
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtCore import pyqtSlot


def main():
    # GUI
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setGeometry(500, 500, 1000, 1000)
    widget.setWindowTitle("Casino Royale")
    widget.setStyleSheet("background-image: url(./SKINS/main_menu2.png)")
    layout = QGridLayout()
    widget.setLayout(layout)

    title = QLabel(widget)
    title.setText("Casino Royale")
    layout.addWidget(title, 1, 3)

    # RULETA
    btn_ruleta = QPushButton(widget)
    btn_ruleta.setText("Ruleta")
    btn_ruleta.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    btn_ruleta.setFixedSize(100, 30)
    layout.addWidget(btn_ruleta, 3, 3)

    # KOSTKY
    btn_kostky = QPushButton(widget)
    btn_kostky.setText("Kostky")
    btn_kostky.setFixedSize(100, 30)
    btn_kostky.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    layout.addWidget(btn_kostky, 4, 3)

    # AUTOMAT
    btn_automat = QPushButton(widget)
    btn_automat.setText("Kostky")
    btn_automat.setFixedSize(100, 30)
    btn_automat.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    layout.addWidget(btn_automat, 5, 3)

    widget.show()




    # load saved users
    users = user.get_users()
    # list is empty
    if not users:
        users.append(user.User('Pepa'))
    # us = user.User("novak")
    us = users[0]
    print("balance", us.get_balance())
    users.append(us)
    while True:
        print(us.get_name(), us.get_balance())
        # numbs = automat.automat(us, 1)
        # print(numbs)
        time.sleep(0.0005)
        numbs = ruleta.ruleta(1, "black", us)
        print("ruleta: ", numbs)
        print(us.get_name(), us.get_balance())
        us.add_balance(10000)
        break
        if us.get_balance() <= 0:
            break

    sys.exit(app.exec_())
exit(main())
