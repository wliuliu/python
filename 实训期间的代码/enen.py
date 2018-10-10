from bs4 import BeautifulSoup
import requests
import os

def get_html(web_url): 
    header = {"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
    html = requests.get(url=web_url, headers=header).text
    Soup = BeautifulSoup(html, "lxml")
    data = Soup.find("ol").find_all("li") 
    return data


def get_info(all_move):
    f = open("E:\pythonwork0\pythonwork\python\实训期间的代码\douban.txt", "a")

    for info in all_move:
        nums = info.find('em')
        num = nums.get_text()
        peos = info.find_all("span", {"class": "star"})
        peo = peos.get_text()
        names = info.find("span")
        name = names.get_text()
        scores = info.find_all("span", {"class": "rating_num"})
        score = scores[0].get_text()


        f.write(num + '、')
        f.write(peo)
        f.write(name + "\n")
        f.write(score)
        f.write("\n\n")

    f.close() 


if __name__ == "__main__":

    page = 0  
    while page <= 225:
        web_url = "https://movie.douban.com/top250?start=%s&filter=" % page
        all_move = get_html(web_url)  
        get_info(all_move)  
        page += 25
