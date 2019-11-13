def each_list(list_name, count=False, level=0):  # 加入控制形参 count 默认为不开启缩进
    for yuansu in list_name:
        if isinstance(yuansu, list):  # 判断当前元素是不是列表
            each_list(yuansu, count, level + 1)  # 如是,则递归调用,并且标记当前元素是列表
        else:
            if count:  # 判断是否开启缩进
                for tab in range(level):  # 固定次数
                    print("\t", end='')
                print(yuansu)
            else:
                print(yuansu)


new_list = ["H1", "H2", 1999, ["hello", "day", ["one", "two"]]]

each_list(new_list, True)

'''
#输出效果
H1
H2
1999
	hello
	day
		one
		two
'''