import pandas as pd
import math


def need_clothes_count():
    sheet1_info = pd.read_excel(r'C:\Users\Admin\Desktop\study\py\越南表\《奇暖越南》6.5.0版本需求表.xlsx', sheet_name='活动衣服需求',
                                header=1)

    sheet2_info = pd.read_excel(r'C:\Users\Admin\Desktop\study\py\越南表\《奇暖越南》6.5.0版本需求表.xlsx', sheet_name='商店上新')
    sheet3_info = pd.read_excel(r'C:\Users\Admin\Desktop\study\py\越南表\《奇暖越南》6.5.0版本需求表.xlsx', sheet_name='签到49期',
                                header=None)

    sheet1_id = sheet1_info.loc[:, 'id'].dropna().tolist()

    sheet2_id = sheet2_info.iloc[:, 0].dropna().tolist()
    sheet3_id = sheet3_info.iloc[:, 12].dropna().tolist()
    all_clothes_id = []
    all_clothes_id.extend(sheet1_id)

    all_clothes_id.extend(sheet2_id)
    all_clothes_id.extend(sheet3_id)
    all_clothes_id = [int(x) for x in all_clothes_id]
    same_id = []
    tag = True
    for i in sheet1_id:
        if i in sheet2_id or i in sheet3_id :
            same_id.append(i)
            tag = False
    for i in sheet2_id:
        if i in sheet3_id :
            same_id.append(i)
            tag = False

    if tag == True:
        print('没有重复id')
    else:
        print(same_id)
    print('版本新衣服数：%d' % (len(sheet1_id) + len(sheet2_id) + len(sheet3_id)))
    return all_clothes_id


def which_id_display():
    clothes_info = pd.read_excel(r'C:\Users\Admin\Desktop\study\py\越南表\衣服_属性表.xlsx', sheet_name='Sheet1',
                                 index_col='id')
    # x = clothes_info.loc[[12111], ['不显示']]
    # y = clothes_info.loc[[12111], ['不显示']].loc[:, '不显示']
    # print(math.isnan(y))
    tag=True
    display_id=[]
    for i in need_clothes_count():
        if not math.isnan(clothes_info.loc[[i], ['不显示']].loc[:, '不显示']):
            print('%d衣服不显示' % i)
            display_id.append(i)
            tag=False
    if tag==True:
        print('衣服都显示')
    else:
        print(display_id)
        print(len(display_id))




if __name__ == '__main__':
    which_id_display()
