import requests
url ="http://119.6.110.75:6677/loginAction.do"
data={"zjh":20170443,"mm":"20170443"}
headers={"User-Agent":" Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; McAfee)"}
session = requests.Session()
session.post(url,data)

temp1="http://119.6.110.75:6677/lnkbcxAction.do"
data2={"zxjxjhh":" 2017-2018-2-1"}
resp=session.post(temp1,data2)
fw = open("课表.html","wb")
fw.write(resp.content)
fw.close()
