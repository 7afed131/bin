# Programming By : RUKS
# Instagram: _v_go
# Telegram : @DIBIBl
# Telegram2 : @TDTDI
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# automatic reaction tool
# TOOL = FREE
import requests
import random
from user_agent import generate_user_agent
import time
ruks1 =("0123456789")
ruks2 =("374","376")
R = '\033[1;37m'
ruks__ = '\033[1;36m'
ruks_ = '\033[1;36m'
jruks = '\033[1;33m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
r=("="*60)
# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
print(f"""{r}

██████╗ ██╗   ██╗██╗  ██╗███████╗
██╔══██╗██║   ██║██║ ██╔╝██╔════╝
██████╔╝██║   ██║█████╔╝ ███████╗
██╔══██╗██║   ██║██╔═██╗ ╚════██║
██║  ██║╚██████╔╝██║  ██╗███████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝


{r}""")

# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
TOKEN = '2036209757:AAG3NNOBVhlk1MehRVkjwKIqnoUDAr3tBAs'
ID = '948449142'
print(r)
def data(k,bin):
	# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
	name = k.json()["country"]["name"]
	emoji = k.json()["country"]["emoji"]
	scheme = k.json()["scheme"]
	type = k.json()["type"]
	brand = k.json()["brand"] 
	bank_name = k.json()["bank"]["name"]
	bank_url= k.json()["bank"]["url"]
	bank_phone = k.json()["bank"]["phone"]
	# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
	txt_ruks=f"""⌯  ʜɪ ѕɪʀ ɴᴇᴡ ʙɪɴ  ⌯
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
• ɪɴғᴏʀᴍᴀᴛɪᴏɴѕ ʙɪɴ 
⌯ ʙɪɴ : {bin}
⌯ ᴄᴏụɴᴛʀʏ : {name} {emoji}
⌯ ɴᴇᴛᴡᴏʀᴋ : {scheme}
⌯ ʙʀᴀɴᴅ : {brand}
⌯ ᴛʏᴘᴇ : {type}

• ʙᴀɴᴋ 
⌯ ɴᴀᴍᴇ : {bank_name}
⌯ ụʀʟ : {bank_url}
⌯ ᴘʜᴏɴᴇ : {bank_phone}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
• Tele : @DIBIBl . @TDTDI. ؟ ، 🔥"""	
	T =(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text='+txt_ruks)
	# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
	RE = requests.post(T)
	
def extract_bin_ruks3():
	Z=0
	# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
	while True:
		Z+=1
		time.sleep(1)
		A = str("".join(random.choice(ruks1)for i in range(3)))
		B = str("".join(random.choice(ruks2)for i in range(1)))
		# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
		headers ={'appCodeName': 'Mozilla',
	 'appName': 'Netscape',
	 'appVersion': generate_user_agent(),
	 'buildID': None,
	 'oscpu': 'Intel Mac OS X 10_8_1',
	 'platform': 'Macintosh; Intel Mac OS X 10_8_1',
	 'product': 'Gecko',
	 'productSub': '20030107',
	 'userAgent': generate_user_agent(),
	 'vendor': 'Google Inc.',
	 'vendorSub': ''}			
		bin =(f"{B}{A}")
		k = requests.get(f"https://lookup.binlist.net/"+bin,headers=headers)
		if "<title>429 Too Many Requests</title>" in k:			
			time.sleep(1.50)		
		try:
			# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
			country = k.json()["country"]["currency"]
			emoji = k.json()["country"]["emoji"]
			print(jruks+'['+_ruks+str(Z)+jruks+']'+jruks+" bin"+BGreen+' work'+R+' | '+bin+R+" | "+emoji+BGreen)
			# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
			if country == "BRL":
				data(k,bin)
			elif country == "USD":
				data(k,bin)
		except:
			# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
			print(jruks+'['+_ruks+str(Z)+jruks+']'+jruks+' bin'+_ruks+' not work'+R+' | '+bin+R+" | "+"False"+BGreen) 
			pass
extract_bin_ruks3()
# code by ruks telegram : @DIBIBl , @TDTDI , @ruks3 	
