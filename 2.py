# -*- encoding: utf-8 -*-

# please input your code here.
# 定义函数
def Conjecture(n):
	c=0
# c表示对n进行变换的次数
	while(n>1):
		c=c+1;
# 条件语句
		if (n%2==0):
			n=n/2
			print("此时N为偶数，第"+str(c)+"次变换的结果是："+str(n))
		else:
			n=n*3+1
			print("此时N为奇数，第"+str(c)+"次变换的结果是："+str(n))
	return c
# 将字符串转换成整数
n=int(input("请输入任意一个自然数N:"))
print("其角谷猜想的变换过程如下:")
# 调用函数
k=Conjecture(n)
print("该数共经过"+str(k)+"次变换，得到自然数1")
# 问题 3:  折纸问题
# -*- encoding: utf-8 -*-

# please input your code here.
# 输入语句
n=input("请输入折叠次数:")
# 将n转化成整数
n=int(n)
# 调用range()函数
for i in range(1,n+1):
	print("折叠第"+str(i)+"次的厚度为:",0.00005*(2**i),"米")
# 问题 4:  排列组合
# -*- encoding: utf-8 -*-

# please input your code here.
# 求n的阶乘n!,输入n为整数
def Factorial(n):
# n需要为非负整数，如果n<0,打印错误信息
	if n<0:
		print("错误，n应为非负整数")
# 如果n为0,0!=1
	elif n==0:
		return 1
# 如果n>=1,n!=n*(n-1)!
	else:
		return n*Factorial(n-1)
# 该程序无输入
# 调用自定义函数
a=Factorial(10)/(Factorial(10-2)*Factorial(2))
b=Factorial(10-2)/(Factorial(10-2-1)*Factorial(1))
c=Factorial(10-2-1)/(Factorial(10-2-1-1)*Factorial(1))
# 最终结果
result=int(a*b*c)
# 输出结果
print("不同的选法共有",result,"种")
# 问题 5:  个人所得税计算
# -*- encoding: utf-8 -*-

# please input your code here.
# 将输入转化为浮点数
a=float(input("请输入总工资:"))
b=float(input("请输入三险一金:"))
c=3500.0
d=a-b-c
# 条件语句
if d<=1500:
	e=d*0.03
elif d<=4500:
	e=d*0.1-105
elif d<=9000:
	e=d*0.2-555
elif d<=35000:
	e=d*0.25-1005
elif d<=55000:
	e=d*0.3-2755
elif d<=80000:
	e=d*0.35-5505
else:
	e=d*0.45-13505
# 输出过程
print("实发工资为:",a-e)