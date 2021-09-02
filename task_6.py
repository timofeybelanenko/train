import re
from datetime import datetime

text = ''' 2016-04-01 Начало работ
 2016-04-01 Генерация отчет по директ
2016-04-02 Генерация отчет по адвордс
2016-04-03 Работа закончена'''


for i in re.findall(r'\d+-\d+-\d+', text):
    print(datetime.strptime(i, "%Y-%m-%d").strftime("%d-%m-%Y"))