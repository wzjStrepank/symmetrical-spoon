## Python内置数据类型
### list--列表
	列表是一个数据容器，可以存放多个数据
	这些数据可以是不同类型的，数据元素之间使用","分割
	列表的格式
		list = [obj1,obj2,obj3,...]
		list = []
		list = list(iterable、序列)
	列表元素的读取
		列表是有序的
		列表可以通过下标获取指定位置的元素：list[index]
		如果下标超出范围会报错
		可以使用for和whil循环遍历内容
	列表的截取
		list[start：],从指定位置截取到最后
		list[start:end],范围左闭右开
		list[start:end:step],step步长，默认为1，可以负数
		列表下标可以负数，表示从后向前数，最后一个元素下标为-1
* 列表的创建

		list[]
		list(iterable)
* 元素的读取
* 列表的常用操作
	* 增
		* list.insert(index,object)
			* 在指定下标index元素位置前面插入元素object,如果index超出列表最大值，则默认放在末尾 ，insert（）必须设定两个参数，insert会对列表产生改变
		* list.append(object)
			* 在列表最后插入元素object
		* list.extend(iterable)
			* 参数iterable可以是列表，也可以是其他类型的序列，拆分之后加入到列表末尾
	* 删
		* del list[index]
			* 删除下标index位置的元素，index超出范围会报错
		* del list
			* 从内存中删除列表
		* list.pop(index)
			* 摘出下标index位置的元素，index默认none，默认最后一个，返回值为这个元素，原列表被改变，index超出范围会报错，
		* list.remove(value)
			* 删除第一个被发现的value元素，找不到value元素则会报错
		* list.clear
			* 清除列表内所有内容
	* 改
		* list[index] = value
			* 指定index位置的元素赋予新值value
	* 查
		* in
		* not in
		* list.index(value,start,stop)
			* start，stop默认none，查找指定元素value在列表中第一次出现的下标，返回值为int，找不到则报错，
		* list.count(value)
			* 查找指定元素value在列表中的个数，返回值为int，找不到则为0
	* 其他操作
		* len()
		 
		* max()
		* min()
		* list.sort()
			* 把列表内元素按照大小顺序排序，改变原本列表变量，返回值为None
		* reverse()
			* 把列表内元素倒序排序，改变原本列表变量，返回值为None
		* 列表相加
		* 列表重复输出
		* 列表比较
* 列表嵌套
	* list = [[list1],[list2],...]
		* 并没有真正的多维列表，实际是把列表当做一个整体放入列表，形成嵌套遍历多位列表中的每一个元素需要使用多重循环
### tuple--元组
	python内置数据类型
	元素一旦确定不可改变---元组的操作方法很少
	元组是不可变类型数据，可通过下标访问数据，可以使用切片方式截取内容
	元组不能为空
* 创建元组
	
		tuple = ()
		tuple = (1,2,3,4,5)
		tuple = (1) xxxx这个不是元组，是括起来的数字
		tuple = (1,)这个是元组
		tuple = tuple(可迭代的序列)
* 元组的访问
	* tuple[index]
		* 元组可可以通过下标访问
	* tuple[start:end:step],元组可以切片

	* 可以使用for和while遍历元组
* 元组的方法
	* tuple.index(value,start,stop)
		* start，stop默认none，查找指定元素value在元组中第一次出现的下标，返回值为int，找不到则报错
	* tuple.count(value)
		* 查找指定元素value在元组中的个数，返回值为int，找不到则为0
* 元组的其他操作
	* len()
	* max()
	* min()
	* in()
	* not in()
	* 元组相加 
	* 元组重复输出
	* 元组比较
		
### dict--字典

	字典概述
		以键值对的方式存储数据
		查询和改变元素值都通过key进行访问，
		键值对使用":"连接，键值对使用","隔开
		同一字典中，键不能重复，如果重复，后面的键值对会覆盖前面的那个
		字典使用{XX:YY}包裹
* 创建字典
	
		dict = {}
		dict = {key1:value1,key2:value2,...}
* 字典元素的读取
	* 通过创建字典对象，调用元素的key可以获取指定的值value，
	* 
			print(dict[key])
			===>
			value
* 字典增删改查
	* 增加
		* dict[new_key]=value
	* 修改
		* dict[old_key]=value
			* 使用字典对象调用key，重新指定一个value，如果没找到key，则新创建键值对
	* 删除
		* dict.pop(key)
			* 删除字典里指定元素，返回值是对应键值对key的value，如果没设定key就报错
		* dict.popitem()
			* 删除字典里的最后一个键值对，返回值是删除的整个键值对
		* dict.clear()
			* 把字典dict内容清除，返回值是None
		* del dict[key]
			* 删除key指向的键值对
		* del dict
			* 从内存中删除这个dict
	* 查看
		* dict.get(key)
			* 在字典中查看key指向的value，返回值是value。如果设定的key不存在，则返回None
		* dict.keys()
			* 获取字典中所有的键值，组成列表
		* dict.values()
			* 获取字典中所有的键值属性value，组成列表
		* dict.items()
			* 获取所有的键值对，组成列表
* 字典的遍历
	* while
		* 字典没有下标，无法直接使用循环遍历
	* for
		* 获取所有的键

				for i in dict_info:
					print(i,end=",")
		* 获取所有的值
		
				for i in dict
					print(dict_info[i]
		* 获取所有的item--键值对

				items = dict_info.items()
				for item in items:
					print(item,end=",")

### set--集合
	集合相对于字典，只有value，没有key的数据集
	相对于列表，集合数据不能重复，数据在集合中无序
	集合是可变类型，集合是无序的
* 集合的遍历
	* 集合是无序的，没有下标
	* 可以使用for循环进行遍历
	* 不可以使用while循环遍历
* 创建集合

		set = {value1,value2,value3,....}
		set = set(序列)-->如果序列中有重复元素，会被忽略
		set = {x x for in rangr(10)}
* 集合的操作
	* 增
		* set.add(element)
			* 添加一个元素到集合中，如果已经存在则无改变,无返回值
		* set.update(iterable)
			* 在集合中添加序列iterable，相当于取并集去重
	* 删除
		* set.pop()
			* 官方说摘除任意一个元素，运行结果发现总是摘除第一个，返回值是此元素	
		* set.remove(element)
			* 删除指定元素element，找不到则报错
		* set.clear()
			* 清空集合
		* del set
			* 删除此集合
		* set.discard(element)
			* 删除指定元素element，找不到就不改变
	* 集合的其他操作
		* len()
		* max()
			* 比较集合内元素大小，返回最大的那个--元素类型要一致，否则报错
		* min()
		* in   not in


		* 差集、并集、交集
		* set.difference(iterable)
			* 