import requests
import os
import re
import json
import time
import random
import timeit
import urllib
from datetime import datetime
from dateutil import tz

result=''
djj_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''
osenviron={}
hd=''
msg=''
urllist=[]
hdlist=[]
btlist=[]
bdlist=[]



def Av(i,hd,k,key=''):
   print('【'+str(k)+'】')
   try:
      if k!=3:
        response = requests.get(i,headers=hd,timeout=10)
        response.raise_for_status()
        response.close()
        userRes=json.loads(response.text)
      if k==3:
         response = requests.post(i,headers=hd,data=key,timeout=10)
         response.raise_for_status()
         response.close()
         userRes=json.loads(response.text)
      hand(userRes,k)
   except Exception as e:
      print(str(e))

def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   global djj_tele_cookie
   if "DJJ_BARK_COOKIE" in os.environ:
      djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_TELE_COOKIE" in os.environ:
      djj_tele_cookie = os.environ["DJJ_TELE_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in os.environ:
      vip = os.environ[flag]
   if flag in osenviron:
      vip = osenviron[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()
def hand(userRes,k):
   msg=''
   try:
     if(userRes['resultCode']==1):
       if(k==1):
         msg+=userRes['data']['customerInfo']['nickname'][0:2]+'|'
       if(k==2):
         msg+=str(userRes['data']['balanceSum']/100)+'|'+str(userRes['data']['coinSum'])
         bd=eval(bdlist[0])
         if userRes['data']['coinSum']/10000>15:
           bd['amount']=1500
         Av(urllist[k],hd,(k+1),json.dumps(bd))
       if(k==3):
          print('wtok(1/2):::::'+str(userRes['data']['withdrawRes']))
   except Exception as e:
     msg+=str(e)
   loger(msg)
def pushmsg(title,txt,bflag=1,wflag=1,tflag=1):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   if bflag==1 and djj_bark_cookie.strip():
      print("\n【通知汇总】")
      purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
      response = requests.post(purl)
      #print(response.text)
   if tflag==1 and djj_tele_cookie.strip():
      print("\n【Telegram消息】")
      id=djj_tele_cookie[djj_tele_cookie.find('@')+1:len(djj_tele_cookie)]
      botid=djj_tele_cookie[0:djj_tele_cookie.find('@')]

      turl=f'''https://api.telegram.org/bot{botid}/sendMessage?chat_id={id}&text={title}\n{txt}'''

      response = requests.get(turl)
      #print(response.text)
   if wflag==1 and djj_sever_jiang.strip():
      print("\n【微信消息】")
      purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
      headers={
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
      body=f'''text={txt})&desp={title}'''
      response = requests.post(purl,headers=headers,data=body)
    #print(response.text)
def loger(m):
   global result
   result +=m     
def getid(id):
   lll=id.split(';')
   for l in lll:
     if l.find('ywguid=')>=0:
      return l[(l.find('ywguid=')+7):len(l)]
def tm13():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple())*1000+timeArray.microsecond/1000)
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
    
@clock
def start():
   global result,hd,urllist,hdlist,bdlist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('xb_sub_url',urllist)
   watch('xb_main_hd',hdlist)
   watch('xb_sub_bd',bdlist)
   for j in range(len(hdlist)):
       print(f'''C【{str(j+1)}】''')
       result+='['+str(len(hdlist))+'-'+str(j+1)+']'
       hd=eval(hdlist[j])
       st=hd['traceid']
       hd['traceid']=st.replace(st[20:33],str(tm13()))
       for k in range(len(urllist)):
         if k!=2:
             Av(urllist[k],hd,(k+1))
         
              
         time.sleep(5)
       result+='\n'
   print('🏆🏆🏆🏆运行完毕')
   pushmsg('二库_XB20210127周三',result)
     
     
    
   
     
if __name__ == '__main__':
       start()
    
