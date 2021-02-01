

import requests
import json
import time
import timeit
import os
import re
import urllib
from datetime import datetime
from dateutil import tz


tg_bot_id=''
tg_member_id=''
osenviron={}
telelist=[]
result=''
msglist=[]
idlist=[]
uslist=[]






headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1'}



def loadbotmsg():
   try:
      global msglist
      username=''
      msgtext=''
      msglist=[]
      res=requests.get(tg_bot_id,headers=headers,timeout=10).json()
      #print(res)
      i=0
      for data in res['result']:
        i+=1
        if 'username' in data['message']['chat']:
          username=data['message']['chat']['username']
        else:
          username='XX'
        id=data['message']['chat']['id']
        if 'text' in data['message']:
          msgtext=data['message']['text']
        else:
          msgtext='no msg'
        smslist=[]
        cc=False
        for i in range(len(msglist)):
          if id in msglist[i]:
             msglist[i].append(msgtext)
             msglist[i].append(data['message']['date'])
             cc=True
        if cc==False:
          smslist.append(id)
          smslist.append(username)
          smslist.append(msgtext)
          smslist.append(data['message']['date'])
          msglist.append(smslist)
          
          
        msgdate=datetime.fromtimestamp(data['message']['date']).strftime('%Y-%m-%d %H:%M:%S')
        print('【'+str(i)+'】'+username+'_'+str(id)+'_'+msgtext+'_'+msgdate)
      print(msglist)
   except Exception as e:
      msg=str(e)
      print(msg)
def bot_sendmsg(id,title,txt):
   try:
      txt=urllib.parse.quote(txt)
      title=urllib.parse.quote(title)
      turl=f'''{tg_member_id}chat_id={id}&text={title}\n{txt}'''
      response = requests.get(turl)
      #print(response.text)
   except Exception as e:
      msg=str(e)
      print(msg)
def bot_chat(id,msg):
   try:
      if msg=='/help':
        bot_sendmsg(id,'','1.新闻请发news;2.视频请发video')
   except Exception as e:
      msg=str(e)
      print(msg)
      
def bot_check():
   try:
      msg=['/help']
      menu=['1.活动字母简写,水果(SG),年兽(NS)\n2.SGxxxxxxxxx@yyyyyyyyy@zzzzzzz\nNSzzzzzzzzz@ggggggggggghgh\n3.不同活动互助码用换行开始,格式不对机器人不提交',]
      num=0
      for i in range(len(msglist)):
        helpid=0
        txttm=0
        for j in range(len(msglist[i])):
           if msglist[i][j]==msg[0]:
             num+=1
             txttm=msglist[i][j+1]
        checktm=tm10()-txttm
        if checktm<60 and txttm>0:
          id=msglist[i][0]
          bot_sendmsg(id,'jd互助码格式:',menu[0])
          time.sleep(2)
        
   except Exception as e:
      msg=str(e)
      print(msg)



   
def tm10():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple()))
   return timeStamp
   
def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[🔔运行完毕用时%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    

def loaddata():
   global tg_bot_id,tg_member_id
   if "tg_bot_id" in os.environ:
      tg_bot_id = os.environ["tg_bot_id"]
   if "tg_bot_id" in osenviron:
      tg_bot_id = osenviron["tg_bot_id"]
   if not tg_bot_id:
       print(f'''【通知参数】 is empty,DTask is over.''')
       exit()
   if 'tg_member_id' in os.environ:
      tg_member_id = os.environ["tg_member_id"]
   if "tg_member_id" in osenviron:
      tg_member_id = osenviron["tg_member_id"]
   if not tg_member_id:
       print(f'''【通知参数】 is empty,DTask is over.''')
       exit()
       
       
def all():
   loaddata()
   loadbotmsg()
   bot_check()
   time.sleep(30)
   all()
   print('💎',result)
  
   print('its over')





@clock
def start():
   
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   all()


if __name__ == '__main__':
       start()
