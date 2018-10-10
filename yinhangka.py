from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11285062'
API_KEY = 'EEZ79phRG58l9MZh8faOOkKG'
SECRET_KEY = '5pDmpjMd7YY33pzRWuKliLYCdHjLt4Gc'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('113.jpg')


""" 调用银行卡识别 """
result = client.bankcard(image)
words_result = result['words_result_num']
+bank_card_numbe = words_result['银行卡号']['words']
+bank_name = words_result['银行名']['words']

print(+bank_card_numbe)
print(+bank_name)
