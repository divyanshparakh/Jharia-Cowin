import requests
from time import sleep
from termcolor import cprint
from datetime import datetime
import os
from pygame import mixer
from dotenv import load_dotenv


ON_HEROKU = os.environ.get('ON_HEROKU')
SLEEP_TIME = 60
load_dotenv()
ChatID = os.getenv('ChatID')
TokenID = os.getenv('TokenID')
TelegramURL = 'https://api.telegram.org/bot' + TokenID + \
    '/sendMessage?chat_id=' + ChatID + '&text={}'

CowinAPI = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
Date = str(datetime.now().day) + '-' + \
    str(datetime.now().month) + '-' + str(datetime.now().year)
Pincode = os.getenv('Pincode')
PARAMS = {
    'pincode': Pincode,
    'date': Date
}

requests.get(TelegramURL.format("App has been Started!"))
mixer.init()
mixer.music.load('./sound/dingdong.wav')
mixer.music.play(0)

while True:

    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    port = os.getenv('PORT', default=8000)

    response = requests.get(CowinAPI, PARAMS, headers={
        "Host": 'cdn-api.co-vin.in',
        "Accept": "application/json",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    })
    if(response.ok):
        responseData = response.json()
        if len(responseData["sessions"]) == 0:
            print("No Slots is yet Scheduled for : " + Date)
            print("Last Checked at " + str(datetime.now()))
            pass
        else:
            for slot in responseData["sessions"]:
                if slot["available_capacity_dose1"] + slot["available_capacity_dose2"] + slot["available_capacity"] > 1:
                    mixer.music.load("./sound/airraid.wav")
                    mixer.music.play(0)
                    cprint(str(slot["name"]) + ' (for ' +
                           str(slot["min_age_limit"]) + '+)', 'red', attrs=['reverse', 'blink'])
                    requests.get(TelegramURL.format(str(slot["name"]) + ' (for ' +
                                                    str(slot["min_age_limit"]) + '+)'))

                else:
                    cprint(str(slot["name"]) + ' (for ' +
                           str(slot["min_age_limit"]) +
                           ") is FULL", "white", "on_blue", attrs=['reverse', 'blink', 'bold'])
    else:
        print("No Response, Check Your Internet Connection or Server is not working")
        requests.get(TelegramURL.format("Something's Wrong"))
        sleep(SLEEP_TIME * 2)
    sleep(SLEEP_TIME)


# https://api.telegram.org/bot1590616085:AAEfA3E7sGZl_SpjeEw13L9ojr2gYhIvstg/getUpdates to get the chat id
# https://api.telegram.org/bot1590616085:AAEfA3E7sGZl_SpjeEw13L9ojr2gYhIvstg/sendMessage?chat_id=-490139406&text="This is the message"
