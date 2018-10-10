from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11297555'
API_KEY = 'ZfqSxzdYiTEGZPwdfEfT8tFx'
SECRET_KEY = 'dZTII9XAptEGoEqnvCkeCY5SVOa1v0t4'
  
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)  
  
 
filePath = "114.jpeg"  
def get_file_content(filePath):  
    with open(filePath, 'rb') as fp:  
        return fp.read()  
  
  
options = {  
    'max_face_num': 1,  
    'face_fields': "age,beauty,expression,faceshape",  
}  
  
result = aipFace.detect(get_file_content(filePath),options)  
  
print(result)  
print(type(result))  
