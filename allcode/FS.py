import os
import json

new_dict={"code":200,"msg":"\u8bfb\u53d6\u52a9\u529b\u7801\u6210\u529f","data":["12333","2222","3333","ghhhjjj"],"powered by":"888888","sponsored by":"66666"}


with open("./allcode/gc.json","w") as f:
   json.dump(new_dict,f)
   print("加载入文件完成...")
