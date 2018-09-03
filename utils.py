from config_manager import ConfigManager
from dbmanager import DBManager
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def add_time(df):
    df['time']=pd.to_datetime(df['year'].astype(str)+'/'+df['month'].astype(str)+'/'+df['day'].astype(str)+' '+df['ora_arrivo'])

def get_data():
    conf=ConfigManager.get_instance('config')
    dbman=DBManager('delays','all',conf.config['conn_string'])
    return pd.DataFrame(list(dbman.get_all()))

# per i treni che fanno ritardo, correlazione tra durata del ritardo e ora di arrivo
def scatter_ora_ritardo(df):
    df=df.copy()
    df=df[df['ritardo']>0]
    to_encode=df['ora_arrivo']
    encoder=LabelEncoder().fit(to_encode) 
    ora_encoded=encoder.transform(to_encode)
    lr=LinearRegression().fit(ora_encoded.reshape(-1,1),df['ritardo']) 
    df['ora_arrivo']=ora_encoded
    p=df.plot.scatter('ora_arrivo','ritardo')
    hrange=[[df['ora_arrivo'].min()],[df['ora_arrivo'].max()]]
    line, =plt.plot(hrange,lr.predict(hrange),color='black')
    line.set_dashes([3,2])
    line.set_linewidth(2)
    return p

# frequenze relative dei ritardi per ora di arrivo (senza considerare i minuti)
def freq_ora(df):
    # non considerare il minuto di arrivo
    df['ora_arrivo']=df['ora_arrivo'].apply(lambda s: int(s.split(':')[0])) 
    return pd.crosstab(df['ora_arrivo'],columns='Rel',normalize=True).plot()

# frequenze congiunte 
def freq_cong_stazioni(df,bins,normalize=True):
    cong=pd.crosstab(pd.cut(df['ritardo'],bins=bins),df['stazione'],normalize=normalize)
    return cong.plot.bar()
