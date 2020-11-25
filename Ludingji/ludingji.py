import requests
import os
import re
import json





hd={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","As-Version": "v1","Content-Type": "application/json","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 qapp","Version": "1211","Version-Name": ""}

def ludingji(i,j,k):
    print('=🔔='*k)
    try:
       response = requests.post(i,headers=hd,data=j)
       if(k==8):
             res=json.dumps(response.text)
             res=re.compile('(\d+.\d+)').findall(res)
             res=res[0]+'-'+res[1]+'-'+res[2]
             print('out',res)
    except Exception as e:
      print(str(e))
      pass

def watch(flag,list):
   vip=''
   if flag in os.environ:
      vip = os.environ[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()
       




def start():
   funlist=[]
   urllist=[]
   tokenlist=[]
   tklist= []
   watch('ludingji_url',urllist)
   watch('ludingji_tk',tklist)
   watch('ludingji_token',tokenlist)
   for i in range(8):
      watch('ludingji_fun'+str(i),funlist)
   print(len(funlist))
   
   for j in range(len(tklist)):
       hd['tk']=tklist[j]
       hd['token']=tokenlist[j]
       print('===='+str(j))
       for k in range(8):
           ludingji(urllist[k],funlist[k*4+j],(k+1))
   print('🔔'*15)
if __name__ == '__main__':
       start()
    
