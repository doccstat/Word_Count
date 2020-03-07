'''
实验报告


实验7  GUI程序设计
实验报告
1.实验目的
(1)、理解掌握GUI程序设计的基本思想和方法。
(2)、学会使用Python tkinter标准图形库。
(3)、学会使用Matplotlib 进行简单的数据分析和数据可视化展示。
2.	实验步骤（详述每一个子实验的关键语法及其实现）
2.1 实验任务7-1
导入tkinter模块的方法，使用Python Tkinter Grid布局管理器配置界面，使用bind 方式关联按钮和函数，ttk的很多组件同Tkinter都是相同的，在这种情况下，ttk将覆盖Tkinter的组件，二者都有的组件，ttk将会override Tkinter，ttk有而Tkinter没有，将采用ttk的特性。
2.2 实验任务7-2
先创建一个空列表，依次加入一表，二表，三表的分数，调用模块添加图表的横纵坐标以及标题
3.实验总结
这次实验非常难，用到了图形GUI设计，其中涉及到了许多的tkinter模块中的函数，相比来说计算器的设计最为困难，因为涉及到了从来没有过的关于按键的设计，其中按键设计可以使用for i in range来减少代码行数，还可以用bind('<Button-1>')的event.widget['text']得到值，稍微简单一点。
实验得分：未评分

问题 1:  计算器
'''
# -*- encoding: utf-8 -*-

# please input your code here.
from tkinter import *
from tkinter import ttk
# 导入tkinter
def callback(num):
	display.set(display.get() + num)
# 定义函数
def calculate():
	try:
		display.set(display.get() + "=" + str(eval(display.get())))
	except:
		display.set("Error!")
# 定义计算函数
def clear():
	display.set("")
# 定义清除函数
root = Tk()
root.title("计算器")
# 计算器的标题
display = StringVar()
lbl = Label(root, relief="sunken", borderwidth=3, anchor=SE)
lbl.configure(background="white",height=2, width=25)
lbl['textvariable'] = display
lbl.grid(row=0, column=0, columnspan=4, sticky=SE)
lbl.bind('<Button-1>', display.set(''))
# 以下为按键设置
ttk.Button(root, text="7", width=5, command=lambda: callback("7")).grid(row=3, column=0)
ttk.Button(root, text="8", width=5, command=lambda: callback("8")).grid(row=3, column=1)
ttk.Button(root, text="9", width=5, command=lambda: callback("9")).grid(row=3, column=2)
ttk.Button(root, text="+", width=5, command=lambda: callback("+")).grid(row=3, column=3)
ttk.Button(root, text="4", width=5, command=lambda: callback("4")).grid(row=4, column=0)
ttk.Button(root, text="5", width=5, command=lambda: callback("5")).grid(row=4, column=1)
ttk.Button(root, text="6", width=5, command=lambda: callback("6")).grid(row=4, column=2)
ttk.Button(root, text="-", width=5, command=lambda: callback("-")).grid(row=4, column=3)
ttk.Button(root, text="1", width=5, command=lambda: callback("1")).grid(row=5, column=0)
ttk.Button(root, text="2", width=5, command=lambda: callback("2")).grid(row=5, column=1)
ttk.Button(root, text="3", width=5, command=lambda: callback("3")).grid(row=5, column=2)
ttk.Button(root, text="*", width=5, command=lambda: callback("*")).grid(row=5, column=3)
ttk.Button(root, text="0", width=5, command=lambda: callback("0")).grid(row=6, column=0)
ttk.Button(root, text=".", width=5, command=lambda: callback(".")).grid(row=6, column=1)
ttk.Button(root, text="%", width=5, command=lambda: callback("%")).grid(row=6, column=2)
ttk.Button(root, text="/", width=5, command=lambda: callback("/")).grid(row=6, column=3)
ttk.Button(root, text="clear", command=lambda:clear()).grid(row=7, column=0, columnspan=2)
ttk.Button(root, text="=", command=lambda: calculate()).grid(row=7, column=2, columnspan=2)
# 运行程序
root.resizable(0, 0)
root.mainloop()
# 问题 2:  柱形图绘制
# -*- encoding: utf-8 -*-

# please input your code here.
import numpy as np
import matplotlib.pyplot as plt
def main():
	N = 4
	ind = np.arange(N) # 获得 x 轴的坐标序列
	width = 0.2 # the width of the bars
	fig, ax = plt.subplots() # 得到图表
	# 空列表
	rects = []
	grade = ((486, 514, 527, 529), (444, 425, 437, 414), (345, 331, 330, 342))
	# 分别构造单个序列的数据对应的图形，并设置颜色
	rects.append(ax.bar(ind + width * 1, grade[0], width, color = 'red'))
	rects.append(ax.bar(ind + width * 2, grade[1], width, color = 'blue'))
	rects.append(ax.bar(ind + width * 3, grade[2], width, color = 'green'))
	ax.set_ylabel('Grade') # 设置纵坐标
	# 设置坐标轴标题
	ax.set_title('Grade analysis')
	ax.set_xticks(ind + 2.5 * width)
	ax.set_xticklabels(('2011', '2012', '2013', '2014'))
	ax.legend((rects[0],rects[1],rects[2]),('Level 1','Level 2','Level 3')) # 绘制图形（柱状图和图例）
	def autolabel(rects): # 定义函数，在每一个序列的柱形图上显示数值
	# attach some text labels
		for rect in rects:
			height = rect.get_height() # 获得每一列的高度值
			ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
	                ha='center', va='bottom') # 显示数值，并设定其显示位置
	for i in range(0, 3):
		autolabel(rects[i]) # 调用函数，给每一列显示数值
	plt.show() # 显示图形
if __name__ == '__main__':
	main()