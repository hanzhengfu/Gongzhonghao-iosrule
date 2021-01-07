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
body=''
osenviron={}
msg={}
hd={}
urllist=[]
hdlist=[]
btlist=[]
tmbdlist=[]
rdbdlist=[]
rflist=[]
uslist=[]
datalist=[]

def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     if(k>2 and k<16):
         response = requests.post(i,headers=hd,data=key,timeout=10)
         userRes=json.loads(response.text)
         hand(userRes,k)
     else:
         userRes = requests.get(i,headers=hd,timeout=10)
         if k!=16:
            userRes=json.loads(userRes.text)
         hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
   try:
     if k==1:
       msg=userRes['items']['nickname'][0:3]+f'''|{userRes['items']['today_score']}|{int(userRes['items']['score'])/10000}|{int(userRes['items']['read_article_second']/60)}|'''
       loger(msg)
       if userRes['items']['sign_status']==0:
          Av(urllist[k],hd,(k+1))
       m=int(userRes['items']['read_article_second']/60)
       if m<155:
         Av(urllist[2],hd,(3),tmbdlist[0])
     elif k==2:
        if userRes['status']==0:
           print(userRes['msg'])
        elif userRes['status']==1:
           print(str(userRes['score']))
     elif k==3:
        print(str(userRes['time']/60))
     elif k==4:
        if userRes['code']==0:
           print(userRes['msg'])
        elif userRes['code']==1:
           print(str(userRes['data']['score']))
     elif k==5:
        if userRes['code']==0:
           print(userRes['msg'])
        elif userRes['code']==1:
           print(str(userRes['data']['score']))
     elif k==6:
        if userRes['status']==0:
           print(userRes['msg'])
        elif userRes['status']==1:
           print(f'''{userRes['num']}-{userRes['score']}''')
        else:
           print('status...')
     elif k==7:
        if userRes['success']==True:
           print(str(userRes['items']['score']))
        elif userRes['success']==False:
           print(userRes['message'])
     elif k==8:
        if userRes['code']==0:
           print(userRes['msg'])
     elif k==9:
        if userRes['code']==0:
           print(userRes['msg'])
     elif k==10:
        if userRes['code']==1:
           print(userRes['msg'])
     elif k==11:
        if userRes['code']==0:
           print(userRes['msg'])
     elif k==12:
        if userRes['status']==1:
          print(f'''{userRes['data']['score']}-{userRes['data']['remainTurn']}''')
          if userRes['data']['doubleNum']>0:
            Av(urllist[k]+str(tm13()),hd,(k+1),body)
          if userRes['data']['remainTurn']>0:
            time.sleep(2)
            Av(urllist[k-1]+str(tm13()),hd,(k),body)
        else:
          print(userRes['msg'])
     elif k==13:
        if userRes['status']==1:
          print(f'''{userRes['data']['score']}-{userRes['data']['doubleNum']}''')
        elif userRes['status']==0:
           print(userRes['msg'])
        time.sleep(5)
        Av(urllist[k-2]+str(tm13()),hd,(k-1),body)
     elif k==14:
       if userRes['success']==True:
          temp1=userRes['data']['list']['sign']
          if len(temp1)==0:
            print('null.')
          elif len(temp1)>0:
            for i in temp1:
              if i['receive_status']==0:
                data='friend_uid='+str(i['friend_id'])
                Av(urllist[k],hd,(k+1),data)
                time.sleep(5)
              else:
                 print('complete.')
          temp2=userRes['data']['list']['unsign']
          if len(temp2)==0:
            print('Null..')
          elif len(temp2)>0:
             for i in temp2:
               if i['receive_status']==0:
                data='friend_uid='+str(i['friend_id'])
                Av(urllist[k],hd,(k+1),data)
                time.sleep(5)
               else:
                  print('complete.')
     elif k==15:
       print('抢红包',userRes)
       if userRes['success']==True:
          print(f'''{userRes['data'][0]['money']}''')
       else:
           print('no red')
     elif k==16:
       print('success')
     elif k==17:
      msg=str(int(userRes['user']['total_score'])/10000)+'\n'
      l=0
      for s in userRes['history']:
        l+=1
        if l==3:
          break
        msg+=s['idx'][6:10]+'|'
        for ss in s['group']:
          if ss['id']==5:
             continue
          msg+=ss['money']+'|'
        msg+='\n'
      loger(msg)
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
      # exit()


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
    
    
def tm13():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple())*1000+timeArray.microsecond/1000)
   return timeStamp   
    
@clock
def start():
   global result,hd,body,btlist,urllist,uslist,hdlist,tmbdlist,rdbdlist,bdlist,rflist,datalist
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('lucky_com_url',urllist)
   watch('lucky_com_hd',hdlist)
   hd=eval(hdlist[0])
   watch('lucky_us_ck',uslist)
   watch('lucky_tm_bd',tmbdlist)
   watch('lucky_rd_bd',rdbdlist)
   watch('lucky_sg_rf',rflist)
   watch('lucky_data_bd1',datalist)
   cc=0
   for cc in range(len(rflist)):
     hd['Referer']=rflist[cc]
     cc+=1
     result+=str(cc)+'.'
     for k in range(len(urllist)):
       if k==1 or k==2 or k==12 or k==14:
         continue
       if k==0:
          Av(urllist[k]+uslist[k],hd,(k+1))
       if k==3 or k==4 or k==7 or k==8 or k==9 or k==10 or k==13 or k==15 :
          Av(urllist[k],hd,(k+1))
       if k==5:
          Av(urllist[k],hd,(k+1),'type=taskCenter')
       if k==6:
          Av(urllist[k],hd,(k+1),datalist[0])
       if k==11:
          body=rflist[0].split('&')[15]+rflist[0].split('&')[8]
          Av(urllist[k]+str(tm13()),hd,(k+1),body)
       if k==16:
          Av(urllist[k]+rflist[0],hd,(k+1))
   
   print('🏆🏆🏆🏆运行完毕')
   pushmsg('Lucky-二库',result)
    
    
   
     
if __name__ == '__main__':
       start()
   
