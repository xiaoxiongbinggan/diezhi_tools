parameters1=input("请输入要查找的关键字1")
parameters2=input("请输入要查找的关键字2")
with open(r"C:\Users\Admin\Desktop\study\py\log.txt") as f:
#从windows直接复制的文件路径是反斜杠，open函数需要是斜杠，需要在路径外面加上r 
    list=[]
    while True:
        data=f.readline()
        if parameters1 in data:
            if parameters2 in data:
                print(data)
                list.append(data)
            else:
                pass
        else:
            pass
        if not data:
            break
        

    
    
 
