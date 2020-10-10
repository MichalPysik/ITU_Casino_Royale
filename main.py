import user
import automat
import time
import ruleta


def main():
    users = []
    us = user.User("novak")
    users.append(us)
    while True:
        print(us.get_name(), us.get_balance())
        #numbs = automat.automat(us, 1)
        #print(numbs)
        time.sleep(0.0005)
        numbs = ruleta.ruleta(1,"black",us)
        print("ruleta: ",numbs)
        print(us.get_name(), us.get_balance())
        if us.get_balance() <= 0:
            break;
    for usr in users:
        print(usr.get_name())
        usr.save()


exit(main())
