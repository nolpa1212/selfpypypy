from requests import get,post
from os import name
from threading import Thread
from pytz import timezone
from datetime import date,datetime
import json 
from os import name
import os
from random import choice
from bs4 import BeautifulSoup
from re import findall
from PIL import Image, ImageDraw, ImageFont
from urllib.request import Request, urlopen
from urllib.parse import quote
from time import time
from rextester_Api import Rextester
import jdatetime
import pyPrivnote as pn

org = [":","0","1","2","3","4","5","6","7","8","9"]
fonts = [[":","๐ถ","๐ท","๐ธ","๐น","๐บ","๐ป","๐ผ","๐ฝ","๐พ","๐ฟ"],
[":","โช","โ ","โก","โข","โฃ","โค","โฅ","โฆ","โง","โจ"],
[":","โฟ","โถ","โท","โธ","โน","โบ","โป","โผ","โฝ","โพ"],
[":","๐","๐","๐","๐","๐","๐"," ๐","๐","๐ ","๐ก"],
[":","๐ฌ","๐ญ","๐ฎ","๐ฏ","๐ฐ","๐ฑ","๐ฒ","๐ณ","๐ด","๐ต"],
[":","๏ผ","๏ผ","๏ผ","๏ผ","๏ผ","๏ผ","๏ผ","๏ผ","๏ผ","๏ผ"],
[":","โฌ0โญ","โฌ1โญ","โฌ2โญ","โฌ3โญ","โฌ4โญ","โฌ5โญ","โฌ6โญ","โฌ7โญ","โฌ8โญ","โฌ9โญ"],
[":","โ๐","โ๐","โ๐","โ๐","โ๐","โ๐","โ๐","โ๐","โ๐","โ๐"],
[":","๐ถ","า1","า2","า3","า4","า5","า6","า7","า8","า9า"],
[":","โ","โ","โ","โ","โ","โ","โ","โ","โ","โ"],
[":","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐"]]
fonts2 = [[':','โฐ','ยน','ยฒ','ยณ','โด','โต','โถ','โท','โธ','โน']]
org_eng = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
name_font = [["๐ฌ","๐ญ","๐ฎ","๐ฏ","๐ฐ","๐ฑ","๐ฒ","๐ณ","๐ด","๐ต","๐ถ","๐ท","๐ธ","๐น","๐บ","๐ป","๐ผ","๐ฝ","๐พ","๐ฟ","๐","๐","๐","๐","๐","๐"],
["๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐ ","๐ก","๐ข","๐ฃ","๐ค","๐ฅ","๐ฆ","๐ง","๐จ","๐ฉ"],
["๊ช","แฅ","แฅด","แฆ","๊ซ","แ ป","แง","๊ซ","โ","๐","๐","๊ชถ","๊ช","๊ช","๊ชฎ","ฯ","๐ข","๐ฃ","เชก","๐ฅ","๊ช","๊ช","แญ","แฅ","๊ช","๐ซ"],
["๐ธ","๐น","โ","๐ป","๐ผ","๐ฝ","๐พ","โ","๐","๐","๐","๐","๐","โ","๐","โ","โ","โ","๐","๐","๐","๐","๐","๐","๐","โค"],
["๏ผก","๏ผข","๏ผฃ","๏ผค","๏ผฅ","๏ผฆ","๏ผง","๏ผจ","๏ผฉ","๏ผช","๏ผซ","๏ผฌ","๏ผญ","๏ผฎ","๏ผฏ","๏ผฐ","๏ผฑ","๏ผฒ","๏ผณ","๏ผด","๏ผต","๏ผถ","๏ผท","๏ผธ","๏ผน","๏ผบ"],
["๐ฐ","๐ฑ","๐ฒ","๐ณ","๐ด","๐ต","๐ถ","๐ท","๐ธ","๐น","๐บ","๐ป","๐ผ","๐ฝ","๐พ","๐ฟ","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐"],
["โถ","โท","โธ","โน","โบ","โป","โผ","โฝ","โพ","โฟ","โ","โ","โ","โ","โ","โ","โ","โ","โ","โ","โ","โ","โ","โ","โ","โ"],
["แดฌ","แดฎ","แถ","แดฐ","แดฑ","แถ ","แดณ","แดด","แดต","แดถ","แดท","แดธ","แดน","แดบ","แดผ","แดพ","Q","แดฟ","หข","แต","แต","โฑฝ","แต","หฃ","สธ","แถป"],
['แด','ส','แด','แด','แด','๊ฐ','ษข','ส','ษช','แด','แด','ส','แด','ษด','แด','แด','Q','ส','๊ฑ','แด','แด','แด ','แดก','x','ส','แดข'],
["โ","B","C","D","โ","F","G","โ","แตข","โฑผ","โ","โ","โ","โ","โ","โ","Q","แตฃ","โ","โ","แตค","แตฅ","W","โ","Y","Z"],
["๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐"],
["๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐","๐ ","๐ก","๐ข","๐ฃ","๐ค","๐ฅ","๐ฆ","๐ง","๐จ","๐ฉ","๐ช","๐ซ","๐ฌ","๐ญ"],
["ๅ","ไน","ๅ","แช","ไน","ๅ","แถ","ๅ","ไธจ","๏พ","า","ใฅ","็ช","ๅ ","ใ","ๅฉ","ษ","ๅฐบ","ไธ","ใ","ใฉ","แฏ","ๅฑฑ","ไน","ใ","ไน"],
["Aา","Bา","Cา","Dา","Eา","Fา","Gา","Hา","Iา","Jา","Kา","Lา","Mา","Nา","Oา","Pา","Qา","Rา","Sา","Tา","Uา","Vา","Wา","Xา","Yา","Zา"]]
Orgtarikh = ["/","0","1","2","3","4","5","6","7","8","9"]
ftarikh = [['/','โฐ','ยน','ยฒ','ยณ','โด','โต','โถ','โท','โธ','โน']]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.qqxnxx.com',
    'Origin': 'http://www.qqxnxx.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'
}
url = 'http://www.qqxnxx.com/download.php'

one = ["ฺฉ?ุฑู ุชู ุฎุงุฑุช", "ุจุต?ฺฉ ุจฺู ฺฉูู?", "ุจุง? ุจุฏู ููู ูพูู?", "ฺฉ?ุฑู ุชู ููุช ุงูุจ?", "ูฺฏุงูุช ฺฉุต ููู ", "ฺฉุต ููู ูพุฑุฏู ุงุฑุชุฌุงุน?ุช", "ููุชู ุดุจ? ฺูุฏ ู?ุฏ?ุ", "ุฎุงุฑุชู ุจุง ุฑูุบู ุฌุงูุฏ ฺฏุง??ุฏู", "ฺฉุต ุขุจุฌ?ุช ", "ุฒูุง ุฒุงุฏุน ", "ููู ุฎ?ุงุจูู?", "ฺฏ? ููู", "ุขุจู ูุง ฺฉุต ููุช ฺุฌูุฑ? ู?ุดู", "ุจุงูุง ุจุงุด ููู ฺฉ?ุฑ ุฏุฒุฏ", "ููุช ูุฌูุณ? ู?ุฒููุฺฉุตุตุตุต ููุช ุฌูููููู", "ููู ุฌุฑ?ุฏู", "ฺฏ? ูพุฏุฑ ุฒูุง ุฒุงุฏุน ", "ููุชู ฺฉุฑุง?ู ู?ุฏ?ุ", "ุดู ููู ุจุงูุง ุจุงุด", "ุฎุงุฑฺฉุตุฏู ุจู ููุช ุจฺฏู ุฑู ฺฉ?ุฑู ุฎูุด ู?ฺฏุฐุฑูุ", "ููู ุชููู ฺฉุต ููุชู ุฌุฑ ู?ุฏู", "ุจ?ุง ููุชู ุจุจุฑ ุฒุฎูุด ฺฉุฑุฏู", "ฺฉุต ููุชู ุจุฒุงุฑู ?ฺฉู ุจุฎูุฏ?ู", "ุจู ููุช ุจฺฏู ุจ?ุงุฏ ูุงุณู ูพุฑ ุชูู ุจุฒูู ุฎุฑุฌุชููู ุจุฏู ?ุช?ู", "ููุฌ ุช?ุฒ ุจุงุด ููุชู ุจ?ุงุฑ", "ููุช ูพุฑ ุชูู ู?ุฒู? ุจุงุจุงุช ุดูุ", "ุงูุจ ฺฉูู? ุจุฒู ุจู ฺุงฺฉ ุชุง ููุชู ุฌููุช ุญุงููู ูฺฉุฑุฏูููู ฺฉูู ุทูุง ุจ?ุง ุจุงูุง", "?ุช?ู ุจ?ุง ุจุบูู ", "ููุช ฺฏูฺฏ ุจูฺฏ ุฏูุณ ุฏุงุฑูุ", "ุจ?ุง ุจฺฏุงูุช ุดุงุฏ ุด? ุฎุงุฑ ฺฉุตุฏู", "ฺฉ?ุฑู ุชู ฺฉุต ููุช ุจฺฏู ุจุงุดู", "ุฏุงุฏุงุด ุฏูุณ ุฏุงุฑ? ?ุง ุขุจุฌ? ููู ูพูู?", "?ต?ฐ ู?ุฏู ููุชู ุจุฏูฺฉ?ุฑู ฺฉุต ุขุจุฌ? ฺฉุต ุทูุงุงุงุงุช", "ููู ูพูู? ฺูุฏ ุณุงูุช ุฏูุณ ุฏุงุฑ?ุ", "ุฏุณุช ู ูพุง ูุฒู ููู ฺฉุต ฺฏุดุงุฏ", "ููู ุณุงฺฉุฑ ูู?ุช ู?ุฎูุง?ุ", "ฺฉ?ุฑ ุณฺฏุง ุชู ฺฉุต ุขุจุฌ?ุช ", "ุงุฒ ููุช ุจูพุฑุณ ุขุจ ฺฉ?ุฑ ูพุฑุชูุงู? ุฏูุณ ุฏุงุฑูุ", "ูพุณุชูู ููุช ฺูุฏู", "ุชุฎุฎุฎุฎ ุจ?ุง ุจุงูุง ุงุฏุจ?", "ูุงุฏุฑุช ุฏุณุชู ูพุง ู?ุฒูู ุฒ?ุฑู", "ููู ุณฺฉุณ? ุจ?ุง ?ู ุณุงฺฉ ุจุฒู ุจุฎูุฏ?ู", "ุฎู?ู? ุงููุฏ ุฌุงุฏู ุฏูุงุชุชููู ุขุณูุงูุช ฺฉุฑุฏ ุงููุฏ?ุฏ ุดูุฑ ู ฺฏุฑูู ููุช ฺฉุฌุง ฺฉุต ู?ุฏุงุฏุ", "ฺฏุต ฺฉุด", "ฺฉุณ ููู", "ฺฉุต ููุช", "ฺฉุณ ุฎูุงูุฑ", "ฺฉุณ ุฎูุงุฑ", "ฺฉุณ ุฎุงุฑุช", "ฺฉุณ ุงุจุฌ?ุช", "ฺฉุต ู?ุณ", "ุณุงฺฉ ุจุฒู", "ุณุงฺฉ ูุฌูุณ?", "ููู ุงูฺฉุณ?ุณ", "ูู ุงูฺฉุณ?ุณ", "ูุงููุณุชู ฺฏุง??ุฏู", "ููู ุฒูุง", "ฺฉุณ ุฎู", "ฺฉุณ ูุฎ", "ฺฉุณ ูุบุฒ", "ฺฉุณ ูุบุฐ", "ุฎูุงุฑฺฉุณ", "ุฎูุงุฑ ฺฉุณ", "ุฎูุงูุฑฺฉุณ", "ุฎูุงูุฑ ฺฉุณ", "ุญุฑูู ุฒุงุฏู", "ุญุฑููุฒุงุฏู", "ุฎุงุฑ ฺฉุณ", "ุชุฎู ุณฺฏ", "ูพุฏุฑ ุณฺฏ", "ูพุฏุฑุณฺฏ", "ูพุฏุฑ ุตฺฏ", "ูพุฏุฑุตฺฏ", "ููู ุณฺฏ", "ูู ุณฺฏ", "ูู ุตฺฏ", "ููู ุตฺฏ", "ููู ุฎุฑุงุจ", "ุชุฎุฎุฎุฎุฎุฎุฎุฎุฎ", "ูู ุฎุฑุงุจ", "ูุงุฏุฑ ุณฺฏ", "ูุงุฏุฑ ุฎุฑุงุจ", "ูุงุฏุฑุชู ฺฏุง??ุฏู", "ุชุฎู ุฌู", "ุชุฎู ุณฺฏ", "ูุงุฏุฑุชู ฺฏุง??ุฏู", "ููู ุญููู?", "ูู ุญููู?", "ูู ฺฏุดุงุฏ", "ููู ฺฏุดุงุฏ", "ูู ุฎุง?ู ุฎูุฑ", "ุชุฎุฎุฎุฎุฎุฎุฎุฎุฎ", "ูู ููู", "ฺฉุณ ุนูุช", "ฺฉุณ ฺฉุด", "ฺฉุณ ุจ?ุจ?ุช", "ฺฉุต ุนูุช", "ฺฉุต ุฎุงูุช", "ฺฉุณ ุจุงุจุง", "ฺฉุณ ุฎุฑ", "ฺฉุณ ฺฉูู", "ฺฉุณ ูุงู?ุช", "ฺฉุณ ูุงุฏุฑู", "ูุงุฏุฑ ฺฉุณุฏู", "ุฎูุงุฑ ฺฉุณุฏู", "ุชุฎุฎุฎุฎุฎุฎุฎุฎุฎ", "ููู ฺฉุณ", "ุจ?ูุงููุณ", "ุจ? ูุงููุณ", "ุดู ูุงููุณ", "ุณฺฏ ูุงููุณ", "ููู ุฌูุฏุชู ฺฏุง??ุฏู ุจุงู ", "ฺฺฺฺ ูฺฏุง??ุฏู ุณ?ฺฉ ฺฉู ูพู?ุฒ D:", "ููู ุญููู?", "ฺฺฺฺฺฺฺ", "ูุฒ ููุน", "ููู ุงูฺฉุณ?ุณ", "ฺฉุต ููุช", "ุจุงูุง ุจุงุด", "ููุช ุฑู ู?ฺฏุงู", "ฺฉ?ุฑู ุงุฒ ูพููุง ุชู ฺฉุต ููุช", "ูุงุฏุฑ ฺฉ?ุฑ ุฏุฒุฏ", "ููุน ุญุฑูู?", "ุชููู ุชู ฺฉุต ููุช", "ฺฉ?ุฑ ุชฺฉ ุชฺฉ ุจฺฉุณ ุชูุน ฺฏูุฏ ุชู ฺฉุต ููุช", "ฺฉุต ุฎูุงุฑ ุจุฏุฎูุงู", "ุฎูุงุฑ ฺฉุตุฏู", "ููุน ุจุงุทู", "ุญุฑูู ูููุน", "ููู ุณฺฏ ูุงููุณ", "ููู ููุช ุดูุง ููู ฺฺฺฺ", "ููู ฺฉ?ุฑ ูุงูพ ุฒู", "ููุน ุงูุจ?", "ููู ฺฉ?ุฑ ุฏุฒุฏ", "ููู ฺฉ?ูู?", "ููู ฺฉุตูพุงุฑู", "ุฒูุง ุฒุงุฏุน", "ฺฉ?ุฑ ุณฺฏ ุชู ฺฉุต ูุชุช ูพุฎุฎุฎ", "ููุฏ ุฒูุง", "ููู ุฎ?ุงุจูู?", "ู?ุณ ุจุน ฺฉุณ ุญุณุงุณ?ุช ุฏุงุฑู", "ฺฉุต ูฺฏู ููู ุณฺฏ ฺฉู ู?ฺฉููุชุชุงุงุงุง", "ฺฉุต ูู ุฌูุฏุช", "ููู ุณฺฏ", "ููู ฺฉูู?", "ููู ุฒ?ุฑุงุจ?", "ุจฺฉู ููุชู", "ููุน ูุงุณุฏ", "ููู ุณุงฺฉุฑ", "ฺฉุณ ููุน ุจุฏุฎูุงู", "ูฺฏุง??ุฏู", "ูุงุฏุฑ ุณฺฏ", "ููุน ุดุฑุท?", "ฺฏ? ููุน", "ุจุงุจุงุช ุดุงุด?ุฏุชุช ฺฺฺฺฺฺ", "ููู ูุงูุฑ", "ุญุฑููุฒุงุฏู", "ููู ฺฉุต", "ฺฉุต ููุช ุจุงู", "ูพุฏุฑ ุณฺฏ", "ุณ?ฺฉ ฺฉู ฺฉุต ููุช ูุจ?ููุช", "ฺฉููุฏู", "ููู ููู", "ููู ุณฺฏ", "ูุงุฏุฑ ุฌูุฏู", "ฺฉุต ฺฉูพฺฉ ุฒุฏุน", "ููุน ููฺฏ?", "ููู ุฎ?ุฑุงุช?", "ุณุฌุฏู ฺฉู ุณฺฏ ููุน", "ููู ุฎ?ุงุจูู?", "ููู ฺฉุงุฑุชูู?", "ุชฺฉุฑุงุฑ ู?ฺฉูู ฺฉุต ููุช", "ุชูฺฏุฑุงู ุชู ฺฉุณ ููุช", "ฺฉุต ุฎูุงุฑุช", "ุฎูุงุฑ ฺฉ?ูู?", "ูพุง ุจุฒู ฺฺฺฺฺ", "ูุงุฏุฑุชู ฺฏุง??ุฏู", "ฺฏูุฒ ููุน", "ฺฉ?ุฑู ุชู ุฏูู ููุช", "ููุน ููฺฏุงู?", "ฺฉ?ุฑู ุชู ฺฉุต ุฒ?ุฏุช", "ฺฉ?ุฑ ุชู ูููุง? ุงุจุฌ?ุช", "ุงุจุฌ? ุณฺฏ", "ฺฉุณ ุฏุณุช ุฑ?ุฏ? ุจุง ุชุง?ูพ ฺฉุฑุฏูุช ฺฺฺ", "ุงุจุฌ? ุฌูุฏู", "ููุน ุณฺฏ ุณ?ุจ?ู", "ุจุฏู ุจฺฉู?ู ฺฺฺฺ", "ฺฉุต ูุงููุณ", "ุดู ูุงููุณ", "ุฑ?ุฏู ูพุณ ฺฉูุช ฺฺฺฺฺ", "ููู ุดู", "ููุน ูุณุท?", "ููู ูู", "ุฏุณุช ู ูพุง ูุฒู ฺฉุณ ููุน", "ููู ููู", "ุฎูุงุฑุชู ฺฏุง??ุฏู", "ูุญู?!ุ", "ููุช ุฎูุจุน!ุ", "ฺฉุณ ุฒูุช", "ุดุงุด ููุน", "ููู ุญ?ุงุท? \\\\\/:", "ูู ุบุณู?", "ฺฉ?ุฑู ุชู ฺฉุณ ููุช ุจฺฏู ูุฑุณ? ฺฺฺฺ", "ุงุจู ุชู ฺฉุต ููุช :\\\\\/", "ูุงฺฉ ?ูุฑ ูุงุฏุฑ ุฎูุงุฑ ุณฺฏ ูพุฎุฎุฎ", "ฺฉ?ุฑ ุณฺฏ ุชู ฺฉุต ููุช", "ฺฉุต ุฒู", "ููู ูุฑุงุฑ?", "ุจฺฉู ููุชู ูู ุจุงู ุฌูุน ฺฉู ููู ุฌูุฏู \\\\\/:::", "ููู ุฌูุฏู ุจ?ุง ูุงุณู ุณุงฺฉ ุจุฒู", "ุญุฑู ูุฒู ฺฉู ูฺฉููุช ูุงุงุง :|", "ฺฉ?ุฑ ุชู ฺฉุต ููุช๐", "ฺฉุต ฺฉุต ฺฉุต ููุช", "ฺฉุตุตุตุต ููุช ุฌูููู", "ุณฺฏ ููุน", "ฺฉุต ุฎูุงุฑุช", "ฺฉ?ุฑ? ู?ุณ", "ฺฉูุน ฺฉ?ุฑ?", "ุช?ุฒ ุจุงุด ุณ?ฺฉ ฺฉู ูุจ?ููุช", "ููุฌ ุช?ุฒ ุจุงุด ฺฺฺ", "ุจ?ุง ููุชู ุจุจุฑ", "ุจฺฉู ููุชู ุจุงู ", "ฺฉ?ุฑู ุชู ุจุฏุฎูุงู", "ฺฺฺฺฺฺฺ", "ููู ุฌูุฏู", "ููู ฺฉุต ุทูุง", "ููู ฺฉูู ุทูุง", "ฺฉุณ ููุช ุจุฒุงุฑู ุจุฎูุฏ?ู!ุ", "ฺฉ?ุฑู ุฏููุช", "ูุงุฏุฑ ุฎุฑุงุจ", "ููู ฺฉูู?", "ูุฑ ฺ? ฺฏูุช? ุชู ฺฉุต ููุช ุฎุฎุฎุฎุฎุฎุฎ", "ฺฉุต ูุงููุณุช ุจุง?", "ฺฉุต ููุช ุจุง? :\\\\\/\\\\\/", "ฺฉุต ูุงููุณุช ุจุงุน? ุชุฎุฎุฎุฎุฎ", "ฺฉูู ฺฏูุงุจ?!", "ุฑ?ุฏ? ุขุจ ูุทุน", "ฺฉุต ฺฉู ููุชู ฺฉุน", "ูู ฺฉูู?", "ูู ุฎูุดูุฒู", "ููู ููุณ", " ูู ?ู ฺุดู ", "ููู ฺุงูุงู", "ููู ุฌ?ูุฏู", "ููู ุญุฑุต? ", "ูู ูุด?", "ููู ุณุงฺฉุฑ", "ูู ุชุฎู?", "ููู ุจ? ูู?ุช", "ูู ฺฉุณ", "ูู ุณฺฉุณ?", "ูู ูุฑุงุฑ?", "ูุด ููู", "ุณฺฏ ููู", "ุดู ููู", "ููู ุชุฎู?", "ููู ุชููู?", "ููู ฺฉููู", "ูู ุฎุดฺฏู", "ูู ุฌูุฏู", "ูู ูู ", "ูู ุณฺฉุณ?", "ูู ูุด", "ฺฉุณ ูู ", "ูู ฺฉูู", "ูู ุฑุง?ฺฏุงู", "ูู ุฎุงุฑุฏุงุฑ", "ููู ฺฉ?ุฑ ุณูุงุฑ", "ูู ูพู?ูุฒ", "ูู ูุญู?", "ููู ุจฺฏุง??", "ููู ุจูุจ?", "ููู ุงูฺฉุณ?ุณ", "ูู ุฎ?ุงุจูู?", "ูู ุนู?", "ูู ุณุงูพูุฑุช?", "ูู ูุงุดุฎูุฑ", "ููู ุทูุง", "ููู ุนููู?", "ููู ูุฑ ุฌุง??", "ูู ุฏ?ูุซ", "ุชุฎุฎุฎุฎุฎุฎุฎุฎุฎ", "ูู ุฑ?ุฏู?", "ูู ุจ? ูุฌูุฏ", "ููู ุณ?ฺฉ?", "ููู ฺฉ??ุฑ", "ูู ฺฏุดุงุฏ", "ูู ูพูู?", "ูู ูู", "ูู ูุฑุฒู", "ููู ูุงุด? ฺฉ?ุฑ?", "ููู ู?ูุฏูุฒ?", "ูู ุชุง?ูพ?", "ูู ุจุฑู?", "ูู ุดุงุด?", "ููู ุฏุฑุงุฒ?", "ุดู ููุน", "?ฺฉู ููุชู ฺฉู", "ฺฉุณ ุฎูุงุฑ ุจุฏุฎูุงู", "ุขุจ ฺุงูุงู", "ููู ุฌุฑ?ุฏู", "ููู ุณฺฏ ุณู?ุฏ", "ุขุจ ฺฉูู", "ููู 85", "ููู ุณููพุฑ?", "ุจุฎูุฑุด", "ฺฉุณ ู", "ุฎูุงุฑุชู ฺฏุง??ุฏู", "ุฎุงุฑฺฉุณุฏู", "ฺฏ? ูพุฏุฑ", "ุขุจ ฺุงูุงู", "ุฒูุง ุฒุงุฏู", "ุฒู ุฌูุฏู", "ุณฺฏ ูพุฏุฑ", "ูุงุฏุฑ ุฌูุฏู", "ููุน ฺฉ?ุฑ ุฎูุฑ", "ฺฺฺฺฺ", "ุช?ุฒ ุจุงูุง", "ููู ุณฺฏู ุจุง ฺฉุณุดุฑ ุฏุฑ ู?ุฑู", "ฺฉ?ุฑ ุณฺฏ ุชู ฺฉุต ููุช", "kos kesh", "kir", "kiri", "nane lashi", "kos", "kharet", "blis kirmo", "ุงูุจ? ฺฉูู? ูุฑุฒู", "ฺฉ?ุฑู ูุง ฺฉุต ุฎุงุฑุช", "ฺฉ?ุฑ?", "ููู ูุงุด?", "ููู", "ฺฉุต", "ฺฉ?ุฑ", "ุจ? ุฎุง?ู", "ููู ูุด", "ุจ? ูพุฏุฑูุงุฏุฑ", "ุฎุงุฑฺฉุตุฏู", "ูุงุฏุฑ ุฌูุฏู", "ฺฉุตฺฉุด", "ฺฉ?ุฑู ฺฉูู ูุงุฏุฑุช", "ุจุงูุง ุจุงุด ฺฉ?ุฑู ฺฉุต ูุงุฏุฑุช", "ูุงุฏุฑุชู ู?ฺฏุงู ููฺู ุฌูู ุจุงูุง??", "ุงุจ ุฎุงุฑฺฉุตุชู ุชูุฏ ุชูุฏ ุชุง?ูพ ฺฉู ุจุจ?ูู", "ูุงุฏุฑุชู ู?ฺฏุงู ุจุฎุง? ูุฑุงุฑ ฺฉู?", "ูุงู ุดู", "ฺฉ?ุฑู ุชู ุฎุงุฑุช", "ุจุต?ฺฉ ุจฺู ฺฉูู?", "ุจุง? ุจุฏู ููู ูพูู?", "ฺฉ?ุฑู ุชู ููุช ุงูุจ?", "ูฺฏุงูุช ฺฉุต ููู ", "ฺฉุต ููู ูพุฑุฏู ุงุฑุชุฌุงุน?ุช", "ููุชู ุดุจ? ฺูุฏ ู?ุฏ?ุ", "ุฎุงุฑุชู ุจุง ุฑูุบู ุฌุงูุฏ ฺฏุง??ุฏู", "ฺฉุต ุขุจุฌ?ุช ", "ุฒูุง ุฒุงุฏุน ", "ููู ุฎ?ุงุจูู?", "ฺฏ? ููู", "ุขุจู ูุง ฺฉุต ููุช ฺุฌูุฑ? ู?ุดู", "ุจุงูุง ุจุงุด ููู ฺฉ?ุฑ ุฏุฒุฏ", "ููุช ูุฌูุณ? ู?ุฒููุ", "ฺฉุตุตุตุต ููุช ุฌูููููู", "ููู ุฌุฑ?ุฏู", "ฺฏ? ูพุฏุฑ ุฒูุง ุฒุงุฏุน ", "ููุชู ฺฉุฑุง?ู ู?ุฏ?ุ", "ุดู ููู ุจุงูุง ุจุงุด", "ุฎุงุฑฺฉุตุฏู ุจู ููุช ุจฺฏู ุฑู ฺฉ?ุฑู ุฎูุด ู?ฺฏุฐุฑูุ", "ููู ุชููู ฺฉุต ููุชู ุฌุฑ ู?ุฏู", "ุจ?ุง ููุชู ุจุจุฑ ุฒุฎูุด ฺฉุฑุฏู", "ฺฉุต ููุชู ุจุฒุงุฑู ?ฺฉู ุจุฎูุฏ?ู", "ุจู ููุช ุจฺฏู ุจ?ุงุฏ ูุงุณู ูพุฑ ุชูู ุจุฒูู ุฎุฑุฌุชููู ุจุฏู ?ุช?ู", "ููู ฺฉูู ุทูุง ุจ?ุง ุจุงูุง", "?ุช?ู ุจ?ุง ุจุบูู ", "ููุช ฺฏูฺฏ ุจูฺฏ ุฏูุณ ุฏุงุฑูุ", "ุจ?ุง ุจฺฏุงูุช ุดุงุฏ ุด? ุฎุงุฑ ฺฉุตุฏู", "ฺฉ?ุฑู ุชู ฺฉุต ููุช ุจฺฏู ุจุงุดู", "ุฏุงุฏุงุด ุฏูุณ ุฏุงุฑ? ?ุง ุขุจุฌ? ููู ูพูู?", "?ต?ฐ ู?ุฏู ููุชู ุจุฏู", "ููุฌ ุช?ุฒ ุจุงุด ููุชู ุจ?ุงุฑ", "ฺฉ?ุฑู ฺฉุต ุขุจุฌ? ฺฉุต ุทูุงุงุงุงุช", "ููู ูพูู? ฺูุฏ ุณุงูุช ุฏูุณ ุฏุงุฑ?ุ", "ุฏุณุช ู ูพุง ูุฒู ููู ฺฉุต ฺฏุดุงุฏ", "ููู ุณุงฺฉุฑ ูู?ุช ู?ุฎูุง?ุ", "ฺฉ?ุฑ ุณฺฏุง ุชู ฺฉุต ุขุจุฌ?ุช ", "ุงุฒ ููุช ุจูพุฑุณ ุขุจ ฺฉ?ุฑ ูพุฑุชูุงู? ุฏูุณ ุฏุงุฑูุ", "ูพุณุชูู ููุช ฺูุฏู", "ุชุฎุฎุฎุฎ ุจ?ุง ุจุงูุง ุงุฏุจ?", "ูุงุฏุฑุช ุฏุณุชู ูพุง ู?ุฒูู ุฒ?ุฑู", "ููู ุณฺฉุณ? ุจ?ุง ?ู ุณุงฺฉ ุจุฒู ุจุฎูุฏ?ู", "ุฎู?ู? ุงููุฏ ุฌุงุฏู ุฏูุงุชุชููู ุขุณูุงูุช ฺฉุฑุฏ ุงููุฏ?ุฏ ุดูุฑ ู ฺฏุฑูู ููุช ฺฉุฌุง ฺฉุต ู?ุฏุงุฏุ", "ฺฉ?ุฑู ุชุง ุชู ู ุงุฒ ูพููุง ุชู ฺฉุต ูุงุฏุฑุช", "ฺฉุต ูุงููุณ ูุงุฏุฑุช", "ูุงุฏุฑ ฺฉุต ูพุงูพ?ูู? ", "ูุงุฏุฑ ุฌูุฏู ุญุฑูู ุชุฎู?", "ุงูุจ? ุฒุงุฏู ุญู?ุฑ", "ุจุงุจุงุช ุฒ?ุฑ ฺฉ?ุฑู ุจุฒุฑฺฏ ุดุฏ", "ุงุณูู ุฑู ฺฉูู ูุงุฏุฑุช ุชุชู ุดุฏู", "ุฎ?ุฎ?ุฎ?ุฎ?ุฎ?", "ฺฺฺฺฺฺฺฺ", "ุฒุฌู ุจุฒู ูุงููุณ ฺฏูุงุจ?", "ูุงุฏุฑุช ฺฉ?ุฑูู ", "ุจุงุจุงุช ููู ", "ุชุฎู ุณฺฏ ุญุฑูู ุฒุงุฏู ", "ฺฉุต ูุงููุณุช ", "ุฎูุงูุฑุชู ฺฏุง??ุฏู", "ุฑ?ุฏู ุจูุช ุจ?ุดุนูุฑ", " ุจ? ุดุฑู", " ุฑ?ุฏู ุชู ูุบุฒุช", " ุจ? ุงุฑุฒุด", " ฺฉุตฺฉุด", " ุฑ?ุฏู ุชู? ูุงููุณุช", " ุจ? ูุงููุณ", " ูุงุฏุฑุฌูุฏู", " ุฎูุงูุฑ ฺฉุตฺฉุด", " ุฑ?ุฏู ุชู? ฺฉู ุทุง?ูุช", " ุจ? ูุงููุณ ุจุฑู", " ุฎูุดู ุงุฒุช ูู?ุงุฏ ฺฉุตฺฉุด", " ุชู ฺฉุตฺฉุด?", " ุจุฑู ุฎูุงูุฑ ุฌูุฏู", "ุจุฑู ูุงุฏุฑุฌูุฏู", " ุจุฑู ุจุฑุงุฏุฑ ฺฉูู?", " ฺฉููฺฉุด", "ุนูุถ ุจ? ูุงููุณ", "ุฑ?ุฏู ุชู ูุจุฑ ูุงุฏุฑุช", "ุฑ?ุฏู ุชู ูุจุฑ ูพุฏุฑุช", " ุฑ?ุฏู ุชู ูุจุฑุช", " ุฑ?ุฏู ุชู ุฒุงุชุช", " ุฑ?ุฏู ุชู ุฎูุงูุฑ ุฌูุฏู", " ุฎูุงูุฑ ุฌูุฏุช ุฎูุจู", " ูุงุฏุฑ ุฌูุฏุช ุฎูุจู", " ูพุฏุฑ ฺฉููฺฉุดุช ุฎูุจู", "ุจุฑุงุฏุฑ ฺฉูู?ุช ุฎูุจ", " ูพุฏุฑุณฺฏ", " ูุงุฏุฑ ุณฺฏ", " ุจุฑุงุฏุฑ ุณฺฏ", " ุฎูุงูุฑ ุณฺฏ", " ุฎูุงูุฑ ุฌูุฏุช ฺ?", " ูุงุฏุฑ ุฌูุฏุช ฺ?", " ูพุฏุฑ ฺฉูู?ุช ฺ?", " ุจุฑุงุฏุฑ ฺฉูู?ุช ฺ?", " ุงุฑู ุฌูุฏู ูุง", " ุชู ุฌูุฏู ุง?", " ุชู ฺฉูู? ุง?", " ุชู? ฺฉุตฺฉุด?", " ุฎูุดู ุงุฒ ุฌูุฏู ูุง ูู?ุงุฏ", " ุฎูุงูุฑุช ุฌูุฏู ุดุฏู", " ูุงุฏุฑุช ุฌูุฏู ุดุฏู", " ุฌูุฏู ุจุฑู ุฎูุฏุช ุฑู ุฌูุน ฺฉู", " ูุงูุงูุช ุงูุดุจ ุฑู? ฺฉ? ูุณุชุด", " ุฎูุงูุฑุช ูพ?ุด ฺฉ?ู", " ุจุฑุงุฏุฑุช ุฏุงุฑู ฺฉุฌุง ฺฉูู ู?ุฏู", " ุจุงุจุง? ูุฑูุณุงูุช ฺฉู", " ุฎูุงูุฑุช ุงูุดุจ ุฑู? ฺฉ? ูุณุชุด", " ูุงุฏุฑุช ุงูุดุจ ุฑู? ฺฉ? ุฎูุงุจ?ุฏู", "ููุช ูพุฑ ุชูู ู?ุฒู? ุจุงุจุงุช ุดูุ", "ุงูุจ ฺฉูู? ุจุฒู ุจู ฺุงฺฉ ุชุง ููุชู ุฌููุช ุญุงููู ูฺฉุฑุฏู", " ุฑ?ุฏู ุจูุช", " ุจ?ุดุนูุฑ", " ุจ? ุดุฑู", " ุฑ?ุฏู ุชู ูุบุฒุช", " ุจ? ุงุฑุฒุด", " ฺฉุตฺฉุด", " ุฑ?ุฏู ุชู? ูุงููุณุช", " ุจ? ูุงููุณ", " ูุงุฏุฑุฌูุฏู", " ุฎูุงูุฑ ฺฉุตฺฉุด", " ุฑ?ุฏู ุชู? ฺฉู ุทุง?ูุช", " ุจ? ูุงููุณ ุจุฑู", " ุฎูุดู ุงุฒุช ูู?ุงุฏ ฺฉุตฺฉุด", " ุชู ฺฉุตฺฉุด?", " ุจุฑู ุฎูุงูุฑ ุฌูุฏู", " ุจุฑู ูุงุฏุฑุฌูุฏู", " ุจุฑู ุจุฑุงุฏุฑ ฺฉูู?", " ฺฉููฺฉุด", " ุนูุถ ุจ? ูุงููุณ", " ุฑ?ุฏู ุชู ูุจุฑ ูุงุฏุฑุช", " ุฑ?ุฏู ุชู ูุจุฑ ูพุฏุฑุช", " ุฑ?ุฏู ุชู ูุจุฑุช", " ุฑ?ุฏู ุชู ุฒุงุชุช", " ุฑ?ุฏู ุชู ุฎูุงูุฑ ุฌูุฏู", " ุฎูุงูุฑ ุฌูุฏุช ุฎูุจู", " ูุงุฏุฑ ุฌูุฏุช ุฎูุจู", " ูพุฏุฑ ฺฉููฺฉุดุช ุฎูุจู", " ุจุฑุงุฏุฑ ฺฉูู?ุช ุฎูุจ", " ูพุฏุฑุณฺฏ", " ูุงุฏุฑ ุณฺฏ", " ุจุฑุงุฏุฑ ุณฺฏ", " ุฎูุงูุฑ ุณฺฏ", " ุฎูุงูุฑ ุฌูุฏุช ฺ?", " ูุงุฏุฑ ุฌูุฏุช ฺ?", " ูพุฏุฑ ฺฉูู?ุช ฺ?", " ุจุฑุงุฏุฑ ฺฉูู?ุช ฺ?", " ุงุฑู ุฌูุฏู ูุง", " ุชู ุฌูุฏู ุง?", " ุชู ฺฉูู? ุง?", " ุชู? ฺฉุตฺฉุด?", " ุฎูุดู ุงุฒ ุฌูุฏู ูุง ูู?ุงุฏ", " ุฎูุงูุฑุช ุฌูุฏู ุดุฏู", " ูุงุฏุฑุช ุฌูุฏู ุดุฏู", " ุฌูุฏู ุจุฑู ุฎูุฏุช ุฑู ุฌูุน ฺฉู", " ูุงูุงูุช ุงูุดุจ ุฑู? ฺฉ? ูุณุชุด", " ุฎูุงูุฑุช ูพ?ุด ฺฉ?ู", " ุจุฑุงุฏุฑุช ุฏุงุฑู ฺฉุฌุง ฺฉูู ู?ุฏู", " ุจุงุจุง? ูุฑูุณุงูุช ฺฉู", " ุฎูุงูุฑุช ุงูุดุจ ุฑู? ฺฉ? ูุณุชุด", " ูุงุฏุฑุช ุงูุดุจ ุฑู? ฺฉ? ุฎูุงุจ?ุฏู", "ฺฉ?ุฑู ฺฉูู ูุงุฏุฑุช", "ุจุงูุง ุจุงุด ฺฉ?ุฑู ฺฉุต ูุงุฏุฑุช", "ูุงุฏุฑุชู ู?ฺฏุงู ููฺู ุฌูู ุจุงูุง", "ุงุจ ุฎุงุฑฺฉุตุชู ุชูุฏ ุชูุฏ ุชุง?ูพ ฺฉู ุจุจ?ูู", "ูุงุฏุฑุชู ู?ฺฏุงู ุจุฎุง? ูุฑุงุฑ ฺฉู?", "ูุงู ุดู ุฏ?ฺฏู ููฺู", "ูุงุฏุฑุชู ู?ฺฏุงู ุงู ุจุด?", "ฺฉ?ุฑู ฺฉูู ูุงุฏุฑุช", "ฺฉ?ุฑู ฺฉุต ูุต ูุงุฏุฑุช ุจุงูุง", "ฺฉ?ุฑู ุชู ฺุดู ฺุงู ูุงุฏุฑุช", "ฺฉูู ูุงุฏุฑุชู ู?ฺฏุงู ุจุงูุง", "ุจ?ูุงููุณ  ุฎุณุชู ุดุฏ?ุ", "ูุจ?ูู ุฎุณุชู ุจุด? ุจ?ูุงููุณ", "ููุชู ู?ฺฉูู", "ฺฉ?ุฑู ฺฉูู ูุงุฏุฑุช ", "ุตูู ุชู ฺฉุตููุช ุจุงูุง", "ุจ?ูุงููุณ ุจุงูุง ุจุงุด ุจูุช ู?ฺฏู", "ฺฉ?ุฑ ุชู ูุงุฏุฑุช", "ฺฉุต ูุต ูุงุฏุฑุชู ุจู?ุณูุ", "ฺฉุต ูุงุฏุฑุชู ฺูฺฏ ุจุฒููุ", "ุจู ุฎุฏุง ฺฉุตููุช ุจุงูุง ", "ูุงุฏุฑุชู ู?ฺฏุงู ", "ฺฉ?ุฑู ฺฉูู ูุงุฏุฑุช ุจ?ูุงููุณ", "ูุงุฏุฑุฌูุฏู ุจุงูุง ุจุงุด", "ุจ?ูุงููุณ ุชุง ฺฉ? ู?ุฎุง? ุณุทุญุช ฺฏุญ ุจุงุดู", "ุงูพุฏ?ุช ุดู ุจ?ูุงููุณ ุฎุฒ ุจูุฏ", "ฺฉ?ุฑู ุงุฒ ูพููุง ุชู ููุช", "ู ุงูุง ุชู ุจ?ูุงููุณ ฺููุด", "ุชู ?ฺฉ?ู ูุงุฏุฑุชู ู?ฺฉูู", "ฺฉ?ุฑู ุชู ูุงููุตุช ", "ฺฉ?ุฑ ุชู ููุช", "ุฑ?ุด ุฑูุญุงู? ุชู ููุช", "ฺฉ?ุฑ ุชู ูุงุฏุฑุช", "ฺฉุต ูุงุฏุฑุชู ูุฌุฑ ุจุฏู", "ุตูู ุชู ููุช", "ุจุงุช ุชู ููุช ", "ูุงูุงูุชู ู?ฺฉูู ุจุงูุง", "ฺฉ?ุฑ ุชุฑฺฉุง ุจู ูุงููุณุช", "ุณุทุญุดู ูฺฏุง", "ุชุง?ูพ ฺฉู ุจ?ูุงููุณ", "ุฎุดุงุจุ", "ฺฉ?ุฑู ฺฉูู ูุงุฏุฑุช ุจุงูุง", "ุจ?ูุงููุณ ูุจ?ูู ุฎุณุชู ุจุด?", "ูุงุฏุฑุชู ุจฺฏุงูุ", "ฺฏุญ ุชู ุณุทุญุช ุดุฑูุช ุฑู", "ุจ?ูุงููุณ ุดุฑูุชู ูุงุจูุฏ ฺฉุฑุฏู ?ู ฺฉุงุฑ? ฺฉู", "ูุง? ฺฉ?ุฑู ุชู ุณุทุญุช", "ุจ?ูุงููุณ ุฑูุงู? ุดุฏ?", "ุฑูุงู?ุช ฺฉุฑุฏูุง", "ูุงุฏุฑุชู ฺฉุฑุฏู ฺฉุงุฑ? ฺฉู", "ุชุง?ูพ ุชู ููุช", "ุจ?ูพุฏุฑ ุจุงูุง ุจุงุด", "ู ุงูุง ุชู ูุฑ ุฎุฑ", "ููุชู ู?ฺฉูู ุจุงูุง ุจุงุด", "ฺฉ?ุฑู ูุจ ูุงุฏุฑุช ุจุงูุง", "ฺุทูุฑู ุจุฒูู ูุตูุชู ฺฏุญ ฺฉูู", "ุฏุงุฑ? ุชุธุงูุฑ ู?ฺฉู? ุงุฑูู? ูู? ูุงุฏุฑุชู ฺฉูุต ฺฉุฑุฏู", "ูุงุฏุฑุชู ฺฉุฑุฏู ุจ?ุบ?ุฑุช", "ูุฑุฒู", "ูุง? ุฎุฏุง? ูู ุง?ูู ูฺฏุง", "ฺฉ?ุฑ ุชู ฺฉุตููุช", "ููุชู ุจู?ุณู", "ููู ูฺฏุง ุจ?ูุงููุณ", "ฺฉ?ุฑ ุชู ููุช ุจุณู ุฏ?ฺฏู", "ุฎุณุชู ุดุฏ?ุ", "ููุชู ู?ฺฉูู ุฎุณุชู ุจุด?", "ูุง? ุฏูู ฺฉูู ูุงุฏุฑุช ุจฺฏุงู", "ุงู ุดู ุงุญูู", "ุจ?ุดุฑู ุงู ุดู ุจูุช ู?ฺฏู", "ูุงูุงู ุฌูุฏู ุงู ุดู", "ฺฉุต ูุงูุงูุช ุงู ุดู", "ฺฉุต ูุด ูุง ูู ฺฉู ุง?ูุฌูุฑ? ุจฺฏูุ", "ุง? ุจ?ูุงููุณ ฺููุด", "ุฎุงุฑฺฉูุตุชู ุง? ูุง", "ูุงูุงูุชู ู?ฺฉูู ุงู ูุด?", "ฺฏุญ ุชู ููุช", "ุณุทุญ ?ู ฺฏุญ ุตูุชู", "ฺฏุญ ฺฉุฑุฏู ุชู ูุตูุชุง", "ฺู ุฑู?? ุฏุงุฑ? ุจ?ูุงููุณ", "ูุงููุณุชู ฺฉุฑุฏู", "ุฑู ฺฉุต ูุงุฏุฑุช ฺฉ?ุฑ ฺฉููุ", "ููฺู ุจุงูุง", "ฺฉ?ุฑู ุชู ูุงููุตุชุงุง", "?ุง ูุงุฏุฑุชู ู?ฺฏุงู ?ุง ุงู ู?ุด?", "ูุงูุดู ุฏ?ฺฏู", "ุจ?ูุงููุณ", "ูุงุฏุฑฺฉุตุชู", "ูุงููุต ฺฉุตุฏู", "ูุง? ุจุฏู ุจุจ?ูู ู?ุฑุณ?", "ฺฉ?ุฑู ฺฉูู ูุงุฏุฑุช ฺ?ฺฉุงุฑ ู?ฺฉู? ุงุฎู", "ุฎุงุฑฺฉุตุชู ุจุงูุง ุฏ?ฺฏู ุนู", "ฺฉ?ุฑู ฺฉุตูุงุฏุฑุช", "ฺฉ?ุฑู ฺฉูู ูุงููุตุฏ", "ุจ?ูุงููุณ ูู ุฎูุฏู ุฎุณุชู ุดุฏู ุชูฺ?ุ", "ุง? ุดุฑู ูุฏุงุฑ", "ูุงูุงูุชู ฺฉุฑุฏู ุจ?ุบ?ุฑุช", "ู ุงูุง ูุงุฏุฑ ุฌูุฏุช", "ุชู ?ฺฉ? ุฒ?ุฑ ุจุงุด", "ุงู ุดู", "ุฎุงุฑุชู ฺฉูุต ู?ฺฉูู", "ฺฉูุตูุงููุตุฏ", "ูุงููุต ฺฉูู?", "ุฎุงุฑฺฉุตุชู ? ุจ? ุบ?ุฑุช", "ุดุฑู ฺฉู ุจ?ูุงููุณ", "ูุงูุงูุชู ฺฉุฑุฏ ", "ุง? ูุงุฏุฑุฌูุฏู", "ุจ?ุบ?ุฑุช", "ฺฉ?ุฑุชู ูุงููุตุช", "ุจ?ูุงููุณ ูู?ุฎุง? ุงู ุจุด?ุ", "ุง? ุฎุงุฑฺฉูุตุชู", "ูุงูุดู ุฏ?ฺฏู", "ููู ฺฉุณ ฺฉูู?", "ุญุฑุงูุฒุงุฏู", "ูุงุฏุฑุชู ู?ฺฉูู", "ุจ?ูุงููุณ", "ฺฉุตุดุฑ", "ุงู ุดู ูุงุฏุฑฺฉูุตุชู", "ุฎุงุฑฺฉุตุชู ฺฉุฌุง??", "ููุชู ฺฉุฑุฏู ฺฉุงุฑ? ูู?ฺฉู?ุ", "ฺฉ?ุฑุชู ูุงุฏุฑุช ูุงู", "ฺฉ?ุฑุชู ููุช ุจุณู", "ฺฉ?ุฑุชู ุดุฑูุช", "ูุงุฏุฑุชู ู?ฺฏุงู ุจุงูุง", "ฺฉ?ุฑ ุชู ูุงุฏุฑุช", "ฺฉูู? ููู ? ุญู?ุฑ ุฒุงุฏู", "ููุช? ุชู ฺฉุต ููุช ุชููุจู ูุง? ุณุฑุนุช? ู?ุฒุฏู ุชู ฺฉูุฑู ุจูุฏ? ุจุนุฏ ุงูุงู ุจุฑุง ุจฺฉูู ููุช ุดุงุฎ ู?ุด? ูุน?   ", "ุชู ?ู ฺฉุต ููู ุง? ฺฉ ููุชู ุจู ูู ูุฏ?ู ฺฉุฑุฏ? ุชุง ุฎุง?ู ูุงู?ูู ฺฉู? ูฺฏ ูู ุฎุฎุฎุฎ", "ุงูฺฏุดุช ูุงฺฉู ุชู ฺฉููู ูุงููุณุช", "ุชุฎุชู ุณ?ุงูู ูุฏุฑุณู ุจุง ูุนุงุฏูุงุช ุฑ?ุงุถ?ู ุฑูุด ุชู ฺฉุต ููุช ุงุตูุง ุฎุฎุฎุฎุฎุฎุฎ ", "ฺฉ?ุฑู ุชุง ุชู ุฎุดฺฉ ุฎุดฺฉ ุจุง ฺฉู? ูููู ุฑูุด ุชู ฺฉุต ุฎุงุฑุช ", "ฺฉุต ููุช ุจู ุตูุฑุช ุถุฑุจุฏุฑ? ", "ฺฉุต ุฎุงุฑุช ุจู ุตูุฑุช ูุณุชุท?ู?", "ุฑุดุชู ฺฉูู ุขููพ ุจู ุตูุฑุช ุฒูุฌ?ุฑู ุง? ุชู ฺฉุต ูุณูุช ุฎุฎุฎุฎ ", "10 ุฏู?ูู ุจ?ุดุชุฑ ุงุจู ู?ุฑ?ุฎุช ุชู ฺฉุณ ููุช ุง?ู ูู?ุดุฏ?", "ูฺฉุฑ ฺฉุฑุฏ? ููุช ?ู ุจุงุฑ ุจููู ุฏุงุฏู ุฏ?ฺฏู ุดุงุฎ?", "ุงฺฏุฑ ููุชู ุฎูุจ ฺฉุฑุฏู ุจูุฏู ุญุงูุง ุชู ุง?ูุฌูุฑ? ูู?ุดุฏ?"]

def fosh_saz(text):
 return f"{choice(one)}{text}"

def font(text, lang):
 request = get('https://api.codebazan.ir/font/?type={}&text={}'.format(lang, text))
 if request.json()['Ok' if lang else 'ok'] == True:
  results = "๐ แดสแดสแด's สแดแดส สแดsแดสแด ๐ \n\n"
  for key, value in request.json()['Result' if lang else 'result'].items():
   results += f"โ โข {key} | `{value}`\n"
 return results

def create_time():
 a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
 ran = choice(fonts)
 for char in a :
  a = a.replace(char , ran[int(org.index(str(char)))])
 return a

def create_time2():
 a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
 ran = choice(fonts2)
 for char in a :
  a = a.replace(char , ran[int(org.index(str(char)))])
 return a

def create_tarikh():
 a = jdatetime.date.today().strftime("%Y/%m/%d")
 ran = choice(ftarikh)
 for char in a :
  a = a.replace(char , ran[int(Orgtarikh.index(str(char)))])
 return a

def fontinname(name):
 name = name.upper()
 rnd = choice(name_font)
 for char in name:
  try:
   name = name.replace(char , rnd[org_eng.index(char)])
  except:
   pass
 return name

def DLX(Url):
    data = {'videoid': Url}
    soup = BeautifulSoup(post(url=url, headers=headers, data=data).text, 'html.parser')
    link = findall(r'"(https://video-hw.xnxx-cdn.com/videos/flv/.*)"', str(soup.find('script', {'type': 'application/ld+json'})))[0].split('"')[0]
    FileName = link.split('/')[-1]
    FileName = FileName[:FileName.find('?')]
    return link

def snippet(params):
    url = 'https://api.crabon.io/v1/snippet'
    path = 'i.png'
    response = post('https://carbonara-42.herokuapp.com/api/cook', json=params)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response:
                f.write(chunk)
    print(response.status_code)
    
def generateimage(text):
    rand_img = ["image1.jpg","image2.jpg","image3.jpg","image4.jpg","image5.jpg","image6.jpg"]
    image = Image.open(choice(rand_img))
    image.load()
    W, H = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='font.ttf', size=190)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font=font, fill=choice(["#00c7a4","#0071c7","#c7a200","#728593","#943633","#6495ed","#43f70a","#e1b2ae","#527130","#629f5d","#3d4e90","#9a9ec4",]))
    image.save('time_image.jpg')

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def if_not_exist_creat(filename):
 if not os.path.isfile(filename):
  with open(filename , "w") as f:
   f.write("")
   f.close() 
def write(filename , text):
 with open(filename , "w", encoding="utf-8") as f:
   f.write(text)
   f.close() 
def write_a(filename , text):
 with open(filename , "a", encoding="utf-8") as f:
   f.write(text)
   f.close() 
def read(filename):
 with open(filename , "r", encoding="utf-8") as f:
   return f.read()
def json_read(filename):
 with open(filename , "r", encoding="utf-8") as f:
   return json.load(f)
   
def run_codi(lang , code):
    a = Rextester(lang , code)
    k = a.stats;k = k.replace(",","")
    run_time = k.index("running time:")
    cpu_time = k.index("cpu time:")
    used_memory = k.index("memory peak:")
    kossher = k.index("absolute service time")
    mamad = f"**Result**: \n`{a.result if a.result else '--'}`{f'**ERROR**: `{a.errors}`' if a.errors else ''}\n**State**:\n__{k[run_time:cpu_time]}\n{k[cpu_time:used_memory]}\n{k[used_memory:kossher]}__"
    return mamad

def moon_or_sun():
  a = datetime.now(timezone("Asia/Tehran")).strftime("%H");a = int(a)
  if a in[20,21,22,23,00,1,2,3,4,5]:
    b = "๐"
  elif a in[6,7]:
    b = "๐"
  elif a in[8,9,10,11]:
    b = "๐"
  elif a in[12,13,14,15,16,17]:
    b = "๐"
  elif a in[18,19]:
    b = "๐"
  return b

def dast_del(text):
  if text.privileges:
     if text.privileges.can_delete_messages == True:
        return True

def have_sec(t):
  if len(t.split(":")) == 3:
    return str(t)
  else:
    return str(t) +":00"
    
def read_note(url):
  b = str()   
  for j in url.split("\n"):
    try: 
      n = pn.read_note(j) 
      b += f"\n({j}) --> ({n})"
    except Exception as er:
      b += f"\n({j}) --> ({er})"
  return b


