from updater import Updater
from threading import Timer
import sys

u=Updater(sys.argv[1])

def run():
    u.update('brescia')
    u.update('milano centrale')
    u.update('verona porta nuova')
    print("updating...")
    t= Timer(240,run) #TODO specify time in config
    t.start()

def main():
    run()
    
if __name__=="__main__":
    main()
