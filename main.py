import sys
import user
import automat
import time

def main():
    users = []
    us = user.user("novak")
    while True:
        print(us.get_name(), us.get_balance())
        numbs = automat.automat(us, 1)
        print(numbs)
        time.sleep(0.5)


exit(main())