# instagram-lunch-notice (인스타그램 자동 급식 알리미)
※주의 해당 문서는 공식 Instagram API를 활용하지 않았습니다. 계정 차단등에 대한 문제를 걱정하시면 공식 API를 활용하시기를 바랍니다.
  해당문서에서는 https://github.com/subzeroid/instagrapi의 instagrapi를 사용합니다.
  
※Note: This document does not utilize the official Instagram API. If you are worried about problems with account blocking, please use the official API.
  This document uses installrapi at https://github.com/subzeroid/instagrapi .

## ⚙️설정

자동화를 할 계정의 username password 입력 후 관리자 계정으로 테스트 메시지를 보낼 수 있도록 본인이 사용하는 계정이름을 admin_username에 입력합니다.
```
cl = Client()
cl.login(username='username', password='password') //변경 Edit
cl.direct_send('작동을 시작합니다.', user_ids=[cl.user_id_from_username('admin_username')]) //변경 Edit
print('로그인을 성공적으로 수행했습니다.')
```


ATPTcode, Schoolcode를 수정합니다. 해당 인자에 대한 설명은 아래 테이블로 저장되어있습니다.
```
http_post_request = requests.get(url, params= {"type":"json", "pIndex":1, "pSize":100, "ATPT_OFCDC_SC_CODE":"ATPTcode", "SD_SCHUL_CODE":Schoolcode, "MLSV_YMD": 오늘})
```

|변수명|타입|변수 설명|
|------|---|---|
|ATPT_OFCDC_SC_CODE|STRING(필수)|시도교육청코드|
|SD_SCHUL_CODE|STRING(필수)|행정표준코드|
|MMEAL_SC_CODE|STRING(선택)|식사코드|
|MLSV_YMD|STRING(선택)|급식일자|
|MLSV_FROM_YMD|STRING(선택)|급식시작일자|
|MLSV_TO_YMD|STRING(선택)|급식종료일자|

자세한 사항은 https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17320190722180924242823&infSeq=2 를 참고하십시오.

## 🚀 실행하기
이제 설정이 모두 끝났습니다. 터미널에서 다음 명령어를 입력하여 실행합니다.
pip install
python main.py
봇이 실행되면, Instagram을 통해 메시지가 옵니다.

## 📝 라이센스
이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 LICENSE 파일에서 확인할 수 있습니다.

-----------------------------------------------------------------------------

# # instagram-lunch

## ⚙Set ️

Type the username password for the account you want to automate and type the account name you use in admin_username so that you can send a test message to your administrator account.
```
cl = Client()
cl.login(username='username', password='password') //변경 Edit
cl.direct_send ('start operation,' user_ids=[cl.user_id_from_username('admin_username')]) //변경 Edit
print ('Login successfully performed).')
```


Modify ATPTcode, Schoolcode. A description of the factor is stored in the table below.
```
http_post_request = requests.get(url, params= {"type":"json", "pIndex":1, "pSize":100, "ATPT_OFCDC_SC_CODE":"ATPTcode", "SD_SCHUL_CODE":Schoolcode, "MLSV_YMD": 오늘})
```

|Variable name|Type|Variable description|
|------|---|---|
|ATPT_OFCDC_SC_CODE|STRING (required) | Metropolitan Office of Education Code|
|SD_SCHUL_CODE|STRING (required)|Administrative Standard Code|
|MMEAL_SC_CODE|STRING (optional)|Meal code|
|MLSV_YMD|STRING (optional) | Meal Service Date|
|MLSV_FROM_YMD|STRING (optional) |Eating start date|
|MLSV_TO_YMD|STRING (optional) | Meal Service End Date|

see https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17320190722180924242823&infSeq=2 for more information.

## Run 🚀
The setup is now complete. On the terminal, type the following command to execute.
pip install
python main.py
When the bot is launched, a message will be sent via Instagram.

## 📝 Licenses
This project is subject to the MIT license. Details can be found in the LICENSE file.
