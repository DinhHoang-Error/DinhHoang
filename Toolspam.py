from urllib.parse import quote
from secrets import compare_digest
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures
    
except ImportError:
    import os
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033[1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]
random_color = random.choice(colors)
def idelay(o):
    while(o>0):
        o=o-1
        print(f"{trang}[{xanhnhat}DinhHoang{trang}] \033[1;33mV\033[1;34mu\033[1;35mi \033[1;32mL\033[1;33mò\033[1;34mn\033[1;35mg \033[1;36mC\033[1;33mh\033[1;34mờ {trang}[\033[1;35m.....""]""["+str(o)+"]""    ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}DinhHoang{trang}] \033[1;31mV\033[1;32mu\033[1;33mi \033[1;34mL\033[1;35mò\033[1;31mn\033[1;32mg \033[1;33mC\033[1;32mh\033[1;35mờ {trang}[\033[1;33m•{trang}....""]"f"{trang}[{xanhnhat}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}DinhHoang{trang}] \033[1;32mV\033[1;33mu\033[1;34mi \033[1;35mL\033[1;36mò\033[1;33mn\033[1;34mg \033[1;35mC\033[1;31mh\033[1;32mờ {trang}[\033[1;35m••{trang}...""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}DinhHoang{trang}] \033[1;31mV\033[1;33mu\033[1;35mi \033[1;33mL\033[1;31mò\033[1;32mn\033[1;34mg \033[1;36mC\033[1;35mh\033[1;31mờ {trang}[\033[1;32m•••{trang}..""]"f"{trang}[{do}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}DinhHoang{trang}] \033[1;32mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;31mn\033[1;35mg \033[1;33mC\033[1;36mh\033[1;35mờ {trang}[\033[1;38m••••{trang}.""]"f"{trang}[{tim}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanhnhat}DinhHoang{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{do}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(0.1)
        print(f"{trang}[{xanhnhat}DinhHoang{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')

chontool = f"""

     {trang}███████╗██████╗░██████╗░░█████╗░██████╗░
     ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
     █████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
     ██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
     ███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
     ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
                              
        𝙏𝙤𝙤𝙡 𝙒𝙖𝙧 𝘾𝙪̛̣𝙘 𝙈𝙪́𝙥 𝟮𝟬𝟮𝟰 ● 𝗨𝗽𝗱𝗮𝘁𝗲 𝟭.𝟮
        ____________________________________
            {trang} 𝘼𝙙𝙢𝙞𝙣 𝘿𝙚𝙥 𝙏𝙧𝙖𝙞 𝘿𝙞𝙣𝙝 𝙃𝙤𝙖𝙣𝙜
             𝙋𝙝𝙤̛̉ 𝘽𝙤̀: Dinh Hoang(Error)
            𝙏𝙞𝙠𝙏𝙤𝙠: @𝙖𝙘𝙘.𝙘𝙡𝙤𝙣𝙚_𝟱
        
               {xanhnhat}𝙉𝙚̂́𝙪 𝘼𝙣𝙝 𝙀𝙢 𝙏𝙝𝙖̂́𝙮 𝙏𝙤𝙤𝙡 𝙉𝙜𝙤𝙣 𝙏𝙝𝙞̀ 
               {trang}𝘾𝙝𝙤 𝘼𝙙𝙢𝙞𝙣 𝙓𝙞𝙣 𝟭 𝙁𝙡 𝙁𝙖𝙘𝙚𝙗𝙤𝙤𝙠 𝙉𝙝𝙚́
   {trang}     ____________________________________
"""

clear()
runbanner(chontool)
idcanspam=input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩{trang}𝗡𝗵𝗮̣̂𝗽 𝗜𝗗 𝗕𝗼𝘅 𝗖𝗮̂̀𝗻 𝗦𝗽𝗮𝗺 :{vang} ")
file_list = []
while True:
    ck=input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩{trang}𝗡𝗵𝗮̣̂𝗽 𝗖𝗼𝗼𝗸𝗶𝗲𝘀 𝗔𝗰𝗰{do}lấy trong mbasic) :{vang} ")
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
    except:
        print(f'{do}Cookie sai!!')   
runbanner(chontool)
lol = input(f"{xanhnhat}Bạn có muốn treo nhiều ngôn không {trang}({tim}y{vang}/{tim}n{trang}): {vang}")
if lol.lower() == "y":
      stt = 0
      loz = int(input(f"{xanhnhat}Bạn muốn treo bao nhiêu ngôn: "))
      while True:
        stt += 1
        name_files=input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩ {trang} 𝙉𝙝𝙖̣̂𝙥 𝙁𝙞𝙡𝙚 𝘾𝙝𝙪̛́𝙖 𝙉𝙤̣̂𝙞 𝘿𝙪𝙣𝙜 𝙈𝙪𝙤̂́𝙣 𝙎𝙥𝙖𝙢 (𝙑𝙙: 𝟭𝟮𝟯.𝘁𝘅𝘁) :{vang} ")
        file_list.append(name_files)
        if stt == loz:
          break
elif lol.lower() == "n":
      name_file=input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩ {trang} 𝙉𝙝𝙖̣̂𝙥 𝙁𝙞𝙡𝙚 𝙉𝙤̣̂𝙞 𝘿𝙪𝙣𝙜 𝙈𝙪𝙤̂́𝙣 𝙎𝙥𝙖𝙢 (𝙑𝙙: 𝟭𝟮𝟯.𝘁𝘅𝘁) :{vang} ")
      file_list.append(name_file)
data_list = []
yn=str(input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩] {xanhnhat}𝗕𝗮̣𝗻 𝗠𝘂𝗼̂́𝗻 𝗧𝗿𝗲𝗼 𝗠𝗮̃𝗶 𝗠𝗮̃𝗶 𝗞𝗵?> {trang}({vang}y{trang}/{vang}n{trang}) :{vang} "))
params = {
    "icm": '1',
}
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"237",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
}  
if yn.lower() == 'y':
      delay=int(input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩ {trang}Nhập delay(khuyến cáo trên 10s) :{vang} "))
      while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for selected_file in file_list:
              with open(selected_file, "rb") as file:
                  nds = file.read()
                  #data_list.append(ndss.decode('utf-8'))
            #for ndss in data_list:
              data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nds.decode('utf-8')}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"
              response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
              print(f"{xanhnhat}𝗜𝗗 𝗕𝗼𝘅\033[1;97m: {idcanspam} {do}| 𝙀𝙧𝙧𝙤𝙧 𝘿𝙚𝙥𝙏𝙧𝙖𝙞 | {trang}Đã 𝗦𝗽𝗮𝗺 𝗗𝗲̂́𝗻 𝗕𝗼𝘅 𝗧𝗵𝗮̀𝗻𝗵 𝗖𝗼̂𝗻𝗴")
              idelay(delay)
        except Exception as e:
          print(f"{do}Bị Ngắt Kết Nối Kìa Thằng Lồn Kết Nối Lại Mạng Đi Để Tao Còn Spam")
          time.sleep(10)

elif yn.lower() == 'n':
      soluong = int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập số tin nhắn muốn gửi :{vang} '))
      delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay(khuyến cáo 5-8) :{vang} '))
      for i in range(soluong):
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for name_file in file_list:
              with open(name_file , "rb") as file:
                nds = file.read()
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nds.decode('utf-8')}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"
              response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
              i = i + 1
              print(f"{xanhnhat}𝗜𝗗 𝗕𝗼𝘅\033[1;97m: {idcanspam} {do}| 𝙀𝙧𝙧𝙤𝙧 𝘿𝙚𝙥𝙏𝙧𝙖𝙞 | {trang}Đã 𝗦𝗽𝗮𝗺 𝗗𝗲̂́𝗻 𝗕𝗼𝘅 𝗧𝗵𝗮̀𝗻𝗵 𝗖𝗼̂𝗻𝗴")
              idelay(delay) 
        except Exception as e:
          print(f"{do}Bị Mất Mạng Rồi Kìa Thằng Cặc Kết Nối Lại Mạng Đi")
          time.sleep(10)
else:
    print(f"{do}Điền đúng")  
