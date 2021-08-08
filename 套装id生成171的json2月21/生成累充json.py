import pandas as pd
import os
import math

def get_clothse_id():
    suitid = int(input('清输入套装id：'))
    clothes_id = pd.read_excel("玩家_成就表.xlsx", sheet_name='Sheet2', index_col='id')  # index_col设置某一列为索引
    return clothes_id.loc[suitid].dropna().tolist()

def set_json(clothes_id):
    os.remove('set_json.txt')
    with open('set_json.txt',mode='w') as f:
        count=1
        for x in clothes_id:
            x=math.floor(x)
            dic = dict(id=x, type=0, num=1)
            if count<len(clothes_id):
                f.write(str(dic))
                f.write(',')
            else:
                f.write(str(dic))
            count+=1
#这里mode='w'是指with open整个模块是只写模式，
# 在这个模块内的读写操作是可以追加的，两次write可以都写进去
#for循环的计数器初始值要写在外面

if __name__ == '__main__':
    set_json(get_clothse_id())
