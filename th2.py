#-*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia, goslate
import timeit
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="EpjV7ifkdcIRf0f6nle8.6S7B6iV24SxpyyIZPkjUga.sDURJhefZmtNiSUyL8bpywUCkdTNp9gnhYir0rEzp4o=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EpZmUMp6CzpG2MxrdrE9.Z2jqcI8fppmz+7xOGNlyEq.ttlVXdxR2I6A72rLY3B7apC+hyyUyuBQnYkKCO5J9RQ=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="Ep5x39yHINyEEVb7eaYa.Ql+Iq95c4olkmxSaoadLoG.guCtCeFRGAxadoTr/JxRhLsDyLTeTNTj285/W6Moadw=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Epezl3XFYfIArh9F82x6.SGby4XQI1gAOTET1lBqQ9G.Kha8WacxePkq1eck0Kaxb83kSJ4odJGyVV9aMSvEspI=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EpUfPCc0QdIkGkErgJca.Q6+YE7DHLRb+4/UXmbKggG.LJL7TYkXyf5UpTvXGKBFSmyYPQJAz9cgbzl5bsKJBJI=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="Epyyzy4CVbNqz8DSept8.7fLTCfOW6V77bikOdoT16a.QFITEuKTLXnmPlJ6XX43+Oe3oF3jKsLCE4JFL/mwOcA=")
ki5.loginResult()

#k1 = LINETCR.LINE()
#k1.login(token="EpRIt20HZXS8hD1yyWFc.EtYI22rmY+HaVsXbeuPt7a.0gBrcWAzR02KZorUTD1KY5xbuVfuvGx4GB0kQlLBGd4=")
#k1.loginResult()

#k2 = LINETCR.LINE()
#k2.login(token="EprPDgioqiDIMzG7ZGl2.r34MSt+faVxmgjmR8r9YCG.JZE+plZvDItp5i/Hjo3rmRkirepPGWu+X2ji1voxhJ8=")
#k2.loginResult()

#k3 = LINETCR.LINE()
#k3.login(token="Epw8a1V8sNQIo3YhiM6f.wQlogedS7pGR6dOBlSWItW.YfaKUl2HHmX3PfTm7pv6+Q3fHJMkayK9F1SKpc3q7VI=")
#k3.loginResult()

#k4 = LINETCR.LINE()
#k4.login(qr=True)
#k4.login(token="..+ZMBUmfsRNTFmzVDJgvs+U8A6o7Y=")
#k4.loginResult()

#k5 = LINETCR.LINE()
#k5.login(qr=True)
#k5.login(token="")
#k5.loginResult()

ki6 = LINETCR.LINE()

AsulLogged = False
print "──────┅═ই۝ई═┅────── ล็อคอินModified by-THIRD~SELFBOTสำเร็จ ──────┅═ই۝ई═┅──────"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""──────┅═ই۝ई═┅──────
             ❉:¸¸.•*´¨`*•.¸¸‧:❉:
       -[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-
      `*✿ °• ☞(॓_॔)☜ •°✿*ﾟ
     line.me/ti/p/4bvwOIMft8
──────┅═ই۝ई═┅──────
❂͜͡☆➣ Tagall •แท๊กสมาชิกทั้งกลุ่ม
❂͜͡☆➣ Mention แท๊กกลุ่ม
❂͜͡☆➣ Me / Contact ME
❂͜͡☆➣ You @ Contact YOU
❂͜͡☆➣ My bot
❂͜͡☆➣ Id / Uid
❂͜͡☆➣ Mid / Mid @
❂͜͡☆➣ Mid all / All mid
❂͜͡☆➣ Gift / Gift all
❂͜͡☆➣ Bot1-18 Gift
❂͜͡☆➣ Gift you @
❂͜͡☆➣ Cn: Display Name
❂͜͡☆➣ Cc: Clock Name
❂͜͡☆➣ Mc: Contact
❂͜͡☆➣ Tl: text
❂͜͡☆➣ Auto join: on/off
❂͜͡☆➣ Auto add: on/off
❂͜͡☆➣ Auto leave: on/off
❂͜͡☆➣ Clock: on/off
❂͜͡☆➣ Share on
❂͜͡☆➣ Add message: text
❂͜͡☆➣ Message:
❂͜͡☆➣ Add comment: text
❂͜͡☆➣ Comment: 
❂͜͡☆➣ Cbroadcast text
❂͜͡☆➣ Gbroadcast text
❂͜͡☆➣ Reject / ลบรัน

[C̶̲̅ᴏ̶̲̅ᴍ̶̲̅ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅ᴅ̶̲̅ ̶̲̅ɪ̶̲̅ɴ̶̲̅ ̶̲̅G̶̲̅ʀ̶̲̅ᴏ̶̲̅ᴜ̶̲̅ᴘ̶̲̅] 
❂͜͡☆➣ Creator / Admins
❂͜͡☆➣ Gn: text name group
❂͜͡☆➣ Invite: mid
❂͜͡☆➣ Ambilin @ Steal dp
❂͜͡☆➣ Sampul @ Steal cover
❂͜͡☆➣ Copy @ All bot copy
❂͜͡☆➣ Mycopy @ Copy profile
❂͜͡☆➣ Botbb  บอทกลับร่างเดิม
❂͜͡☆➣ Mebb แอดมินกลับร่าง
❂͜͡☆➣ Keluar @ target
❂͜͡☆➣ Hack @ mid contact
❂͜͡☆➣ Hack1 @
❂͜͡☆➣ Hack All @
❂͜͡☆➣ Hack2 @ Steal picS
❂͜͡☆➣ Hack3 @ Steal coveR
❂͜͡☆➣ Hack4 @ Steal statuS
❂͜͡☆➣ Mybot contactbot
❂͜͡☆➣ Allgift Gift All
❂͜͡☆➣ All mid / Bot mid
❂͜͡☆➣ Cancel / ยกเลิก ค้างเชิญ
❂͜͡☆➣ Link on/off
❂͜͡☆➣ Ginfo / ginfo / กลุ่ม
❂͜͡☆➣ Gurl / Up Qr group
❂͜͡☆➣ Glist
❂͜͡☆➣ Setting / Set / Man set
❂͜͡☆➣ Gcancel: number
❂͜͡☆➣ Masuk / Join
❂͜͡☆➣ Sayang
❂͜͡☆➣ Beb
❂͜͡☆➣ Cinta
❂͜͡☆➣ Pulang
❂͜͡☆➣ Ban @ target
❂͜͡☆➣ Uban @ target
❂͜͡☆➣ Ban -> send contact
❂͜͡☆➣ Unban -> send contact
❂͜͡☆➣ Invite:on Send contact
❂͜͡☆➣ Comment bl/wl
❂͜͡☆➣ Banlist
❂͜͡☆➣ Cekban / Conban  คท.ดำ
❂͜͡☆➣ Clear ban / Cb / ล้างดำ
❂͜͡☆➣ Kill เตะดำ
❂͜͡☆➣ Kill ban เตะบัญชีดำ
❂͜͡☆➣ Speed / !Sp / Sp
❂͜͡☆➣ music 
❂͜͡☆➣ .reboot
❂͜͡☆➣ Wikipedia
❂͜͡☆➣ Cleanse
❂͜͡☆➣ Pbot
❂͜͡☆➣ Pcancel
❂͜͡☆➣ P1-P2 tl:
❂͜͡☆➣ P1-P2 say
❂͜͡☆➣ P1-P2 tag
❂͜͡☆➣ P1-P2 invite:
❂͜͡☆➣ P1-P3 mid
❂͜͡☆➣ P1-P2 gurl
❂͜͡☆➣ P1-P5 gift
❂͜͡☆➣ P1-P5 join
❂͜͡☆➣ P1-P5 bye
❂͜͡☆➣ P1-P5 link on/off
❂͜͡☆➣ P1-P18 rgroup
❂͜͡☆➣ P1-P18 rename:
❂͜͡☆➣ All: rename all:
❂͜͡☆➣ Allbio: Isi bio:
❂͜͡☆➣ @bye / Bye / #bye
❂͜͡☆➣ Kicker / มาหำ
❂͜͡☆➣ Kick @ เตะ
❂͜͡☆➣ Nk/Mk/??¿ @
❂͜͡☆➣ Error! ล้างกลุ่ม
❂͜͡☆➣ Run group  รันกลุ่ม
❂͜͡☆➣ Man1-Man18  ข้อมูลบอท
Help2-Hp2-Ky set-Set protect-Ky key
──────┅═ই۝ई═┅──────
            line.me/ti/p/4bvwOIMft8
──────┅═ই۝ई═┅──────   
"""

Thaihelp ="""❉:¸¸.•*´¨`*•.¸¸‧:❉:
       -[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-
      `*✿ °• ☞(॓_॔)☜ •°✿*ﾟ

|╠❂➣〘คท〙           - ส่งคท.ตัวเอง(Me)
|╠❂➣〘ไอดี〙          - ส่งMidตัวเอง
|╠❂➣〘เชคชื่อ〙        - เชครายชื่อคิกเกอร์
|╠❂➣〘คิกเกอร์〙       - เชคคท.คิกเกอร์ทั้งหมด
|╠❂➣〘คิกมา〙         - เรียกคิกเกอร์เข้ากลุ่ม
|╠❂➣〘คิกออก〙        - สั่งคิกเกอร์ออกกลุ่ม
|╠❂➣〘1-10 in〙      - เรียกคิกเกอร์
|╠❂➣〘1-10 bye.〙    - สั่งคิกเกอร์ออก
|╠❂➣〘แทค〙          - แทคสมาชิก
|╠❂➣〘จุด〙           - ตั้งจุดเชคคนอ่าน
|╠❂➣〘อ่าน〙          - เชครายชื่อคนอ่าน
|╠❂➣〘เชคกลุ่ม〙       - เชคข้อมูลกลุ่ม
|╠❂➣〘ลิสกลุ่ม〙        - เชคกลุ่มที่มีทั้งหมด
|╠❂➣〘ยกเชิญ,ยก〙     - ยกเลิกเชิญ
|╠❂➣〘Mid @〙        - เชคMidรายบุคคล
|╠❂➣〘ดึง〙           - เชิญคนเข้ากลุ่มด้วยคท.
|╠❂➣〘ดึง:〙          - เชิญคนเข้ากลุ่ม้ดวยMid
|╠❂➣〘ขาว〙          - แก้ดำ(ส่งคท.)
|╠❂➣〘ดำ〙           - เพิ่มบัญชีดำ(ส่งคท.)
|╠❂➣〘เชคดำ〙        - เชคบัญชีดำ
|╠❂➣〘ล้างดำ〙        - ล้างบัญชีดำ
|╠❂➣〘เปิดลิ้ง〙
|╠❂➣〘ปิดลิ้ง〙
|╠❂➣〘ลิ้ง〙           - เปิดและขอลิ้งกลุ่ม
|╠❂➣〘Gname:〙       - เปลี่ยนชื่อกลุ่ม
|╠❂➣〘รัน @〙         - รันกลุ่ม
|️╠❂➣〘ลบรัน〙         - ลบรันตัวเอง
|️╠❂➣〘ลบรัน1〙        - ขอลิ้งให้ลอคอินก่อน
|╠❂➣️〘ขอลิ้ง〙         - ขอลิ้งให้เพื่อนลอคอิน
|╠❂➣〘.〙            - เชคสถานะลอคอิน
|╠❂➣〘Sp〙           - เชคสปีด
|╠❂➣〘Bot sp〙       - เชคสปีดคิกเกอร์
|╠❂➣〘Save〙         - บันทึกสถานะ บัญชี
|╠❂➣〘Load〙         -โหลดสถานะ บัญชี
|╠❂➣〘Mycopy @〙     - กอพปี้โปรไฟล์
|╠❂➣〘Copy @〙       - คิกเกอร์1กอพปี้
|╠❂➣〘Mybackup〙     - กลับร่างเดิม
|╠❂➣〘Backup〙       - คิกเกอร์1กลับร่างเดิม
|╠❂➣〘Spam on/off〙  - ส่งข้อความสแปม
|╠❂➣〘ยูทูป〙          -เว้นหนึ่งครั้งแล้วตามด้วยชื่อเพลง
|╠❂➣〘เพลง〙         -เว้นหนึ่งครั้งแล้วตามด้วยชื่อเพลง
|╠❂➣〘รีบอท〙
|╠❂➣〘Spam Contact @〙
|╠❂➣〘Siri:〙        -แล้วตามด้วยข้อความ
|╠❂➣〘Steal bio @〙
|╠❂➣〘Steal cover @〙
|╠❂➣〘Pict group:〙
|╠❂➣〘Steal pict @〙
|╠❂➣〘Steal mid @〙
|╠❂➣〘Steal contact〙                                                                                                                           ||==========================||

||===== ✯〖คำสั่งตั้งค่า〗✯ =====||

|╠❂➣〘เปิดไลค์/ปิดไลค์〙
|╠❂➣〘เปิดแอด/ปิดแอด〙
|╠❂➣〘เปิดเข้า/ปิดเข้า〙
|╠❂➣〘เปิดคท./ปิดคท.〙
|╠❂➣〘เปิดออก/ปิดออก〙
|╠❂➣〘เปิดแชร์/ปิดแชร์〙
|╠❂➣〘เปิดแอด/ปิดแอด〙
|╠❂➣〘Jam on/off〙
|╠❂➣〘Jam say:〙
|╠❂➣〘Com on/off〙
|╠❂➣〘Tag on〙
|╠❂➣〘Tag off〙
|╠❂➣〘Message set:〙
|╠❂➣〘Comment set:〙
|╠❂➣〘Pesan add:〙

||===== ✯〖คำสั่งป้องกัน〗✯ =====||

|╠❂➣〘เปิดหมด/ปิดหมด〙
|╠❂➣〘เปิดกัน/ปิดกัน〙
|╠❂➣〘เปิดกันลิ้ง/ปิดกันลิ้ง〙
|╠❂➣〘เปิดเชิญ/ปิดเชิญ〙
|╠❂➣〘เปิดกันยก/ปิดกันยก〙
|╠❂➣〘Staff add/remove @〙
||===== ✯〖สำหรับแอดมิน〗✯ =====||

✯★Creator By:-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-★✯
                line.me/ti/p/4bvwOIMft8

"""
help2 ="""╔═════════════════════╗
║             ‧:❉:¸¸.•*´¨`*•.¸¸‧:❉:
 ┅═✥ -[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅
             `*✿ °• ☞(॓_॔)☜ •°✿*ﾟ
╠═════════════════════╝
║[Massage add: "text"]:
║[Add confirmasi]:
║[Comment set : "Text"]:
║[Comment check]:
║[Clock: on]: "Clock name on"
║[Clock: off]: "Clock name off"
║[Ban]: "Add blacklist"
║[Unban]: "Dalate blacklist"
║[Banlist]: "Check blacklist"
╠═════════════════════╗
║         ༺•㏒.ƇƠMMƛƝƊƧ ƧЄƬ. ㏒•༻
╠═════════════════════╝
║[Contact: on/off]
║[Auto join: on/off]
║[Auto join: on/off]
║[Cancel Invite: 1 on/off]
║[Auto share: on/off]
║[Auto leave: on/off]
║[Comment: on/off]
║[Auto add: on/off]
║[Auto like: on/off]
╠═════════════════════╗
║༺•㏒.ƇƠMMƛƝƊƧ ƖƝ ƬHЄ ƓƦƠƲƤƧ. ㏒•༻
╠═════════════════════╝
║[Ban " @Tag]:
║[Unban " @Tag]:
║[Urlon]: "Open urL"
║[Urloff]: "Closed urL"
║[Url]: " Check urL room"
║[Ginfo]: "~÷~ data room"
║[Invite: "mid"]:
║[Say: "Text"]: "Kicker talk"
║[Cancel]: "Cancel invite"
║[Gns: "name"]:"Change Gname"
║[NKs: "Name"]:
║[Dead]: "Kick Blacklist"
║[Protect: on/off]:
║[Block url: on/off]:
║[Namelock: on/off]:
║[Blockinvite: on/off]:
╚═════════════════════╝
"""
help3 ="""‧:❉:¸¸.•*´¨`*•.¸¸‧:❉:
       -[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-
      `*✿ °• ☞(॓_॔)☜ •°✿*ﾟ

"""

KAC=[cl,ki,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
#k1mid = k1.getProfile().mid
#k2mid = k2.getProfile().mid
#k3mid = k3.getProfile().mid
#k4mid = k4.getProfile().mid
#k5mid = k5.getProfile().mid
Bots = [mid,"ueacedbe88bf6e2c5cf6188b3a4a26e18"]
bot1 = cl.getProfile().mid
admsa = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
admin = "ueacedbe88bf6e2c5cf6188b3a4a26e18"

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":3},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':" Add Me",
    "lang":"JP",
    "comment":"Auto Like ",
    "commentOn":False,
    "likeOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

lgncall = ""
def logincall(this):
    cl.sendText(lgncall,"Asul login url: "+this)

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup = ki2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
backup = ki3.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
backup = ki4.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
backup = ki5.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

#contact = k1.getProfile()
#backup = k1.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = k2.getProfile()
#backup = k2.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = k3.getProfile()
#backup = k3.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

user1 = mid
user2 = ""

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def sendImageWithURL(self, to_, url):
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
         s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
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

#Getting all links with the help of '_images_get_next_image'
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

    image = client.upload_from_path(image_path, config=config, anon=False)
    print()
	
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d ชั่วโมง %02d นาที %02d วินาที' % (hours, mins, secs)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    print nm
    for mm in nama:
      akh = akh + 3
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 4
      akh = akh + 1
      bb += "@x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       cl.sendMessage(msg)
    except Exception as error:
        print error
    
def bot(op):
    global AsulLogged
    global ki6
    global user2
    global readAlert
    global lgncall
    global save1
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ueacedbe88bf6e2c5cf6188b3a4a26e18":
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
# ----------------- NOTIFED MEMBER OUT GROUP
       if op.type == 15:
            if op.param2 in bot1:
                return
            cl.sendText(op.param1,"ไปสะล่ะ ไว้เจอกันใหม่น่ะ @  " + cl.getContact(op.param2).displayName + "  ลาก่อน\n～(^з^)-♡\n\n😍-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-😍")
            print ("MEMBER HAS LEFT THE GROUP")
#------------------ KICK OUT FORM GROUP
        if op.type == 19:
            if op.param2 in Bots:
                return
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + " ซัดเต็มข้อเลยครับ ท่านผู้ชม")
            print "MEMBER KICK OUT FORM GROUP"
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
            if op.param2 in bot1:
                retur
            ginfo = cl.getGroup(op.param1)
            cl.sendText(op.param1, "【．╭╮╭╮．\n ∵╭═════════════════╮】\n【╭◆┴┴◆╮．│-----ยินดีต้อนรับ------****** │】\n 【│︵　　︵│＜.. Good nigt na ｜】\n 【│　╰╯　│．╰═════════════════╯】\n 【╰○－－○╯．∵▼．∵▼．∵▼．∵▼．@ " + cl.getContact(op.param2).displayName + " สู่กลุ่ม " + "👉" + str(ginfo.name) + "👈""\n\n.¸.•´¸.•´¨) ¸.•*¨) \n( ¸.•´ (¸.•´ .•´ \n( ´¸．．★／＼︽﹨︽﹨︽☆︽＼．☆ \n☆．　／我　＼︽﹨︽﹨︽★︽＼° \n☆　│來　║﹌﹌﹌﹌﹌﹌﹌│．▲\n ★　　│簽簽║　田　╭┬╮田│◢█◣ \n＠　│　囉║　　　│││　◢███◣ \n║╓╥╥☆. ●　 ●. ╥★╥╥▊╥╥╖\n ╔╩╬╬╬╬. _/█_/█_╔╩╬╬╬╬╬╬╬ \n\n--ขอให้มีความสุขกับบ้านหลังนี้--")
            print "MEMBER HAS JOIN THE GROUP"
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited this nigga💋: \n➡" + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
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
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif msg.text.lower()  == 'คำสั่ง':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Thaihelp)
                else:
                    cl.sendText(msg.to,Thaihelp)
            elif msg.text.lower()  == 'help2':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,help2)
                else:
                    cl.sendText(msg.to,help2)
            elif msg.text.lower()  == 'ใบออ':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,help3)
                else:
                    cl.sendText(msg.to,help3)
            elif msg.text in ["Mybot","คิกเกอร์"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                k1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                k2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                k3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                k4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                k5.sendMessage(msg)
            elif "As1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "As2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "As3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "As4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "As5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "As6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                k1.sendMessage(msg)
            elif "As7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                k2.sendMessage(msg)
            elif "As8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                k3.sendMessage(msg)
            elif "As9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                k4.sendMessage(msg)
            elif "As10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                k5.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","แจก"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)

            elif msg.text in ["Cancel","cancel","ยก","ยกเชิญ"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"ไม่มีคำเชิญ👈")
                        else:
                            cl.sendText(msg.to,"ไม่มีสมาชิกค้างเชิญ👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เรียบร้อย👈")
                    else:
                        cl.sendText(msg.to,"ไม่มีคำเชิญแล้ว")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "6 mid" == msg.text:
                k1.sendText(msg.to,k1mid)
            elif "7 mid" == msg.text:
                k2.sendText(msg.to,k2mid)
            elif "8 mid" == msg.text:
                k3.sendText(msg.to,k3mid)
            elif "9 mid" == msg.text:
                k4.sendText(msg.to,k4mid)
            elif "10 mid" == msg.text:
                k5.sendText(msg.to,k5mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                k1.sendText(msg.to,k1mid)
                k2.sendText(msg.to,k2mid)
                k3.sendText(msg.to,k3mid)
                k4.sendText(msg.to,k4mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname: " in msg.text:
                string = msg.text.replace("Allname: ","")
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
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
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
                    profile = k1.getProfile()
                    profile.statusMessage = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k2.getProfile()
                    profile.statusMessage = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k3.getProfile()
                    profile.statusMessage = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k4.getProfile()
                    profile.statusMessage = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k5.getProfile()
                    profile.statusMessage = string
                    k5.updateProfile(profile)
#--------------------------------
            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
                    
            elif 'Youtube > ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube > ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")

            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"ไม่พบสื่งที่คุณต้องการค้นหา (｀・ω・´)")
            elif 'Song ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"ไม่พบสื่งที่คุณต้องการค้นหา (｀・ω・´)")
#---------------------------
            elif "Tx: " in msg.text:
                txt = msg.text.replace("Tx: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[ @ ]	Kedapkedip"
            
            elif "เพลง " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        kr.sendText(msg.to, hasil)
                        kr.sendText(msg.to, "Please Wait for audio...")
                        kr.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        kr.sendText(msg.to, str(njer))

            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Id-en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id-en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'CHROMEOS\t7.18.0\tChrome_OS\t1'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"╔═══════\n║    From ID    \n╚═══════\n" + "" + kata + "╔═══════\n║    To EN    \n╚═══════\n" + "" + result + "\n·÷±‡±±‡±÷··÷±‡±±‡±÷·")
            elif "En-id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En-id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'CHROMEOS\t7.18.0\tChrome_OS\t1'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"╔═══════\n║    From En    \n╚═══════\n" + "" + kata + "╔═══════\n║    To ID    \n╚═══════\n" + "" + result + "\n·÷±‡±±‡±÷··÷±‡±±‡±÷·")
            elif "Id-jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id-jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'CHROMEOS\t7.18.0\tChrome_OS\t1'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"╔═══════\n║    From ID    \n╚═══════\n" + "" + kata + "╔═══════\n║    To JP    \n╚═══════\n" + "" + result + "\n·÷±‡±±‡±÷··÷±‡±±‡±÷·")
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
            elif "siri:" in msg.text.lower():
                    query = msg.text.lower().replace("siri:","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "siri-en " in msg.text.lower():
                    query = msg.text.lower().replace("siri-en ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "พูด " in msg.text.lower():
                    query = msg.text.lower().replace("Talk ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'CHROMEOS\t7.18.0\tChrome_OS\t1'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithURL(msg.to, mp3)
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)    
	
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
			
            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		
            elif "Steal pict " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
	
            elif msg.text in ["Bot restart","รีบอท"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "โปรดรอกำลังรีบอทอยู่ครับ...")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access")
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Mc:" in msg.text:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

#---------------------------------------------------------
            elif "1pro: " in msg.text:
                string = msg.text.replace("1pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2pro: " in msg.text:
                string = msg.text.replace("2pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "3pro: " in msg.text:
                string = msg.text.replace("3pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4pro: " in msg.text:
                string = msg.text.replace("4pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "5pro: " in msg.text:
                string = msg.text.replace("5pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "6pro: " in msg.text:
                string = msg.text.replace("10pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                    k1.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "7pro: " in msg.text:
                string = msg.text.replace("11pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                    k2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "8pro: " in msg.text:
                string = msg.text.replace("12pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                    k3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "9pro: " in msg.text:
                string = msg.text.replace("13pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                    k4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "10pro: " in msg.text:
                string = msg.text.replace("14pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                    k5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "Mid: " in msg.text:
                mmid = msg.text.replace("Mid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Contact on","เปิดคท."]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ระบบอ่านคท.เปิดอยู่แล้ว")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอ่านคท. 👈")
                    else:
                        cl.sendText(msg.to,"เปิดระบบอ่านคท.􀜁􀇔􏿿")
            elif msg.text in ["Contact off","ปิดคท."]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว 👈")
                    else:
                        cl.sendText(msg.to,"ระบบอ่านคท.ปิดอยู่แล้ว 👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอ่านคท.")
                    else:
                        cl.sendText(msg.to,"ปิดระบบอ่านคท. 👈")
            elif msg.text in ["protect on","เปิดกัน"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"บอทป้องกันเปิดอยู่แล้ว 👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดบอทป้องกัน􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"เปิดบอทป้องกันเรียบร้อย ")
            elif msg.text in ["qrprotect on","เปิดกันลิ้ง"]:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันลิ้งเปิดอยู่ 👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดป้องกันลิ้ง􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"เปิดระบบป้องกันลิ้ง ")
            elif msg.text in ["inviteprotect on","เปิดกันเชิญ"]:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันการเชิญเปิดอยู่ 👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดป้องกันเชิญ􀜁􀇔􏿿 👈")
                    else:
                        cl.sendText(msg.to,"เปิดระบบป้องกันการเชิญ")
            elif msg.text in ["cancelprotect on","เปิดกันยก"]:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันการยกเลิกคำเชิญเปิดอยู่ 👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดกันยกเลิกเชิญ􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"เปิดระบบป้องกันการยกเลิกเชิญ")
            elif msg.text in ["Join on","เปิดเข้า"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"เข้ากลุ่มอัตโนมัติเปิดอยู่👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดเข้ากลุ่มอัตโนมัติ")
                    else:
                        cl.sendText(msg.to,"เปิดระบบเข้ากลุ่มอัตโนมัติ")
            elif msg.text in ["Allprotect on","เปิดหมด"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite on 􀜁􀇔􏿿")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel on 􀜁􀇔􏿿")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already on")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Allprotect off","ปิดหมด"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite off 􀜁􀇔􏿿")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel off 􀜁􀇔􏿿")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Join off","ปิดเข้า"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ระบบเข้ากลุ่มอัตโนมัติปิดอยู่")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดเข้ากลุ่มอัตโนมัติ")
                    else:
                        cl.sendText(msg.to,"ปิดระบบเข้ากลุ่มอัตโนมัติ👈")
            elif msg.text in ["Protect off","ปิดกัน"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันปิดอยู่👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดระบบป้องกัน")
                    else:
                        cl.sendText(msg.to,"ปิดระบบป้องกัน👈")
            elif msg.text in ["Qrprotect off","ปิดกันลิ้ง"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันลิ้งปิดอยู่👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดป้องกันลิ้ง")
                    else:
                        cl.sendText(msg.to,"ปิดระบบป้องกันลิ้ง👈")
            elif msg.text in ["Inviteprotect off","ปิดกันเชิญ"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันการเชิญปิดอยู่ 👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดป้องกันการเชิญ")
                    else:
                        cl.sendText(msg.to,"ปิดระบบป้องกันการเชิญ 👈")
            elif msg.text in ["Cancelprotect off","ปิดกันยก"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว👈")
                    else:
                        cl.sendText(msg.to,"ระบบป้องกันการยกเลิกเชิญปิดอยู่ 👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดป้องกันการยกเลิกเชิญ")
                    else:
                        cl.sendText(msg.to,"ปิดระบบป้องกันการยกเลิกเชิญ 👈")
            elif "Group cancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","เปิดออก"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"ออกแชตอัตโนมัติเปิดอยู่ 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดออกแชตอัตโนมัติ👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"เปิดระบบออกแชตอัตโนมัติ👈􀜁􀇔􏿿")
            elif msg.text in ["Leave off","ปิดออก"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"ระบบออกแชตปิดอยู่👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดออกแชตอัตโนมัติ👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"ปิดระบบออกแชตอัตโนมัติ👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","เปิดแชร์"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดแล้ว 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"เปิดระบบแชร์แล้ว👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบแชร์👈")
                    else:
                        cl.sendText(msg.to,"เปิดระบบแชร์👈")
            elif msg.text in ["Share off","ปิดแชร์"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดแล้ว👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"ระบบแชร์ปิดอยู่ 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดแชร์อัตโนมัติ👈")
                    else:
                        cl.sendText(msg.to,"ปิดระบบแชร์อัตโนมัติ👈")
            elif msg.text in "Set":
                print "Setting pick up..."
                md = "─┅══-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-══┅─\n\n"
                if wait["likeOn"] == True: md+="☣ Auto like ➣ ✔\n"
                else:md+="☣ Auto like ➣ ❌\n"
                if wait["alwayRead"] == True: md+="☣ ➣ ✔\n"
                else:md+="☣ Read ➣ ❌\n"
                if wait["detectMention"] == True: md+="☣ Autorespon ➣ ✔\n"
                else:md+="☣ Autorespon ➣ ❌\n"
                if wait["kickMention"] == True: md+="☣ Autokick ➣ ✔\n"
                else:md+="☣ Autokick ➣ ❌\n"
                if wait["Notifed"] == True: md+="☣ Notifed ➣ ✔\n"
                else:md+="☣ Notifed ➣ ❌\n"
                if wait["Notifedbot"] == True: md+="☣ Notifedbot ➣ ✔\n"
                else:md+="☣ Notifedbot ➣ ❌\n"
                if wait["winvite"] == True: md+="☣ Invite ➣ ✔\n"
                else:md+="☣ Invite ➣ ❌\n"
                if wait["pname"] == True: md+="☣ Namelock ➣ ✔\n"
                else:md+="☣ Namelock ➣ ❌\n"
                if wait["contact"] == True: md+="☣ Contact ➣ ✔\n"
                else: md+="☣ Contact ➣ ❌\n"
                if wait["autoJoin"] == True: md+="☣ Auto join ➣ ✔\n"
                else: md +="☣ Auto join ➣ ❌\n"
                if wait["autoCancel"]["on"] == True:md+="☣ Group cancel ➣" + str(wait["autoCancel"]["members"]) + "✔\n"
                else: md+= "☣ Group cancel ➣ ❌\n"
                if wait["leaveRoom"] == True: md+="☣ Auto leave ➣ ✔\n"
                else: md+="☣ Auto leave ➣ ❌\n"
                if wait["timeline"] == True: md+="☣Share ➣ ✔\n"
                else:md+="☣ Share ➣ ❌\n"
                if wait["clock"] == True: md+="☣ Clock Name ➣ ✔\n"
                else:md+="☣ Clock Name ➣ ❌\n"
                if wait["autoAdd"] == True: md+="☣ Auto add ➣ ✔\n"
                else:md+="☣ Auto add ➣ ❌\n"
                if wait["commentOn"] == True: md+="☣ Comment ➣ ✔\n"
                else:md+="☣ Comment ➣ ❌\n"
                if wait["Backup"] == True: md+="☣ Backup ➣ ✔\n"
                else:md+="☣ Backup ➣ ❌\n"
                if wait["qr"] == True: md+="☣Protect QR ➣ ✔\n"
                else:md+="☣ Protect QR ➣ ❌\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)

            elif msg.text in "เชคค่า":
                print "Setting pick up..."
                md = "─┅══-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-══┅─\n\n"
                if wait["likeOn"] == True: md+="☣ ไลค์ออโต้ ➣ ✔\n"
                else:md+="☣ ไลค์ออโต้ ➣ ❌\n"
                if wait["alwayRead"] == True: md+="☣ อ่านออโต้ ➣ ✔\n"
                else:md+="☣ อ่านออโต้ ➣ ❌\n"
                if wait["detectMention"] == True: md+="☣ การตอบกลับ ➣ ✔\n"
                else:md+="☣ การตอบกลับ ➣ ❌\n"
                if wait["kickMention"] == True: md+="☣เตะคนแท็ค ➣ ✔\n"
                else:md+="☣ เตะคนแท็ค ➣ ❌\n"
                if wait["Notifed"] == True: md+="☣ เเจ้งเตือนต้อนรับตนเอง ➣ ✔\n"
                else:md+="☣ 􀬁เเจ้งเตือนต้อนรับตนเอง ➣ ❌\n"
                if wait["Notifedbot"] == True: md+="☣ เเจ้งเตือนต้อนรับบอท ➣ ✔\n"
                else:md+="☣ เเจ้งเตือนต้อนรับบอท ➣ ❌\n"
                if wait["winvite"] == True: md+="☣ การเชิญ ➣ ✔\n"
                else:md+="☣ การเชิญ ➣ ❌\n"
                if wait["pname"] == True: md+="☣ ล๊อกชื่อกลุ่ม ➣ ✔\n"
                else:md+="☣ ล๊อกชื่อกลุ่ม ➣ ❌\n"
                if wait["contact"] == True: md+="☣ ข้อมูลติดต่อ ➣ ✔\n"
                else: md+="☣ ข้อมูลติดต่อ ➣ ❌\n"
                if wait["autoJoin"] == True: md+="☣ เข้าร่วมกลุ่มออโต้ ➣ ✔\n"
                else: md +="☣ เข้าร่วมกลุ่มออโต้ ➣ ❌\n"
                if wait["autoCancel"]["on"] == True:md+="☣􀬁ป้องกันเชิญจำนวน ➣" + str(wait["autoCancel"]["members"]) + "✔\n"
                else: md+= "☣ ป้องกันเชิญจำนวน ➣ ❌\n"
                if wait["leaveRoom"] == True: md+="☣􀬁ป้องกันเชิญเเชทรวม ➣ ✔\n"
                else: md+="☣ ป้องกันเชิญเเชทรวม ➣ ❌\n"
                if wait["timeline"] == True: md+="☣ เเชร์ลิ้งค์ ➣ ✔\n"
                else:md+="☣ เเชร์ลิ้ง ➣ ❌\n"
                if wait["clock"] == True: md+="☣􀬁ชื่อเวลา ➣ ✔\n"
                else:md+="☣ ชื่อเวลา ➣ ❌\n"
                if wait["autoAdd"] == True: md+="☣ เพิ่มเพื่อนออโต้ ➣ ✔\n"
                else:md+="☣ เพิ่มเพื่อนออโต้ ➣ ❌\n"
                if wait["commentOn"] == True: md+="☣ ความคิดเห็นออโต้ ➣ ✔\n"
                else:md+="☣ ความคิดเห็นออโต้ ➣ ❌\n"
                if wait["Backup"] == True: md+="☣ ป้องกันเชิญ ➣ ✔\n"
                else:md+="☣ ป้องกันเชิญ ➣ ❌\n"
                if wait["qr"] == True: md+="☣ ป้องกันลิ้ง ➣ ✔\n"
                else:md+="☣ ป้องกันลิ้ง ➣ ❌\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            
            elif msg.text in ["Like on","เปิดไลค์"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว。")
                else:
                    wait["likeOn"] = True
                if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบออโต้ไลค์。")
            elif msg.text in ["ปิดไลค์","Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดระบบออโต้ไลค์。")
                        
            elif msg.text in ["Add on","เปิดแอด"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"ระบบแอดอัตโนมัติเปิดอยู่👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดแอตอัตโนมัติ👈")
                    else:
                        cl.sendText(msg.to,"เปิดระบบแอดอัตโนมัติ👈")
            elif msg.text in ["Add off","ปิดแอด"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว 👈")
                    else:
                        cl.sendText(msg.to,"ระบบแอดอัตโนมัติปิดอยู่👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดแอดอัตโนมัติ👈")
                    else:
                        cl.sendText(msg.to,"ปิดระบบแอดอัตโนมัติ👈")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message set: ","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
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
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","เปิดเม้น","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดอยู่แล้ว👈")
                    else:
                        cl.sendText(msg.to,"คอมเม้นอัตโนมัติเปิดอยู่👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดคอมเม้นอัตโนมัติ👈")
                    else:
                        cl.sendText(msg.to,"เปิดระบบคอมเม้นอัตโนมัติ👈")
            elif msg.text in ["Com off","ปิดเม้น"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดอยู่แล้ว")
                    else:
                        cl.sendText(msg.to,"คอมเม้นอัตโนมัติปิดอยู่")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดคอมเม้นอัตโนมัติ👈")
                    else:
                        cl.sendText(msg.to,"ปิดระบบคอมเม้นอัตโนมัติ")
            elif msg.text in ["Com","Comment","เชคเม้น"]:
                cl.sendText(msg.to,"คอมเม้นอัตโนมัติถูกตั้งไว้ดังนี้:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say: " in msg.text:
                n = msg.text.replace("Jam say: ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
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

            elif msg.text in ["Point","จุด"]:
                if msg.toType == 2:
                    cl.sendText(msg.to, "ตั้งจุดเช็คคนอ่าน:" + datetime.now().strftime('\n📅%Y/%m/%d 🕛 %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('📅%Y-%m-%d 🕛 %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text in ["Read","อ่าน"]:
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "==============================\nActive readers:%s\n\n\n\nPassive readers:\n%s\n\n==============================\nIn the last seen point:\n[%s]\n==============================\n Powered By:-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-々•┅──" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('📅%Y-%m-%d 🕛 %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Auto set reading point in:" + datetime.now().strftime('\n📅%Y-%m-%d 🕛 %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "Reading point has not been set.")

#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list: ")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"								
#-----------------------------------------------------------

#----------------------------------------------------------------
            elif msg.text in ["Reject","ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ปฏิเสทคำเชิญเข้ากลุ่มทั้งหมดเรียบร้อย")
                else:
                    cl.sendText(msg.to,"key is wrong")
            elif msg.text in ["Reject1","ลบรัน1"]:
                gid = ki6.getGroupIdsInvited()
                for i in gid:
                    ki6.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki6.sendText(msg.to,"ปฏิเสทค้างเชิญเรียบร้อย")
                else:
                    ki6.sendText(msg.to,"key is wrong")
#-----------------------------------------------------------
            elif msg.text in ["Aslogin","ขอลิ้ง"]:
                    if not AsulLogged:
                        lgncall = msg.to
                        ki6.login(qr=True,callback=logincall)
                        ki6.loginResult()
                        user2 = ki6.getProfile().mid
                        AsulLogged = True
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        kk.sendText(user1,"ล็อกอินสำเร็จ Asul พร้อมใช้งานแล้ว (｀・ω・´)"+tm)
                    else:
                        cl.sendText(msg.to,"Asul ได้ทำการล็อคอินไปแล้ว")
            elif msg.text.lower() == ".":
                    gs = []
                    try:
                        gs = cl.getGroup(msg.to).members
                    except:
                        try:
                            gs = cl.getRoom(msg.to).contacts
                        except:
                            pass
                    tlist = ""
                    for i in gs:
                        tlist = tlist+i.displayName+" "+i.mid+"\n\n"
                    if AsulLogged == True:
                        try:
                            ki6.sendText(user1,tlist)
                        except:
                            ki6.new_post(tlist)
                    else:
                        cl.sendText(msg.to,"Asul ยังไม่ได้ล็อคอิน")
#-----------------------------------------------------------)
#----------------------ADMIN COMMAND------------------------------#

            elif ("Kick " in msg.text):
                if msg.from_ in admin:
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
                    
            elif msg.text in ["Mention","Tagall","แทค"]:
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
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 

            elif "Ratakan" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Ratakan","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:                            
                             if not target in Bots:
                                if not target in admin:
                                  try:
                                      klist=[ki3,ki4,ki5,k1,k2,k3,k4,k5]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      print (msg.to,[g.mid])
                                  except:
                                      cl.sendText(msg.to,"Sukses Bosqu")
                                      cl.sendText(msg.to,"masih mauko sundala")
#------------------------------------------------
            if msg.text.lower() in ["Kie@@"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "[Member List TAG number : " + str(jml) +  " Members]\n┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅"
                cnt.to = msg.to
                cl.sendMessage(cnt)
#------------------------------------
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["อย่าแท็กกู กูไม่ว่าง!!",cName + " มีปัญหาอะไร ?!",cName + " หยุดแท็กเหอะ ถ้าสำคัญจริงก็คอลมา","ยังๆ ยังไม่หยุด","ขอร้องเหอะ.กุว่าวอยู่!!", cName + " ทำไมต้องแท็ก?" + cName, "ชอบแท็กนักหราา " + cName, "คุณเป็นใคร? " + cName + "?", "เห้ออ.." + cName + "?","ขาดความอบอุ่นหราาา ","== ww =="]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break
#-----------------------------------
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["อย่าแท็กกู กูไม่ว่าง!!",cName + " มีปัญหาอะไร ?!",cName + " หยุดแท็กเหอะ ถ้าสำคัญจริงก็คอลมา","ยังๆ ยังไม่หยุด","ขอร้องเหอะตีป้อมอยู่!!", cName + " ทำไมต้องแท็ก?" + cName, "ชอบแท็กนักหราา " + cName, "คุณเป็นใคร? " + cName + "?", "เห้ออ.." + cName + "?","ขาดความอบอุ่นหราาา ","== ww =="]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
                                  
            elif msg.text in ["List grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif msg.text in ["Info grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"===[List Details Group]===")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = ki.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"===[List Details Groups Invited]===")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif "Details grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/DetailsGroup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
            
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)

            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gname: ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Tidak Dapat Mengubah Nama Grup")

            elif "Kick: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "Mysteal @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Mysteal @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "ไม่สำเร็จ...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "ก็อพปี้สำเร็จ")
                                except Exception as e:
                                    print e

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "ไม่สำเร็จ")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki.sendText(msg.to, "ก็อพปี้เรียบร้อย")
                                except Exception as e:
                                    print e

            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "กลับร่างเดิมแล้ว")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki.sendText(msg.to, "กลับร่างเดิมแล้ว")
                except Exception as e:
                    ki.sendText(msg.to, str (e))

            elif "Bc:ct " in msg.text:
                bctxt = msg.text.replace("Bc:ct ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))

            elif "Bot:ct " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:ct ", "")
                b = ki.getAllContactIds()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getAllContactIds()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getAllContactIds()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getAllContactIds()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getAllContactIds()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                k = k1.getAllContactIds()
                for manusia in k:
                    k1.sendText(manusia, (bctxt))
                l = k2.getAllContactIds()
                for manusia in l:
                    k2.sendText(manusia, (bctxt))
                m = k3.getAllContactIds()
                for manusia in m:
                    k3.sendText(manusia, (bctxt))
                n = k4.getAllContactIds()
                for manusia in n:
                    k4.sendText(manusia, (bctxt))
                o = k5.getAllContactIds()
                for manusia in o:
                    k5.sendText(manusia, (bctxt))
                
            elif "Bc:grup " in msg.text:
                bctxt = msg.text.replace("Bc:grup ", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            
            elif "Bot:grup " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:grup ", "")
                b = ki.getGroupIdsJoined()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getGroupIdsJoined()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getGroupIdsJoined()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getGroupIdsJoined()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getGroupIdsJoined()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                k = k1.getGroupIdsJoined()
                for manusia in k:
                    k1.sendText(manusia, (bctxt))
                l = k2.getGroupIdsJoined()
                for manusia in l:
                    k2.sendText(manusia, (bctxt))
                m = k3.getGroupIdsJoined()
                for manusia in m:
                    k3.sendText(manusia, (bctxt))
                n = k4.getGroupIdsJoined()
                for manusia in n:
                    k4.sendText(manusia, (bctxt))
                o = k5.getGroupIdsJoined()
                for manusia in o:
                    k5.sendText(manusia, (bctxt))

            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "รัน @" in msg.text:
                print "[Command]covergroup"
                _name = msg.text.replace("Covergroup @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                           thisgroup = cl.getGroups([msg.to])
                           Mids = [target for contact in thisgroup[0].members]
                           mi_d = Mids[:33]
                           cl.createGroup("Asul Group",mi_d)
                           ki.createGroup("Asul Group",mi_d)
                           ki2.createGroup("Asul Group",mi_d)
                           ki3.createGroup("Asul Group",mi_d)
                           ki4.createGroup("Asul Group",mi_d)
                           ki5.createGroup("Asul Group",mi_d)
                           k1.createGroup("Asul Group",mi_d)
                           k2.createGroup("Asul Group",mi_d)
                           k3.createGroup("Asul Group",mi_d)
                           k4.createGroup("Asul Group",mi_d)
                           k5.createGroup("Asul Group",mi_d)
                           cl.sendText(msg.to,"เรียบร้อย")
                        except:
                            pass
                print "[Command]covergroup"

            elif msg.text in ["Sp","Speed","speed"]:
                cl.sendText(msg.to, "LOADING:▒...0%")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "% s seconds" % (elapsed_time))
                print "[Command]Speed palsu executed"
            elif msg.text in ["BotSp","sp","Speed"]:
                ki.sendText(msg.to, "Progress.......")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                k1.sendText(msg.to, "%sseconds" % (elapsed_time))
                k2.sendText(msg.to, "%sseconds" % (elapsed_time))
                k3.sendText(msg.to, "%sseconds" % (elapsed_time))
                k4.sendText(msg.to, "%sseconds" % (elapsed_time))
                k5.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu executed"

            elif msg.text in ["Keyy"]:
                cl.sendText(msg.to, "[-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-]\n\n❂͜͡☆➣ Namelock on\n❂͜͡☆➣ Namelock off\n❂͜͡☆➣Blockinvite on\n❂͜͡☆➣Blockinvite off\n❂͜͡☆➣ Backup on\n❂͜͡☆➣ Backup off\n\n[By.-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-]")

#=========================================================================================
            elif msg.text in ["Me","เก๊า","เค้า","เก๊าเอา","คท"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"SELF BOT BY:\n\n                              ꧁✯-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✯꧂")

            elif cms(msg.text,["ผู้สร้าง","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"😹SelfBOT BY:-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"😸line.me/ti/p/4bvwOIMft8")
            
            elif "Inviteme: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("Inviteme: ","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif msg.text in ["Clear grup"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = k1.getGroupIdsJoined()
                gid = k2.getGroupIdsJoined()
                gid = k3.getGroupIdsJoined()
                gid = k4.getGroupIdsJoined()
                gid = k5.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    k1.leaveGroup(i)
                    k2.leaveGroup(i)
                    k3.leaveGroup(i)
                    k4.leaveGroup(i)
                    k5.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

            elif msg.text in ["Ginfo","เชคกลุ่ม"]:
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text == "ไวรัส01":
	            cl.sendText(msg.to,"หยุดดดดดด....\nขอให้ทุกคนอยู่ในความสงบ\n\n1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
            
            elif ".music" in msg.text.lower():
	            songname = msg.text.lower().replace(".music","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])
            
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])

            elif "Block @" in msg.text:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("Block @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.blockContact(target)
                               cl.sendText(msg.to, "Success block contact~")
                            except Exception as e:
                               print e

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
            
            elif msg.text in ["Glist","ลิสกลุ่ม"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[★] %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"▒▒▓█[List Group]█▓▒▒\n"+ h +"Total Group =" +"["+str(len(gid))+"]")

            elif msg.text in ["Invite","ดึง"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"ส่งคท.ด้วย 😉")
                
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Mid @" in msg.text:
              if msg.from_ in admin:  
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ki.sendText(msg.to, g.mid)
                    else:
                        pass

            elif msg.text in ["Mymid","ไอดี"]:
                cl.sendText(msg.to,mid)

            elif msg.text in ["Link on","เปิดลิ้ง"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group 👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ")
            
            elif msg.text in ["Link off","ปิดลิ้ง"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close👈")
                    else:
                        cl.sendText(msg.to,"URL close👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ")

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
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")

            elif msg.text in ["Gurl","ลิ้ง"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = ki2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki2.getGroup(i).name + " | [ " + str(len (ki2.getGroup(i).members)) + " ]")
                ki2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = ki3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki3.getGroup(i).name + " | [ " + str(len (ki3.getGroup(i).members)) + " ]")
                ki3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S4glist"]:
                gs = ki4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki4.getGroup(i).name + " | [ " + str(len (ki4.getGroup(i).members)) + " ]")
                ki4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S5glist"]:
                gs = ki5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki5.getGroup(i).name + " | [ " + str(len (ki5.getGroup(i).members)) + " ]")
                ki5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S10glist"]:
                gs = k1.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k1.getGroup(i).name + " | [ " + str(len (k1.getGroup(i).members)) + " ]")
                k1.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S11glist"]:
                gs = k2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k2.getGroup(i).name + " | [ " + str(len (k2.getGroup(i).members)) + " ]")
                k2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S12glist"]:
                gs = k3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k3.getGroup(i).name + " | [ " + str(len (k3.getGroup(i).members)) + " ]")
                k3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S13glist"]:
                gs = k4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k4.getGroup(i).name + " | [ " + str(len (k4.getGroup(i).members)) + " ]")
                k4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S14glist"]:
                gs = k5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k5.getGroup(i).name + " | [ " + str(len (k5.getGroup(i).members)) + " ]")
                k5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                    
            elif msg.text == "Link bokep":
                    ki.sendText(msg.to,"nekopoi.host")
                    ki.sendText(msg.to,"sexvideobokep.com")
                    ki.sendText(msg.to,"memek.com")
                    ki.sendText(msg.to,"pornktube.com")
                    ki.sendText(msg.to,"faketaxi.com")
                    ki.sendText(msg.to,"videojorok.com")
                    ki.sendText(msg.to,"watchmygf.mobi")
                    ki.sendText(msg.to,"xnxx.com")
                    ki.sendText(msg.to,"pornhd.com")
                    ki.sendText(msg.to,"xvideos.com")
                    ki.sendText(msg.to,"vidz7.com")
                    ki.sendText(msg.to,"m.xhamster.com")
                    ki.sendText(msg.to,"xxmovies.pro")
                    ki.sendText(msg.to,"youporn.com")
                    ki.sendText(msg.to,"pornhub.com")
                    ki.sendText(msg.to,"anyporn.com")
                    ki.sendText(msg.to,"hdsexdino.com")
                    ki.sendText(msg.to,"rubyourdick.com")
                    ki.sendText(msg.to,"anybunny.mobi")
                    ki.sendText(msg.to,"cliphunter.com")
                    ki.sendText(msg.to,"sexloving.net")
                    ki.sendText(msg.to,"free.goshow.tv")
                    ki.sendText(msg.to,"eporner.com")
                    ki.sendText(msg.to,"Pornhd.josex.net")
                    ki.sendText(msg.to,"m.hqporner.com")
                    ki.sendText(msg.to,"m.spankbang.com")
                    ki.sendText(msg.to,"m.4tube.com")
                    ki.sendText(msg.to,"brazzers.com")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
                
            elif "Dj " in msg.text:
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           random.choice(KAC).kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
#-----------------------------------------------------------
            
            elif msg.text in ["Responsname","เชคชื่อ"]:
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text + "รายงานตัว")
                profile = ki2.getProfile()
                text = profile.displayName
                ki2.sendText(msg.to, text + "รายงานตัว")
                profile = ki3.getProfile()
                text = profile.displayName
                ki3.sendText(msg.to, text + "รายงานตัว")
                profile = ki4.getProfile()
                text = profile.displayName
                ki4.sendText(msg.to, text + "รายงานตัว")
                profile = ki5.getProfile()
                text = profile.displayName
                ki5.sendText(msg.to, text + "รายงานตัว")
                profile = k1.getProfile()
                text = profile.displayName
                k1.sendText(msg.to, text + "รายงานตัว")
                profile = k2.getProfile()
                text = profile.displayName
                k2.sendText(msg.to, text + "รายงานตัว")
                profile = k3.getProfile()
                text = profile.displayName
                k3.sendText(msg.to, text + "รายงานตัว")
                profile = k4.getProfile()
                text = profile.displayName
                k4.sendText(msg.to, text + "รายงานตัว")
                profile = k5.getProfile()
                text = profile.displayName
                k5.sendText(msg.to, text + "รายงานตัว")

#------------------------------------------------------------------	
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
 #------------------------------------------------------------------
            elif "Blacklist @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Blacklist @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Boss")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "Blacklist all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Blacklist all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Semua Telah Di Hapus")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       cl.sendText(msg.to,"Success Boss")
                                   except:
                                       cl.sentText(msg.to,"Berhasil Dihapus")
            
            elif "Whitelist @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Whitelist @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")

            elif "Blacklist: " in msg.text:       
             if msg.from_ in admin:           
                       nk0 = msg.text.replace("Blacklist: ","")
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

            elif "Whitelist: " in msg.text:             
              if msg.from_ in admin:     
                       nk0 = msg.text.replace("Whitelist: ","")
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

            elif msg.text in ["Clear ban","ล้างดำ"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"clear")
            elif msg.text in ["Whitelist","ขาว"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Blacklist","ดำ"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Banlist","เชคดำ"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Ban cek","Cekban"]:
              if msg.from_ in admin:
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
            elif msg.text.lower() == 'kill':
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            k1.kickoutFromGroup(msg.to,[jj])
                            k2.kickoutFromGroup(msg.to,[jj])
                            k3.kickoutFromGroup(msg.to,[jj])
                            k4.kickoutFromGroup(msg.to,[jj])
                            k5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Nuke" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = k1.getGroup(msg.to)
                    gs = k2.getGroup(msg.to)
                    gs = k3.getGroup(msg.to)
                    gs = k4.getGroup(msg.to)
                    gs = k5.getGroup(msg.to)
                    cl.sendText(msg.to,"Masih Mauko Sundala")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ada Member")
                        ki2.sendText(msg.to,"Nothing Bosqu")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[k1,k2,k3,k4,k5,ki,ki2,ki3,ki4,ki5]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Hahaha")
                                ki2.sendText(msg,to,"Fakyu Sundala")

#-----------------------------------------------

#-----------------------------------------------
            elif msg.text.lower() == 'kicker':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text in ["คิกมา","มามะ","กุ๊กๆๆ","โม่ๆ"]:
                if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.02)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text.lower() == 'ให้ไว':
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
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "1 in" in msg.text:
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
#-----------------------------------------------
            elif "2 in" in msg.text:
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
#-----------------------------------------------
            elif "3 in" in msg.text:
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
#-----------------------------------------------
            elif "4 in" in msg.text:
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
#-----------------------------------------------
            elif "5 in" in msg.text:
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
#-----------------------------------------------
            elif "6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k1.updateGroup(G)
#-----------------------------------------------
            elif "7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k2.updateGroup(G)
#-----------------------------------------------
            elif "8 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k3.updateGroup(G)
#-----------------------------------------------
            elif "9 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k4.updateGroup(G)
#-----------------------------------------------
            elif "10 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k5.updateGroup(G)
#-----------------------------------------------
            elif msg.text.lower() == '#bye':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        ki.leaveGroup(msg.to)
                        kk.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kk.leaveGroup(msg.to)
                        kc.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kc.leaveGroup(msg.to)
                        kd.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kd.leaveGroup(msg.to)
                        ke.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        ke.leaveGroup(msg.to)
                        kf.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kf.leaveGroup(msg.to)
                        kg.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kg.leaveGroup(msg.to)
                        kh.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kh.leaveGroup(msg.to)
                        kj.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kj.leaveGroup(msg.to)
                        kl.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kl.leaveGroup(msg.to)
                        km.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        km.leaveGroup(msg.to)
                        kn.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kn.leaveGroup(msg.to)
                        ko.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        ko.leaveGroup(msg.to)
                        kp.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kp.leaveGroup(msg.to)
                        kq.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kq.leaveGroup(msg.to)
                        kr.sendText(msg.to,"•┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kr.leaveGroup(msg.to)
                        ks.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        ks.leaveGroup(msg.to)
                        kt.sendText(msg.to,"┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n Bye~Bye ["  +  str(ginfo.name)  + "]")
                        kt.leaveGroup(msg.to)
                    except:
                        pass

            elif"V10" in msg.text:
                cl.sendText(msg.to,"""┅═✥-[✭]-Ⓣ-Ⓗ-Ⓘ-Ⓡ-Ⓓ-[✭]-✥═┅\n\n
နับთิஏთั้ଏบਹທ Sirichan V⒑
คำสั่งบอท siri
คำนี้เป็นการล็อกห้องสั่งแล้วทุกคนจะทำอะไรไม่ได้นอกจากเจ้าของห้องทำได้คนเดียวเช่น•เปิดลิงค์•เชิญเพื่อน•เปลี่ยนรูปกลุ่ม•เปลี่ยนชื่อกลุ่มไรแบบนี้• บอทจะไม่เตะเเอทมินทุกกรณี
มีตั้งเเต่ชุดบอท 12-37 บอท
ชุดล๊อกห้อง
ล๊อกกันรันสติ๊กเกอร์
Set:StampLimitation:on

ล๊อกชื่อกลุ่ม
Set:changenamelock:on

ล๊อกการเชิญของสมาชิก
Set:blockinvite:on

ล๊อกแอทมินกลุ่ม
Set:ownerlock:on

ล๊อกรูปกลุ่ม
Set:iconlock:on

➖➖➖➖➖➖➖➖➖➖➖➖➖➖
set:changeowner
เปลี่ยนเจ้าของห้องสั่งแล้วส่งคอลแทคคนที่จะเป็นเจ้าของห้องคนต่อไปลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
set:addblacklist
บัญชีดำแบ็คลิสคนไม่ให้เข้ากลุ่มสั่งแล้วส่งคอลแทคคนที่เราจะแบ็คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
set:addwhitelist
บัญชีขาวแก้ดำสั่งแล้วส่งคอลแทคคนที่เราจะแก้แบ๊คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:off  ปลดล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:on  ล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:inviteurl         เปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:DenyURLInvite  ปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:cancelinvite  ยกเลิกค้างเชิญสั่ง2ครั้ง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:groupcreator เช็คเจ้าของบ้านตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:extracreator  เช็คเจ้าของบ้านคนสำรอง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
set:changeextraowner 
เพิ่มเจ้าของบ้านคนที2หรือเรียกคนสำรองสั่งแล้วส่งคอลแทคคนที่จะเป็นคนสำรองลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:turncreator

สลับให้เจ้าของบ้านคนที่2เป็นตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
ดูคนอ่าน สั่งตั้งค่าก่อนแล้วค่อยสั่งอ่านคน

Setlastpoint     ตั้งค่า

Viewlastseen   สั่งอ่าน

➖➖➖➖➖➖➖➖➖➖➖➖➖➖


──────┅═ই۝ई═┅──────
รับปรึกษาและสร้างปัญหาในไลน์ทุกรูปแบบ
รับปรึกษา เรื่องบอทไลน์ เชลบอท และอื่นๆ
                           สนใจติดต่อ  
    line.me/ti/p/4bvwOIMft8
[รับประกันความ เกรียนแบบ เหี้ยเรียก.พ่อง]
ในแบบ ฉบับของ พวกเรา..คลับ สะกิดตรีน
──────┅═ই۝ई═┅──────
""")

#-----------------------------------------------
            elif "1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k1.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "8 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "9 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "10 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#----------------------------------------------- 
#-----------------------------------------------
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in k1mid:
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in k1mid:
                        G = k1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)
                    else:
                        G = k1.getGroup(op.param1)

                        
                        k1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)

                elif op.param3 in k1mid:
                    if op.param2 in k2mid:
                        G = k2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)

                        
                        k2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)

                elif op.param3 in k3mid:
                    if op.param2 in k2mid:
                        G = k2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)

                        
                        k2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)

                elif op.param3 in k4mid:
                    if op.param2 in k3mid:
                        G = k3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)
                    else:
                        G = k3.getGroup(op.param1)

                        
                        k3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)

                elif op.param3 in k3mid:
                    if op.param2 in k4mid:
                        G = k4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                    else:
                        G = k4.getGroup(op.param1)

                        
                        k4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)

                elif op.param3 in k5mid:
                    if op.param2 in k4mid:
                        G = k4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                    else:
                        G = k4.getGroup(op.param1)

                        
                        k4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)

                elif op.param3 in k4mid:
                    if op.param2 in k5mid:
                        G = k5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)
                    else:
                        G = k5.getGroup(op.param1)

                        
                        k5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)

                elif op.param3 in k5mid:
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
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
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
            except:
                pass

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
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
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
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
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
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open QR Kick finish-----#
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n|| " + Nama
                        wait2['ROM'][op.param1][op.param2] = "|| " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass

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

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   k5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          k5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

#def autolike():
#     for zx in range(0,50):
#        hasil = cl.activity(limit=1000)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#          try:    
#            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            print "Like"
#            print "Like"
#            print "Like"
#          except:
#            pass
#        else:
#            print "Already Liked"
#     time.sleep(600)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
 