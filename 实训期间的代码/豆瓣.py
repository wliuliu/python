from selenium import webdriver
import time
def get_paiming():
    driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    driver.maximize_window()    
    driver.get('https://movie.douban.com/chart')
    driver.implicitly_wait(3)     
    try:
        driver.find_element_by_id('ranking')
        b=True
        print('可以访问')
    except:
        b=False
        print('没有访问权限或者网络错误，请重试')

    if b==True:
        delete=driver.find_element_by_id('100:90&action=').click()
        delete=driver.implicitly_wait(10)
        print('开始加载')
        dianying=driver.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[4]/a').click()
        driver.implicitly_wait(3)
        driver.switch_to.frame(driver.find_element_by_class_name('app_canvas_frame'))
       
        time.sleep(3)
        num=driver.find_element_by_id('cnt')
        x=int(num.text)
       
        for i in range(y):
            time.sleep(3)
            names=driver.find_elements_by_xpath('//*[@class="username"]/a')
            ments=driver.find_elements_by_class_name('cont')
            print('第%s页留言'%(i+1))
            for name,ment in zip(names,ments):
                data={
                    '电影名':name.text,
                    '评分':ment.text
                    '评分人数'
                    '主演'
                    }
                print(data)
            if i+1!=y:
                page_down=driver.find_element_by_xpath('//*[@id="pager_bottom"]/div/p[1]/a[2]')
                page_down.click()
                driver.implicitly_wait(3)
    print('OK')
    print("=======完成=======")
##    driver.close() 
##    driver.quit() 
if __name__=='__main__':
    get_liuyanban('1535833348','fengchenxue520,')

