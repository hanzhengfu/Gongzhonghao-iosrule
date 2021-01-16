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
osenviron={}
hd={}
body1={}
body2={}
body3={}
body4={}
urllist=[]
hdlist=[]
bdlist=[]
alllist=[]







def Av(i,hd,k,key=''):
   try:
      if k==1:
        response = requests.get(i,headers=hd,timeout=10)
        response.raise_for_status()
        response.close()
        userRes=json.loads(response.text)
      if k==2 or k==3 or k==4:
         response = requests.post(i,headers=hd,data=key,timeout=10)
         response.raise_for_status()
         response.close()
         userRes=json.loads(response.text)
      hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
   msg=''
   try:
    if k==1:
      if userRes['resultCode']== 1:
         print('complte...')
    if k==2:
       if userRes['resultCode']== 1:
         print(str(userRes['data']['goldCoinNumber']))
       else:
          print(userRes['errorDesc'])
    if k==4:
       if userRes['resultCode']== 1:
         print(str(userRes['data']['goldCoinAmt']))
       else:
          print(userRes['errorDesc'])
   except Exception as e:
      print(str(e))
      
      

def watch(flag,list):
   vip=''
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
    
  
def tm13():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple())*1000+timeArray.microsecond/1000)
   return timeStamp   
  
def allinone(i):
   global alllist
   try:
     response = requests.get(i,timeout=10)
     response.raise_for_status()
     response.close()
     userRes=json.loads(response.text)
     if userRes['resultCode']==1:
      for l in userRes['data']['records']:
        alllist.append(l['videoPublishId'])
   except Exception as e:
      print(str(e))



      
def allinbd(alllist):
   global body1,body2,body3,body4
   try:
      tf=[1,1,1,1,2]
      body2['videoList'][0]['videoId']=random.choice(alllist)
      body2['videoList'][0]['type']=random.choice(tf)
      body2['videoList'][1]['videoId']=random.choice(alllist)
      body2['videoList'][1]['type']=body2['videoList'][0]['type']
      
      
      body1['videoPublishId']=body2['videoList'][0]['videoId']
      body1['playTimeLenght']=random.randint(4,30)
      body1['videoTime']=random.randint(20,60)
      
      body3['videoPublishId']=body2['videoList'][1]['videoId']
      body3['playTimeLenght']=random.randint(4,30)
      body3['videoTime']=random.randint(20,60)
      
      body4['liveId']=random.choice(alllist)
   except Exception as e:
      print(str(e))
      
      

@clock
def start():
   global result,hd,body1,body2,body3,body4,alllist,hdlist,urllist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   try:
      watch('xb_main_url',urllist)
      watch('xb_main_hd',hdlist)
      watch('xb_main_bd',bdlist)
      allcode=[]
      for i in range(1,len(urllist)-2):
        allcode.append(urllist[i])
      allinone(random.choice(allcode))
      for ac in range(60):
        for k in range(0,4):
          body1=json.loads(bdlist[0])
          body2=json.loads(bdlist[1])
          body4=json.loads(bdlist[2])
          hd=eval(hdlist[k])
          st=hd['traceid']
          hd['traceid']=st.replace(st[20:33],str(tm13()))
          if len(alllist)>10:
            allinbd(alllist)
          print('【C】'+str(k+1))
          Av(urllist[1]+body1['videoPublishId'],hd,(1))
          
          time.sleep(random.randint(1,5))
          Av(urllist[0],hd,(2),json.dumps(body2))
          print('await.............' )
          time.sleep(random.randint(15,20))
          Av(urllist[len(urllist)-2],hd,(3),json.dumps(body3))
          Av(urllist[len(urllist)-1],hd,(4),json.dumps(body4))
          time.sleep(random.randint(15,20))
        print('<<<<<<<'+str(ac+1)+'>>>>>>>>>')
   
   except Exception as e:
      print(str(e))
   print('🏆🏆🏆🏆运行完毕')
    
    
   
     
if __name__ == '__main__':
       start()
    
