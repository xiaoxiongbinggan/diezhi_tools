import pandas as pd


def nodis_clothes_count():#在两个sheet里分别计算，最后求和
    clothes_info = pd.read_excel('衣服_属性表.xlsx', sheet_name='Sheet1')
    clothes_display = clothes_info.loc[:, '不显示']
    clothes = clothes_display.count()
    all_clothes = clothes_display.shape[0]
    print(all_clothes)
    nodis_clothes = all_clothes - clothes
    print('隐藏的衣服数:%d,总数：%d,打开的总数：%d' % (clothes, all_clothes , nodis_clothes))

    clothes_info2 = pd.read_excel('衣服_属性表.xlsx', sheet_name='miraclesoul')
    clothes_display2 = clothes_info2.loc[:, '不显示']
    miracles = clothes_display2.count()
    all_miracles = clothes_display2.shape[0]
    nodis_miracles = all_miracles - miracles

    print('隐藏的荧光之灵数：%d,总数：%d,打开的总数:%d' % (miracles, all_miracles, nodis_miracles))
    result = nodis_clothes + nodis_miracles
    print('版本衣服数：%d' % result)

def nodis_clothes_count2():#合并两个sheet，一起求和
    clothes_info_sheet1=pd.read_excel('衣服_属性表.xlsx',sheet_name='Sheet1',index_col='id')
    clothes_inf_sheet2=pd.read_excel('衣服_属性表.xlsx',sheet_name='miraclesoul',index_col='id')
    new_clothes_info=pd.concat([clothes_info_sheet1,clothes_inf_sheet2])
    all_count=new_clothes_info.loc[:,'不显示'].shape[0]
    dis_count=new_clothes_info.loc[:,'不显示'].count()
    result=all_count-dis_count
    print(result)
if __name__ == '__main__':

    nodis_clothes_count()
