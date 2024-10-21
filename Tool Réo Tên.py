from urllib.parse import quote
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

# fix
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
             𝙋𝙝𝙤̛̉ 𝘽𝙤̀: 𝘿𝙞𝙣𝙝 𝙃𝙤𝙖𝙣𝙜
            𝙏𝙞𝙠𝙏𝙤𝙠: @𝙖𝙘𝙘.𝙘𝙡𝙤𝙣𝙚_𝟱
        
               {xanhnhat} 𝗞𝗵𝗼̂𝗻𝗴 𝗣𝗵𝗮̉𝗶 𝗗𝗼 𝗕𝗮̣𝗻 𝗗𝗼̂́𝘁
               {trang}𝗠𝗮̀ 𝗟𝗮̀ 𝗗𝗼 𝗧𝗼̂𝗶 𝗤𝘂𝗮́ 𝗧𝗵𝗼̂𝗻𝗴 𝗠𝗶𝗻𝗵
   {trang}     ____________________________________
"""
clear()
runbanner(chontool)
idcanspam=input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩{trang}𝗜𝗗 𝗕𝗼𝘅 𝗖𝗮̂̀𝗻 𝗥𝗲́𝗼 𝗧𝗲̂𝗻: {vang} ")
while True:
      ck=input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩{trang} 𝗡𝗵𝗮̣̂𝗽 𝗖𝗼𝗼𝗸𝗶𝗲𝘀 𝗔𝗰𝗰{do}(lấy trong mbasic): {vang} ")
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Địt Con Mẹ Mày Có Cái Cookies Acc Cũng Nhập Sai Bố Chịu.')   
params = {
      "icm": '1',
    }
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"247",
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
runbanner(chontool)
chon_name = str(input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩{trang} 𝗡𝗵𝗮̣̂𝗽 𝗧𝗲̂𝗻 𝗖𝗮̂̀𝗻 𝗥𝗲́𝗼 {trang}: "))
if chon_name.lower() == "{chon_name}":
      lag = "{chon_name}"
elif chon_name.lower() == "ndjjdkd":
      lag = " "
else:
      CAU_CHUI = [
f"Địt Con Mẹ Mày Dậy Sủa Đi {chon_name}",
f"Địt Con Mẹ {chon_name} Sủa Mạnh Lên Em😹",
f"Địt Con Mẹ {chon_name} Rén Anh À",
f"Anh Cho Phép Mày Sủa Đấy Con Chó Ngu Đần {chon_name} À",
f"Ồ Giờ Anh Mới Biết Hoàn Cảnh Của Mày Đấy {chon_name}",
f"Tội Nghiệp {chon_name} Quá Chỉ Vì Mẹ Mày Thích Địt Chó",
f"Nên Mới Tạo Ra Mày Đấy {chon_name} À Mày Đúng Là 1 Con Chó Đáng Thương🤣",
f"Ơ Con Chó Ngu {chon_name} Bắt Đầu Khóc Rồi À🤣",
f"Ngoan Anh Cho Phép Mày Sủa Nè🤣 {chon_name}",
f"Ngoan Đi Anh Còn Cho Phép Mày Sủa {chon_name}",
f"Ui Ui Con Chó Ngu {chon_name} Bắt Đầu Cay Anh Rồi Kìa🤣",
f"Ô Con Chó {chon_name} Khóc Rồi À",
f"Con Chó {chon_name} Sủa Mạnh Lên Em",
f"Con Chó {chon_name} Cố Mà Sủa Mạnh Lên Em🤪",
f"Cố Mà Win Anh Sàn Mày Đi Con Chó Óc Lồn {chon_name}",
f"À Anh Quên Mày Lấy Đâu Ra Ngôn Mà Đấu Lại Anh🤣",
f"Thôi Thôi Đừng Cố Ẳng Nữa Chứng Tỏ Được Gì Đâu Con Chó Ngu {chon_name}",
f"Cho Dù Mày Có Ẳng Đến Sáng Mai Thì Anh Mày Vẫn Win Thôi Thằng Lồn🤣{chon_name}",
f"Con Chó Rách {chon_name} Cạn Ngôn Rồi Thì Add Mấy Con Chó Khác Vào Sủa Cùng Đi🤣",
f"Chỉ Cần 1 Mình Anh Mày Vẫn Thừa Sức Win Mấy Con Chó Rách Chúng Mày {chon_name} À😂",
f"Ơ KÌA DẬY SỦA ĐI EM {chon_name}",
f"Sợ Rồi À Con Chó Ngu {chon_name}",
f"Huhu,con chó ngu {chon_name} sợ anh rồi chứ gì😂",
f"Dòng Họ Ngoại Mày Con Lồn Nào Cũng Là 1 Con Đĩ Thích Bú Cặc Chó Nhỉ {chon_name}",
f"Tao Nể Gia Phả Nhà Ngoại Mày Thật Đấy {chon_name}",
f"Từ CON CHÓ CỤ M CŨNG ĐỊT CHÓ ĐẺ RA ÔNG MÀY NHỈ {chon_name} CẢ GIA PHẢ ĐỊT CHÓ ĐẺ RA NGƯỜI🤣",
f"Tội Mày Quá {chon_name} Đúng Là 1 Thg Sản Phẩm Lỗi",
f"MÀY HỌC LÀM CON CẶC GÌ NỮA VỀ NỐI NGHIỆP GIA ĐÌNH KÌA {chon_name} ",
f"DẬY SỦA ĐI THẰNG SẢN PHẨM LỖI",
f"Địt Mẹ Chưa Gì Cạn Sạch Ngôn Rồi Thế Em🤣",
]
      clear()
      runbanner(chontool)
      delay=int(input(f"{xanhnhat}[𝙀𝙧𝙧𝙤𝙧] ➩{trang}{xanhnhat}𝗡𝗵𝗮̣̂𝗽 𝗗𝗲𝗹𝗮𝘆(Khuyến Cáo Trên 2) :{vang} "))
      while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for nd in CAU_CHUI:
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
                response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
                chonname = chon_name
                NOIDUNG = f"{xanhnhat}𝙀𝙧𝙧𝙤𝙧 Đã Nói{trang} {nd}"
                print(f"{NOIDUNG}")
                idelay(delay)
        except Exception as e:
          print(f"{do}Lỗi bị ngắt kết lối vui lòng kết lối lại mạng để tiếp tục nhây")
          time.sleep(5)
