import requests

url= "https://www.taobao.com"

result = requests.get(url)
result.encoding=result.apparent_encoding
print("-----encoding-----")
print(result.encoding)
print("-----apparent_encoding -----" )
print(result.apparent_encoding)
print("-----status_code-----")
print(result.status_code)
print("-----headers-----")
print(result.headers)
#print("-----text-----")
#print(result.text)
#print("-----content-----")
#print(resu1t.content)
fw = open("淘宝.html","wt",encoding=result.encoding)
fw.write(result.text)
fw.close()
