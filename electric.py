import requests
import json
import time
import os
import re
import urllib
from datetime import datetime
from dateutil import tz



result=''
djj_bark_cookie=''
djj_sever_jiang=''
wetcard_wasai_cookie = ''
wetcard_wasailist=[]



headers={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "application/json","Host": "minigame.ucpopo.com","Referer": "https://servicewechat.com/wx02dc0dd2497b3b80/21/page-frame.html","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/4G Language/zh_CN",}



def levelup(ck):
   msg=''
   electric={
   	1:'喷壶',
   	2:'活水车',
   	3:'自动灌溉'
   }
   try:
      for id in range(1,4):
        print(f'''\n{electric[id]}升级中...''')
        login=taskurl(f'''electric/levelup?electricid={str(id)}&''',ck)
        print(login.text)
        if(json.dumps(login.text).find('\u8bf7\u5148\u767b\u5f55')>=0):
           print()
           pushmsg('wasai','please get your cookies')
           exit()
        login=taskurl(f'''electric/done?electricid={str(id)}&''',ck)
        print(login.text)
   except Exception as e:
      msg=str(e)
      print(msg)
   loger(msg)

def taskurl(func,ck):
   url=f'''https://minigame.ucpopo.com/wasai/{func}appName=wasai&env=release&ver=1.0.9&{ck}'''
   taskres = requests.get(url,headers=headers)
   return taskres
	



def check(st,flag,list):
   result=''
   if "DJJ_BARK_COOKIE" in os.environ:
     djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in os.environ:
      st = os.environ[flag]
   if st:
       for line in st.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
   else:
       print('DTask is over.')
       return 
   j=0
   for count in list:
      j+=1
      print(f'''>>>>>>>>>【账号{str(j)}开始】''')
      if count:
         levelup(count)
   


def pushmsg(title,txt,bflag=1,wflag=1):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   if bflag==1 and djj_bark_cookie.strip():
      print("\n【通知汇总】")
      purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
      response = requests.post(purl)
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
   print(m)
   global result
   result +=m
   
   



print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
check(wetcard_wasai_cookie,'WETCACARD_WASAI_COOKIE',wetcard_wasailist)
