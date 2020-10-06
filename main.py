import user
import automat
import time
import ruleta

def main():
    users = []
    us = user.User("novak")
    users.append(user)
    while True:
        print(us.get_name(), us.get_balance())
        #numbs = automat.automat(us, 1)
        #print(numbs)
        time.sleep(0.5)
        numbs = ruleta.ruleta(1,0,us)
        print("ruleta: ",numbs)
        print(us.get_name(), us.get_balance())


exit(main())
