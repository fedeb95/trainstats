from urllib import request,parse
from bs4 import BeautifulSoup
import re

URL='http://mobile.my-link.it/mylink/mobile/stazione'

class Treno:
    def __init__(self,direzione,destinazione,ora_arrivo,minuti_ritardo,blocco):
        self.direzione=direzione
        self.destinazione=destinazione
        self.ora_arrivo=ora_arrivo
        self.minuti_ritardo=minuti_ritardo  
        self.blocco=blocco

class Crawler:
    _TEMPO_REGEX='<img[ ]+src=\"[\./a-zA-Z0-9 ]+\"\/>([a-zA-Z0-9 ]+)</div>'
    _MINUTI_REGEX='ritardo[ ]+([0-9]+)[ ]+minuti'
    _DESTINAZIONE_REGEX='(Per|Da)[ ]+<strong>([A-Z0-9 ]+)<\/strong>'
    _ORA_ARRIVO_REGEX='Delle ore[ ]+<strong>([0-9]+:[0-9]+)<\/strong>'

    def __init__(self,url,stazione):
        self.stazione=stazione
        self.url=url
    
    def get_treni(self):
        data = parse.urlencode({'stazione':self.stazione}).encode()
        req=request.Request(self.url, data=data)
        resp=request.urlopen(req)
        page=resp.read()
        soup = BeautifulSoup(page, 'html.parser')
        blocchi=soup.find_all('div', class_="bloccotreno")
        treni=[]
        for b in blocchi:
            b=str(b).replace('\r\n','').replace('\t','')
            re_tempo=re.compile(Crawler._TEMPO_REGEX)
            re_minuti=re.compile(Crawler._MINUTI_REGEX)
            re_destinazione=re.compile(Crawler._DESTINAZIONE_REGEX)
            re_ora_arrivo=re.compile(Crawler._ORA_ARRIVO_REGEX)

            match=re_destinazione.search(b)
            if match is not None:
                dest=match.group(2).strip() 
                direzione=match.group(1).strip()
            else:
                dest=''
                direzione=''
            
            match=re_ora_arrivo.search(b)
            if match is not None:
                ora_arrivo=match.group(1)
            else:
                ora_arrivo=''

            match=re_tempo.search(b)
            if match is not None:
                ritardo=match.group(1).strip()
                match=re_minuti.search(ritardo)
            if match is not None:
                minuti_ritardo=int(match.group(1)) 
            else:
                minuti_ritardo=0
            treni.append(Treno(direzione,dest,ora_arrivo,minuti_ritardo,b))
        return treni
         
def main():
    c=Crawler(URL,'brescia')    
    treni=c.get_treni() 
    for t in treni:
        print('{} {} delle ore: {} ritardo: {}'.format(t.direzione,t.destinazione,t.ora_arrivo,t.minuti_ritardo))

            
if __name__=='__main__':
    main() 
