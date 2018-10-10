import requests

url="http://www.163.com/" #地址字符串。http不能少

result=requests.get(url) #调用request库的get方法获取url
result.encoding=result.apparent_encoding
print("------encoding-----")
print(result.encoding) #encoding返回结果的编码，若网站没有设置，则为默认编码 
print("------apparent_encoding------")
print(result.apparent_encoding)
print("------status_code------")
print(result.status_code)
print("------headers------")
print(result.headers)
#print("------text------")
#print(result.text) #把返回数据以文本形式展示
#print("------content------")
#print(result.content) #把返回数据以二进制流的形式展示
fw=open("网易.html","wt",encoding=result.encoding)#wt为文本形式，把encoding设置为结果里的编码
fw.write(result.text)
fw.close()
