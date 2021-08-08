import pandas as pd
import operator


def shop_clothes_check():
    # need_shop_clothes_info=pd.read_excel('《奇暖越南》6.5.0版本需求表.xlsx',sheet_name='活动衣服需求',header=1).set_index('id',drop=False)
    need_shop_clothes_info = pd.read_excel('《奇暖越南》6.5.0版本需求表.xlsx', sheet_name='商店上新')
    need_new_id = need_shop_clothes_info.iloc[:, 0].dropna().tolist()

    game_shop_clothes_info = pd.read_excel('衣服_商店表.xlsx', sheet_name='Sheet1')
    game_display_id = game_shop_clothes_info.loc[:, ['id', '不显示']].dropna().loc[:, 'id'].tolist()
    for i in need_new_id:
        if i in game_display_id:
            print('%s在商店表里隐藏了' % i)
    else:
        print('‘不显示’正常')
    game_old_id = game_shop_clothes_info.loc[:, ['id', '是否老商品']].dropna().loc[:, 'id'].tolist()
    for i in need_new_id:
        if i in game_old_id:
            print('%s衣服填在了老商品里' % i)
    else:
        print('‘老衣服’正常')

    game_activity_id = game_shop_clothes_info.loc[:, ['id', '是否活动']].dropna().loc[:, 'id'].tolist()
    for i in need_new_id:
        if i in game_activity_id:
            print('%s衣服填在了‘活动’里' % i)
    else:
        print('‘活动’正常')

    # tag_new_id1=game_shop_clothes_info.iloc[:,[0,23]].dropna().iloc[:,0].tolist()
    game_new_id = game_shop_clothes_info.loc[:, ['id', '是否新品']].dropna().loc[:, 'id'].tolist()
    list = [
        83094, 83095, 83096, 83097, 83100, 83104, 83105, 83106, 83107
    ]
    need_new_id.extend(list)  # extend把列表插入到列表内
    # 心得：
    # 单纯获取表里一列，不需要每次读表的时候都要写索引。要拉表里的所有符合条件的列id，索引也设置成id，得到的表就是索引和内容都是id
    # 设置索引为id列后，再loc索引就取不到值，需要写drop=False把索引列的值保留在表里
    # loc可以一句套一句，相当于在上一次切片里再切片
    for i in need_new_id:
        if i in game_new_id:
            pass
        else:
            print(i)
    for x in game_new_id:
        if x in need_new_id:
            pass
        else:
            print(x)

    need_new_id.sort()
    game_new_id.sort()
    print(operator.eq(need_new_id, game_new_id))


if __name__ == '__main__':
    shop_clothes_check()
