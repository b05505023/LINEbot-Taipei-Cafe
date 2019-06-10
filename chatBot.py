
# import datetime
# 使用者輸入地區/星期幾/wifi/特殊要求：要不要蛋糕/插座 最終推薦符合條件的分數最高前三個



import pandas as pd
import datetime

PATH = "./cafe_list.csv"


TOPK = 3 #推薦三家咖啡廳
YES = 'Yes'

class cafeChatbot():
    def __init__(self, path):
        self.load_data(path)
        self.weeks = ['週一','週二', '週三', '週四', '週五','週六',  '週日']
    
    def load_data(self, path):
        self.df = pd.read_csv(path)

    def filter_district(self, df, district):
        return df[df['地址'].str.contains(district) == True]

    def filter_weekday(self, df, weekday):
        return df[df[weekday].str.contains('未營業') == False]

    def filter_score(self, df, attr, score):
        return df[df[attr]>= score]

    def filter_attr(self, df, attr):
        return df[df[attr].str.contains(YES)== True]

    def get_topK(self, df, topK):
        df["total"] = df[["wifi 穩定","價格便宜","咖啡好喝", "安靜程度"]].sum(1)
        df = df.sort_values(by="total", ascending=False).head(topK)
        return df
    
    def get_today_weekday(self):
        weekday  =datetime.datetime.today().weekday()
        return self.weeks[weekday]

    def output(self, df, weekday):
        df = df[["店名","地址","官網", weekday]]    
        df = df.rename(columns = {weekday:'營業時間'}) # rename 營業時間
        return df.to_dict(orient='records')

    def run(self, user):
        df = self.df
        # 輸入所在區域
        district = user['district']
        # print(district)
        if district != '不限制':
            df = self.filter_district(df, district)
        today = user['today']
        weekday = self.get_today_weekday()
        if today:
            # 現在有營業的咖啡廳
            df = self.filter_weekday(df, weekday)
        else :
            # 選擇其他星期
            # print(weekday)
            weekday = user['week']
            df = self.filter_weekday(df, weekday)
         # 其他條件 
        wifi = user['wifi']
        dessert = user['dessert']
        electric = user['elecrtic']
        if (wifi):
            # print('wifi: {}'.format(wifi))
            df = self.filter_score(df, 'wifi 穩定', 3) #三分以上
        if (dessert):
            # print('dessert: {}'.format(dessert))
            df = self.filter_attr(df, '有賣甜點')
        if (electric):
            # print('electric: {}'.format(electric))
            df = self.filter_attr(df, '插座')
        df = self.get_topK(df, TOPK)
        return self.output(df, weekday)


''' 有限制區域'''
USER1 = {
    'district': '淡水區',
    'week':'週一',
    'today': True,
    'wifi':True,
    'dessert':True,
    'elecrtic':True,
}  

''' 不限制區域''' 
USER2 = {
    'district': '不限制',
    'week':'週一',
    'today': False,
    'wifi':True,
    'dessert':False,
    'elecrtic':True,
}  

if __name__== "__main__":
    bot = cafeChatbot(PATH)
    print('======= User 1 =======')
    result1 = bot.run(USER1)
    for r in result1:
        print(r)
    print('======= User 2 =======')
    result2 = bot.run(USER2)
    for r in result2:
        print(r)
