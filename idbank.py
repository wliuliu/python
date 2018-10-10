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
result_bank=client.bankcard(image)
print("银行卡号：",result_bank[ "result"]["bank_card_number"])
print("发卡银行：",result_bank[ "result"]["bank_name"])
