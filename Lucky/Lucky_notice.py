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
tmbody=''
osenviron={}
msg={}
hd={}
urllist=[]
hdlist=[]
btlist=[]
tmbdlist=[]
rflist=[]
uslist=[]
datalist=[]
redlist=[]






def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     if(k>2 and k<6) or (k>6 and k<21):
         response = requests.post(i,headers=hd,data=key,timeout=10)
         userRes=json.loads(response.text)
         #print(userRes)
         hand(userRes,k)
     else:
         userRes = requests.get(i,headers=hd,timeout=10)
         if k!=21:
            userRes=json.loads(userRes.text)
            #print(userRes)
         hand(userRes,k)
   except Exception as e:
      print(str(e))


def hand(userRes,k):
   msg=''
   try:
     if k==1:
       msg=userRes['items']['nickname'][0:3]+f'''|{userRes['items']['today_score']}|{int(userRes['items']['score'])/10000}|{int(userRes['items']['read_article_second']/60)}|'''
       loger(msg)
       if userRes['items']['sign_status']==0:
          Av(urllist[k],hd,(k+1))
       m=int(userRes['items']['read_article_second']/60)
       if m<155:
         Av(urllist[2],hd,(3),tmbody)
         time.sleep(2)
         Av(urllist[2],hd,(3),tmbody)
         time.sleep(2)
         Av(urllist[2],hd,(3),tmbody)
         time.sleep(2)
         Av(urllist[2],hd,(3),tmbody)
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
       if userRes['code']==1:
        print('continue_card_days:'+str(userRes['data']['luck']['continue_card_days'])+"----luckdraw_num:"+star(userRes['data']['luck']['luckdraw_num']))
        if userRes['data']['user']['status']==0:
           Av(urllist[k],hd,(k+1))
        else:
           today=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%H:%M", )
           print('today:',today)
           if(int(today[0:2])>5 and int(today[0:2])<8):
              Av(urllist[k+1],hd,(k+2))
        if userRes['data']['user']['is_get_share_reward']==0:
           	Av(urllist[k+2],hd,(k+3))
           	time.sleep(10)
           	Av(urllist[k+3],hd,(k+4))
        if userRes['data']['luck']['luckdraw_num']=='1':
           	Av(urllist[k+4],hd,(k+5))
     elif k==7:
        if userRes['code']==0:
           print(userRes['msg'])
     elif k==8:
        if userRes['code']==0:
           print(userRes['msg'])
     elif k==9:
        if userRes['code']==1:
           print(userRes['msg'])
     elif k==10:
        if userRes['code']==0:
           print(userRes['msg'])
     elif k==11:
      if userRes['code']==1:
           print(userRes['data']['score'])
     elif k==12:
        if userRes['status']==1:
          print(f'''score:{userRes['data']['score']}-remainTurn:{userRes['data']['remainTurn']}''')
          if userRes['data']['doubleNum']>0:
            Av(urllist[k]+str(tm13()),hd,(k+1),body)
          if userRes['data']['remainTurn']>0:
            print('继续++++status:'+str(userRes['status']))
            time.sleep(2)
            Av(urllist[k-1]+str(tm13()),hd,(k),body)
            
        elif userRes['status']==0:
            print(userRes['msg'])
     elif k==13:
        print('doubleNum......')
        if userRes['status']==1:
          print(f'''score:{userRes['data']['score']}-doubleNum:{userRes['data']['doubleNum']}''')
        elif userRes['status']==0:
           print(userRes['msg'])
        time.sleep(5)
        Av(urllist[k-2]+str(tm13()),hd,(k-1),body)
     elif k==14:
        if userRes['status']==0:
           print(userRes['msg'])
        elif userRes['status']==1:
           print(f'''num:{userRes['num']}-score:{userRes['score']}''')
        else:
           print('status...')
     elif k==15:
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
     elif k==16:
       if userRes['success']==True:
          print(f'''{userRes['data'][0]['money']}''')
       else:
           print('no red')
     elif k==17:
       if userRes['success']==True:
          print(f'''{userRes['items']['score']}''')
     elif k==18:
       if userRes['status']==1:
         kkk=0
         for jjj in userRes['data']['chestOpen']:
           kkk+=1
           if jjj['received']==0:
             Av(urllist[k]+str(tm13()),hd,(k+1),'num='+str(kkk))
     elif k==19:
        if userRes['status']==1:
          print(userRes['data']['score'])
     elif k==20:
        if userRes['success']==True:
           print(str(userRes['items']['score'][0:3]))
        elif userRes['success']==False:
           print(userRes['message'])
     elif k==21:
       print('success')
     elif k==22:
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
    
    
def tm13():
   Localtime=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S.%f", )
   timeArray = datetime.strptime(Localtime, "%Y-%m-%d %H:%M:%S.%f")
   timeStamp = int(time.mktime(timeArray.timetuple())*1000+timeArray.microsecond/1000)
   return timeStamp   
    
@clock
def start():
  global result,hd,body,tmbody,btlist,urllist,uslist,hdlist,tmbdlist,rflist,datalist,redlist
  try:
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('lucky_com_url',urllist)
   watch('lucky_com_hd',hdlist)
   hd=eval(hdlist[0])
   watch('lucky_us_ck',uslist)
   watch('lucky_tm_bd',tmbdlist)
   watch('lucky_red_bd',redlist)
   watch('lucky_sg_rf',rflist)
   watch('lucky_data_bd',datalist)
   for cc in range(len(rflist)):
     hd['Referer']=rflist[cc]
     tmbody=tmbdlist[cc]
     print('账号'+str(cc+1))
     result+=str(cc+1)+'.'
     for k in range(len(urllist)):
       if k==1 or k==2 or (k>5 and k<11) or k==14 or k==18:
         continue
       if k==0:
          Av(urllist[k]+uslist[cc],hd,(k+1))
       if k==3 or k==4:
          Av(urllist[k],hd,(k+1))
       if k==11:
          body=rflist[cc].split('&')[15]+rflist[cc].split('&')[8]
          Av(urllist[k]+str(tm13()),hd,(k+1),body)
       if k==13:
          Av(urllist[k],hd,(k+1),'type=taskCenter')
       if k==16:
          Av(urllist[k],hd,(k+1),redlist[cc])
       if k==17:
          Av(urllist[k]+str(tm13()),hd,(k+1))
       if k==19:
          Av(urllist[k],hd,(k+1),datalist[cc])
       if k==5 or k==21:
          Av(urllist[k]+rflist[cc],hd,(k+1))
  except Exception as e:
      print(str(e))
  print('🏆🏆🏆🏆运行完毕')
  pushmsg('Lucky-二库2020109',result)
    
    
   
     
if __name__ == '__main__':
       start()
    
