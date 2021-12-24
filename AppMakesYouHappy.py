#良い日になるプログラムを作りました
#Google Colaboratoryで実行できます
from datetime import date
today = date.today()
if today == date(2022, 1, 1):
  message = 'Happy New Year!'
else:
  message = 'Have a nice day!'
print(today,message)
