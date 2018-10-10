import urllib.request  
import json
def http_get(url):
    response = urllib.request.urlopen(url)
    return response.read()
def formatName(name):
    return'{name:<{len}}'.format(name=name,len=22-len(name.encode('GBR'))+len(name))

url1='http://api.douban.com/v2/movie/top250?start=0&count=100'
url2='http://api.douban.com/v2/movie/top250?start=100&count=200'
url3='http://api.douban.com/v2/movie/top250?start=200&count=250'
result1=http_get(url1)
result2=http_get(url2)
result3=http_get(url3)
jsonResult1=json.loads(result1)
jsonResult2=json.loads(result2)
jsonResult3=json.loads(result3)

subjects=jsonResult1['subjects']
subjects+=jsonResult2['subjects']
subjects+=jsonResult3['subjects']
count=0
for s in subjects:
    count+=1
    print(str(count)+":"+s['title']+"\t评分:"+str(s['rating']['average'])+"\t上映年份:"+str(s['year']))
