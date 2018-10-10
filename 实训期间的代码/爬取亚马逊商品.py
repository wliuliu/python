import requests
url = "https://www.amazon.cn/dp/B0043T7FXE/ref=gwgfloorv1_AGS_a_0?_encoding=UTF8&ie=UTF8&smid=A2EDK7H33M5FFG&pf_rd_p=de9bf570-0292-48c6-afed-1492835470c4&pf_rd_s=desktop-4&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=Z0607XB3Q91RREWA7N0J&pf_rd_r=Z0607XB3Q91RREWA7N0J&pf_rd_p=de9bf570-0292-48c6-afed-1492835470c4"
try:
    kv = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")
