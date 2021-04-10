# ●	Посмотреть документацию к API GitHub,
# разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

# curl -i https://api.github.com/users/barksun/repos просмотрим все доступные репозитории пользователя barksun
# curl -i -H "Authorization: token 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" \ https://api.github.com/user/repos
# просмотрим все доступные репозитории пользователя barksun с использованием токена
# curl \-H "Accept: application/vnd.github.v3+json" \  https://api.github.com/repos/barksun/python
# просмотрим репозиторий python пользователя barksun и выведем информацию в json
# подберем еще несколько пользователей у которых есть публичные репозитории:
# https://github.com/binakot/My-Public-Activities
# https://github.com/jumichot
# https://api.github.com/users/jumichot/repos

import requests
import json
from pprint import pprint
main_link ='https://api.github.com/users/jumichot/repos'
response = requests.get(main_link)
j_data = response.json()
with open('j_data_hw1.json', 'w') as outfile:
    json.dump(j_data, outfile, indent=2)
pprint(j_data)

# только у меня почему-то тип j_data получается 'list'

