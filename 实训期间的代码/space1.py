from selenium import webdriver
import time
def get_liuyanban(qq,pwd):
    #加载驱动
    driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    driver.maximize_window()#打开网页全屏操作

    #访问QQ号路径
    driver.get('https://qzone.qq.com')
    driver.implicitly_wait(3)
    print(qq+'的空间留言板')
    try:
        driver.find_element_by_id('login_div')
        a=True
    except:
        a=False
        
    if a==True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()#模拟鼠标点击（按钮或标签）
        driver.find_element_by_id('u').clear()#把之前的寻找记录（文本框中的文本）清楚
        driver.find_element_by_id('u').send_keys(qq)#用户名密码写入文本框
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(pwd)
        driver.find_element_by_id('login_button').click()#调用登陆按钮的ID，实现登录
        driver.implicitly_wait(3)#等待，3s内一直尝试执行上一行代码
         
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')#找当前页面特有的标签判断是否登录进页面（头像）
        b=True
        print('可以访问')
    except:
        b=False
        print('没有访问权限或者网络错误，请重试')

    if b==True:
        delete=driver.find_element_by_id('dialog_button_1').click()#去除黄钻框
        delete=driver.implicitly_wait(10)#等待
        print('开始加载')
        liuyan=driver.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[4]/a').click()#模拟点击留言板
        driver.implicitly_wait(3)
        driver.switch_to.frame(driver.find_element_by_class_name('app_canvas_frame'))#跳转到此frame
       

        num=driver.find_element_by_id('cnt')#获取留言数量
        x=int(num.text)
        y=x//10+1 #整除10
        for i in range(y):
            time.sleep(3)#让系统进行加载 ，没加载一页等待3秒
            names=driver.find_elements_by_xpath('//*[@class="username"]/a')#//*表示在整个文档中查找括号里的内容,/a指class下面的a标签
            ments=driver.find_elements_by_class_name('cont')#找到留言内容的class
            print('第%s页留言'%(i+1))#提取
            for name,ment in zip(names,ments):#把留言人和留言内容打包在一个元组，zip里的元素必须是可以循环的元素，且长度必须一样
                data={
                    '留言人':name.text,
                    '留言内容':ment.text
                    }#打包为一个字典
                print(data)
            if i+1!=y:
                page_down=driver.find_element_by_xpath('//*[@id="pager_bottom"]/div/p[1]/a[2]')
                page_down.click()#翻页操作
                driver.implicitly_wait(3)
    print('OK')
    print("=======完成=======")
##    driver.close() #关闭模拟的浏览器窗口
##    driver.quit() #退出selenium模拟器
if __name__=='__main__':
    get_liuyanban('1535833348','fengchenxue520,')





















































