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

image = get_file_content('112.jpg')
idCardSide = "front"

""" 调用身份证识别 """
result = client.idcard(image, idCardSide)
words_result = result['words_result']
address = words_result['住址']['words']
born = words_result['出生']['words']
name = words_result['姓名']['words']

print(address)
print(born)
print(name)
