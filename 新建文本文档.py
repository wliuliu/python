#成员关系测试
##set1={"PYTHON","BIT",123,"GOOD"}
##print("BIT" in set1)


#list,tuple元素去重
tuple1=("PYTHON","BIT",123,"GOOD",123,123)
print(tuple1)
set1=set(tuple1)
print(set1)



#删除数据项
set1-={"PYTHON"}
tuple1=tuple(set1)
print(tuple1)
