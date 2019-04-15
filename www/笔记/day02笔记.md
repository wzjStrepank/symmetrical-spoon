### 运算符
#### 算数运算符

#### 逻辑运算符

#### 关系（比较）运算符

#### 赋值运算符

#### 位运算符

#### 身份运算符
* is     
* is not
### 选择结构--if
####
* if
	* 关键字
		* 选择语句的关键字
	* 条件判断语句
		* 可以是bool类型的值
		* 可以是条件表达式，表示式的结果必须是bool值
		* 可以是其他类型的值，除了0表示False，其他可以看作True
	* ：
		* 
	* 代码块
		* 
		* 
		* 

#### if...else结构
	if 条件判断语句
		代码块
	else：
		代码块

	scor = 60
	if score >= 60:
		print("及格啦")
	else:
		print("不及格")

* if else
	* 选择语句的关键字
	* 条件判断语句
		* 可以是bool类型的值
		* 可以是条件表达式，表达式的结果必须是bool值
		* 可以是其他类型的值，除了0表示False，其他可以看作Ture
	* else:
		* if条件判断语句结果为False或0的时候执行，如果if条件成立则不执行 
	* ：
		* 固定格式，表示上一句结果

#### if...elif...elif....else
	if 
		代码块
	elif 
		代码块
	elif
		代码块
	... ...
	else
		代码块
* if
	* 条件选择语句关键字
* 条件判断语句
	* 可以是bool类型的值
	* 可以是条件表达式，表达式的结果必须是bool值
	* 可以是其他类型的值，除了0表示False，其他可以看作Ture
* ：
	* 固定格式，表示上一句结束
* elif
	* 条件选择语句关键字
	* 上一个if或者elif条件不成立运行到这一步
	* 的
	* 从
* else 





#### if嵌套
	if 第一个条件判断语句：
		代码块1
		if 第二个条件判断语句：
			代码块2
			if 第三个条件判断语句：
				代码块3
			else：
				第三个条件不成立语句
		else：
			第二个条件不成立语句
	else:
		第一个条件不成立语句
### str
* 什么是字符串
	* 串起来的字符叫字符串
	* 一串字符就成为字符串
	* Python中使用单引号或双引号报过的内容称为字符串
* 字符串的定义方式
	* str = "hello"
	* str = "123"
	* str = "Ture"
	* ... ...
* 字符串的运算
	* 字符串之间支持相加运算:字符串的拼接
	* 单个字符串支持正整数乘法运算:"abc" * 3 = "abcabcabc"
* 字符串的操作

* 字符串自带方法
	* eval(str) 
		* 求字符串表达式的值
	* len(str)
		* 求字符串的长度
	* str.lower() 
		* 把字符串中所有内容变成小写
	* str.upper() 
		* 把字符串中所有内容变成大写
	* str.swapcase() 
		* 把字符串中大写转换为小写，小写转换为大写
	* str.capitalize() 
		* 把字符串中元素第一个字母大写，其他全变为小写
	* str.title() 
		* 把字符串中元素每个单词首字母大写，其余小写
	* str.cent(width,fillchar) 
		* 设定字符串的宽度和填充元素,把字符串元素居中
			* width:设置长度
			* fillchar：设置填充元素
	* str.ljust(width[,fillchar]) 
		* 设定字符串的宽度和填充元素,把字符串元素居左
			* width:设置长度
			* fillchar：设置填充元素
	* str.rjust(width[,fillchar]) 
		* 设定字符串的宽度和填充元素,把字符串元素居右
			* width:设置长度
			* fillchar：设置填充元素
	* str.zfill(width) 
		* 设定字符串宽度，如果字符串长度小于设定宽度，就把字符串放在右侧，左侧填充0
	* str.count(x,start,end) 
		* 在字符串中查找指定元素出现的次数，可以设定的开始和结束位置。
	* str.find(x,start,end) 
		* 在字符串中查找指定元素在字符串中第一次出现的位置，可以设定开始结束位置，没找到则返回值-1
	* str.index(x,start,end) 
		* 查找指定元素在字符串中第一次出现的位置，可以设置起始和结束位置，找不到就报错
	* str.rfind(x,start,end)
		* 从右侧向左查找指定元素位置，返回值为最远元素位置值，可以指定范围，找不到会返回-1
	* str.rindex(x,start,end)
		* 从右侧向左查找指定元素位置，返回值为最远元素位置值，可以指定范围，找不到会报错
	* str.strip(x)
		* 去除字符串两侧的空格或指定内容
	* str.lstrip(x)
		* 去除字符串左侧的空格或指定内容
	* str.rstrip(x)
		* 去除字符串右侧的空格或指定内容
	* str.split(spe,maxsplit)
		* 使用sep作为分隔符分割字符串，从字符串中删除sep，给定maxsplit来设定分割次数。无设定sep时则以空白字符串为分隔符。
	* str.splitline()
		* 把字符串以\n为分割点分割成列表
		* 
			    str01 = "床前明月光，\n疑是地上霜，\n举头望明月，\n低头思故乡"
				print(str01.splitlines())
				>>>['床前明月光，', '疑是地上霜，', '举头望明月，', '低头思故乡']
	* str.join(iterable)
		* 把字符串str插入到序列iterable每个元素中间
	* max(str)
		* 查找字符串中最大的元素
	* min(str)
		* 查找字符串中最小的元素
	* str.replace(old,new[,max])
		* 把字符串中元素old替换成new，count设定个数
	* str.maketrans(str01,str02)
	* str.translate(table,deletechars,"")
		* 按照映射的规则替换内容
		* maketrans制顶映射规则
		* translatean按照映射规则替换内容
	* str.isalpha()
		* 判断字符串内容是否是字符，字母、文字返回值True，数字、符号返回值False
	* str.isalnum()
		* 判断字符串内容是否全是字母、文字、数字返回值True，符号返回值False
	* str.isupper()
		* 判断字符串内容是否全部大写
	* str.islower()
		* 判断字符串内容是否全部小写
	* str.istitle()
		* 判断字符串内容，满足titl的特征，每个英文单词首字符大写。
	* str.isdigit()
		* 判断字符串内容是否是阿拉伯数字，浮点数返回值False
	* str.isnumeric()
		* 判断字符串内容是否是数字，浮点数返回值False，支持中文数字，中文大写数字，其他国家语言数字。
	* str.isdecimal()
		* 判断数字字符串是否全部是十进制
	* str.isspace()
		* 判断字符串是否是空格
	* str.startswith(x)
		* 判断字符串是否以x为开头
	* str.endswith
		* 判断字符串是否以x为结尾
	* str.encode()
		* 编码成二进制
	* str.decode()
		* 二进制解码
	* ord()
		* 把字符转换为数字
		* 
				print(ord("杜"))
				>>>26460
	* chr()
		* 把数字转换为字符 
		* 	
				print(chr(26460))
				>>>杜