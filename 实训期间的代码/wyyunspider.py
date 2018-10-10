import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

#chrome_options=Options()
#chrome_options.add_argument('headless')

def get_song_times(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    driver.switch_to.frame('g_iframe')
    comments=driver.find_element_by_class_name('j-flag').get_attribute('textContent')
    driver.close()

    return comments
###########################################################################################
###爬取主要信息，解析函数加写入csv
def parse(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    driver.switch_to.frame('g_iframe')

    # 歌单名
    song_list_title = driver.find_elements_by_xpath('//div[@class="tit"]/h2')[0].get_attribute('textContent')
    # 歌单作者
    song_list_author = driver.find_elements_by_xpath('//span[@class="name"]/a')[0].get_attribute('textContent')
    # 歌单播放量
    song_list_times = driver.find_element_by_id('play-count').get_attribute('textContent')

    base_path=os.getcwd()  #
    dir_path=os.path.join(base_path,'yun_song_list')
    if not os.path.exists(dir_path):
         os.mkdir(dir_path)

    if '|' in  song_list_title:
        song_list_title=song_list_title.replace('|','')


    filename='%s.csv'%song_list_title
    filepath=os.path.join(dir_path,filename)
    with open(filepath,'a',encoding='utf-8',newline='\n') as fp1:
        csvobj=csv.writer(fp1)
        csvobj.writerow(['歌单名','歌单作者','歌单播放量'])
        csvobj.writerow([song_list_title, song_list_author, song_list_times])
        csvobj.writerow(['歌曲名', '歌曲作者', '评论数'])

    for i in driver.find_elements_by_xpath('//tbody/tr'):

        # 歌曲名
        song_title = i.find_elements_by_tag_name('td')[1].find_element_by_tag_name('b').get_attribute('title')
        # 歌曲url
        song_url = i.find_elements_by_tag_name('td')[1].find_element_by_tag_name('a').get_attribute('href')
        # 歌曲作者
        song_author = i.find_elements_by_tag_name('td')[3].find_element_by_tag_name('span').get_attribute('title')
        # 评论数
        song_comments = get_song_times(song_url)

        with open(filepath, 'a', encoding='utf-8', newline='\n') as fp2:
            csvobj = csv.writer(fp2)
            csvobj.writerow([song_title, song_author, song_comments])

    driver.close()


if __name__ == '__main__':
    page = 1
    try:
        page = int(input('请输入要获取的歌单页数:'))
    except:
        raise ('请输入正确的页数')
    for i in range(1, page + 1):
        base_url = r'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset={}'.format(
            (page - 1) * 35)

        driver = webdriver.Chrome()
        driver.get(base_url)
        time.sleep(1)
        driver.switch_to.frame('g_iframe')
        j=1
        for i in driver.find_elements_by_class_name('msk'):
            song_list_url = i.get_attribute('href')
            parse(song_list_url)
            print('歌单{}爬取完成'.format(j))
            j+=1
        print('第{}页爬取完成'.format(i))
        driver.close()
