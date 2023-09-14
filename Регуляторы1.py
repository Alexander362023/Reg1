import re
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("Desktop/Сценарии пробники/регуляторы_данные.csv", encoding='utf=8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)


pattern = re.compile(r'(\+7|8)\s*\(*(495)\)*\s*\-*(\d{3})[\-]*(\d{2})[\-]*(\d+)\s*(\(*\доб*\.\s*\d*\)*)?')  
subst_pattern= r'+7(\2)\3-\4-\5 \6'
result = pattern.sub(subst_pattern, contacts_list)
print(result)


# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf=8') as f:
  datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
  cont =[]
  datawriter.writerows(cont) 
pprint(cont)