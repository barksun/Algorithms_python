# ●	Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
# de4v3mLbCf3w токе для API ФССП
# https://api-ip.fssp.gov.ru/api/v1.0/

#  curl -G https://api-ip.fssp.gov.ru/api/v1.0/search/legal \
#    --data-urlencode "region=66" \
#    --data-urlencode "name=Ромашка" \
#    --data-urlencode "token=yourapikey"

import requests
from pprint import pprint
import json
main_link_1 ='https://api-ip.fssp.gov.ru/api/v1.0/search/legal'
region = '77'
name = 'КарМани'
token = 'xxxxxx'
params_1 = {'region': region,
          'name': name,
          'token': token}
response = requests.get(main_link_1, params=params_1)
j_data_1 = response.json()
pprint(j_data_1)
print (type(j_data_1))

#https://api-ip.fssp.gov.ru/api/v1.0/result \
#    --data-urlencode "task=BDAB49B2-F435-49CC-80DF-55F2F57D3057" \
#    --data-urlencode "token=yourapikey"

main_link_2 ='https://api-ip.fssp.gov.ru/api/v1.0/result'
task = '0060302c-999f-48ec-bfb6-0ad54ee728d6'     # остался вопрос: как в переменную task подставлять значение
# из 'response': {'task': '07ccf42a-4b97-4381-9c72-cda4fbf31fbf'},
token = 'xxxx'
params_2 = {'task': task,
          'token': token}
response = requests.get(main_link_2, params=params_2)
j_data_2 = response.json()
with open('j_data_hw2.json', 'w', encoding='utf-8') as file:
    json.dump(j_data_2, file, indent=4, ensure_ascii=False)
pprint(j_data_2)


