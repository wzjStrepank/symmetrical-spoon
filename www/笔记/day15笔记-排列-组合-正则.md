## 15.01_Python语言基础(排列)(熟练)
* 在python中使用iterTools模块来完成排列
* 从n不同的元素中取m个元素，会按照特定的顺序排成一列-----》排列
* 格式：
	* iterTools.permutations(序列，排列个数)
	
	[1,2,3,4]  2
#### 排列案例：

#
	import itertools
	mylst = list(itertools.permutations([1,2,3,4],2))#12
	print(mylst)
	mylst = list(itertools.permutations([1,2,3,4],3))#24
	print(mylst)

#### 排列可能出现的次数
* n!/(n-m)!






## 15.02_Python语言基础(组合)(熟练)
* itertolls模块
* combinations(序列，组合的个数)
#### 组合案例	
	import itertools
	
	mylist = list(itertools.combinations([1,2,3,4,5],3))
	print(mylist)
	"""
	m    n
	5    5   1
	5    4   5
	5    3   10
	5    2   10
	
	n！/（m!*(n-m)!）




## 15.03_Python语言基础(破解密码)(练习)
#### 破解数字和字母组成的六位数的密码
#### 生成6为数字密码
	import itertools

	list02 = itertools.product("012345", repeat=6)
	list03 = list(list02)
	# print((list03))
	count = 0
	str = ""
	for l in list03:
	    # print(l)
	    count += 1
	    str = "".join(l)
	    print(str)
	print(count)
	print(str)
	print(type(str))
#### 生成字母和数字组成密码
#
	
	# 获取六位字符
	# 6789qweryuiopasdfghjklzxcvbnmqwerqQWERTYUIOPASDFGHJKLZXCVBNM
	password = list(itertools.product("012345", repeat=6))
	print(type(password))
	# 定义密码字符变量
	password_str = ""
	# 开始破解
	for i in password:
	    password_str = "".join(i)
	    # 如果找到则破解完成
	    if password_str == "543210":
	        break
	print(password_str)




## 15.04_Python语言基础(正则表达式的概述)(重点)
* 开发中会有大量的字符串的处理，字符串的格式化的校验
	* 场景：
   		* 判断一个字符串否是手机号
* 文件中，查找以qianfeng开头的语句
* 定义：
   * 正则表达式：   regex   re
* python 内置模块   re   ---->正则表达式





## 15.05_Python语言基础(re模块的基本操作)(重点)

* Python中内置re模块
* 在python中需要通过对正则表达式对字符串进行匹配，需要使用re模块

#### re模块的使用案例：
#
	#导入re模块
	# import re
	#使用match方法进行匹配
	"""
	match 格式：
	   match(正则表达式（Match），需要匹配的字符串(object))
	
	"""
	# reslut = re.match(正则表达式，需要匹配的字符串)
	#提取数据  group（）函数
	# reslut.group()

>**说明：**
re.match()用来进行正则表达式匹配检查方法，<br/>
如果字符串匹配正则，match方法返回的是匹配的对象（MAtch,object）<br/>
否则返回None(注意不是"")
***
#
	import re
	reslut = re.match("qianfeng","qianfeng.com")
	reslut1 = re.match("haha","qianfeng.com")
	print(reslut.group())
	print(reslut1)






## 15.06_Python语言基础(表示字符)(重点)

* 正则表达式的单个字符匹配
# 
	字符      功能
	.        匹配任意1个字符（除\n）
	[]       匹配[]中列举的字符
	\d       匹配数字（0~9）
	\D       匹配非数字，即不是数字
	\s       匹配空白格   空格  tab
	\S       匹配非空格
	\w       匹配单词字符，a~z A~Z 0~9 _
	\W       匹配非单词字符
#### 正则表达式的单个字符匹配案例：
#
	import re
	
	ret = re.match(".","a")
	print(ret.group())
	
	ret = re.match(".","M")
	print(ret.group())
	
	ret = re.match(".","1.0")
	print(ret.group())
	
	#如果hello的首字母小写，那么正在表达式的匹配需要小写吗？
	ret = re.match("h","hello python")
	print(ret.group())
	ret = re.match("H","Hello python")
	print(ret.group())
	
	ret = re.match("[hH]","hello python")
	print(ret.group())
	
	ret = re.match("[hH]","Hello python")
	print(ret.group())
	
	#匹配0~9的数字
	ret = re.match("[0123456789]","7hello python")
	print(ret.group())
	ret = re.match("[0-9]","7hello python")
	print(ret.group())
	ret = re.match("\d","5hello python")
	print(ret.group())
	
	ret = re.match("嫦娥1号","嫦娥1号发射成功")
	print(ret.group())
	ret = re.match("嫦娥2号","嫦娥2号发射成功")
	print(ret.group())
	ret = re.match("嫦娥3号","嫦娥3号发射成功")
	print(ret.group())
	
	ret = re.match("嫦娥\d号","嫦娥1号发射成功")
	print(ret.group())
	ret = re.match("嫦娥\d号","嫦娥2号发射成功")
	print(ret.group())
	ret = re.match("嫦娥\d号","嫦娥3号发射成功")
	print(ret.group())













## 15.07_Python语言基础(转义字符和原始字符)(重点)
### 转义字符和原始字符案例：
	import re
	mm = r"c:\a\b\c"
	print(mm)
	mm = "c:\\a\\b\\c"
	print(mm) 
	
	reslut = re.match("c:\\\\",mm).group()
	print(reslut)#c:\
	
	reslut1 = re.match("c:\\\\a",mm).group()
	print(reslut1)#c:\a
	
	reslut = re.match(r"c:\\", mm).group()
	print(reslut)  
	
	reslut1 = re.match("c:\\\\a", mm).group()
	print(reslut1)  
	
	"""
	python中字符串前面加上r表示原生字符串
	”\“:转义的作用
	"""
	ret = re.match("c:\\\\a", mm).group()	
	print(ret)









## 15.08_Python语言基础(表示数量)(重点)
#### 表示数量
	字符        功能
	*      表示匹配前一个字符出现0次或者无限次，即可有可无
	+      表示匹配前一个字符出现1次或者无限次，即至少一次
	？     表示匹配前一个字符出现1次或则0次,即，要么一次，要么没有
	
	{m}    表示匹配前一个字符出现m次
	{m,}   表示前一个字符至少出现m次
	{m,n}  表示匹配字符出现从m到n次
	{,n}   不存在的写法
	
		案例：
		需求：一个字符串第一个字母为大写字符，后面都是小写并且这些小写字母可有可无




#### 表示数量案例：
	import re
	ret = re.match("[A-Z][a-z]*","Mm").group()
	print(ret)
	ret1 = re.match("[A-Z][a-z]*","Aabcdef").group()
	print(ret1)
	
	"""
	匹配变量名是否有效
	"""
	
	ret2 = re.match("[a-zA-Z_]+[\w_]*","name1").group()
	print(ret2)
	
	
	ret3 = re.match("[a-zA-Z_]+[\w]*","m_name").group()
	print(ret3)
	
	"""
	案例：
	匹配0~99之间的数字
	"""
	ret4 = re.match("[1-9][\d]*","5").group()
	print(ret4)




## 15.09_Python语言基础(表示边界)(重点)
#
	字符      功能
	^        匹配字符串的开头
	$        匹配字符串的结尾
	\b       表示匹配一个单词的边界


#### 匹配@XXX.com邮箱地址
#
	result = re.match("[\w]{4,20}@126\.com", "dushine@126.com")
	print(result.group())

	result = re.match("[\w]{4,20}@126\.com$", "dushine@126.com")
	print(result.group())
	
	result = re.match("[\w]{4,20}@126\.com$", "dushine@126.comcom")
	print(result.group())
	
	
	#\b--匹配单词--ver
	ret2 = re.match(r".*\bver\b","ho ver abc").group()
	print(ret2)
	
	# 报错
	# ret3 = re.match(r".*\bver\b", "ho verabc").group()
	# print(ret3)
	
	# 报错	
	ret4 = re.match(r".*\bver\b", "hover abc").group()
	print(ret4)












## 15.10_Python语言基础(匹配分组、断言)(重点)
#
	字符        	功能
	|       	或，匹配左右任意一个表达式
	(ab)    	将括号中字符作为分组

#### 匹配分组案例
	import re
	# | 连接表达式
	#需求匹配0~100之间的数字

#### 匹配邮箱案例：
	#案例：匹配163 /  126 / qq  邮箱之间的数字
	#()
	result = re.match("\w{6,20}@(hotmail|126|163|qq)\.com", "dushine2008@126.com").group()
	print(result)
	
	result = re.match("[\w\d]{6,20}@(hotmail|126|163|qq)\.com", "20082008@126.com").group()
	print(result)



####匹配html标签
	   # <html>haha11_#$%^</html>
	"""
	
	<a>
	<>
	<p>
	<br>
	<html>
	"""
	result = re.match("<[a-zA-Z]*>.*</[a-zA-Z]*>", "<html>hello</html>").group()
	print(result)
 







## 15.11_Python语言基础(re模块的高级用法)(掌握)
#### 字符串的切割
#
	import re
	str01 = "life is short and i use Python!"
	# 字符串的切割
	result = re.split("\s*", str01)
	print(result)
	result = re.split(" *", str01)
	print(result)
	result = re.split(" +", str01)
	print(result)

#
	#findall()
	"""
	格式：
	findall(pattern，String,flags=0)
	
	pattern:匹配的正则表达式
	string：需要匹配的字符串
	
	功能findall：查找所有元素得到一个列表  
#### findall使用案例：
	str01 = "life is short and i use Python! life life"

	result = re.findall("life", str01)
	print(result)



#### 字符串的替换和修改
* sub(pattern,rep1,string,count = 0)
* subn(pattern,rep1,string,count = 0)
* pattern:正则表达式
* rep1：指定用来替换的字符串
* string：目标字符串
* count：最多替换的次数

功能：
   在目标字符串中以正则的方式匹配字符串，
   匹配完成后在替换成指定的字符串，可以指定替换的次数，如果不写表示替换全部
#### 替换内容案例：
#
	str1 = "life is short and i use Python!"
	ret1 = re.sub(r"(i)", "we", str1)
	print(ret1)
	
	# 显示替换次数
	ret2 = re.subn(r"(i)", "oo", str1)
	print(ret2)


* sub返回的是一个被替换的字符串
* subn返回的是一个元祖，第一个元素是一个被替换的字符串，
* 第二个元素被替换的次数










## 15.12_Python语言基础(re模块运行原理)(掌握)
* re模块做两个事
	* 1.编译正则：如果正则本身不合法，报错
	* 2.用编译后的正则表达式去匹配对象
#### compile(pattern,flags=0)
	#编译正则
	pat = r"\w{4,20}@(126|163|qq)\.com"
	ret3 = re.compile(pat)
	print(ret3.match("XXXXXX"))
	
	re对象的调用
	re.match(pattern,string,flags= 0)
	ret3.match(string)


#### compile使用案例：
	# compile(pattern,flags=0)
	
	result = re.match("\w{4,20}@(126|163|qq)\.com", "dushine@126.com").group()
	print(result)
	print("*" * 20)
	pat = r"\w{4,20}@(126|163|qq)\.com"
	ret03 = re.compile(pat)
	result = ret03.match("dushine@126.com")
	print(result)
	
	
	
#### search使用案例：
	
	result = ret3.search("dushine@126.com")
	print(result)
	
	result = ret3.findall("dushine@126.com")
	print(result)
	
	result = ret3.finditer("dushine@126.com")
	print(result)


