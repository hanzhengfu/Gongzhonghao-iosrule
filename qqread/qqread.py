import requests
import os
import re
import json
import time
import random
import timeit
import urllib
result=''
djj_bark_cookie='azjFQzUeTG5hVYx7cRJRTU'
djj_sever_jiang='SCU124498Teba646995bd06b3e0bb128138c7f06ac5fa7952a4ab92'


osenviron={}
osenviron['ios_url']='''https://mqqapi.reader.qq.com/mqq/user/init
https://mqqapi.reader.qq.com/mqq/red_packet/user/page?fromGuid=
https://mqqapi.reader.qq.com/mqq/me/query/page
https://mqqapi.reader.qq.com/mqq/red_packet/user/watch_video
https://mqqapi.reader.qq.com/mqq/red_packet/user/treasure_box
https://mqqapi.reader.qq.com/mqq/red_packet/user/treasure_box_video
https://mqqapi.reader.qq.com/mqq/red_packet/user/clock_in/page
https://mqqapi.reader.qq.com/mqq/red_packet/user/read_book
https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?scene=1008&refer=pages%2Fbook-shelf%2Findex&bid=27693007&readTime=188447&read_type=0&conttype=1&read_status=0&chapter_info=%5B%7B%222%22%3A%7B%22readTime%22%3A188447%2C%22pay_status%22%3A0%7D%7D%5D&sp=-1
https://mqqapi.reader.qq.com/mqq/page/config?router=%2Fpages%2Fbook-read%2Findex&options=%7B%22bid%22%3A%2227693007%22%2C%22cid%22%3A%222%22%2C%22from%22%3A%22shelf%22%7D
https://mqqapi.reader.qq.com/mqq/sign_in/user
https://mqqapi.reader.qq.com/mqq/red_packet/user/read_time?seconds=
https://mqqapi.reader.qq.com/mqq/red_packet/user/read_time_reward?seconds=
https://mqqapi.reader.qq.com/mqq/bookShelfInit
https://mqqapi.reader.qq.com/mqq/pickPackageInit
https://mqqapi.reader.qq.com/mqq/pickPackage?readTime=
'''
osenviron['ios_bt']='''ywguid=164399269;ywkey=ywFQl0eNUCrs;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=166019834;ywkey=ywip07A0groH;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=166909638;ywkey=ywfOZ4KSX3bR;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=1951201271;ywkey=yw4yvgKaMSnb;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=1518936683;ywkey=ywquW9dsDU4O;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=18336323;ywkey=yw9RzWgZ7ug6;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=858483425;ywkey=ywUNJnfxx6mA;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=1720277098;ywkey=ywHHtCh7XRBV;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=461528264;ywkey=ywabYFOi2tzh;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=12694594;ywkey=ywZOFwuTqPVF;platform=ios;channel=mqqmina;mpVersion=0.28.0
ywguid=1330182460;ywkey=ywPzzfendt5Q;platform=ios;channel=mqqmina;mpVersion=0.28.0
'''

osenviron['ios_hd']='''
{'User-Agent': 'QQ/8.4.10.666 CFNetwork/978.0.7 Darwin/18.7.0','Content-Type':'application/json'}
'''

msg=''
hd=''
urllist=[]
hdlist=[]
btlist=[]
redtm=0
def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   if(k==6):
       time.sleep(31)
   try:
     if(k==11):
         response = requests.post(f'''{i}{key}''',headers=hd,data={},timeout=10)
     else:
         response = requests.get(f'''{i}{key}''',headers=hd,timeout=10)
         print(f'''{i}{key}''')
     print(response.text)
     userRes=json.loads(response.text)
     hand(userRes,k)
   except Exception as e:
      print(str(e))

def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   if "DJJ_BARK_COOKIE" in os.environ:
     djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
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
   global redtm
   if(userRes['code']==0):
       if(k==1):
           msg+=f'''【{userRes['data']['user']['nickName']}】'''
       elif(k==2):
            msg+=f'''-{userRes['data']['user']['amount']}'''
       elif(k==3):
             msg+=f'''-{userRes['data']['readTime']}min-{userRes['data']['balance']['allBalance']}'''
       elif(k==10):
           if(userRes['msg']=='ok'):
              for item in userRes['data']['pageParams']['readTimeRewardTask']:
                  if item['enableFlag']==1 and item['doneFlag']==0:
                      Av(urllist[11],hd,12,item['seconds'])
              for item in userRes['data']['pageParams']['readTimeTask']:
                    if item['enableFlag']==1 and item['doneFlag']==0:
                       Av(urllist[12],hd,13,item['seconds'])
       elif(k==14):
           if(userRes['code']==0 and userRes['data'] ['hasPackage']):
             redtm=userRes['data']['readTime']
             print(redtm)
             print(len(urllist))
             print(urllist[14])
             Av(urllist[14],hd,15)
       elif(k==15):
         if userRes['code']==0:
           for item in userRes['data']:
                if(not item['isPick'] and item['readTime']<=redtm):
                   Av(urllist[15],hd,16,item['readTime'])
             
   loger(msg)             
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
def notice(b,e):
    ll=False
    start_time = datetime.strptime(str(datetime.now().date())+b, '%Y-%m-%d%H:%M')
    end_time =  datetime.strptime(str(datetime.now().date())+e, '%Y-%m-%d%H:%M')
    now_time = datetime.now()
    if now_time > start_time and now_time<end_time:
       ll=True
    else:
    	ll=False
    return ll
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
   global result,hd
   watch('ios_url',urllist)
   watch('ios_hd',hdlist)
   watch('ios_bt',btlist)
   time.sleep(random.randint(1,4))
   for j in range(len(btlist)):
       print(f'''===={str(j)}({len(urllist)})''')
       hd=eval(hdlist[0])
       hd['Cookie']=btlist[j]
       for k in range(len(urllist)):
         if(k==11 or k==12 or k==14 or k==15):
            continue
         Av(urllist[k],hd,(k+1))
       print(str(j)+'💎'*15+'干就完了')
       result+='\n'
   if notice('4:00','5:00') or notice('22:00','23:00') or notice('13:00','14:00'):
       pushmsg('干就完事儿了',result)
if __name__ == '__main__':
       start()
    
