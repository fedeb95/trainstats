from updater import Updater
import sys

def main():
    u=Updater(sys.argv[1])
    u.update('brescia')
    u.update('milano centrale')
    
if __name__=="__main__":
    main()
