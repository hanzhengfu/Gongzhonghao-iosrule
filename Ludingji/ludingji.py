import requests
import os


hd={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","As-Version": "v1","Content-Type": "application/json","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 qapp","Version": "1211","Version-Name": ""}

def ludingji(i,j,k):
    print('=🔔='*k)
    try:
       response = requests.post(i,headers=hd,data=j)
       print(response.text)
    except Exception as e:
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
   for j in range(len(tklist)):
       hd['tk']=tklist[j]
       hd['token']=tokenlist[j]
       for k in range(8):
           ludingji(urllist[k],funlist[k][j],(k+1))
   print('🔔'*15)
if __name__ == '__main__':
       start()
    
