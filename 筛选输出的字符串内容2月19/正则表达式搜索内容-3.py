import re

with open("log.txt","r") as f:
    while True:
      data=f.readline()

#不能用readlines，readlines会按行返回到一个列表中
      ui_name=re.match(r'.*activity.*267.*',data,re.S)
      if ui_name:
        print(ui_name.group())
      else:
        pass
      if not data:
         break
             

    


