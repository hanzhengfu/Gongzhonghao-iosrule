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


djj_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''
   
   
result=''
osenviron={}
msg={}
hd={}
urllist=[]
hdlist=[]
btlist=[]
bdlist=[]



def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     if(k==8):
         response = requests.post(i,headers=hd,data=key,timeout=10)
         userRes=json.loads(response.text)
         hand(userRes,k)
     else:
         response = requests.get(i,headers=hd,timeout=10)
         userRes=json.loads(response.text)
         
         hand(userRes,k)
         
   except Exception as e:
      print(str(e))


def hand(userRes,k):
   try:
     
     if k==1:
       msg['continuation']=str(userRes['data']['signIn']['continuation'])+'Days'
       if userRes['data']['signIn']['today']==0:
          Av(urllist[1]+btlist[0],hd,2)
     elif k==2:
        print(userRes['message'])
     elif k==3:
        msg['times']=str(userRes['data']['times'])+'times'
        print('times:'+str(userRes['data']['times'])+'|next_time:'+str((userRes['data']['next_time']-userRes['data']['last_time'])/60))
        if userRes['data']['next_time']<=0:
          Av(urllist[3]+btlist[0],hd,4)
     elif k==4:
        print(userRes['message'])
     elif k==5:
        if userRes['code']==0:
           print(str(userRes['data']['curr_task'])['amount'])
        else:
           print(userRes['message'])
     elif k==6:
        msg['nick']=userRes['data'][0]['data']['member_info']['nickname']+'|'+userRes['data'][2]['newCoinSystem']['todayCoinsFormat']+'|'+str(int(userRes['data'][2]['newCoinSystem']['remainderCoinsFormat'])/10000)+'|'+userRes['data'][2]['newCoinSystem']['read_time']['time']
        
     elif k==7:
        ll=''
        for ii in userRes['data']['coin']:
           ll+=str(ii['date'])+'-'+str(ii['num'])+'\n'
        msg['income']=ll
        loger(msg['nick']+'|'+msg['continuation']+'|'+msg['times']+'\n'+msg['income'])
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


def pushmsg(title,txt,bflag=1,wflag=1,tflag=1):
   try:
     txt=urllib.parse.quote(txt)
     title=urllib.parse.quote(title)
     if bflag==1 and djj_bark_cookie.strip():
         print("\n【Bark通知】")
         purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
         response = requests.post(purl)
   except Exception as e:
      print(str(e))
   try:
     if tflag==1 and djj_tele_cookie.strip():
         print("\n【Telegram消息】")
         id=djj_tele_cookie[djj_tele_cookie.find('@')+1:len(djj_tele_cookie)]
         botid=djj_tele_cookie[0:djj_tele_cookie.find('@')]

         turl=f'''https://api.telegram.org/bot{botid}/sendMessage?chat_id={id}&text={title}\n{txt}'''

         response = requests.get(turl,timeout=5)
   except Exception as e:
      print(str(e))
   try:
     if wflag==1 and djj_sever_jiang.strip():
        print("\n【微信消息】")
        purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
        headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        body=f'''text={txt})&desp={title}'''
        response = requests.post(purl,headers=headers,data=body)
   except Exception as e:
      print(str(e))
def loger(m):
   #print(m)
   global result
   result +=m     

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
   global result,hd,btlist,urllist,hdlist,bdlist,taskidlist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('laji_hd',hdlist)
   hd=eval(hdlist[0])
   watch('laji_url',urllist)
   watch('laji1_ck',btlist)
   watch('laji1_nk',btlist)
   for k in range(len(urllist)):
       if k==1 or k==3 or k==4:
         continue
       elif k==5:
          Av(urllist[k]+btlist[1],hd,(k+1))
       else:
          Av(urllist[k]+btlist[0],hd,(k+1))
   print('🏆🏆🏆🏆运行完毕')
   pushmsg('垃圾AppQ_二库1',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
