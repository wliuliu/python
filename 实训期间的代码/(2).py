from bs4 import BeautifulSoup
import requests
import os
def get_html(web_url):
    header = {"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
    html = requests.get(url=web_url, headers=header)
    Soup = BeautifulSoup(html, "lxml")
    data = Soup.find("ol").find_all("li")
    return data

def get_info(movie):
    f = open("E:\pythonwork0\pythonwork\python\实训期间的代码\paiming.txt", "a")
    for info in movie:
        nums = info.find('em')
        num = nums.get_text()
        names = info.find("span")
        name = names.get_text()
        director = info.find("p") 
        director = directors.get_text()
        scores = info.find_all("span", {"class": "rating_num"})
        score = scores[0].get_text()

        f.write(num + '、')
        f.write(name + "\n")
        f.write(director + "\n")
        f.write(score)
        f.write("\n\n")

    f.close() 


if __name__ == "__main__":
    if os.path.exists("E:\pythonwork0\pythonwork\python\实训期间的代码\Pythontest1") == False:  
        os.mkdir("E:\pythonwork0\pythonwork\python\实训期间的代码\Pythontest1")
    if os.path.exists("E:\pythonwork0\pythonwork\python\实训期间的代码\douban.txt") == True:
        os.remove("E:\pythonwork0\pythonwork\python\实训期间的代码\douban.txt")

    page = 0  
    while page <= 225:
        web_url = "https://movie.douban.com/top250?start=%s&filter=" % page
        movie = get_html(web_url) 
        get_info(movie) 
        page += 25
