from bs4 import BeautifulSoup
import requests

def getHTML(web_url):
    url = "https://movie.douban.com/top250?start=%s&filter=%22%20%%20page"
    header = {"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
    html = requests.get(url=web_url, headers=header)
    Soup = BeautifulSoup(html, "lxml")
    data = Soup.find("ol").find_all("li")
    return data

def get_info(movie):
    f = open("E:\pythonwork0\pythonwork\python\实训期间的代码\dianpai.txt", "a")
    for info in movie:
        nums = info.find('em')
        num = nums.get_text()
        names = info.find("span")  
        name = names.get_text()
        scores = info.find_all("span", {"class": "rating_num"})
        score = scores[0].get_text()


        f.write(num + '、')
        f.write(name + "\n")
        f.write(score)
        f.write("\n\n")
        
    f.close()


