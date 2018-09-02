from config_manager import ConfigManager
from dbmanager import DBManager
import pandas as pd

def add_time(df):
    df['time']=pd.to_datetime(df['year'].astype(str)+'/'+df['month'].astype(str)+'/'+df['day'].astype(str)+' '+df['ora_arrivo'])

def get_data():
    conf=ConfigManager.get_instance('config')
    dbman=DBManager('delays','all',conf.config['conn_string'])
    return pd.DataFrame(list(dbman.get_all()))
