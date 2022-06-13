# -*- coding: utf-8 -*-
'''
方法	         作用
json.dumps()	将 Python 对象转换成 JSON 字符串。
json.loads()	将 JSON 字符串转换成 Python 对象。
json.dump()  	将 Python 中的对象转化成 JSON 字符串储存到文件中。
json.load() 	将文件中的 JSON 字符串转化成 Python 对象提取出来。
'''

import json

# 转为python对象
website_info = '{"name":"测试","pv":"50万"}'
py_dict = json.loads(website_info)
print("python字典数据格式:%s;数据类型:%s" % (py_dict, type(py_dict)))

# 将对象转为json格式写入到文件中
dict_info = {'name': 'test', 'age': 18}
with open('web.json', 'a') as f:
    json.dump(dict_info, f, ensure_ascii=False)

# 操作文件流对象，转为python对象
with open('web.json', 'r') as f:
    print(json.load(f))

# 将对象转json字符串
items = json.dumps(dict_info, ensure_ascii=False)
print("转换之后的数据类型为:", type(items))
