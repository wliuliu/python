from selenium import webdriver
import requests
from requests import get 
import json
kd_dict={1:'shentong',2:'ems',3:'shunfeng',4:'yuantong',5:'zhongtong',6:'yunda',7:'quanfengkuaidi',8:'debangwuliu',9:'zhaijisong',10:'tiantian',11:'huitongkuaidi'}  
while True:  
    print('支持以下快递类型')  
    print('1.申通快递')  
    print('2.EMS邮政快递')  
    print('3.顺丰速运')  
    print('4.圆通快递')  
    print('5.中通快递')  
    print('6.韵达快递')  
    print('7.全峰快递')  
    print('8.德邦物流')  
    print('9.宅急送')  
    print('10.天天快递')  
    print('11.汇通快递')  
    print('0.退出程序')  
    num=int(input('请输入你选择的快递类型：'))  
    if num==0:  
        break  
    while num not in range(1,12):  
        num = int(input('选项有误，请重新选择：'))  
    type=kd_dict[num]  
    postid=input('请输入你的快递单号')  
    #拼接一个url  
    url='http://www.kuaidi100.com/query?type=%s&postid=%s '%(type,postid)  
    #发送请求  
    rs=requests.get(url)  
    kd_info=json.loads(rs.text)  
    msg=kd_info['message']  
    if msg=='ok':  
        data=kd_info['data']  
        for msg in data:  
            time=msg['time']  
            context=msg['context']  
            print('时间：%s\n%s'%(time,context))  
    else:  
        if msg=='参数错误':  
            print('您输入的快递单号有误，请重新输入：')  
        else:  
            print('您的单号已过期 ')

