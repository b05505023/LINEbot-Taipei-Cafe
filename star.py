import random
import requests

"""來吧！抽出你的今日運勢"""
def fortune_slip(name):
	#抽出隨機數字(共7種籤詩)
	f = random.randint(0,6)
	#籤詩名稱與內容
	fortune_slip_type = ["大吉","小吉","吉","普","凶","小凶","大凶"]
	fortune_slip_content = ["萬中選一\n運勢無敵","心想事成\n無事一身輕","平安順遂\n事事順心","平淡無奇\n也無風雨也無晴","時運不濟\n晴時多雲偶陣雨","白費苦心\n時運不濟","時不我與\n還是在家睡覺吧"]
	a = fortune_slip_type[f]
	b = fortune_slip_content[f]
	#輸出使用者姓名與運勢
	fortune = str(name)+"的今日運勢"+"\n"+str(a)+"\n"+str(b)
	return fortune

"""幾次能猜中呢？快來猜猜炸彈是哪顆"""
def bomb_number():
	#猜的次數計數
	i = 1
	#隨機生成一個編號
	a = random.randint(0,100)
	b = int( input('請在0-100中選一個數字\n看你是否能猜中炸彈編號：'))
	while a != b:
		if a > b:
			print('你第%d次猜的數字太小啦'%i)
			b = int(input('請再猜一次:'))
		else:
			print('你第%d次猜的數字太大啦'%i)
			b = int(input('請再猜一次:'))
		i+=1
	else:
		print('恭喜你，你第%d次猜的數字與炸彈編號%d一樣'%(i,b))

"""今天星象如何呢？快來占星吧"""
def horoscope(str):
	url='https://www.astroinfo.com.tw/node/2333'
	html=requests.get(url)
	html.encoding="utf-8"
	htmllist=html.text.splitlines()
	for i in range (0,len(htmllist)):
		if(str in htmllist[i]):
			result = htmllist[i+1]
			output = result.split("</p>")
			horoscope = output[0]
	return(horoscope)
