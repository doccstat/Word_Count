'''
实验报告


 实验5 问题的求解 算法实现（1）
实验报告
1.实验目的
（1）掌握穷举法的基本思想，学会用穷举的方法解决问题。
（2）学会二分法解决问题的方法，体会二分法的优点。
2.实验步骤（详述每一个子实验的关键语法及其实现）
2.1 实验任务5-1
不停地用if语句，先确定个个位置的数字，再对不同位数进行讨论
2.2 实验任务5-2
'''
for number in range(int(input("请输入共有多少数字:"))):
	list1.append(int(input("数字%d:" % number)))
'''
2.3 实验任务5-3
for n in range(-100,100):以及二分法，剩余就是不断循环
3.实验总结
这次两个实验用到了二分法，第一个实验用暴力的方法也可以解决，但是消耗时间过长，第二个实验可以用我注释中的方法，不用二分法也可以
4.简答题
1)结合实际生活，在举出几个能够用穷举或者二分的方法解决的实际问题，并简要阐述你的思路。

在判断许多球中哪个更轻是可以用二分法
2)实验任务二也可以通过穷举的方法实现，你觉得两种方法有哪些不同？（提示：结合二分法的优点回答）
二分法的步骤更少，效率更高
'''
#list1=[]
#a=int(input("共有多少个数"))
#while a!=0:
#	x=input("输入数字")
#	list1.append(x)
#	a=a-1
#b=input("输入要查找的数")
#t=0
#l=len(list1)-1
#for i in range(0,l):
#	if list1[i]==b:
#		t=1
#		print(i+1)
#if t==0:
#	print("NO FOUND!")

# 实验得分：未评分

# 问题 1:  阿姆斯特朗数
# -*- encoding: utf-8 -*-

# please input your code here.
for i in range(100,10000000):
	a = i%10
	b = (i%100-a)/10
	c = (i%1000-b*10-a)/100
	d = (i%10000-c*100-b*10-a)/1000
	e = (i%100000-d*1000-c*100-b*10-a)/10000
	f = (i%1000000-e*10000-d*1000-c*100-b*10-a)/100000
	g = (i%10000000-f*100000-e*10000-d*1000-c*100-b*10-a)/1000000
# 求出每位数
	if g==0:
		if f==0:
			if e==0:
				if d==0:
					if a**3+b**3+c**3==i:
						print(i)
				elif a**4+b**4+c**4+d**4==i:
					print(i)
			elif a**5+b**5+c**5+d**5+e**5==i:
				print(i)
		elif a**6+b**6+c**6+d**6+e**6+f**6==i:
			print(i)
	elif a**7+b**7+c**7+d**7+e**7+f**7+g**7==i:
		print(i)
# 问题 2:  二分查找
#list1=[]
#a=int(input("共有多少个数"))
#while a!=0:
#	x=input("输入数字")
#	list1.append(x)
#	a=a-1
#b=input("输入要查找的数")
#t=0
#l=len(list1)-1
#for i in range(0,l):
#	if list1[i]==b:
#		t=1
#		print(i+1)
#if t==0:
#	print("NO FOUND!")
list1 = []
def Search(xiao, da, target, *list1):
	while xiao <= da:
		if target < list1[(xiao + da)//2]:
			da = (xiao + da)//2 - 1
		elif target > list1[(xiao + da)//2]:
			xiao = (xiao + da)//2 + 1
		else:
			return (xiao + da)//2
		Search(xiao, da, target, *list1)
for number in range(int(input("请输入共有多少数字:"))):
	list1.append(int(input("数字%d:" % number)))
l = Search(0, len(list1) - 1,int(input("输入要找的数字:")), *tuple(list1))
if l != None:
	print("要求数字为第%d个" % (l + 1))
else:
	print("NO FOUND!")
# 问题 3:  方程求解
def f(n):
	f=a*n**3+b*n**2+c*n+d
	return f
a=float(input("请输入三次方程的三次项系数:"))
b=float(input("请输入三次方程的二次项系数:"))
c=float(input("请输入三次方程的一次项系数:"))
d=float(input("请输入三次方程的常数项系数:"))
for n in range(-100,100):
	if f(n) == 0:
# 检验是否为整数，若为整数直接输出精确值
		print ("其中一根为整数(精确值)",int(n))
	else:
		if f(n)*f(n+1) < 0:   #因为规定根只差大于1，则若小于零，必有根
			xia=n   #令下界、上界、中值，进行夹逼
			shang=n+1
			mid=(xia+shang)/2
			while shang-xia>0.01:
# 调整精确度，0.01则精确到小数点后两位
				if f(xia)*f(mid)<0:
					shang=mid
					mid=(xia+shang)/2
# 用while循环赋值,直到满足精确度
				if f(xia)*f(shang)<0:
					xia=mid
					mid=(shang+xia)/2
# 结构'%.2f'%表示保留两位小数
			print("其中一根为(精确到小数点后2位)",'%.2f'%mid)