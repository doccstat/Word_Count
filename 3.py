# -*- encoding: utf-8 -*-

# please input your code here.
# 存放每月日均最高气温
maxC=[2,5,12,20,26,30,31,30,26,19,10,3]
# 存放每月日均最低温度
minC=[-9,-6,0,8,14,19,22,21,15,8,0,-6]
# 存放每月平均降水总量
evr=[3,6,9,22,36,74,179,177,53,23,8,2]
# 存放秋季日均最高温度
maxF=[maxC[8],maxC[9],maxC[10]]
# 存放秋季日均最低温度
minF=[minC[8],minC[9],minC[10]]
# 输出年平均最高气温
print("年平均最高气温:%.2f度"%(sum(maxC)/len(maxC)))
# 输出年平均最低气温
print("年平均最低气温:%.2f度"%(sum(minC)/len(minC)))
# 输出年平均降水总量
print("年平均降水总量:%.2fmm"%(sum(evr)/len(evr)))
# 输出秋季平均最高气温
print("秋季平均最高气温:%.2f度"%(sum(maxF)/len(maxF)))
# 输出秋季平均最低气温
print("秋季平均最低气温:%.2f度"%(sum(minF)/len(minF)))
问题 2:  英汉字典
# -*- encoding: utf-8 -*-

# please input your code here.
# 空字典
dic = {}
# 定义向字典中添加
def add_diction(dictionary,en,ch):
    dictionary[en] = ch
    dictionary[ch] = en
    print("添加成功")
# 定义在字典中查找单词
def find(a,b):
    if b in a:
        print("该单词",b,"的意思是",a[b])
    else:
        print("该单词不在词典中")
# 添加单词
for i in range(10):
    en = input("增添的英文单词:")
    ch = input("对应的中文单词:")
    add_diction(dic,en,ch)
# 输出过程
string = input("需要翻译的单词为:")
find(dic,string)
问题 3:  字符串加密
# -*- encoding: utf-8 -*-

# please input your code here.
# 创建list
LIST=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
yuan=input("输入原字符:").lower()
# 将字符变为小写
temp=list(yuan)
# 输入的字符串转换为整数
k=int(input("向后移动位数:"))
def Function(a):
	a=ord(a)+k
	while a>ord("z"):
		a=a-26
	return a
# 对每个字符进行更改
for i in range(len(yuan)):
	if ord(temp[i])!=32:
		temp[i]=chr(Function(temp[i]))
# 单个字符连接起来
print("".join(temp))