import requests

url="https://movie.douban.com/top250?start=%s&filter=%22%20%%20page" 

result=requests.get(url) 
result.encoding=result.apparent_encoding
print("------encoding-----")
print(result.encoding) 
print("------apparent_encoding------")
print(result.apparent_encoding)
print("------status_code------")
print(result.status_code)
print("------headers------")
print(result.headers)
print("------text------")
print(result.text) 
print("------content------")
print(result.content) 
fw=open("排行榜.html","wt",encoding=result.encoding)
fw.write(result.text)
fw.close()
