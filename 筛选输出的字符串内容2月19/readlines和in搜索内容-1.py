import csv
import os

with open("log.txt" ,"r") as f:
#这个写法不用close，f=open(file)需要写close
    data = f.readlines()
#这个地方不能用read，readlines返回值是一个列表，每一行对应列表的每一个元素，对应下文中的line就是每一行
#如果用read，返回值是一整坨，下文中的line就对应log.txt中每一个字母，就无法对每一行的内容进行遍历
list=[]
newlist=[] 
for line in data:

    if "activity" in line:
        
        if "267" in line:
            
            #new_line=print(line.strip('cocos2d: fullPathForFilename:'),end='')
            #这种偷懒写在一句代码里的方法，遍历查找到的内容被打印出来没有传递到new_line
            #遍历打印可以把列表，每一个元素逐行输出，想要每行一句话格式的时候可以用
            #end='' 打印内容行尾默认是换行，替换成空白，即取消换行
            new_line=line.strip('cocos2d: fullPathForFilename:')
            list.append(new_line)
            #line.strip去除每行开头的多余字符串
            #end=''，将print打印每行的结尾默认的换行替换成空白，即不换行
        else:
            pass
    else:
        pass

#（判断列表里是否有重复行，去除重复内容）
   
for i in list:
    if i in newlist:
        pass
    else:
        newlist.append(i)

print(newlist)

    

#（列表内容写入单独文件）
with open('newfile.csv','w',newline='')as newf:#newline=''避免读取的内容有空行
    for i in list:
        newf.write(i)
with open('newfile2.txt','w',newline='')as newf:
    for i in newlist:
        newf.write(i)

#列表不能直接写入到文件里，必须逐行写入，下面借助csv下的函数实现
with open('csvfile2.csv','w',newline='')as newf:
    writer=csv.writer(newf)
    writer.writerow(list)
#writerow把列表每一个元素写入到一个单元格里，writerows把列表每一个字母写入到单元格里
