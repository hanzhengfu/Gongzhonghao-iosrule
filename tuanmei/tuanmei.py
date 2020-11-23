import requests
import json
import time
import timeit
import os
import re
import urllib
from datetime import datetime
from dateutil import tz



result=''
djj_bark_cookie=''
djj_sever_jiang=''
ios_mt_body=''
ios_mt_pass1=r'''{"riskRequest":"{\"fingerprint\":\"######/Bt3V+FvHcLwTBkTYmkBS3/AxbNAKxb+PStQUkx0m7uhN/Ly8CJGocOBCiNYjbe/hisFFXWwxl8zPUs7rNs0P7VoYiz19vveVxhb0oxK17f9pUZPVtJvuY8YWMTlQXSGMoCsB+0rEcgPZShcOP3huhGbp49ragyGBJQxxCQ7A0qzq439vvj3OqD5ukhNlkS0KVyj9kcmN/2AKT70xmoiZrZgIcG/QvCuAfwBM9QB8pKAWkSpPAyLj1kIWrA6E30hzkbYLbcktmK7XBBZDFw7MEz9/2LOrTS5BqE4KKYWyFCDgZkId8tWq/vWjMi1nRnm4B+66+AZJeAZmh9Rm5FD9LdY+KX4cTC9FxVn7xwhPchPzZzFSbVYRpvh1qrhg58eKMmIR6n8bvifWzVCFET8yYFFGvyKv/FYZh7b4z5daMzHEgEbDnzsceh5UWliusP5sHQYFYKcqtOboR7li4/YU99iwapyK/5lTiH8aZAw8OTTh28UHN4TS4yAMHq8ZSC3VJNU5cgru8fqTJAYtEeBmSyMwJM1Y+XSAEwEDZsBFR450CRZPjYN68Kz/GrmN5HAYtelIK+Cy2hR+ZDkSAR3vIWSlvRNKWHEcXGW3LDgNKN/ckuBJMmlYbd0rClgq/cX7DqcSHXQHJzrdRBcwnG1QMmf9FdqOaxtJaJ9xDPZri6HJDUzzKi9IZ+HoDmiq6DhxI0Ko1xQj+PpiWJFSnK3Mn+EnJS8JS4mvtJUqeGanwo1aZGj7G1b26fXkySqN4YrZp9OzPKI9hlzFR95fYWsjeaMiJBvLe0UJ+6FHoKUm4vrYL2KrHhWn6GY0CtUVr4dx/zm01ntdMrQ3JypxM0hiykgQl0n/hYwxLla5U5/2a/XtbKuZDQ8MMNcHPltBdDtNkBSOjtLPkcBiC5CikPeb0QqFz1TvEIHO6GshGmofww1zQc10zwmntPnTRDEV0/o3092GPTnGyvBnJfAkUX8ueX1kgAeC3oUprcA8yszWmMUU3+7mk5NoSuGf+fdmbXnDoV3purnfyoYJjRpdqKhgum7fiSwZGRwK/P1smR+/t3p672DKE350LBJf1dahw06o+5xzxB5fcnFDjRjYPI7FdgIAIFYuxk7GM0yoMMdoj4r0cKXlPo1IG3kgZPXGezCzioA2lwF2aR19SHaIige0aT5lWVeN7kwObVeF9drbMaRHxLW6gCyqW0eZFbLkwvhsrWSQtdmDhK0gDTAHS8Fc7T35duqeCaqcy/lQEePVgbvuInPw==\",\"uuid\":\"00000000000004120AC8FA0124E08BB39BE5C96A57258A157407299565126496\",\"version\":\"10.8.201\",\"platform\":5,\"app\":\"0\",\"campaignPlatform\":\"14\",\"campaignType\":\"1\",\"h5Fingerprint\":\"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\"}","code":""}'''
ios_mt_pass2=r'''{"riskRequest":"{\"fingerprint\":\"######/6yXzx9eOoagSVWSttNLWn3fMn94+lsd44a5bwNeEe4ABGffPO0tCVB89oGelOo6P7KvP/ktXJ7ecUgf0IPg7RlPmk5DuA4BEgTCRAznrqDUhrUUScFCz3nJrQ+B/PQ8Ej1GG3r7JGJhBIRX9xEFFAJEa06NTI/5FVy3RPG2S0TmI/3IClADg9MB6ZW5jgFw1DpjUwK5q29DDVOOEIik83VcedKCRNag98UMEnbDG0LIT0Ryz2VdsHMimK2ZwIkuDFD3DfISmh00G/dgFPEkpDNW38P654wK+9TweZc3NUnEYxEXg/OJOj73dRCwwmNHUDjzRoaCqYtqfukT5Y3mMhx68/f48qQ95UwsJNEYs8PyjTc6Dr09Rkpbi/xPmAkK3FjrdRN98VEYIxZMJKl0tteyG6bNVxk/11AujCA4CWbLt3z1owWTwahWTJLLb9GOi5rUzvfqi+wIuJHkKcSJApQ+d4CuKbpDglvDuj19WuKmPHtwnn7uDZM4k1StL3PiIyhh/ITkymeJMxUVMUGhMH9ojRFADdFT6D84Omffg5BWb94g/EMNirigLl5OkLp+GxDxhh775vOP4Iio4xBXAf7bVyk8qmLuF/rUZZe5fUZ58GQFlb5bj5UMgE4EXKsfUNVcCsfWTwcm5aj0ImCc24zOgWSh7J0OUE8neHVaAU2qmQlr96R/I5ul4EuHYncshSukOh/9EP7+LNN1FxY9s7DYusAwCcaa5c2kM/ysb6zcEq6SHQRMMBjdqfs2kxqUb1DFiTOMe54TFJF+GHN+ZSiyGgQAKTUkyHqqJH+w/g+YGr2F96sXlDv43pFK8PPKD8Vdgfyn39rPQoVYx0HnlyfvUbreU29L7x1mHr6jQFxXChwH5X47EbqZ0Hk9dP/VE8QaQOtxHdi43Xro9RsFaVx1KB0zinZeivl39/FNrdJosrX3PA5geAG06liqD7jUhcJC9BnOOBLbHfOOvbDR+HkJJ4QdyypAYiYUnJeIaibdOj6FcbZez6MnHdze+NMywRqU3+PZpCwRTu2HBQIck6ryhGHTtBSlwIBnp+CPOdT4R+1PqEvCbjHXuhnr2DQDKDa0OzgLDzyNixFB9xbzWb3RAJ0vMnxj8PqYJkJ7E4Dya93iqm8SN/k4JzKOoXxLHkB3tUu+cwJkLj38HflhdXEi22qHVZJ0F8onLPAihAR2wYydzDISOzFZiZxatl8PPiwGi2MsX1NycI7/ous/uNPeciTCtRByWTYvg7fPsASK922ttYXjNyD9t5BPsyvUtVklT0FU4sPztfXEPQqc3eld2x5r4cTnPP0i8b271\",\"uuid\":\"00000000000008F5CD7519A5B4D7AA2545079CF72D487A160589514215282742\",\"version\":\"11.3.402\",\"platform\":5,\"app\":\"0\",\"campaignPlatform\":\"14\",\"campaignType\":\"1\",\"h5Fingerprint\":\"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\"}","code":""}'''


ios_mt_cookie=''






headers={"Content-Type": "application/json","Host": "i.meituan.com","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 TitansX/11.27.5 KNB/1.0 iOS/12.4 meituangroup/com.meituan.imeituan/10.8.201 meituangroup/10.8.201 App/10110/10.8.201 iPhone/iPhoneXR WKWebView"}



def login(ck):
   print('登录')
   msg='【登录】'
   try:
      response=taskurl('signin/getAccuAmount/100219',ck,2)
      #print(response.text)
      obj=json.loads(response.text)
      if (obj['code']==0):
           msg+= f'''
      【账号】{obj['data']['userName']}
      【奖励金】{obj['data']['amount']/100}元
      【累计签到天数】{obj['data']['totalSignDays']}天,打败全国{obj['data']['percentage']}的用户
      【补签卡】{obj['data']['supplementCardCount']}张
      '''
      else:
            msg+='please get your cookies'
   except Exception as e:
      msg+=str(e)
      #print(msg)
   loger(msg)
   
def sign(ck,bd):
   print('\n签到')
   msg='【签到】'
   try:
       login=taskurl('signin/signpost/100219',ck,1,bd)
       print(login.text)
       obj=json.loads(login.text)
       if (obj['code']==2002):
          msg+=f'''{obj['msg']}'''
   except Exception as e:
      msg+=str(e)
      #print(msg)
   loger(msg+'\n')
	


def taskurl(func,ck,flag,bd={}):
   url=f'''https://i.meituan.com/evolve/{func}'''
   headers['Cookie']=ck
   if flag==2:
      taskres = requests.get(url,headers=headers,timeout=10)
   elif (flag==1):
      taskres = requests.post(url,headers=headers,data=bd)
   return taskres
	


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
    

def check(st,flag,list):
   result=''
   global djj_bark_cookie
   global djj_sever_jiang
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
       return list
   else:
       print('DTask is over.')
       exit()
def mt():
   cklist=[]
   bdlist=[]
 
   check(ios_mt_cookie,'IOS_MT_COOKIE',cklist)
   bdlist=check(ios_mt_body,'IOS_MT_BODY',bdlist)
   #print(bdlist)
   #bdlist.append()
   
   for index in range(len(cklist)):
      print(f'''>>>>>>>>>【账号{str(index+1)}开始】''')
      if cklist[index]:
        if index==0:
            newbody=ios_mt_pass1.replace('######',bdlist[0])
        elif index==1:
         	  newbody=ios_mt_pass2.replace('######',bdlist[1])
        login(cklist[index])
        sign(cklist[index],newbody)
   pushmsg('meituan',result)
   print('its over')





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
   
@clock
def start():
   
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   mt()

def main_handler(event, context):
    return start()

if __name__ == '__main__':
       start()
