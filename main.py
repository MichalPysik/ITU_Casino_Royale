import user
import automat
import time
import ruleta
import pickle
import dice

def main():

    # load saved users
    users = user.get_users()
    # list is empty
    if not users:
        users.append(user.User('Pepa'))
    #us = user.User("novak")
    us = users[0]
    print("balance",us.get_balance())
    users.append(us)
    while True:
        print(us.get_name(), us.get_balance())
        #numbs = automat.automat(us, 1)
        #print(numbs)
        time.sleep(0.0005)
        numbs = ruleta.ruleta(1,"black",us)
        print("ruleta: ",numbs)
        print(us.get_name(), us.get_balance())
        us.add_balance(10000)
        break
        if us.get_balance() <= 0:
            break

exit(main())
