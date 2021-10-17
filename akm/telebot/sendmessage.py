import requests

token = '2018618673:AAFeAMB9pYqGNAOZpwhd57MsYvtSe_byLWQ'
chat_id = '-586479976'
text = 'Тестовое сообщение 2'

def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': 'Тестовое сообщение 2'
    })

sendTelegram()