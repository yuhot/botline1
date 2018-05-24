# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE() 
cl.login(token="Et4dAcXqNZY1MdJpQjId.EK+RXmzq+hz56T9crCkLRq.owlMIqHyRcWNCw6nHrla0S9F9gByJvz/bfbuvZUerDI=")
cl.loginResult()
print "cl login success"

# ki = LINETCR.LINE() 
# ki.login(token="EpZmUMp6CzpG2MxrdrE9.Z2jqcI8fppmz+7xOGNlyEq.ttlVXdxR2I6A72rLY3B7apC+hyyUyuBQnYkKCO5J9RQ=")
# print "ki login success"

# ki2 = LINETCR.LINE() 
# ki2.login(token="Ep5x39yHINyEEVb7eaYa.Ql+Iq95c4olkmxSaoadLoG.guCtCeFRGAxadoTr/JxRhLsDyLTeTNTj285/W6Moadw=")
# print "ki2 login success"

# ki3 = LINETCR.LINE() 
# ki3.login(token="Epezl3XFYfIArh9F82x6.SGby4XQI1gAOTET1lBqQ9G.Kha8WacxePkq1eck0Kaxb83kSJ4odJGyVV9aMSvEspI=")
# print "ki3 login success"

# ki4 = LINETCR.LINE() 
# ki4.login(token="EpUfPCc0QdIkGkErgJca.Q6+YE7DHLRb+4/UXmbKggG.LJL7TYkXyf5UpTvXGKBFSmyYPQJAz9cgbzl5bsKJBJI=")
# print "ki4 login success"

# ki5 = LINETCR.LINE() 
# ki5.login(token="Epyyzy4CVbNqz8DSept8.7fLTCfOW6V77bikOdoT16a.QFITEuKTLXnmPlJ6XX43+Oe3oF3jKsLCE4JFL/mwOcA=")
# print "ki5 login success"

#ki6 = LINETCR.LINE() 
#ki6.login(token="EpPC6mLG2zwhDQo5Vx0d.2zlXNOJh2/W1Z19qm0HVpq.1KpNIxthj+z/VqsRGk5q7Yg99BKSdL8ZrC7t2SSmPHE=")
#print "ki6 login success"

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""    •─ ͜͡✫-[✭] ༺ πနးຫຮี่のีধ์͜͡ ༻[✭]- ͜͡✫─•
👻 คำสั่ง ➠ ดูคำสั่ง
👻 คำสั่ง2 ➠ ดูคำสั่ง2
👻 ทักเข้า ➠ เช็คข้อความทักเข้า
👻 ทักออก ➠ เช็คข้อความทักออก
👻 ทักลบ ➠ เช็คข้อความทักคนลบ
👻 ทักเข้า: +ข้อความ ➠ ตั้งทักเข้า
👻 ทักออก: +ข้อความ ➠ ตั้งทักคนออก
👻 ทักลบ: +ข้อความ ➠ ตั้งทักคนลบ
👻 แท็ก1 ➠ เช็คข้อความแท็ก
👻 แท็ก2 ➠ เช็คข้อความแท็ก
👻 แท็ก1: +ข้อความ ➠ ตั้งแท็ก
👻 แท็ก2: +ข้อความ ➠ ตั้งแท็ก
👻 Message set:: +ข้อความ ➠ ตั้งข้อความ
👻 Help set:: +ข้อความ ➠ ตั้งข้อความ
👻 Pesan add- ➠ เพิ่มข้อความ
👻 เช็คข้อความแอด ➠ เช็คตั้งข้อความแอด
👻 Change ➠ ยกเลิกการตั้งข้อความ
👻 Message set ➠ ข้อความ
👻 Come Set: ➠ ตั้งคอมเม้น
👻 Com ➠ เช็คคอมเม้น
👻 me ➠ คทเรา
👻 ผู้สร้าง ➠ ผู้สร้างบอท
👻 midเรา ➠ เช็คเราเรา
👻 1-6mid ➠ เช็คmidคลิ้ก
👻 คลิ้กmid ➠ เช็คmidคลิ้ก
👻 ชื่อ: +ข้อความ ➠ เปลี่ยนชื่อคลิ้ก
👻 เช็คออน์ ➠ เช็คเวลาทำงานบอท
👻 ตัส: +ข้อความ ➠ ตั้งตัสคลิ้ก
👻 ชื่อเรา: +ข้อความ ➠ เปลี่ยนชื่อเรา
👻 1-6ชื่อ: +ข้อความ ➠ เปลี่ยนชื่อคลิ้ก
👻 ตัสเรา: +ข้อความ ➠ เปลี่ยนตัสเรา
👻 บอท ➠ คทคลิ้ก
👻5-6ตัส: +ข้อความ  ➠ เปลี่ยนตัสคลิ้กตัว5-6
👻 1-6 ➠ เช็คคลิ้ก
👻 Mid: +mid ➠ g=H88mmid
👻 kick +mid ➠ ลบโดยmid
👻 เช็ค: +mid ➠ เชิญโดยmid
👻 Me ➠  เช็คเซล
👻 กำ ➠ เช็คเซล
👻 5555 ➠ เช็คเซล
👻 Sp ➠ เช็คสปีด
👻 respon ➠ เช็คเซล
👻 Bot? ➠ เช็คเซล
👻 บอทเข้า ➠ สั่งคลิ้กเข้า
👻 เข้า3-6 ➠ คลิ้ก3-6เข้า
👻 1-6เข้า ➠ คลิ้กเข้า
👻 ออก ➠ คลิ้กออก
👻 1-6ออก ➠ สั่งคลิ้กออก
👻 #leave ➠ ออกแชทรวม
👻 คนอ่าน ➠ ดูคนอ่าน
👻 Name me ➠ ชื่อ
👻 Copy @ ➠ คัดลอก
👻 backup ➠ คืนร่าง
👻 Tx: +ข้อความ ➠ 
👻 Fancytext:: +ข้อความ ➠ 
👻 Spam on +เลข+ข้อความ ➠ รันข้อความ
👻 มอง ➠ รายชื่ออ่าน
👻 tag all ➠ แท็ก
👻 เช็คอ่าน ➠ เช็คระบบอ่าน
👻 Gbroadcast +ข้อความ ➠ 
👻 Cbroadcast +ข้อความ ➠ 
👻 Nuke ➠ บิน
👻 Bye @ ➠ ลบ
👻 Nk @ ➠ เตะ
👻 blocklist ➠ เช็ครายการบล็อค
👻 kill ➠ ลบบชดำ
👻 ข้อมูลบัญชีดำ ➠ เช็คข้อมูลบัญชีดำ
👻 ล้างดำ ➠ ล้างบชดำ
👻 banlist ➠  เช็ครายการดำ
👻 เช็คดำ ➠ เช็ครายการดำ
👻 ขาวคท ➠ ทำขาวโดยคท
👻 ดำคท ➠ ทำดำโดยคท
👻 ขาว: ➠ ทำขาว
👻 ดำ1: ➠ ทำดำ
👻 ขาว @ ➠ ทำขาว
👻 ดำ @ ➠ ทำดำ
👻 Group cancelall ➠ ยกเลิกห้องรัน
👻 รายละเอียดกลุ่ม ➠ เช็ครายละเอียดกลุ่ม
👻 เช็คidกลุ่ม ➠ เช็คGIDกลุ่ม
👻 เช็คกลุ่ม ➠ เช็ครายการกลุ่ม
👻 Cancel ➠ ยกเลิกค้างเชิญ
👻 ยกเลิกเชิญ ➠ ยกเลิกค้างเชิญ
👻 ลบแชทบอท ➠ ลบแชทคลิ้ก
👻 l-7ลบรัน ➠ ลบรันคลิ้ก
👻 url ➠ ขอลิ้งค์ห้อง
👻 update ➠ ปรับเวลา
👻 ตั้งเวลา: +เลข ➠ ตั้งเวลา
👻 ชื่อวลาปิด ➠ ปิดชื่อมีเวลา
👻 ชื่อเวลาเปิด ➠ เปิดชื่อมีเวลา
👻 1ลิ้งค์กลุ่ม ➠ ขอลิ้งค์ห้อง
👻 2ลิ้งค์กลุ่ม ➠  ขอลิ้งค์ห้อง
👻 ลิ้งค์+ ➠ ขอลิ้งค์ห้อง
👻 Gn +ข้อความ ➠ เปลี่ยนชื่อห้อง
👻 ชื่อกลุ่ม: +ข้อความ ➠ เปลี่ยนชื่อห้อง
👻 ของขวัญ ➠ ให้ของขวัญ
👻 1-4ของขวัญ ➠ ให้ของขวัญ
👻 Mimic target ➠ เลียนแบบ
👻 เช็คพูดตาม ➠ เช็ครายชื่อคนพูดตาม
👻 ลบพูดตาม @ ➠ ลบที่เพิ่มพูดตาม
👻 พูดตาม @ ➠ เพิ่มคนพูดตาม
👻 lurkers ➠ อ่านแบบแทก
👻 lurk off ➠ ปิดอ่าน
👻 lurk on ➠ เปิดอ่าน
👻 อ่าน ➠ เแดดูชื่อคนอ่าน
👻 Set2 ➠ เช็คตั้งค่า
👻 Set1 ➠ เช็คตั้งค่า
👻 ปิดหมด ➠ ปิดระบบกัหมด
👻 เปิดหมด ➠ เปิดระบบหมด
👻 ปิดลิ้งค์ ➠ ปิดลิ้งค์กลุ่ม
👻 เปิดลิ้งค์ ➠ เปิดลิ้งค์กลุ่ม
👻 กันยกเลิก1ปิด ➠ ปิดการยันเลิก
👻 กันยกเลิก1เปิด ➠ เปิดกันยกเลิก
👻 ปิดเเจ้งเตือนบอท ➠ ปิดเเจ้งเตือนบอท
👻 เปิดเเจ้งเตือนบอท ➠ เปิดเเจ้งเตือนบอท
👻 ปิดแจ้งเตือน ➠ ปิดระบบแจ้งเตือน
👻 เปิดแจ้งเตือน ➠ เปิดระบบแจ้งเตือน
👻 คอมเม้นปิด ➠ ปิดระบบคอมเม้น
👻 คอมเม้นเปิด ➠ เปิดระบบคอมเม้น
👻 แอดปิด ➠ ออโต้แอดปิด
👻 แอดเปิด ➠ ออโต้แอดเปิด
👻 แชร์ปิด ➠ เช็คลิ้งค์โพสปิด
👻 แชร์เปิด ➠ เช็คลิ้งค์โพสเปิด
👻 Group cancel: off ➠ ปิดระบบกินห้องรัน
👻 Group cancel: on ➠ เปิดระบบกินห้องรัน
👻 ออกแชทรวมปิด ➠ ปิดออกจากแชทรวม
👻 ออกแชทรวมเปิด ➠ เปิดออกจากแชทรวม
👻 เข้าออโต้ปิด ➠ ปิดการเข้าออโต้
👻 เข้าออโต้เปิด ➠ เปิดการเข้าออโต้
👻 กันยกเลิกปิด ➠ ปิดระบบกันยกเลิก
👻 กันยกเลิกเปิด ➠ เปิดระบบกันยกเลิก
👻 กันเชิญปิด ➠ ปิดระบบกันเชิญ
👻 กันเชิญเปิด ➠ เปิดระบบกันเชิญ
👻 กันลิ้งค์ปิด ➠ ปิดระบบกันลิ้งค์
👻 กันลิ้งค์เปิด ➠ เปิดระบบกันลิ้งค์
👻 ป้องกันปิด ➠ ปิดระบบกันลบ
👻 ป้องกันเปิด ➠ เปิดระบบกันลบ
👻 เช็คคทปิด ➠ ปิดอ่านคท
👻 เช็คคทเปิด ➠ เปิดอ่านคท
👻 ทักลบเปิด ➠ เปิดรับละลบ
👻 ทักลบปิด ➠ ปิดทักละลบ
👻 ทักออกปิด ➠ ปิดระบบทักคนออก
👻 ทักออกเปิด ➠ เปิดระบบทัดคนออก
👻 ต้อนรับปิด ➠ ปิดระบบทักเข้า
👻 ต้อนรับเปิด ➠ เปิดระบบทักเข้า
👻 เตะแท็กเปิด ➠ เปิดระบบเตะคนแท็ก
👻 เตะแท็กปิด ➠ ปิดระบบเตะคนแท็ก
👻 แท็กปิด ➠ ปิดระบบแท็ก
👻 แท็กเปิด ➠ เปิดระบบแท็ก
👻 อ่านปิด ➠ ปิดระบบอ่าน
👻 อ่านเปิด ➠ เปิดระบบอ่าน
👻 ปิดอ่าน ➠ ปิดระบบอ่าน
👻 เปิดอ่าน ➠ เปิดระบบอ่าน
👻 TL:  ➠ โพส

    •─ ͜͡✫-[✭] ༺ πနးຫຮี่のีধ์͜͡ ༻[✭]- ͜͡✫─•
"""
helpMessage2 ="""👻 .11 ➠ 
👻 T say  ➠ 
👻 Me ban ➠ 
👻 Banlistall ➠ 
👻 Mban: ➠ 
👻 Com Bl cek ➠ 
👻 Com hapus Bl ➠ 
👻 Com Bl ➠ 
👻 Sayang say  ➠ 
👻 Welcome ➠ 
👻 Say  ➠ 
👻 ping ➠ 
👻 cancel ➠ 
👻 Beb @ ➠ 
👻 Cek @ ➠ 
👻 Telan @ ➠ 
👻 Bunuh @ ➠ 
👻 ☜ʕ•ﻌ•ʔ  ➠ 
👻 [Auto]  ➠ 
👻 พูด ➠ 
👻 siri-en  ➠ 
👻 siri: ➠ 
👻 siri  ➠ 
👻 Ry20 ➠ 
     ─────┅═ই۝ई═┅─────
╔══════════════════
║       ✦โหมดเช็คตั้งค่าข้อความ✦
╠══════════════════
║✰ Hhx1 ➠เช็คข้อความต้อนรับ
║✰ Hhx2 ➠เช็คข้อความคนออก
║✰ Hhx3 ➠เช็คข้อความคนลบ
╠════════════════
║•─ ͜͡✫-[✭] ༺ πနးຫຮี่のีধ์͜͡ ༻[✭]- ͜͡✫─•
╚════════════════
"""
helo=""

KAC=[cl]
mid = cl.getProfile().mid
# kimid = ki.getProfile().mid
# ki2mid = ki2.getProfile().mid
# ki3mid = ki3.getProfile().mid
# ki4mid = ki4.getProfile().mid
# ki5mid = ki5.getProfile().mid
#ki6mid = ki6.getProfile().mid

mid = cl.getProfile().mid
Bots = ["u7a4febc4c650fc7679eadf4245c2a5ad"]
self = ["u7a4febc4c650fc7679eadf4245c2a5ad"]
admin = ["u7a4febc4c650fc7679eadf4245c2a5ad"]
owner = ["u7a4febc4c650fc7679eadf4245c2a5ad"]
Creator = ["u7a4febc4c650fc7679eadf4245c2a5ad"]

wait = {
    "alwayRead":False,
    "detectMention":True,    
    "kickMention":False,
    "steal":False,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False, "members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"•─ ͜͡✫-[✭] ༺ πနးຫຮี่のีধ์͜͡ ༻[✭]- ͜͡✫─•",
    "lang":"JP",
    "comment":"AutoLike by •─ ͜͡✫-[✭] ༺ πနးຫຮี่のีধ์͜͡ ༻[✭]- ͜͡✫─•",
    "commentOn":False,
    "acommentOn":False,
    "bcommentOn":False,
    "ccommentOn":False,
    "Protectcancl":False,
    "pautoJoin":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "ainvite":False,
    "binvite":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Hhx1":False,
    "Hhx2":False,
    "Hhx3":False,
    "Notifed":False,
    "Notifedbot":False,
    "atjointicket":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "tag1":"แท็กทำไมหรือ",
    "tag2":"จะแท็กทำไม",
    "posts":False,
    }

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendImageWithUrl(self, to_, url):
    path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception('Download image failure.')
    try:
        self.sendImage(to_, path)
    except Exception as e:
         raise e

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def sendImageWithUrl(self, to_, url):
    path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception('Download image failure.')
    try:
         self.sendImage(to_, path)
    except Exception as e:
         raise e
def yt(query):
    with requests.session() as s:
        isi = []
        if query == "":
            query = "S1B tanysyz"   
            s.headers['user-agent'] = 'Mozilla/5.0'
            url    = 'http://www.youtube.com/results'
            params = {'search_query': query}
            r    = s.get(url, params=params)
            soup = BeautifulSoup(r.content, 'html5lib')
        for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
        return isi

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
        aa = (aa[:int(len(aa)-1)])
        msg = Message()
        msg.to = to
        msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print error

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)

def sendImage(self, to_, path):
    M = Message(to=to_, text=None, contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M2 = self._client.sendMessage(0,M)
    M_id = M2.id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
        raise Exception('Upload image failure.')
    return True

def sendImage2(self, to_, path):
    M = Message(to=to_,contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M_id = self._client.sendMessage(M).id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = cl.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
        raise Exception('Upload image failure.')
    return True

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if op.param2 in Boss + admin:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                        cl.acceptGroupInvitation(op.param1)
                G = cl.getGroup(op.param1)
                ginfo = cl.getGroup(op.param1)
            G.preventJoinByTicket = False
            invsend = 0
            Ticket = cl.reissueGroupTicket(op.param1)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
            G.preventJoinByTicket = False
            cl.sendText(op.param1,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")

        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)

        if op.type == 15:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "ไปแร้วสะละ\n􀜁􀄄􏿿 เเล้วพบกันใหม่นะ 􀜁􀄄􏿿")
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + " ☜ʕ•ﻌ•ʔ ")
                cl.sendText(op.param1, "􀜁􀄁􏿿 ยินดีต้อนรับครับ 􀜁􀄁􏿿\n􀄃􀅸􏿿 สวัสดีครับผม 􀄃􀅸􏿿\n􂜁􀆄􏿿 อย่าลืมปิดเสียงการเเจ้งเตือนด้วยนะ 􂜁􀆄􏿿\n\n[By. ༺ πနးຫຮี่のีধ์͜͡ ༻]")
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄄􏿿 Bye~bye 􀜁􀄄􏿿")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄄􏿿 Bye~bye 􀜁􀄄􏿿")
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n•─ ͜͡✫-[✭] ༺ πနးຫຮี่のีধ์͜͡ ༻[✭]- ͜͡✫─•")
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["bcommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["bcomment"]))
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["acommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["acomment"]))
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["ccommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["ccomment"]))
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
                    group.name = wait["pro_name"][op.param1]
                    cl.updateGroup(group)
                    cl.sendText(op.param1, "Groupname protect now")
                    wait["blacklist"][op.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass

        if op.type == 13:
            if wait["Protectcancl"] == True:
                if op.param2 not in Bots:
                    group = cl.getGroup(op.param1)
                    gMembMids = [contact.mid for contact in group.invitee]
                    random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)

        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    cl.sendText(op.param1,"")
            else:
                cl.sendText(op.param1,"")

        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    cl.sendText(op.param1,"URL/QRが更新されました.☆（´・ω・｀）\n時間 [⏰] ")

        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                else:
                    cl.sendText(op.param1,"❇BY ༺ πနးຫຮี่のีধ์͜͡ ༻️ [⏰] ") 
                if op.param2 not in Bots:
                    if op.param2 in Bots:
                        pass
                elif wait["cancelprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                else:
                    cl.sendText(op.param1,"❇️ มีการเชิญสมาชิกเข้าร่วมกลุ่ม ❇️ [⏰] ")

        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    cl.sendText(op.param1,"")
            else:
                cl.sendText(op.param1,"")

        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    cl.sendText(op.param1,"")
            else:
                cl.sendText(op.param1,"")
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
                else:
                    cl.sendText(op.param1,"")
            else:
                cl.sendText(op.param1,"")
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["cancelprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
                else:
                    cl.sendText(op.param1,"")
            else:
                cl.sendText(op.param1,"")

        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                if wait["protect"] == True:
                    if wait["blacklist"][op.param2] == True:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventJoinByTicket = True
                            ks.updateGroup(G)
                        except:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                G = random.choice(KAC).getGroup(op.param1)
                                G.preventJoinByTicket = True
                                random.choice(KAC).updateGroup(G)
                            except:
                                pass
                elif op.param2 not in admin + Bots:
                    random.choice(KAC).sendText(op.param1,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    pass
#  Op program in Admin and User Comment By Googlez  #
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"ᴄᴏᴍᴘʟᴇᴛᴇ ᴀʟʀᴇᴀᴅʏ")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"ɴᴏᴛ ᴛᴏ ᴄᴏᴍᴍᴇɴᴛ")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"ᴅᴇʟᴇᴛᴇ ʙʟᴀᴄᴋʟɪsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"ᴅᴇʟᴇᴛᴇ ʙʟᴀᴄᴋʟɪsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"ᴄᴏᴍᴘʟᴇᴛᴇ ᴀʟʀᴇᴀᴅʏ")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"ᴄᴏᴍᴘʟᴇᴛᴇ ᴀʟʀᴇᴀᴅʏ")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"ᴅᴇʟᴇᴛᴇ ʙʟᴀᴄᴋʟɪsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"ɴᴏ ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")

            if 'MENTION' in msg.contentMetadata.keys() != None:
                if wait["kickMention"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["จุกไมละมึง By.  ༺ πနးຫຮี่のีধ์͜͡ ༻" + cName]
                    ret_ = random.choice(balas)                     
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in admin:
                            cl.sendText(msg.to,ret_)
                            random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                            break                                  
                        if mention['M'] in Bots:
                            cl.sendText(msg.to,ret_)
                            random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                            break 

            if 'MENTION' in msg.contentMetadata.keys() != None:
                if wait["detectMention"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\n" + str(wait["tag1"]) , cName + "\n" + str(wait["tag2"])]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in Bots:
                            cl.sendText(msg.to,ret_)
                            break

            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    

            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u7a4febc4c650fc7679eadf4245c2a5ad":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)

            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)

            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
#   Op program in bot  Comment By Googlez  #
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"ᴄᴏᴍᴘʟᴇᴛᴇ ᴀʟʀᴇᴀᴅʏ")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"ɴᴏᴛ ᴛᴏ ᴄᴏᴍᴍᴇɴᴛ")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"ᴅᴇʟᴇᴛᴇ ʙʟᴀᴄᴋʟɪsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"ᴅᴇʟᴇᴛᴇ ʙʟᴀᴄᴋʟɪsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"ᴄᴏᴍᴘʟᴇᴛᴇ ᴀʟʀᴇᴀᴅʏ")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"ᴄᴏᴍᴘʟᴇᴛᴇ ᴀʟʀᴇᴀᴅʏ")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"ᴅᴇʟᴇᴛᴇ ʙʟᴀᴄᴋʟɪsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"ɴᴏ ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")

                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])

            elif msg.text in ["Help","คำสั่ง"]:
                    cl.sendText(msg.to, helpMessage + "")

            elif msg.text in ["Help2"]:
                    cl.sendText(msg.to, helpMessage2 + "")
#======================================================#
            elif msg.text in ["อ่านเปิด","Read:on"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"Auto Sider ON")

            elif msg.text in ["อ่านปิด","Read:off"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"Auto Sider OFF")
#======================================================#
            elif msg.text in ["แท็กเปิด","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"Auto Respon ON")

            elif msg.text in ["แท็กปิด","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Auto Respon OFF")
#======================================================#
            elif msg.text in ["เตะแท็กเปิด","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"Auto Kick ON")

            elif msg.text in ["เตะแท็กปิด","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"Auto Kick OFF")
#======================================================#
            elif msg.text in ["ทักเข้า","Hhx1"]:
                cl.sendText(msg.to,"[เช็คข้อความต้อนรับของคุณ]\n\n" + str(wait["acomment"]))

            elif msg.text in ["ทักออก","Hhx2"]:
                cl.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนออกจากกลุ่ม]\n\n" + str(wait["bcomment"]))

            elif msg.text in ["ทักลบ","Hhx3"]:
                cl.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนลบสมาชิก]\n\n" + str(wait["ccomment"]))
#======================================================#
            elif "ทักเข้า: " in msg.text:
                c = msg.text.replace("ทักเข้า: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["acomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)

            elif "ทักออก: " in msg.text:
                c = msg.text.replace("ทักออก: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["bcomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความกล่าวถึงคนออกจากกลุ่ม👌\n\n" + c)

            elif "ทักลบ: " in msg.text:
                c = msg.text.replace("ทักลบ: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["ccomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความกล่าวถึงคนลบสมาชิก👌\n\n" + c)
#======================================================#
            elif msg.text in ["ต้อนรับเปิด"]:
                if wait["acommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["acommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already on")

            elif msg.text in ["ต้อนรับปิด"]:
                if wait["acommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["acommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already off")
#======================================================#
            elif msg.text in ["ทักออกเปิด"]:
                if wait["bcommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["bcommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already on")

            elif msg.text in ["ทักออกปิด"]:
                if wait["bcommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["bcommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already off")
#======================================================#
            elif msg.text in ["ทักลบเปิด"]:
                if wait["ccommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["ccommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already on")

            elif msg.text in ["ทักลบปิด"]:
                if wait["ccommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["ccommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already off")
#======================================================#
            elif msg.text.lower() == 'เช็คคทเปิด':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบเช็ค คท \n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to," ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to," ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"เปิดระบบคอมเช็ค คท\n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif msg.text.lower() == 'เช็คคทปิด':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดระบบเช็ค คท")
                    else:
                        cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดระบบเช็คคทอยู่ \n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to," ༺ πနးຫຮี่のีধ์͜͡ ༻")
#======================================================#
            elif msg.text in ['ป้องกันเปิด']:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบกัน By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"เปิดระบบกัน\n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบกัน\n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"เปิดระบบป้องกันอยุ่")

            elif msg.text in ["ป้องกันปิด"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดระบบป้องกัน \nBy. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"ปิดระบบป้องกัน \n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to," ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to," ༺ πနးຫຮี่のีধ์͜͡ ༻")
#======================================================#
            elif msg.text in ['กันลิ้งค์เปิด']:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protect Enable􀜁��􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")

            elif msg.text in ["กันลิ้งค์ปิด","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Link Protection Disable ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
#======================================================#
            elif msg.text in ['กันเชิญเปิด']:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")

            elif msg.text in ["กันเชิญปิด"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite Protection Disable ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
#======================================================#
            elif msg.text in ['กันยกเลิกเปิด']:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")

            elif msg.text in ["กันยกเลิกปิด"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Disable ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
#======================================================#
            elif msg.text.lower() == 'เข้าออโต้เปิด':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")

            elif msg.text.lower() == 'เข้าออโต้ปิด':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
#======================================================#
            elif msg.text in ["ออกแชทรวมเปิด","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")

            elif msg.text in ["ออกแชทรวมปิด","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
#======================================================#
            elif msg.text in ["แชร์เปิด","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")

            elif msg.text in ["แชร์ปิด","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
#======================================================#
            elif msg.text in ["แอดเปิด","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")

            elif msg.text in ["แอดปิด","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
#======================================================#
            elif msg.text in ["คอมเม้นเปิด","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบคอมเม้น \n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบคอมเม้น\nBy. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to," ༺ πနးຫຮี่のีধ์͜͡ ༻")
            elif msg.text in ["คอมเม้นปิด"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดระบบคอมเม้น \n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
#======================================================#
            elif msg.text in ["Notifed on","เปิดแจ้งเตือน","M on"]:
              if msg.from_ in admin:
                if wait["Notifed"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดเเจ้งเเตือนของคุณเเล้ว\n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"เปิดเเจ้งเเตือนของคุณเเล้ว")
                else:
                    wait["Notifed"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดเเจ้งเเตือนของคุณเเล้ว \n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"เปิดเเจ้งเเตือนของคุณเเล้ว")

            elif msg.text in ["Notifed off","ปิดแจ้งเตือน","M off"]:
              if msg.from_ in admin:
                if wait["Notifed"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดเเจ้งเเตือนของคุณเเล้ว \n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"ปิดเเจ้งเเตือนของคุณเเล้ว \n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["Notifed"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดเเจ้งเเตือนของคุณเเล้ว \n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"ปิดเเจ้งเเตือนของคุณเเล้ว \n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
#======================================================#
            elif msg.text in ["Notifedbot on","เปิดเเจ้งเตือนบอท","Mbot on"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดเเจ้งเเตือนบอทเเล้ว\n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"เปิดเเจ้งเเตือนบอทเเล้ว\n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["Notifedbot"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดเเจ้งเเตือนบอทเเล้ว\n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"เปิดเเจ้งเเตือนบอทเเล้ว \n  ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif msg.text in ["Notifedbot off","ปิดแจ้งเตือนบอท","Mbot off"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดเเจ้งเเตือนบอทเเล้ว\n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"ปิดเเจ้งเเตือนบอทเเล้ว\n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["Notifedbot"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดเเจ้งเเตือนบอทเเล้ว\n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"ปิดเเจ้งเเตือนบอทเเล้ว\n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
#======================================================#
            elif msg.text in ["กันยกเลิก1เปิด","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")

            elif msg.text in ["กันยกเลิก1ปิด","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
#======================================================#
            elif msg.text in ["เปิดลิ้งค์"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")

            elif msg.text in ["ปิดลิ้งค์"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close ô€¨👈")
                    else:
                        cl.sendText(msg.to,"URL close ��€¨👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
#======================================================#
            elif msg.text in ["เปิดหมด"]:
                    cl.sendText(msg.to,"อ่านเปิด")
                    cl.sendText(msg.to,"แท็กเปิด")
                    cl.sendText(msg.to,"เตะแท็กเปิด")
                    cl.sendText(msg.to,"ต้อนรับเปิด")
                    cl.sendText(msg.to,"ทักออกเปิด")
                    cl.sendText(msg.to,"ทักลบเปิด")
                    cl.sendText(msg.to,"เช็คคทเปิด")
                    cl.sendText(msg.to,"ป้องกันเปิด")
                    cl.sendText(msg.to,"กันลิ้งค์เปิด")
                    cl.sendText(msg.to,"กันเชิญเปิด")
                    cl.sendText(msg.to,"กันยกเลิกเปิด")
                    cl.sendText(msg.to,"เข้าออโต้เปิด")
                    cl.sendText(msg.to,"ออกแชทรวมเปิด")
                    cl.sendText(msg.to,"แอดเปิด")
                    cl.sendText(msg.to,"คอมเม้นเปิด")
                    cl.sendText(msg.to,"เปิดแจ้งเตือน")
                    cl.sendText(msg.to,"เปิดแจ้งเตือนบอท")
                    cl.sendText(msg.to,"กันยกเลิก1เปิด")
                    cl.sendText(msg.to,"แชร์เปิด")
                    cl.sendText(msg.to,"༺ πနးຫຮี่のีধ์͜͡ ༻")
#======================================================#
            elif msg.text in ["ปิดหมด"]:
                    cl.sendText(msg.to,"อ่านปิด")
                    cl.sendText(msg.to,"แท็กปิด")
                    cl.sendText(msg.to,"เตะแท็กปิด")
                    cl.sendText(msg.to,"ต้อนรับปิด")
                    cl.sendText(msg.to,"ทักออกปิด")
                    cl.sendText(msg.to,"ทักลบปิด")
                    cl.sendText(msg.to,"เช็คคทปิด")
                    cl.sendText(msg.to,"ป้องกันปิด")
                    cl.sendText(msg.to,"กันลิ้งค์ปิด")
                    cl.sendText(msg.to,"กันเชิญปิด")
                    cl.sendText(msg.to,"กันยกเลิกปิด")
                    cl.sendText(msg.to,"เข้าออโต้ปิด")
                    cl.sendText(msg.to,"ออกแชทรวมปิด")
                    cl.sendText(msg.to,"แอดปิด")
                    cl.sendText(msg.to,"คอมเม้นปิด")
                    cl.sendText(msg.to,"ปิดแจ้งเตือน")
                    cl.sendText(msg.to,"ปิดแจ้งเตือนบอท")
                    cl.sendText(msg.to,"กันยกเลิก1ปิด")
                    cl.sendText(msg.to,"แชร์ปิด")
                    cl.sendText(msg.to,"༺ πနးຫຮี่のีধ์͜͡ ༻")
#======================================================#
            elif msg.text in ["Set1"]:
                md = "   ༺ πနးຫຮี่のีধ์͜͡ ༻\n"
                if wait["contact"] == True: md+="􀜁􀇔􏿿 Contact:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Contact:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀜁􀇔􏿿 Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􀜁􀇔􏿿 Auto Join:off􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀜁􀇔􏿿 Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "􀜁􀇔􏿿 Group cancel:off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀜁􀇔􏿿 Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Auto leave:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀜁􀇔􏿿 Share:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀜁􀇔􏿿 Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto add:off 􀜁��􏿿\n"
                if wait["commentOn"] == True: md+="􀜁􀇔􏿿 Auto komentar:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto komentar:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􀜁􀇔􏿿 Protect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Protect:off 🔒\n"
                if wait["linkprotect"] == True: md+="􀜁􀇔􏿿Link Protect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Link Protect:off🔒\n"
                if wait["inviteprotect"] == True: md+="􀜁􀇔􏿿Invitation Protect:on🔓\n"
                else:md+="􀜁􀇔􏿿 Invitation Protect:off🔒\n"
                if wait["cancelprotect"] == True: md+"􀜁􀇔􏿿 CancelProtect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Cancel Protect:off 🔒\n"
                cl.sendText(msg.to,"""
   ༺ πနးຫຮี่のีধ์͜͡ ༻
""" + md)
#======================================================#
            elif msg.text in ["Set2"]:
                md = " ༺ πနးຫຮี่のีধ์͜͡ ༻\n\n"
                if wait["likeOn"] == True: md+="􀬁􀆐􏿿 Auto like : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Auto like : off 􀜁􀄰􏿿\n"
                if wait["alwayRead"] == True: md+="􀬁􀆐􏿿 Read : on 􀜁􀄯􏿿\n"
                else:md+="􀬁��􏿿 Read : off 􀜁􀄰􏿿\n"
                if wait["detectMention"] == True: md+="􀬁􀆐􏿿 Autorespon : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Autorespon : off 􀜁􀄰􏿿\n"
                if wait["kickMention"] == True: md+="􀬁􀆐􏿿 Autokick: on 􀜁����􏿿\n"
                else:md+="􀬁􀆐􏿿 Autokick : off 􀜁􀄰􏿿\n"
                if wait["Notifed"] == True: md+="􀬁􀆐􏿿 Notifed : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Notifed : off 􀜁􀄰􏿿\n"
                if wait["Notifedbot"] == True: md+="􀬁􀆐􏿿 Notifedbot : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Notifedbot : off 􀜁􀄰􏿿\n"
                if wait["acommentOn"] == True: md+="􀬁􀆐􏿿 Hhx1 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx1 : off 􀜁􀄰􏿿\n"
                if wait["bcommentOn"] == True: md+="􀬁􀆐􏿿 Hhx2 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx2 : off 􀜁􀄰􏿿\n"
                if wait["ccommentOn"] == True: md+="􀬁􀆐􏿿 Hhx3 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx3 : off 􀜁􀄰􏿿\n"
                if wait["Protectcancl"] == True: md+="􀬁􀆐􏿿 Cancel : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Cancel : off 􀜁􀄰􏿿\n"
                if wait["winvite"] == True: md+="􀬁􀆐􏿿 Invite : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Invite : off 􀜁􀄰􏿿\n"
                if wait["pname"] == True: md+="􀬁􀆐􏿿 Namelock : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Namelock : off 􀜁􀄰􏿿\n"
                if wait["contact"] == True: md+="􀬁􀆐􏿿 Contact : on 􀜁􀄯􏿿\n"
                else: md+="􀬁􀆐􏿿 Contact : off 􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀬁􀆐􏿿 Auto join : on 􀜁􀄯􏿿\n"
                else: md +="􀬁􀆐􏿿 Auto join : off 􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀬁􀆐􏿿 Group cancel :" + str(wait["autoCancel"]["members"]) + " 􀜁􀄯􏿿\n"
                else: md+= "􀬁􀆐􏿿 Group cancel : off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀬁􀆐􏿿 Auto leave : on 􀜁􀄯􏿿\n"
                else: md+="􀬁􀆐􏿿 Auto leave : off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀬁􀆐􏿿 Share : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Share : off 􀜁􀄰􏿿\n"
                if wait["clock"] == True: md+="􀬁􀆐􏿿 Clock Name : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Clock Name : off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀬁􀆐􏿿 Auto add : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Auto add : off 􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀬁􀆐􏿿 Comment : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Comment : off 􀜁􀄰􏿿\n"
                if wait["Backup"] == True: md+="􀬁􀆐􏿿 Backup : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Backup : off 􀜁􀄰􏿿\n"
                if wait["qr"] == True: md+="􀬁􀆐􏿿 Protect QR : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Protect QR : off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,"""
       ༺ πနးຫຮี่のีধ์͜͡ ༻
""" + md)
#======================================================#
            elif msg.text in ["แท็ก1","Tag1"]:
                cl.sendText(msg.to,"ᴍᴇssᴀɢᴇ ᴄʜᴀɴɢᴇᴅ\n\n" + str(wait["tag1"]))
            elif msg.text in ["แท็ก2","Tag2"]:
                cl.sendText(msg.to,"ᴍᴇssᴀɢᴇ ᴄʜᴀɴɢᴇᴅ\n\n" + str(wait["tag2"]))
            elif "แท็ก1: " in msg.text:
                    wait["tag1"] = msg.text.replace("Tag1: ","")
                    cl.sendText(msg.to,"ᴍᴇssᴀɢᴇ ᴄʜᴀɴɢᴇᴅ")
            elif "แท็ก2: " in msg.text:
                    wait["tag2"] = msg.text.replace("Tag2: ","")
                    cl.sendText(msg.to,"ᴍᴇssᴀɢᴇ ᴄʜᴀɴɢᴇᴅ")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JกP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["เช็คข้อความแอด","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)

            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))

            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

            elif msg.text in ["ผู้สร้าง"]:
                msg.contentType = 13
                msg.contentMetadata = {"mid":"u7a4febc4c650fc7679eadf4245c2a5ad"}
                cl.sendText(msg.to," ༺ πနးຫຮี่のีধ์͜͡ ༻")
                cl.sendMessage(msg)

            elif "midเรา" == msg.text:
                cl.sendText(msg.to,mid)

            elif "1mid" == msg.text:
                ki.sendText(msg.to,kimid)

            elif "2mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)

            elif "3mid" == msg.text:
                ki3.sendText(msg.to,kimid)

            elif "4mid" == msg.text:
                ki4.sendText(msg.to,ki2mid)

            elif "5mid" == msg.text:
                ki5.sendText(msg.to,kimid)

            elif "6mid" == msg.text:
                ki6.sendText(msg.to,ki2mid)

            elif "คลิ้กmid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki5mid)

            elif "ชื่อ: " in msg.text:
                string = msg.text.replace("ชื่อ: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    
            elif msg.text.lower() == 'เช็คออน์':
                eltime = time.time() - mulai
                van = "༺ πနးຫຮี่のีধ์͜͡ ༻\nเวลาการทำงานของบอท \n"+waktu(eltime)
                cl.sendText(msg.to,van)        

            elif "ตัส: " in msg.text:
                string = msg.text.replace("ตัส: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)

            elif "ชื่อเรา: " in msg.text:
                string = msg.text.replace("ชื่อเรา: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")

            elif "1ชื่อ: " in msg.text:
                string = msg.text.replace("1ชื่อ: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"༺ πနးຫຮี่のีধ์͜͡ ༻\n" + string + "👈")

            elif "2ชื่อ: " in msg.text:
                string = msg.text.replace("2ชื่อ: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"༺ πနးຫຮี่のีধ์͜͡ ༻\n" + string + "â‡‡â‡‡👈")

            elif "3ชื่อ: " in msg.text:
                string = msg.text.replace("3ชื่อ: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"༺ πနးຫຮี่のีধ์͜͡ ༻\n" + string + "â‡‡â‡‡👈")

            elif "4ชื่อ: " in msg.text:
                string = msg.text.replace("4ชื่อ: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"༺ πနးຫຮี่のีধ์͜͡ ༻\n" + string + "â‡‡â‡‡👈")

            elif "ตัสเรา: " in msg.text:
                string = msg.text.replace("ตัสเรา: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "â‡‡â‡‡👈")

            elif "5ตัส: " in msg.text:
                string = msg.text.replace("5ตัส: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "â‡‡â‡‡👈")

            elif "6ตัส: " in msg.text:
                string = msg.text.replace("6ตัส: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "â‡‡â‡‡👈")

            elif "บอท" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)

            elif "1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)

            elif "2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)

            elif "3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)

            elif "4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)

            elif "5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)

            elif "6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)

            elif "Mid: " in msg.text:
                mmid = msg.text.replace("Mid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif "kick " in msg.text:
                midd = msg.text.replace("kick ","")
                cl.kickoutFromGroup(msg.to,[midd])

            elif "เชิญ:" in msg.text:
                midd = msg.text.replace("เชิญ:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif msg.text in [".me","me","Me"]:
                        cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")

             
            elif msg.text in ["กำ","กำกำ","กำกำกำ"]:
                        cl.sdndText(msg.to," กำควยหรือ \n  ༺ πနးຫຮี่のีধ์͜͡ ༻")
                        
            elif msg.text in ["55","555","5555"]:
                        cl.sdndText(msg.to," ตลกมากหรอไอสัส...By. ༺ πနးຫຮี่のีধ์͜͡ ༻")            
                        

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki6.sendText(msg.to, "%sseconds" % (elapsed_time))

            elif msg.text.lower() == 'respon':
                profile = ki.getProfile()
                text = profile.displayName + " ༺ πနးຫຮี่のีধ์͜͡ ༻"
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + " ༺ πနးຫຮี่のีধ์͜͡ ༻"
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + " ༺ πနးຫຮี่のีধ์͜͡ ༻"
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + " ༺ πနးຫຮี่のีধ์͜͡ ༻"
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + " ༺ πနးຫຮี่のีধ์͜͡ ༻"
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName + " ༺ πနးຫຮี่のีধ์͜͡ ༻"
                ki6.sendText(msg.to, text)

            elif "Bot?" in msg.text:
                ki.sendText(msg.to,"Bot 💀1💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki2.sendText(msg.to,"Bot 💀2💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki3.sendText(msg.to,"Bot 💀3💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki4.sendText(msg.to,"Bot 💀4💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki5.sendText(msg.to,"Bot 💀5💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki6.sendText(msg.to,"Bot 💀6💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki.sendText(msg.to,"Bot 💀1💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki2.sendText(msg.to,"Bot 💀2💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki3.sendText(msg.to,"Bot 💀3💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki4.sendText(msg.to,"Bot 💀4💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki5.sendText(msg.to,"Bot 💀5💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki6.sendText(msg.to,"Bot 💀6💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki.sendText(msg.to,"Bot 💀1💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki2.sendText(msg.to,"Bot 💀2💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki3.sendText(msg.to,"Bot 💀3💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki4.sendText(msg.to,"Bot 💀4💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki5.sendText(msg.to,"Bot 💀5💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")
                ki6.sendText(msg.to,"Bot 💀6💀 \n ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif "T say " in msg.text:
                        bctxt = msg.text.replace("T say ","")
                        ki.sendText(msg.to,(bctxt))
                        ki2.sendText(msg.to,(bctxt))
                        ki3.sendText(msg.to,(bctxt))
                        ki4.sendText(msg.to,(bctxt))
                        ki5.sendText(msg.to,(bctxt))
                        ki6.sendText(msg.to,(bctxt))

            elif msg.text.lower() == 'บอทเข้า':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)

            elif msg.text.lower() == 'เข้า3':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text.lower() == 'เข้า6':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif "1เข้า" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif "2เข้า" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)

            elif "3เข้า" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)

            elif "4เข้า" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)

            elif "5เข้า" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)

            elif "6เข้า" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)

            elif msg.text.lower() == 'บอทออก':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye "  +  str(ginfo.name)  + "By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text.lower() == "ออก":
#                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif "1ออก" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass

            elif "2ออก" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass

            elif "3ออก" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass

            elif "4ออก" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass

            elif "5ออก" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass

            elif "6ออก" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )

            elif "Sayang say " in msg.text:
                bctxt = msg.text.replace("Sayang say ","")
                ki12.sendText(msg.to,(bctxt))

            elif "Say " in msg.text:
                bctxt = msg.text.replace("Say ","")
                ki.sendText(msg.to,(bctxt))
                ki2.sendText(msg.to,(bctxt))
                ki3.sendText(msg.to,(bctxt))
                ki4.sendText(msg.to,(bctxt))
                ki5.sendText(msg.to,(bctxt))
                ki6.sendText(msg.to,(bctxt))

            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")

            elif msg.text in ["เปิดอ่าน","R on","ตั้งเวลา"]:
                        cl.sendText(msg.to,"lurk on")
            elif msg.text in ["ปิดอ่าน","R off"]:
                        cl.sendText(msg.to,"lurk off")
            elif msg.text in ["อ่าน","Ry"]:
                        cl.sendText(msg.to,"lurkers")
            elif msg.text in ["Ry20"]:
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")

            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                            cl.sendText(msg.to,"เปิดการอ่านอัตโนมัต")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                            pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendText(msg.to, "เปิดการอ่านอัตโนมัต\n" + datetime.now().strftime('%H:%M:%S'))
                        print wait2

            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"ปิดการอ่านอัตโนมัต")
                else:
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                        cl.sendText(msg.to, "ปิดการอ่านอัตโนมัต\n" + datetime.now().strftime('%H:%M:%S'))

            elif "lurkers" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                    if wait2["ROM"][msg.to].items() == []:
                        cl.sendText(msg.to, "Lurkers:\nNone")
                    else:
                        chiya = []
                        for rom in wait2["ROM"][msg.to].items():
                            chiya.append(rom[1])
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@a\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                            msg.contentType = 0
                            print zxc
                            msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                            lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                            print lol
                            msg.contentMetadata = lol
                            try:
                                cl.sendMessage(msg)
                            except Exception as error:
                                print error
                            pass
                        else:
                            cl.sendText(msg.to, "Lurking has not been set.")

            elif ("พูดตาม " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break

            elif ("ลบพูดตาม " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break

            elif msg.text in ["Miclist","เช็คพูดตาม"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "• "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")

            elif "siri " in msg.text.lower():
                    query = msg.text.lower().replace("siri ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)

            elif "siri:" in msg.text.lower():
                    query = msg.text.lower().replace("siri:","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)

            elif "siri-en " in msg.text.lower():
                    query = msg.text.lower().replace("siri-en ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)

            elif "พูด " in msg.text.lower():
                    query = msg.text.lower().replace("พูด ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)

            elif msg.text in ["1ของขวัญ","t1gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["ของขวัญ","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["2ของขวัญ","t2gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["3ของขวัญ","t3gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["4ของขวัญ","t4gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)

            elif ("ชื่อกลุ่ม: " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("ชื่อกลุ่ม: ","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")

            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"ได้ทำการเปลี่ยนชื่อเรียบร้อยแล้ว\n  ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif "ลิ้งค์+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ลิ้งค์ของกลุ่ม By. ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif "2ลิ้งค์กลุ่ม" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "1ลิ้งค์กลุ่ม" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ลิ้งค์กลุ่มปิดอยู่ \n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif msg.text.lower() == 'ชื่อเวลาเปิด':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เแิดชื่อ+เวลาเรียบร้อย by. ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif msg.text.lower() == 'ชื่อวลาปิด':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"ปิดเวลาในชื่อ \n By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"ปิดอยู่")

            elif "ตั้งเวลา:" in msg.text:
                n = msg.text.replace("ตั้งเวลา:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to," ༺ πနးຫຮี่のีধ์͜͡ ༻\n\n" + n)

            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        cl.sendText(msg.to,"By. ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif msg.text in ["lลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ลบห้องเชิญเรียบร้อยแล้ว \nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    cl.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
            elif msg.text in ["2ลบรัน"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"ลบห้องเชิญเรียบร้อยแล้ว\n By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    ki.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
            elif msg.text in ["3ลบรัน"]:
                gid = ki2.getGroupIdsInvited()
                for i in gid:
                    ki2.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki2.sendText(msg.to,"ลบห้องเชิญเรียบร้อยแล้ว\n By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    ki2.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
            elif msg.text in ["4ลบรัน"]:
                gid = ki3.getGroupIdsInvited()
                for i in gid:
                    ki3.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki3.sendText(msg.to,"ลบห้องเชิญเรียบร้อยแล้ว\n By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    ki3.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
            elif msg.text in ["5ลบรัน"]:
                gid = ki4.getGroupIdsInvited()
                for i in gid:
                    ki4.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki4.sendText(msg.to,"ลบห้องเชิญเรียบร้อยแล้ว\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    ki4.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
            elif msg.text in ["6ลบรัน"]:
                gid = ki5.getGroupIdsInvited()
                for i in gid:
                    ki5.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki5.sendText(msg.to,"ลบห้องเชิญเรียบร้อยแล้ว\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    ki5.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
            elif msg.text in ["7ลบรัน"]:
                gid = ki6.getGroupIdsInvited()
                for i in gid:
                    ki6.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                   ki6.sendText(msg.to,"ลบห้องเชิญเรียบร้อยแล้ว\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    ki6.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
            elif msg.text in ["ลบแชท","ล้างแชท"]:                                   
                cl.removeAllMessages(op.param2)
                cl.sendText(msg.to,"ลบแชทเรียบร้อย\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
#-----------------------------------------------------------
            elif msg.text in ["ลบแชทบอท","ล้างแชทบอท"]:                                   
                ki.removeAllMessages(op.param2)
                ki2.removeAllMessages(op.param2)                  
                ki3.removeAllMessages(op.param2)
                ki4.removeAllMessages(op.param2)
                ki5.removeAllMessages(op.param2)
                ki6.removeAllMessages(op.param2)
                cl.sendText(msg.to,"❇️Delete Chat Bot❇️")
                cl.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻\nได้ลบแชทBot 6Kicker เรียบร้อย")

            elif msg.text in ["ยกเลิกเชิญ","Cancel dong","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")


            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ไม่มีการเชิญ\n By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                        else:
                            cl.sendText(msg.to,"ยกเลิกเรียบร้อย\n By . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ปิดระบบกินห้องรัน\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                        else:
                            cl.sendText(msg.to,"ปิดระบบกินห้องรัน\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "เปิดระบบกินห้องรัน\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                        else:
                            cl.sendText(msg.to,strnum + "เปิดระบบกินห้องรัน\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")

            elif msg.text in ["เช็คกลุ่ม","Glist"]:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[⭐] %s \n" % (cl.getGroup(i).name + "  Members : " + str(len (cl.getGroup(i).members)))
                        cl.sendText(msg.to, "☆รายการกลุ่ม☆\n"+ h +"จำนวนกลุ่ม  " +str(len(gid)))

            elif msg.text.lower() == 'เช็คidกลุ่ม':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)

            elif "รายละเอียดกลุ่ม" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)

            elif "[Auto] " in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("[Auto] ","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
            elif "☜ʕ•ﻌ•ʔ " in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("☜ʕ•ﻌ•ʔ ","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass

            elif msg.text in ["Group cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"บกเลิกห้องทั้งหมดแล้ว\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                else:
                    cl.sendText(msg.to,"By . ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif ("ดำ " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        wait["blacklist"][target] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendText(msg.to,"Succes Banned")
                    except:
                        pass

            elif "ขาว @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("ขาว @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "ดำ1:" in msg.text:                  
                    nk0 = msg.text.replace("ดำ1:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                        if targets == []:
                            sendMessage(msg.to,"user does not exist")
                            pass
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "ขาว:" in msg.text:                  
                    nk0 = msg.text.replace("ขาว:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                        if targets == []:
                            sendMessage(msg.to,"user does not exist")
                            pass
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif msg.text in ["ดำคท"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")

            elif msg.text in ["ขาวคท"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")

            elif msg.text.lower() == 'เช็คดำ':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "�" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "�" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Daftar Hitam")

            elif msg.text in ["Cb","ล้างดำ"]:
                                wait["blacklist"] = {}
                                cl.sendText(msg.to,"clear")

            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")

            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")

            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
                cl.sendText(msg.to,"Target Lock")

            elif msg.text in ["Banlistall","Mcheck"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")

            elif msg.text in ["Me ban","Cekban","Mcheck mid"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈]Mid Blacklist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")

            elif msg.text in ["Conban","ข้อมูลบัญชีดำ","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)

            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass

            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif "Nk " in msg.text:
                    nk0 = msg.text.replace("Nk ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    gs.preventJoinByTicket = False
                    cl.updateGroup(gs)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                ki3.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                    ki3.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs.preventJoinByTicket = True
                                    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                                    cl.updateGroup(gs)

            elif "Nuke" in msg.text:
                if msg.toType == 2:
                    print "Nuke ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    start = time.time()
                    ki.sendText(msg.to, "Nuke Speed")
                    elapsed_time = time.time() - start
                    ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki3.sendText(msg.to, "Nuke Start")
                    ki4.sendText(msg.to, "Nuke Proses")
                    ki5.sendText(msg.to,"􀜁􀇔􏿿 See You Bitch 􀜁􀇔􏿿")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                        ki6.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Nuke Finish")
                                ki1.sendText(msg,to,"Nuke Succes Bos")

            elif ("Bunuh " in msg.text):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")
            elif ("Telan " in msg.text):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.kickoutFromGroup(msg.to,[target])
                        except:
                            ki.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    mi = cl.getContact(key1)
                    cl.sendText(msg.to,"Mid:" +  key1)

            elif "Beb " in msg.text:                  
                    nk0 = msg.text.replace("Beb ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"Good Bye")

            elif ("Bye " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        random.choice(KAC).kickoutFromGroup(msg.to,[target])
                    except:
                        pass

            elif "Cbroadcast " in msg.text:
                bctxt = msg.text.replace("Cbroadcast ", "")
                t = cl.getAllContactIds()
                for manusia in t:
                    cl.sendText(manusia,(bctxt))

            elif "Gbroadcast " in msg.text:
                bctxt = msg.text.replace("Gbroadcast ", "")
                n = cl.getGroupIdsJoined()
                for manusia in n:
                    cl.sendText(manusia,(bctxt))

            elif msg.text == "เช็คอ่าน":
                    cl.sendText(msg.to, "เปิดระบบเช็คคนอ่าน\nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif msg.text == "อ่าน":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to,"======ชื่อคนอ่าน====== %s\n=====ชื่อคนอ่าน======\n%s\nเวลาอ่าน \n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                         cl.sendText(msg.to,"กรุณาสั่งเช็คอ่านและสั่งอ่านใหม่ \n By . ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif "tag all" == msg.text.lower():
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                    if jml > 500:
                        print "Terlalu Banyak Men 500+"
                    cnt = Message()
                    cnt.text = "จำนวนที่ีแท็ก \n" + str(jml) +  " คน \n By . ༺ πနးຫຮี่のีধ์͜͡ ༻"
                    cnt.to = msg.to
                    cl.sendMessage(cnt)

            elif "มอง" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += "@Krampus\n"
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)

            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 1000:
                        for x in range(jmlh):
                            cl.sendText(msg.to, text)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "[Auto Respond]" in msg.text:
                cl.sendImageWithUrl(msg.to, "http://dl.profile.line.naver.jp/0hlGvN3GXvM2hLNx8goPtMP3dyPQU8GSIgJVUpCTpiPVtiA3M2clJ-C2hia11mUn04cAJ-DWljOVBj")

            elif "Fancytext: " in msg.text:
                txt = msg.text.replace("Fancytext: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"

            elif "Tx: " in msg.text:
                txt = msg.text.replace("Tx: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"

            elif msg.text in ["Kembali","backup"]:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    print "[COPY] Ok"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendMessage(msg.to, "Not Found...")
                else:
                     for target in targets:
                        try:
                             cl.cloneContactProfile(target)
                        except Exception as e:
                             print e

            elif msg.text in ["Name me","Men"]:
                G = cl.getProfile()
                X = G.displayName
                cl.sendText(msg.to,X)

            elif "siri " in msg.text.lower():
                    query = msg.text.lower().replace("siri ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
            elif "siri:" in msg.text.lower():
                    query = msg.text.lower().replace("siri:","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
            elif "siri-en " in msg.text.lower():
                    query = msg.text.lower().replace("siri-en ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)

            elif msg.text == ".11":
                    cl.sendText(msg.to, "มีใครอยู่ไหม…… !?")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('📅%d-%m-%Y ⏰%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif msg.text == "คนอ่าน":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═════════════════%s\n╠═════════════════\n%s╠═════════════════\n║Readig point creation:\n║ [%s]\n╚══════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "กรุณาพิมเช็คอ่านใหม่ \nBy . ༺ πနးຫຮี่のีধ์͜͡ ༻")

            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")

            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass

        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)

                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)

                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)

                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
            except:
                pass

        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                cl.sendText
        if op.type == 59:
            print op
    except Exception as error:
        print error

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))
    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
