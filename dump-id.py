#-*-coding:utf-8-*-
# coding by Romi Afrizal
import os, re, sys, itertools, time, requests, random, threading, json, random
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 dump.py')
    
from mechanize import Browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; Infinix X652B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171848;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/243389251;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]')]
br.addheaders = [('User-Agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
os.system('clear')
done = False

#def animate():
 #   for c in itertools.cycle(['\x1b[0;91m.', '\x1b[0;93m.', '\x1b[0;91m.', '\x1b[0;93m.']):
   #     if done:
        #    break
    #    sys.stdout.write('\r\x1b[0;97mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
      #  sys.stdout.flush()
        #time.sleep(0.1)


#t = threading.Thread(target=animasis)
#t.start()
#time.sleep(5)
#done = True

def keluar():
    print '\x1b[0;91m•\x1b[0;93m Sampai Jumpa :)\x1b[0;97m'
    os.sys.exit()
    
def hapus():
	os.system('rm -rf login.txt')
	time.sleep(0.01)
	masuk()

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
logo = ('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')

back = 0
threads = []
id = []
idteman = []
idfromteman = []

def masuk():
    os.system('clear')
    os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    time.sleep(0.07)
    print '\x1b[1;97m1). Login Via Token Facebook'
    time.sleep(0.07)
    print '\x1b[1;97m2). Login Via Cookie Facebook'
    time.sleep(0.07)
    print '\x1b[1;91m0\x1b[1;97m).\x1b[1;97m Exit'
    time.sleep(0.07)
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    time.sleep(0.07)
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('* --> ')
    if msuk == '':
        print ' Isi Yg Benar Sayang!'
        pilih_masuk()
    elif msuk == '1':
        login_token()
    elif msuk == '2':
        login_cookie()
    elif msuk == '0':
        os.sys.exit()
    else:
        print ' Isi Yg Benar Sayang!'
        pilih_masuk()

def login_token():
    os.system('clear')
    os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    toket = raw_input(' Token \x1b[1;94m>\x1b[1;93m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan ('\x1b[1;92m Login Berhasil !\x1b[0;97m ')
        dump()
    except KeyError:
        print 'Token salah !'
        time.sleep(1.7)
        masuk()
    except requests.exceptions.SSLError:
        print ' Koneksi Bermasalah'
        exit()


def login_cookie():
    os.system('clear')
    os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
    print '\x1b[1;91m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    time.sleep(0.07)
    try:
        cookie = raw_input(' Cookie \x1b[1;94m>\x1b[1;93m ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        cari = re.search('(EAAA\\w+)', coki.text)
        hasil = cari.group(1)
        zedd = open('login.txt', 'w')
        zedd.write(hasil)
        zedd.close()
        jalan ('\x1b[1;92m Login Berhasil !\x1b[0;97m ')
        time.sleep(2)
        dump()
    except AttributeError:
        print ' Cookie salah !'
        time.sleep(2)
        masuk()
    except UnboundLocalError:
        print ' Cookie salah !'
        time.sleep(2)
        masuk()
    except requests.exceptions.SSLError:
        os.system('clear')
        print ' Koneksi Bermasalah'
        exit()



def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' Token invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    os.system('clear')
    os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    print '\x1b[1;97m1). Dump ID Dari Daftar Teman '
    print '\x1b[1;97m2). Dump ID Dari Teman/Publik '
    print '\x1b[1;91m0\x1b[1;97m).\x1b[1;97m Keluar '
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    dump_pilih()


def dump_pilih():
    cuih = raw_input(' *--> ')
    if cuih == '':
        print ' Isi Yg Benar Sayang!'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        id_teman()
    elif cuih == '2' or cuih == '02':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        hapus()
    else:
        print ' Isi Yg Benar Sayang!'
        dump_pilih()


def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;95m • \x1b[1;91mMengambil semua ID Teman \x1b[1;97m...')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;95m • \x1b[1;93m' + str(len(idteman)) + '\x1b[1;93m -> ',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;92m' + a['id']

        bz.close()
        print '\n\x1b[1;93m [\x1b[1;92m\xe2\x9c\x93\x1b[1;93m] \x1b[1;92mSukses Mengambil ID '
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mTotal ID\x1b[1;91m :\x1b[1;92m %s' % len(idteman)
        done = raw_input('\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mSimpan Nama File\x1b[1;91m : \x1b[1;92m')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mFile tersimpan \x1b[1;91m: \x1b[1;92mout/' + done
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except IOError:
        print '\x1b[1;91m Gagal membuat file'
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m Terhenti ! '
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except KeyError:
        print '\x1b[1;91m Gagal '
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except OSError:
        print '\x1b[1;91m File anda tidak tersimpan !'
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m Tidak ada koneksi !'
        keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        idt = raw_input(' User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print ' Nama Akun      : ' + op['name']
        except KeyError:
            print ' \x1b[1;91mID Publik Tidak Ada !'
            raw_input('\n\x1b[1;93m[\x1b[1;91mKembali\x1b[1;93m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;95m • \x1b[1;91mMengambil semua ID Teman \x1b[1;97m...')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;95m • \x1b[1;93m' + str(len(idfromteman)) + '\x1b[1;93m -> ',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;92m' + a['id']

        bz.close()
        print '\n\x1b[1;93m [\x1b[1;92m\xe2\x9c\x93\x1b[1;93m] \x1b[1;92mSukses Mengambil ID '
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mTotal ID\x1b[1;91m :\x1b[1;92m %s' % len(idfromteman)
        done = raw_input('\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mSimpan Nama File\x1b[1;91m : \x1b[1;92m')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mFile tersimpan \x1b[1;91m: \x1b[1;92mout/' + done
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except OSError:
        print '\x1b[1;91m File tidak tersimpan '
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except IOError:
        print '\x1b[1;91m Gagal membuat file'
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m Terhenti '
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except KeyError:
        print '\x1b[1;91m Gagal '
        raw_input('\n\x1b[1;93m [\x1b[1;91mKembali\x1b[1;93m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m Tidak ada koneksi !'
        keluar()
        
        
if __name__ == '__main__':
	dump()
	masuk()
      
