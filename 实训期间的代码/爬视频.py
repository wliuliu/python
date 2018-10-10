import requests
try:
    url="https://cn-sdjn2-cu-v-02.acgvideo.com/upgcxcode/69/72/45067269/45067269-1-64.flv?expires=1530883800&platform=pc&ssig=QWG6KeymyMCaNw5buq7v_A&oi=1708109758&nfa=BpfiWF+i4mNW8KzjZFHzBQ==&dynamic=1&hfa=2030860003&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=2bb90d9e448440b4a0b11772beb0f4b6&nfc=1"
    headers ={"Referer":"https://www.bilibili.com/video/av26245192/?spm_id_from=333.334.bili_music.4","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
    result = requests.get(url,headers=headers)
    print(result.headers)
    if result.status_code==200:
        result.encoding=result.apparent_encoding
        fw = open('E:\python\pythonwork0\pythonwork\python\实训期间的代码video1.flv',"wb")
        fw.write(result.content)
        fw.close()
    else:
        print(result.status_code)
except MemoryError:
    print(" ")
