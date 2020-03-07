'''
实验4 问题的描述 数据结构（二）
实验报告

1.实验目的
（1）学习Python的类的基本语法，掌握如何用类去描述具体的事物。
（2）掌握Stack和Queue这两种数据结构，并能够根据具体问题选择合适的数据结构，解决问题。
2.实验步骤（详述每一个子实验的关键语法及其实现）
2.1 实验任务4-1
'''
class Circle:
	def __init__(self,radius):
		self.r = radius
	def girth(self):
		return 2*math.pi*self.r
	def area(self):
		return math.pi*self.r*self.r
	def volume(self,h):
		return h*self.area()
	def area1(self,h):
		result = 2*self.area()+self.girth()*h
		return result
# 这是我们创建的类，其中每个函数都有其计算方法，我们都可以去调用。
# 2.2 实验任务4-2
dict = {'{':-1,'}':1,'[':-2,']':2,'(':-3,')':3,'<':-4,'>':4}
while dict[list1[i-1]]+dict[list1[i]]==0 and dict[list1[i-1]]<dict[list1[i]]:
			del list1[i]
			del list1[i-1]
# 这是最关键的一步，我们对每一个符号赋值，当这是合理的时必然有两个连着的相对的符号，他们的和为零。此时list里的合理的元素将一一被删除，如果list里没删完则为不合理，删完即为合理，我们要注意i的取值，不能越界，而且要注意控制变量。
# 这种方法不是最好的，用实验指导书中的会更好。以下是核心代码
def check(string):
	stack=Stack()
	for c in string:
		if c=='{' or c=='['or c=='<'or c=='(':
			stack.push(c)
		elif not stack.isEmpty():
			top=stack.pop()
			if  c=='}'and top!='{':
				return 'no'
			if  c==']'and top!='[':
				return 'no'
			if  c=='<'and top!='>':
				return 'no'
			if  c==')'and top!='(':
				return 'no'
		else:
			return 'no'
	if stack.isEmpty():
		return'yes'
	else:
		return'no'
'''
这种方法更好想。
2.3 实验任务4-3
没有选...这个有些类似于约瑟夫环。
3.实验总结
这次我们使用了类等概念去解决问题，随着学的越多难度也在上升，我们也在进步。
4.简答题
1)在本次实验中，我们使用了类的方法解决问题，请问，类的引入对编程求解问题的过程有哪些好处？
我们不需要去定义那么多的函数，比如第一题如果不用类我们对于每一个量都要定义一个函数。定义一个类更简洁方便。
2)请说明栈和队列在功能上的区别？在实际生活中，还有那些情形可以用栈或者队列的形式来描述？
栈和队列都属于一位链表
区别是:
栈是后进先出,进和出都是在同一端进行,称为"压栈"(push)和"弹栈"(pop),就好象一筒羽毛球,只有把上面拿出来,下面的才能拿出来
队列是先进先出的,进和出分别在不同的端进行,比如排队的人,排在前面的人先到柜台办理业务,后面来的人后得到服务,所以称为"队列"。
实验得分：未评分

问题 1:  圆与圆柱问题
'''
# -*- encoding: utf-8 -*-
# please input your code here.
import math
class Circle:
	def __init__(self,radius):
		self.r = radius
	def girth(self):
		return 2*math.pi*self.r
	def area(self):
		return math.pi*self.r*self.r
	def volume(self,h):
		return h*self.area()
	def area1(self,h):
		result = 2*self.area()+self.girth()*h
		return result
n = input("请输入圆的半径")
h = input("请输入圆的高")
h = float(h)
n = float(n)
n = Circle(n)
print(n.volume(h))
print(n.area1(h))

if __name__=="__main__":
	A = Circle(3)
	print (A)
	print('area=',A.area())
	print('girth=',A.girth())
	print('volume=',A.volume(5))


# 问题 2:  括号匹配
# -*- encoding: utf-8 -*-
dict = {'{':-1,'}':1,'[':-2,']':2,'(':-3,')':3,'<':-4,'>':4}
astring = input("输入一段字符")
b = 1
list1=[]
for i in astring:
	if i in dict:
		list1.append(i)
if len(list1)%2!=0:
	b = 0
while len(list1)!=0 and b!=0:
	b = 0
	i = 1
	while i<len(list1):
		while dict[list1[i-1]]+dict[list1[i]]==0 and dict[list1[i-1]]<dict[list1[i]]:
			del list1[i]
			del list1[i-1]
			b+=1
			if i+1>len(list1):
				break
		i+=1
if len(list1)==0:
		print("yes")
else:
		print("no")