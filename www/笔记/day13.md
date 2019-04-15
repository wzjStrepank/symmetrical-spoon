## 13.01_Python语言基础(Python实现英汉字典)(掌握)
#### Python实现英汉字典
#
	# 打开英汉字典文件
	file = open("dict.txt", "r", encoding="utf-8")
	# 读取字符串
	lines = file.readlines()
	# 创建字典
	dictionary = {}
	# 字典添加内内容
	for i in lines:
	    line_list = i.split("\t")
	    dictionary[line_list[0]] = line_list[1]
	# 单词查询功能
	while True:
	    print("请输入要查询的单词,输入0退出:")
	    eng = input()
	    if eng == "0":
	        break
	    if eng in dictionary.keys():
	        print(eng + ":\t" + dictionary[eng])
	    else:
	        print("您查询的词尚未收录,敬请期待")








## 13.02_Python语言基础(tkinter概述)(熟练)
* tkinter的概述支持
* Python的GUI库
* Tkinter： 
	* Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 
	* Tk 和 Tkinter 可以在大多数的 Unix 平台下使用,同样可以应用在 Windows 和 Macintosh 系统里。
	* Tk8.0 的后续版本可以实现本地窗口风格,并良好地运行在绝大多数平台中。
	* Tkinter 是 Python 的标准 GUI 库。
	* Python 使用 Tkinter 可以快速的创建 GUI 应用程序。
	* 由于 Tkinter 是内置到 python 的安装包中、只要安装好 Python 之后就能 import Tkinter 库
	* IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。
* wxPython
	* wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI 图形库，
	* 允许 Python 程序员很方便的创建完整的、功能健全的 GUI 用户界面。
* Jython
	* Jython 程序可以和 Java 无缝集成。
	* 除了一些标准模块，Jython 使用 Java 的模块。
	* Jython 几乎拥有标准的Python 中不依赖于 C 语言的全部模块。
	* 比如，Jython 的用户界面将使用 Swing，AWT或者 SWT。
	* Jython 可以被动态或静态地编译成 Java 字节码。








## 13.03_Python语言基础(创建一个图形化界面)(熟练)
* 使用方式：
	* 1.导入tkinter
	* 2.创建控件
	* 3.指定这个控件的master，即这个控件属于谁
	* 4. 通知GM(geometry，manager)执行
#### 示例
#
	import tkinter
	# 创建主窗口
	window = tkinter.Tk()
	# 设置标题
	window.title("英汉词典")
	# 设置窗口的大小和位置400×400：宽高   200+20   初始化时候窗口的位置
	window.geometry("400x400+200+20") # 符号为（x）小写矮科斯
	# 显示内容
	window.mainloop()









## 13.04_Python语言基础(控件lable)(熟练)
* 定义：
   * 标签控件可以显示文本
#### lable控件
	import tkinter
	
	#创建主窗口
	window = tkinter.Tk()
	#设置标题
	window.title("英汉词典")
	#设置窗口的大小和位置400×400：大小宽高   200  20   初始化时候窗口所在的位置
	window.geometry("400x400+200+20")
	"""
	window:父窗体
	text:显示的文本内容
	bg:背景
	fg:字体颜色
	wrapLength :指定text文本中多宽进行换行
	justify:设置换行后的对齐方式
	anchor: 位置  n 北   e  东  s南   w  西   center  居中
	"""
	label = tkinter.Label(window,text="1806",
	              bg="blue",fg="red",
	              font=("黑体",20),width="10",
	              height="4",wraplength= 100,
	              justify="left",anchor = "center")
	
	# 管理控件
	label.pack()#pack是一个布局管理器

	# 循环消息
	window.mainloop()











## 13.05_Python语言基础(控件Button)(熟练)
* button定义：
   * button理解为按钮
* 按钮的功能：
   * 当点击按钮时发生对应的事
#### 按钮显示和控制
#
	import tkinter
	
	# 创建窗口
	from tkinter import Frame
	
	window = tkinter.Tk()
	# 设置窗口
	window.title("英汉词典")
	window.geometry("500x500")
	
	
	# 控制台输出信息的方法
	def show_info():
	    print("666")
	
	
	# 显示按钮
	btn_show = tkinter.Button(window, text="查询", command=show_info)
	btn_show.pack(side="left")
	
	# 退出按钮
	btn_exit = tkinter.Button(window, text="退出", command=window.quit)
	btn_exit.pack(side="right")
	
	# 按钮布局
	btn_frame = Frame(window, height=30)
	btn_frame.pack()
	#
	# # 显示按钮
	# btn_show = tkinter.Button(btn_frame, text="查询", command=show_info)
	# btn_show.pack(side="left")
	#
	# # 退出按钮
	# btn_exit = tkinter.Button(btn_frame, text="退出", command=window.quit)
	# btn_exit.pack(side="right")
	
	# 消息循环
	window.mainloop()








## 13.06_Python语言基础(Text控件)(熟练)
* Text：
	* 显示文本信息
#### 文本显示框
#
	
	#
	import tkinter
	from tkinter import *
	
	# 创建窗口
	window = tkinter.Tk()
	
	# 配置窗口
	window.title("英汉词典")
	window.geometry("500x300")
	window.resizable(width=True, height=False)
	
	# 文本显示框
	text = Text(window, width=68, height=20)
	text.pack(side="bottom")
	
	# 文本框插入内容
	word = "hello hello hello hello hello hello hello hello hello"
	text.insert(tkinter.INSERT, word)
	
	# 消息循环
	window.mainloop()









## 13.07_Python语言基础(文本输入框)(熟练)
* 输入文本内容的控件
	* 通过get()方法可以获取到输入内容
	* 通过set()方法可以预设内容
#### 文本输入框案例
#
	import tkinter

	# 创建窗口
	window = tkinter.Tk()
	# 设置窗口
	window.title("英汉词典")
	window.geometry("500x500")
	
	# 输入框
	entry = tkinter.Entry(window)
	entry.pack()
	
	
	# 控制台输出内容
	def show_info():
	    print(entry.get())
	
	
	# 按钮
	button = tkinter.Button(window, text="查询", command=show_info)
	button.pack()

	# 消息循环
	window.mainloop()










## 13.08_Python语言基础(文本输入框关联文本显示框)(熟练)
* 用户在文本输入框书写内容
* 内容显示在文本显示框
* 通过按钮点击事件关联
#### 获取内容并显示案例
#
	import tkinter
	from tkinter import *
	
	
	# 显示信息
	def show_info():
	    text.insert("1.0", entry.get() + "\n")
	
	
	# 创建窗口
	window = tkinter.Tk()
	
	# 配置窗口
	window.title("英汉词典")
	window.geometry("500x300")
	window.resizable(width=True, height=False)
	
	# 输入框布局
	input_frame = Frame(window, width=30, height=30)
	input_frame.pack(side="top")
	
	# 输入框
	entry = Entry(input_frame, width=30)
	entry.pack(side="left")
	
	# 查询按钮
	btn_search = Button(input_frame, text="查询", command=show_info)
	btn_search.pack(side="left")
	
	# 退出按钮
	btn_search = Button(input_frame, text="退出", command=window.quit)
	btn_search.pack(side="right")
	
	# 文本
	text = Text(window, width=68, height=20)
	text.pack(side="bottom")
	
	# 循环消息
	window.mainloop()









## 13.09_Python语言基础(进度条)(熟练)
* 文本内容超出文本显示框一页容量时，内容将无法完全展示
* 拖动进度条可显示全部内容
#### 进度条案例
# 
	import tkinter
	from tkinter import *
	
	
	# 显示信息
	def show_info():
	    text.insert("1.0", entry.get() + "\n")
	
	
	# 创建窗口
	window = tkinter.Tk()
	
	# 配置窗口
	window.title("英汉词典")
	window.geometry("500x300")
	window.resizable(width=True, height=False)
	
	# 输入框布局
	input_frame = Frame(window, width=30, height=30)
	input_frame.pack(side="top")
	
	# 输入框
	entry = Entry(input_frame, width=30)
	entry.pack(side="left")
	
	# 查询按钮	
	btn_search = Button(input_frame, text="查询", command=show_info)
	btn_search.pack(side="left")
	
	# 退出按钮
	btn_search = Button(input_frame, text="退出", command=window.quit)
	btn_search.pack(side="right")

	# 清空数据
	def clear_info():
	    text.delete(0.0, tkinter.END)
	
	# 滚动条
	scroll = tkinter.Scrollbar()
	scroll.pack(side="right", fill=tkinter.Y)
	
	# 文本
	text = Text(window, width=68, height=20)
	text.pack(side="bottom")
	
	# 关联滚动条和文字
	text.config(yscrollcommand=scroll.set)
	scroll.config(command=text.yview)
	
	# 循环消息
	window.mainloop()







## 13.10_Python语言基础(绝对布局)(熟练)
* 绝对布局
	* 使用place方法可以通过坐标的方式确定控件的位置
	* 其他控件的变化（增加或删除）不会影响自身的位置
#### 绝对布局 案例
# 
	import tkinter

	from tkinter import Label
	
	# 创建窗口
	window = tkinter.Tk()

	# 设置窗口参数
	window = tkinter.Tk()
	window.title("英汉词典")
	window.geometry("500x500")

	# 创建控件
	label_01 = Label(window, text="label_01", bg="blue")
	label_02 = Label(window, text="label_02", bg="green")
	label_03 = Label(window, text="label_03", bg="red")

	# 管理控件
	label_01.place(x=10, y=10)
	label_02.place(x=50, y=50)
	label_03.place(x=100, y=100)

	# 循环消息
	window.mainloop()




## 13.11_Python语言基础(相对布局)(熟练)
* 相对布局
	* 相对布局的控件会参照上一个控件的位置摆放自己
	* 其他控件的变化（增加或删除）会影响自身的位置
#### 相对布局案例：
#
	import tkinter

	from tkinter import Label
	
	# 创建窗口
	window = tkinter.Tk()

	# 设置窗口参数
	window = tkinter.Tk()
	window.title("英汉词典")
	window.geometry("500x500")

	# 创建控件
	label_01 = Label(window, text="label_01", bg="blue")
	label_02 = Label(window, text="label_02", bg="green")
	label_03 = Label(window, text="label_03", bg="red")

	# 管理控件
	label_01.pack(fill=tkinter.Y, side=tkinter.LEFT)
	label_02.pack(fill=tkinter.X, side=tkinter.TOP)
	label_03.pack(fill=tkinter.X, side=tkinter.LEFT)

	# 循环消息
	window.mainloop()






## 13.12_Python语言基础(表格布局)(熟练)
* 参照表格中的位置摆放
	* 参数row表示行数
	* 参数column表示列数
#### 表格布局案例
#
	import tkinter

	from tkinter import Label
	
	# 创建窗口
	window = tkinter.Tk()

	# 设置窗口参数
	window = tkinter.Tk()
	window.title("英汉词典")
	window.geometry("500x500")

	# 创建控件
	label_01 = Label(window, text="label_01", bg="blue")
	label_02 = Label(window, text="label_02", bg="green")
	label_03 = Label(window, text="label_03", bg="red")
	label_04 = Label(window, text="label_01", bg="yellow")
	label_05 = Label(window, text="label_02", bg="orange")
	label_06 = Label(window, text="label_03", bg="pink")

	# 管理控件
	label_01.grid(row=1, column=1)
	label_02.grid(row=2, column=2)
	label_03.grid(row=3, column=3)
	label_04.grid(row=1, column=4)
	label_05.grid(row=2, column=5)
	label_06.grid(row=3, column=6)

	# 循环消息
	window.mainloop()





## 13.13_Python语言基础(浮雕布局)(熟练)
* 浮雕布局可以让控件以3D的效果呈现
* 浮雕布局属性为relief，共有五种类型：
	* FLAT    ---平的
	* RAISED  ---凸起的
	* RIDGE   ---脊状边缘
	* SUNKEN  ---凹陷
	* GROOVE  ---沟状
#### 浮雕布局案例
#
	import tkinter
	
	from tkinter import Label, GROOVE, SUNKEN, RAISED, FLAT, RIDGE

	# 创建窗口
	window = tkinter.Tk()

	# 设置窗口参数
	window.title("英汉词典")
	window.geometry("500x500")

	"""
	relief:3D效果
	FLAT    ---平的
	RAISED  ---凸起的
	RIDGE   ---脊状边缘
	SUNKEN  ---凹陷
	GROOVE  ---沟状
	"""

	# 创建控件
	label_01 = Label(window, text="label_01", bg="blue", relief=GROOVE)
	label_02 = Label(window, text="label_02", bg="green", relief=SUNKEN)
	label_03 = Label(window, text="label_03", bg="red", relief=RAISED)
	label_04 = Label(window, text="label_04", bg="yellow", relief=FLAT)
	label_05 = Label(window, text="label_05", bg="orange", relief=RIDGE)

	# 管理控件
	label_01.grid(row=1, column=1)
	label_02.grid(row=2, column=2)
	label_03.grid(row=3, column=3)
	label_04.grid(row=4, column=4)
	label_05.grid(row=5, column=5)

	# 循环消息
	window.mainloop()





## 13.14_Python语言基础(单选按钮)(熟练)
* 只可以选中一个选项，比如性别，毕业状况等信息
#### 单选按钮示例
#
	import tkinter
	
	# 创建窗口
	from tkinter import Checkbutton, IntVar, Radiobutton
	
	window = tkinter.Tk()
	
	# 设置窗口参数
	window.title("英汉词典")
	window.geometry("500x500")
	
	# 一组按钮绑定一个变量
	check_box = tkinter.BooleanVar()
	
	
	# 接收显示结果
	def send_result():
	    print(check_box.get())
	
	
	# 创建单选按钮
	radio_man = Radiobutton(window, text="man", value=True, variable=check_box, command=send_result)
	radio_woman = Radiobutton(window, text="woman", value=False, variable=check_box, command=send_result)
	
	# 管理控件
	radio_man.pack()
	radio_woman.pack()
	
	# 循环消息
	window.mainloop()






## 13.15_Python语言基础(多选按钮)(熟练)
* 只可以选中多个选项，比如兴趣爱好等信息
#### 多选按钮示例
#
	import tkinter

	from tkinter import Checkbutton, StringVar, BooleanVar
	
	# 创建窗口
	window = tkinter.Tk()
	
	# 设置窗口参数
	window.title("英汉词典")
	window.geometry("500x500")
	# 存放选中信息
	hobby_list = set()
	
	
	# 获取选中信息
	def update_info():
	    if check_01.get():
	        hobby_list.add("篮球")
	    else:
	        if "篮球" in hobby_list:
	            hobby_list.remove("篮球")
	
	    if check_02.get():
	        hobby_list.add("足球")
	    else:
	        if "足球" in hobby_list:
	            hobby_list.remove("足球")
	
	    if check_03.get():
	        hobby_list.add("排球")
	    else:
	        if "排球" in hobby_list:
	            hobby_list.remove("排球")
	
	    print(hobby_list)
	
	
	# 给每一个选项创建一个变量
	check_01 = BooleanVar()
	check_02 = BooleanVar()
	check_03 = BooleanVar()
	
	# 复选框
	check_box_01 = Checkbutton(window, text="篮球", variable=check_01, command=update_info)
	check_box_02 = Checkbutton(window, text="足球", variable=check_02, command=update_info)
	check_box_03 = Checkbutton(window, text="排球", variable=check_03, command=update_info)
	
	# 管理控件
	check_box_01.pack()
	check_box_02.pack()
	check_box_03.pack()
	
	# 循环消息
	window.mainloop()






## 13.16_Python语言基础(带界面的字典)(熟练)
#### 结合以上知识，编写代码实现带界面的字典


## 13.17_Python语言基础(Listbox)(熟练)
* Listbox为列表框控件
* 它可以包含一个或多个文本项(text item)
* 可以设置为单选或多选
#### Listbox案例
#
	"""
	1.导入模块
	2.创建窗口
	3.设置窗口属性
	4.创建Listbox控件
	5.设置控件属性
	6.保存控件属性
	7.显示控件
	"""
	# 1.导入模块
	import tkinter
	
	# 2.创建窗口
	window = tkinter.Tk()
	# 3.设置窗口属性
	window.title("list_box")
	window.geometry("500x500+300+100")
	# 创建list_box控件，
	# 可以多选的Listbox,使用属性selectmaod,
	# 还可以设置为BROWSE,可以通过鼠标来移动Listbox中的选中位置（不是移动item）
	# 单选的Listbox，是有那个属性SINGLE
	# 使用selectmode  = EXPANDED使用Listbox来支持Shift和Control。'''
	list_box = tkinter.Listbox(window, selectmode=tkinter.MULTIPLE)
	list_box.pack()
	# 创建列表，向list_box添加内容
	list01 = ["hello", "world", "good", "nice"]
	for item in list01:
	    list_box.insert(tkinter.END, item)
	# 向末尾添加控件
	list_box.insert(tkinter.END, list01)
	# 获取指定范围的内容
	print(list_box.get(1, 2))
	# 选中自动范围的内容
	print(list_box.select_set(0, 3))
	# 删除指定位置元素
	list_box.delete(2)
	print(list_box.get(tkinter.ACTIVE, tkinter.END))
	# 判断一个item是否被选中,越界返回False
	print(list_box.select_includes(23))
	# 循环消息
	window.mainloop()




## 13.18_Python语言基础(Menu)(熟练)
* Tkinter提供了一个组件Menu用来实现菜单
* 菜单包括顶级菜单，下拉菜单和弹出菜单，下面我们将会看到顶级菜单和下拉菜单的案例。
* 菜单需要用config关联窗口
* 添加菜单使用add_command
* 添加下拉菜单使用add_cascade
#### 顶级菜单案例：
#
	# 1.导入模块
	import tkinter
	
	# 2.创建窗口
	window = tkinter.Tk()
	# 3.设置窗口属性
	window.title("list_box")
	window.geometry("500x500+300+100")	
	# 创建菜单
	menu_language = tkinter.Menu(window, tearoff=False)
	
	
	# 响应菜单回调函数
	def callback():
	    print("hello")
	
	
	# 菜单添加内容
	list01 = ["python", "java", "oc", "c#", "php", "js", "c++", "汇编", "shell", "退出"]
	for item in list01:
	    if item == "退出":
	        menu_language.add_command(label=item, command=window.quit)
	    else:
	        menu_language.add_command(label=item, command=callback)
	# 菜单栏关联window
	# 虽然menu已经创建，但是还没添加到root窗口中，所以要调用config方法对root的menu选项相关联
	window.config(menu=menu_language)
	# 循环消息
	window.mainloop()

#### 顶级菜单和下拉菜单案例：
#	
    # 1.导入模块
    import tkinter
    # 2.创建窗口
    window = tkinter.Tk()
    # 3.设置窗口属性
    window.title("list_box")
    window.geometry("500x500+300+100")
    # 创建菜单
    menu_bar = tkinter.Menu(window)
    menu_language = tkinter.Menu(menu_bar, tearoff=False)

    def python_show():
        print("python")

    list01 = ["python", "java", "oc", "c#", "php", "js", "c++", "汇编", "shell", "退出"]
    for item in list01:
        if item == "退出":
            menu_language.add_command(label=item, command=window.quit)
        else:
            menu_language.add_command(label=item, command=python_show)
    # 菜单栏关联window
    # 创建子菜单
    menu_bar.add_cascade(label="语言", menu=menu_language)
    # menu_list.
    # 虽然menu已经创建，但是还没添加到root窗口中，所以要调用config方法对root的menu选项相关联
    window.config(menu=menu_bar)
    window.mainloop()