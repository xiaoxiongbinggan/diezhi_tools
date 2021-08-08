import pandas as pd


def get_clothes_id(suitid):
    achi = pd.read_excel('玩家_成就表.xlsx', sheet_name='Sheet2').set_index('id')
    # sheet_name=[''],返回值是一个字典dict，sheet_name='',返回值是dataframe.加[]返回值是字典dict后，就不能用set_index方法了
    # id列设置为列索引！！！
    # tip:reset_index重置索引,变为原来的序号索引
    suit_clothes_id=achi.loc[suitid]
    return suit_clothes_id.dropna().tolist()
    # dict=suit_clothes_id.dropna().to_dict()
    #这里drop要写在tolist前面
    #tolist转化成列表，to_dict转化成字典，注意一个有下划线,一个没有下划线

    # suit_clothes_id.to_csv('suitid.txt',sep='\t',header=True,index=False,float_format=None)
    #sep是分隔符，index是否保存数据的索引,header是否要表头,
    #to_csv可以保存为csv和txt，to_excel可以保存为xlsx
    #excel表里的默认列标签是根据序号生成的，所有根据标签搜索和根据序号搜索结果一样，也就是loc和iloc结果一样

    #axis=0竖向合并，axis=1横向合并
def if_display(clothes_id):
    clothes_property1 = pd.read_excel('衣服_属性表.xlsx', sheet_name='Sheet1').set_index('id')
    clothes_property2 = pd.read_excel('衣服_属性表.xlsx', sheet_name='miraclesoul').set_index('id')
    all_clothes_property = pd.concat([clothes_property1, clothes_property2], axis=0)
    for i in clothes_id:
        clothes_display_id=all_clothes_property.loc[[i],['不显示']]
        clothes_display_id.to_csv('ifdisplay.txt','a',sep='\t',index=True)
    #注意指定行列的写法！！！
    #mode='a'，追加的形式添加到txt文件中
    # dic2=clothes_display_id.to_dict()
    #dataframe只能to_dict转化为字典，series类型才可以tolist


if __name__ == '__main__':
    try:
        suit=int(input('请输入搜索的套装id:'))
        clothes_id=get_clothes_id(suit)
        if_display(clothes_id)
    except KeyError:
        print('您输入的id在衣服表中Sheet1和miraclesoul没有找到')
    else:
        print('查询成功！')
#异常控制需要在实际控制函数运行的过程中，上面只是定义函数，并没有运行函数体