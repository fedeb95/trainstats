from updater import Updater
from threading import Timer
from config_manager import ConfigManager
import sys

path=sys.argv[1]
u=Updater(path)

def run():
    config=ConfigManager.get_instance(path)
    for station in config.config['stations']:
        u.update(station)
        print("updating {}".format(station))
    t= Timer(config.config['timer'],run) #TODO specify time in config
    t.start()

def main():
    run()
    
if __name__=="__main__":
    main()
