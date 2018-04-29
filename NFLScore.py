import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET
import time
from datetime import datetime

print("NFL Score:")
hnn = [] #Home Team
vnn = [] #Away Team
hs = [] #Home Team Score
vs = [] #Away Team Score
on_start = True; #on start

#Runs on start to get current teams and scores
def onStart():
    print("Initializing...")
    for e in root[0]:
        hnn.append(e.get('hnn'))
        hs.append(e.get('hs'))
        vs.append(e.get('vs'))
        vnn.append(e.get('vnn'))

#Loops every 5 second getting new scores and checking old
while True:
    #get xml and format
    e = requests.get('http://www.nfl.com/liveupdate/scorestrip/ss.xml')
    root = ET.fromstring(e.content)
    #onStart
    if (on_start):
        onStart()
        on_start = False
    tVs = []
    tHs = []
    #get current scores
    for e in root[0]:
        tHs.append(e.get('hs'))
        tVs.append(e.get('vs')) 
    #check if scores are different
    if(tHs != hs or tVs != vs):
        for x in range (0, len(tVs)):
            if(vs[x] != tVs[x]):
                #send req vnn[x]
                requests.get('http://192.168.0.132/'+vnn[x].title())
                vs[x] = tVs[x] 
                print(vnn[x].title() + " just scored")
            if(hs[x] != tHs[x]):          
                #send req hnn[x]
                requests.get('http://192.168.0.132/'+hnn[x].title())
                hs[x] = tHs[x] 
                print(hnn[x].title() + " just scored")
       
    print(str(datetime.now()))           
    time.sleep(5)
    
