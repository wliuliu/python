import requests
ip = input("输入想要解析的IP")
url = "http://m.ip138.com/ip.asp"
params={"ip":ip}   #打包参数
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}    #模拟浏览器爬取信息
result = requests.get(url,params= params,headers=headers) #模拟了浏览器记得在request里加headers

if result.status_code==200:
    result.encoding=result.apparent_encoding #避免出现乱码
    fw = open('IPsearch.html',"wb")
    fw.write(result.content)
    fw.close()
else:
        print (result. status_code)
