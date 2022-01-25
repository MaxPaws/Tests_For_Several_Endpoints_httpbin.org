# Файл с настройками логгера и записью ответов на необходимые запросы на сайт в переменные,
# для дальнейшего их использования в тестах.
# 
# Логи запросов к эндпоинтам и их ответов записываются в файл "Test_Requests_To_Httpbin_Log.log"
# после каждого запуска тестов.

import logging
import requests

# Логгер, подхватывающий GET запросы библиотеки requests.
# Запросы с их статусами пишутся и в консоль и в файл "Test_Requests_To_Httpbin_Log.log".
log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)

# Для обработчика - один для вывода в консоль, второй для записи в файл,
# оба пишут события уровня DEBUG и выше.
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
tfh = logging.FileHandler("Test_Requests_To_Httpbin_Log.log", mode='w')
tfh.setLevel(logging.DEBUG)

# Форматтер для вывода записей в следующем стиле:
# DEBUG - 25-Jan-22 21:12:33 - urllib3.connectionpool - сообщение
lf = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Установка форматтера для обработчиков и обработчиков в логгер.
ch.setFormatter(lf)
tfh.setFormatter(lf)
log.addHandler(ch)
log.addHandler(tfh)

# Далее идут сами запросы на сайт и сохранение ответов в переменные.
# Воизбежание блокировки, между запросами можно было бы вызывать таймаут time.sleep(3).

# GET запрос к "https://httpbin.org/headers" и логирование полученного ответа
headers_page_response = requests.get("https://httpbin.org/headers")
log.info(headers_page_response)

# Сохранение тела ответа "https://httpbin.org/headers" в формате JSON и вывод тела в лог
headers_page_response_body = headers_page_response.json()
log.info(headers_page_response_body)

# GET запрос к страницам "https://httpbin.org/status/статус_код" и логирование полученных ответов
code_200_page_response = requests.get("https://httpbin.org/status/200")
log.info(code_200_page_response)
code_300_page_response = requests.get("https://httpbin.org/status/300")
log.info(code_300_page_response)
code_400_page_response = requests.get("https://httpbin.org/status/400")
log.info(code_400_page_response)
code_500_page_response = requests.get("https://httpbin.org/status/500")
log.info(code_500_page_response)
