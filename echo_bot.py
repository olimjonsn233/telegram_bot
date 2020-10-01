import requests
import json
def getUpdates():
    url=requests.get('https://api.telegram.org/bot1116012218:AAHXOvZDGx3mUOBIaCD7B83r7v4eJevk8GQ/getUpdates')
    data=url.json()
    id1=data['result'][a]['message']['chat']['id']
    txt=data['result'][a]['message']['text']
    return id1,txt
def habaryoz(id1,txt):
    yukla={'chat_id':id1,'text':txt}
    url1=requests.get('https://api.telegram.org/bot1116012218:AAHXOvZDGx3mUOBIaCD7B83r7v4eJevk8GQ/sendMessage',params=yukla)
    
a=0
while a<50:
    try:
        id1,txt=getUpdates()
        habaryoz(id1,txt)
        a+=1
    except:
        print('sizi kutayverish jonga tegdi yozing!')
        continue