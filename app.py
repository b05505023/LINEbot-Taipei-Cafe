from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import os.path
import sys
import json
import apiai
import star2
import random
from chatBot import cafeChatbot
import read_jokes
app = Flask(__name__)
# YOUR GOOGLE DIALOGFLOW API KEY
ai = apiai.ApiAI('YOUR GOOGLE DIALOGFLOW API KEY')
# Channel Access Token
line_bot_api = LineBotApi('LINE CHANNEL ACCESS TOKEN')
# Channel Secret
handler = WebhookHandler('LINE CHANNEL SECRET')
#man
men=["https://imgur.com/UQINa8n.jpg",
"https://imgur.com/3FFrELS.jpg",
"https://imgur.com/rzpidOW.jpg",
"https://imgur.com/2NPW9v3.jpg",
"https://imgur.com/8lyrjKk.jpg",
"https://imgur.com/6Pzsgii.jpg",
"https://imgur.com/K5dmaWW.jpg",
"https://imgur.com/uXJX3oi.jpg",
"https://imgur.com/AQ3nNIl.jpg",
"https://imgur.com/PKlVYab.jpg",
"https://i.imgur.com/FH4XQVp.jpg"]
#WEMEN
wemen=["https://imgur.com/Nk326kA.jpg",
"https://imgur.com/JTYZhBt.jpg",
"https://imgur.com/nHdQwTH.jpg",
"https://imgur.com/XrBLLbI.jpg",
"https://imgur.com/tuzdqXE.jpg",
"https://imgur.com/reZ2efV.jpg",
"https://imgur.com/TbvCuKZ.jpg",
"https://imgur.com/HUyGV6i.jpg",
"https://imgur.com/pAuGluN.jpg",
"https://imgur.com/Cjq2MGM.jpg"]
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    verb=["喝","推薦","附近","告訴","講"]
    n=["coffee","cafe","咖啡"]
    flag1=False
    flag2=False
    flag=False
    lasthero=False
    inputtext=str(event.message.text)
    
    uid = event.source.user_id
    ai_request = ai.text_request()
    ai_request.lang = "zh-tw"
    ai_request.session_id = uid
    ai_request.query = inputtext
    ai_response = json.loads(ai_request.getresponse().read())
    
    for i in verb:
        if inputtext.find(i) != -1:
            flag1=True
            break
    for i in n:
        if inputtext.find(i) != -1 and flag1==True:
            flag2=True
            break
    if inputtext=="抽籤":
        outcome1 = star2.fortune_slip("您")
        message = TextSendMessage(text=outcome1)
    elif inputtext=="笑話":
        joke = read_jokes.tell_jokes('笑話')
        message = [TextSendMessage(text="這是我嚴選的喔><"),TextSendMessage(text=joke)]
    elif inputtext=="表特":
        message = [
            TextSendMessage(text="想看帥哥還是美女解悶呢?"),
            TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    
                    CarouselColumn(
                        
                        text='帥哥美女?',
                        actions=[
                            MessageTemplateAction(
                                
                                label='帥哥',
                                text='帥哥'

                            ),
                            MessageTemplateAction(
                                label='美女', 
                                text= '美女'
 
                            ),
                            
                           
                        ]
                    )
                    
                ]
            )
        )]
        '''message = ImageSendMessage(
            original_content_url="https://imgur.com/Nk326kA.jpg",
            preview_image_url="https://imgur.com/Nk326kA.jpg"
        )'''
    elif inputtext in ["帥哥","美女"]:
        #r=random.randint(0,9)
        if inputtext=="帥哥":
            r=random.randint(0,10)
            message = ImageSendMessage(
            original_content_url=men[r],
            preview_image_url=men[r]
        )
        elif inputtext=="美女":
            r=random.randint(0,9)
            message = ImageSendMessage(
            original_content_url=wemen[r],
            preview_image_url=wemen[r]
        )
        
    elif inputtext=="咖啡":
        message = [
        TextSendMessage(text="請輸入地區喔喔~~"),
        TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            MessageTemplateAction(
                                
                                label='中正',
                                text='中正區'

                            ),
                            MessageTemplateAction(
                                label='大同',
                                text='大同區'

                            ),
                            MessageTemplateAction(

                                label='中山',
                                text='中山區'

                            )
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            
                            MessageTemplateAction(
                                label='松山',
                                text='松山區'
                                
                            ),
                            MessageTemplateAction(
                                label='大安',
                                text='大安區'
                                
                            ),
                            MessageTemplateAction(
                                
                                label='萬華',
                                text='萬華區'
                                
                            )
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            MessageTemplateAction(
                                
                                label='信義',
                                text='信義區'
                                
                            ),
                            MessageTemplateAction(
                                
                                label='士林',
                                text='士林區'
                                
                            ),
                            
                            MessageTemplateAction(

                                label='北投',
                                text='北投區'
                            )
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            MessageTemplateAction(

                                label='內湖',
                                text='內湖區'
                            
                            ),
                            MessageTemplateAction(
                                
                                label='南港',
                                text='南港區'
                            ),
                                    
                            MessageTemplateAction(
                                
                                label='文山',
                                text='文山區'
                                
                            )
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            MessageTemplateAction(
                                
                                label='隨便',
                                text='不限制'

                            ),
                            MessageTemplateAction(
                                
                                label='隨便',
                                text='不限制'

                            ),
                            MessageTemplateAction(
                                
                                label='隨便',
                                text='不限制'

                            )
                            
                           
                        ]
                    ),
                ]
            )
        )]
    elif inputtext in ['不限制','中正區','大同區','中山區','松山區','大安區','萬華區','信義區','士林區','北投區','內湖區','南港區','文山區']:
        message = [
        TextSendMessage(text="請問是禮拜幾要喝咖啡呢?"),
        TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    
                    CarouselColumn(
                        
                        text='日期',
                        actions=[
                            MessageTemplateAction(
                                
                                label='週一',
                                text='週一 '+str(inputtext)

                            )
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='日期',
                        actions=[
                            MessageTemplateAction(
                                
                                label='週二',
                                text='週二 '+str(inputtext)

                            )                           
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='日期',
                        actions=[
                            MessageTemplateAction(
                                
                                label='週三',
                                text='週三 '+str(inputtext)

                            )                           
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='日期',
                        actions=[
                            MessageTemplateAction(
                                
                                label='週四',
                                text='週四 '+str(inputtext)

                            )                           
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='日期',
                        actions=[
                            MessageTemplateAction(
                                
                                label='週五',
                                text='週五 '+str(inputtext)

                            )                           
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='日期',
                        actions=[
                            MessageTemplateAction(
                                
                                label='週六',
                                text='週六 '+str(inputtext)

                            )                           
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='日期',
                        actions=[
                            MessageTemplateAction(
                                
                                label='週日',
                                text='週日 '+str(inputtext)

                            )                           
                           
                        ]
                    )
                    
                ]
            )
        )]
    elif( inputtext.split(" ")[0] in ['週一','週二','週三','週四','週五','週六','週日']) and (inputtext.split(" ")[1] in ['不限制','中正區','大同區','中山區','松山區','大安區','萬華區','信義區','士林區','北投區','內湖區','南港區','文山區']) and len(inputtext.split(" "))==2:
        message =[
        TextSendMessage(text="有需要wifi嗎?"), 
        TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    
                    CarouselColumn(
                        
                        text='WIFI',
                        actions=[
                            MessageTemplateAction(
                                
                                label='需要',
                                text=str(inputtext)+" O"

                            ),
                            MessageTemplateAction(
                                label='隨便', 
                                text=str(inputtext)+" X"
 
                            ),
                            
                           
                        ]
                    )
                    
                ]
            )
        )]
    elif( inputtext.split(" ")[0] in ['週一','週二','週三','週四','週五','週六','週日']) and (inputtext.split(" ")[1] in ['不限制','中正區','大同區','中山區','松山區','大安區','萬華區','信義區','士林區','北投區','內湖區','南港區','文山區']) and (inputtext.split(" ")[2] in ['O','X']) and len(inputtext.split(" "))==3:
        message =[
        TextSendMessage(text="甜點咧?"), 
        TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    
                    CarouselColumn(
                        
                        text='甜點',
                        actions=[
                            MessageTemplateAction(
                                
                                label='需要',
                                text=str(inputtext)+" O"

                            ),
                            MessageTemplateAction(
                                label='隨便', 
                                text=str(inputtext)+" X"
 
                            ),
                            
                           
                        ]
                    )
                    
                ]
            )
        )]
    elif( inputtext.split(" ")[0] in ['週一','週二','週三','週四','週五','週六','週日']) and (inputtext.split(" ")[1] in ['不限制','中正區','大同區','中山區','松山區','大安區','萬華區','信義區','士林區','北投區','內湖區','南港區','文山區']) and (inputtext.split(" ")[2] in ['O','X']) and(inputtext.split(" ")[3] in ['O','X']) and len(inputtext.split(" "))==4:
        message = [
        TextSendMessage(text="最後了~有需要提供插座嗎?"),
        TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    
                    CarouselColumn(
                        
                        text='插座',
                        actions=[
                            MessageTemplateAction(
                                
                                label='需要',
                                text=str(inputtext)+" O"

                            ),
                            MessageTemplateAction(
                                label='隨便', 
                                text=str(inputtext)+" X"
 
                            ),
                            
                           
                        ]
                    )
                    
                ]
            )
        )]
    elif( inputtext.split(" ")[0] in ['週一','週二','週三','週四','週五','週六','週日']) and (inputtext.split(" ")[1] in ['不限制','中正區','大同區','中山區','松山區','大安區','萬華區','信義區','士林區','北投區','內湖區','南港區','文山區']) and (inputtext.split(" ")[2] in ['O','X']) and(inputtext.split(" ")[3] in ['O','X']) and(inputtext.split(" ")[4] in ['O','X']) and len(inputtext.split(" "))==5:
        bot = cafeChatbot("./cafe_list.csv")
        if inputtext.split(" ")[2]=="O":
            wf=True
        else:
            wf=False
        if inputtext.split(" ")[3]=="O":
            ds=True
        else:
            ds=False
        if inputtext.split(" ")[4]=="O":
            el=True
        else:
            el=False
        USER1 = {
            'district': inputtext.split(" ")[1],
            'week': inputtext.split(" ")[0],
            'today': False,
            'wifi': wf,
            'dessert':ds,
            'elecrtic':el,
        }  
        result1 = bot.run(USER1)
        if "https" in result1[0]['官網']:
            a=URITemplateAction(
                                
                label='官方網站',
                uri=str(result1[0]['官網'])
                        

            )
        else:
            a=URITemplateAction(
                                
                label='沒官網自己查QQ',
                uri="https://www.google.com/"
                        

            )
    
        if "https" in result1[1]['官網']:
            b=URITemplateAction(
                                
                label='官方網站',
                uri=str(result1[1]['官網'])
                        

            )
        else:
            b=URITemplateAction(
                                
                label='沒官網自己查QQ',
                uri="https://www.google.com/"
                        

            )
        if "https" in result1[2]['官網']:
            c=URITemplateAction(
                                
                label='官方網站',
                uri=str(result1[2]['官網'])
                        

            )
        else:
            c=URITemplateAction(
                                
                label='沒官網自己查QQ',
                uri="https://www.google.com/"
                        

            )
        
        message = [
        TextSendMessage(text="以下是為您推薦的三家咖啡廳喔 ~"),
        TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    
                    CarouselColumn(
                        
                        text=str(result1[0]['店名'])+"\n"+str(result1[0]['地址']+"\n"+str(result1[0]['營業時間'])),
                        actions=[
                            a

                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text=str(result1[1]['店名'])+"\n"+str(result1[1]['地址']+"\n"+str(result1[1]['營業時間'])),
                        actions=[
                             b
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text=str(result1[2]['店名'])+"\n"+str(result1[2]['地址']+"\n"+str(result1[2]['營業時間'])),
                        actions=[
                             c
                           
                        ]
                    ),
                   
                ]
            )
        )]



    elif inputtext=="星座":
        lasthero=True
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            
                            MessageTemplateAction(
                                label='牡羊',
                                text='牡羊座'
                                
                            ),
                            MessageTemplateAction(
                                label='金牛',
                                text='金牛座'
                                
                            ),
                            MessageTemplateAction(
                                
                                label='雙子',
                                text='雙子座'
                                
                            )
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            MessageTemplateAction(
                                
                                label='巨蟹',
                                text='巨蟹座'
                                
                            ),
                            MessageTemplateAction(
                                
                                label='獅子',
                                text='獅子座'
                                
                            ),
                            
                            MessageTemplateAction(

                                label='處女',
                                text='處女座'
                            )
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            MessageTemplateAction(

                                label='天秤',
                                text='天秤座'
                            
                            ),
                            MessageTemplateAction(
                                
                                label='天蠍',
                                text='天蠍座'
                            ),
                                    
                            MessageTemplateAction(
                                
                                label='射手',
                                text='射手座'
                                
                            )
                           
                        ]
                    ),
                    CarouselColumn(
                        
                        text='請選擇',
                        actions=[
                            MessageTemplateAction(
                                
                                label='魔羯',
                                text='魔羯座'

                            ),
                            MessageTemplateAction(
                                label='水瓶',
                                text='水瓶座'

                            ),
                            MessageTemplateAction(

                                label='雙魚',
                                text='雙魚座'

                            )
                           
                        ]
                    )
                ]
            )
        )
    elif inputtext in ['獅子座','處女座','天秤座','天蠍座','射手座','魔羯座','水瓶座','雙魚座','牡羊座','金牛座','雙子座','巨蟹座']:
        message=[TextSendMessage(text=str(inputtext)+"今日運勢是"),TextSendMessage(text=star2.horoscope(inputtext))]
        
    #elif flag1==True and flag2==True and inputtext.find("不")==-1:
    #    message = TextSendMessage(text="喝屁喝喔")

    #elif flag1==True and flag2==True and inputtext.find("不")!=-1:
    #    message = TextSendMessage(text="不喝就不喝阿")
    else:
        message = TextSendMessage(text=ai_response["result"]["fulfillment"]["speech"])
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
