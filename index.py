import time
import requests
import json
import re
import time
import schedule
from datetime import datetime, timedelta
from instagrapi import Client
from instagrapi.types import StoryMention, StoryHashtag

cl = Client()
cl.login(username='lunch_sch', password='hhssbb@0306H')
insta_ids = ['seoung_0306','juchan_312', 'xonu_.iz', 'kho_923']

# 
def get_lunch():

    today = datetime.now()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    date = today.strftime("%d")
    오늘 = f"{year}{month}{date}"


    try:
        url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'

        http_post_request = requests.get(url, params= {"type":"json", "pIndex":1, "pSize":100, "ATPT_OFCDC_SC_CODE":"J10", "SD_SCHUL_CODE":7530929, "MLSV_YMD": 오늘})

        데이터 = json.loads(http_post_request.text)
        점심 = 데이터["mealServiceDietInfo"][1]['row'][0]['DDISH_NM']
        점심 = 점심.replace(" ", "")
        점심 = re.sub(r'(<br>|<br\/>|<br \/>)+', '\n', 점심)
        점심 = re.sub(r'\(\d+(\.\d+)*\.\)', '', 점심)

        for id in insta_ids:
            try:
                user_id = cl.user_id_from_username(id)

                text = '오늘의 급식은' + '\n\n' + 점심

                cl.direct_send(text, user_ids=[user_id])
                
            except:
                pass
        print("모든 계정에 전송이 완료되었습니다.")
    except:
        print("급식이 제공되지 않습니다.")



schedule.every().day.at("06:00").do(get_lunch)
while True:
    schedule.run_pending()