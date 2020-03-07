# 实验8 综合实验
# 实验报告
# 1.实验题目（你选择的题目）
# 文本统计

# 2.实验步骤
# 在网上找一篇300词左右的演讲稿存入C:/yanjiang.txt中，在网上找一份完整停用词表存入C:/tingyongci.txt中，首先将文章整体全部小写化，然后将所有标点替换为空格便于处理，将字符串转换为列表，列表长度就是单词数。对于列表中的单词可以使用重复检索的方法查单词的使用频率。将单词频数进行降序排序，用到提示中的语句wturple=sorted(dict2.items(),key=lambda d:d[1],reverse=True) 然后选择最高的10个运用实验7中的GUI图形绘制制作一个图形界面，不太清楚题目中要求是什么意思，所以制作了两个按钮，还有一个无空格版本。

# 3.结果说明
# 点击不同按钮对应不同函数，第一个函数仅仅显示由字母组成的文章，没有除了空格以外的任何符号，第二个函数将空格也去掉，仅仅是字母的连续组成，总单词数是由文章转换成的列表进行长度统计得到的，词频统计是进行遍历查看重复次数得到的，图表的设计要考虑到字符串与数字之间的转化，在最后一个函数中我进行了双重按键的设计，在按下显示词频的按钮后，显示出词频的同时给用户一个按钮用来显示图表。

# 4.心得体会
#     对于这次实验，我本来是想将图形界面设计成更为规则的窗口，而不是简简单单的一列按键，但是当我进行尝试之后发现第二排的按键中间始终有一块空白将两个按键间隔开而不是紧紧连在一起，这个困扰我始终不能把GUI做成我想的样子，这点很是奇怪。
#     通过探索，在第一次设计好程序后发现空格竟然被计算成为了一个单词，并且将其算入高频词语之列，我很是奇怪，通过各种探索，尝试，增删文章中的各种字符以及换行符号，最后终于发现是两个空格连在一起导致了错误识别，我想这是一个非常容易犯错误的地方。
#     而且在进行替换时我发现不能使用s2=s2.replace(''','')来进行替换，因为这会造成Python的错误识别将第一个和第二个'识别为一对，这造成了以后的所有的字符串都被错误识别为注释导致不能运行，所以我们应该使用s2=s2.replace("'",'')，这样就避免了识别错误。
#     对于这学期的Python学习，我学会了很多东西，大学计算机基础在其他学校可以说是基本不用上的课，excel、word等等，而我们是学一种编程语言，这对于我们的整个生活中都是非常有益的，我想我已经基本掌握了Python编程的技巧，这是一门非常好学易懂的语言，我想我还会在其他地方继续使用这种语言，不仅因为我学过它，更因为它功能上的强大。
# 实验得分：未评分

# 问题 1:  文本统计

# -*- coding: utf-8 -*-

# please input your code here.
import string
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
f=open(r'C:/yanjiang.txt','r')
#读取文件
s=f.read()
#将文件转换为字符串
s=s.lower()
#将字母全部转换为小写
s2=s.replace(',','')
s2=s2.replace('.','')
s2=s2.replace('-','')
s2=s2.replace('+','')
s2=s2.replace("'",'')
s2=s2.replace("' ",'')
# 在这里有个很容易犯错误的地方，英文中的'要想去掉，应用""将其包含
s2=s2.replace('(','')
s2=s2.replace('!','')
s2=s2.replace(':','')
s2=s2.replace('/','')
s2=s2.replace('\n','')
s2=s2.replace(')','')
s2=s2.replace('?','')
s2=s2.replace('  ',' ')
'''
有时会产生两个空格连起来的情况，此时会将一个空格视为单词而增加单词数，应将两个连续的空格替换为一个空格
'''
#除去标点符号
s2=s2.strip(string.punctuation)
l=s2.split(' ')
#将字符串转换为列表
# 在这里我们已经转换为小写，需哦一在接下来的任务中我们一直使用小写
def f():
	#输出转化为小写，并剥去空白字符和标点的文本
	root=Tk()
	root.title('转换输出')
	label=Label(root,text=s2,justify='left',wraplength=500)
	label.pack()
	label.mainloop()
	#定义一个窗口并输出结果
def b():
	#除去空格
	root=Tk()
	root.title('转换输出')
	label=Label(root,text=s2.replace(' ',''),justify='left',wraplength=500)
	label.pack()
	label.mainloop()

# 这是任务1)和2)

def c():
	root=Tk()
	root.title('总单词数')
	label=Label(root,text=('这篇文章的单词数为：',len(l)))
	label.pack()
	label.mainloop()
	#统计单词数并输出

# 这是任务3)

dict={}
#定义一个空字典
l2=[]
for i in l:
	s=0
	if not i in l2:
	#对所有词进行遍历并且不再搜索已经搜索过的词
		for a in l:
			if a==i:
				s+=1
		dict[i]=s
		l2.append(i)
		# 向l2中加入单词
def d():
	jieguo=''
	for i in l2:
		a=i+'的词频是'+str(dict[i])
		jieguo=jieguo+'  '+a
	root=Tk()
	root.title('词频统计')
	label=Label(root,text=jieguo,justify='left',wraplength=700)
	label.pack()
	label.mainloop()

# 这是任务4)

f2=open(r'C:/tingyongci.txt','r')
#读取文件
b2=f2.read()
l3=b2.split()
#将文件转换为列表
def e():
	dict2={}
	l4=[]
	#定义一个空列表
	for i in l:
		s=0
		if not i in l3:
		#排除掉那些停用词
			if not i in l4:
			#对筛选出的所有词进行遍历并且不再搜索已经搜索过的词
				for a in l:
					if a==i:
						s+=1
				dict2[i]=s
				l4.append(i)
				# 向l4中添加i
	wturple=sorted(dict2.items(),key=lambda d:d[1],reverse=True)
	#对词频进行降序排序
	l5=[]
	l6=[]
	jieguo=''
	for i in range(10):
		a=tuple(wturple[i])
		l5.append(a[0])
		#将出现频率高的前十个单词放到l5中
		l6.append(a[1])
		b='排在第'+str(i+1)+'位的是'+a[0]+'，'+'出现了'+str(dict2[a[0]])+'次'
		jieguo=jieguo+'\n'+b
	danci=tuple(l5)
	cipin=tuple(l6)
	def tubiao():
		N = 10
		# 图表最终要取十个频率最大的，所以N = 10
		ind = np.arange(N)
		# 获得 x 轴的坐标序列
		width = 0.7
		# the width of the bars
		fig, ax = plt.subplots()
		# 得到图表
		rects = []
		grade = (cipin)
		# 分别构造单个序列的数据对应的图形，并设置颜色
		rects.append(ax.bar(2*ind + width * 1, grade, width, color = 'pink',label='Number'))
		ax.set_ylabel('Number')
		# 设置y坐标轴名称
		# 设置坐标轴标题
		ax.set_title('Key words')
		ax.set_xticks(2*ind + 1.5 * width)
		ax.set_xticklabels(danci)
		# 设置x坐标轴名称
		ax.legend()
		# 绘制图形（柱状图和图例）
		def autolabel(rects):
		# 定义函数，在每一个序列的柱形图上显示数值
			for rect in rects:
				height=rect.get_height()
				# 获得每一列的高度值
				ax.text(rect.get_x(),int(height)+0.1,'%d'%int(height))
				# 显示数值，并设定其显示位置
		autolabel(rects[0])
		plt.show()
		# 显示图形
	root=Tk()
	root.title('找关键词')
	label=Label(root,text=jieguo,width=40,height=11).grid(row=0,column=0)
	Button(root,text='显示图表',width=40,height=3,command=lambda:tubiao()).grid(row=1,column=0)
	root.mainloop()

# 这是任务5)

root=Tk()
root.title('文本统计')
#建立一个窗口并命名
Button(root,text='去符号输出(含空格)',width=25,command=lambda:f()).grid(row=0,column=0)
#定义按钮
Button(root,text='去符号输出(无空格)',width=25,command=lambda:b()).grid(row=1,column=0)
Button(root,text='总单词数',width=25,command=lambda:c()).grid(row=2,column=0)
Button(root,text='词频统计',width=25,command=lambda:d()).grid(row=3,column=0)
Button(root,text='找出关键词(图表)',width=25,command=lambda:e()).grid(row=4,column=0)

# 这是任务6)