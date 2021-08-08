import pandas as pd


def xxx():
    list = []
    list2 = []

    list = [11376, 21172, 71234, 83094, 83095, 83096, 83098, 83099, 83100, 83101, 83102, 90167 | 11377, 21174, 83103,
            83104,
            83108, 90168]
    list2 = [11376, 21171, 60553, 60554, 71233, 83098, 83099, 90167, 11377, 21173, 30571, 60555, 71235, 83108, 90168]
    for i in list:
        if not i in list2:
            print(i)
    for i in list2:
        if not i in  list:
            print(i)


if __name__ == '__main__':
    xxx()
