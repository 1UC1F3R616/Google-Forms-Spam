# internal imports
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# external imports
import requests


"""
Change 4 Fields (Compulspory) | 3 Fields are optional | Sample Video on where and how to find them is available in Readme.

URL: your form url # URL must be response URL, sample is provided
REFERER: Take by Filling a response
COOKIE: Take by filling a response
DATA: Fill a form and find it :)

PROXYS: You can provide proxies also.
MAX_WORKERS: Change this value to increase the speed of spam. Don't go beyond 500.
SPAM_COUNT: Change this to increase spam count
"""

MAX_WORKERS = 63 # Change this value to increase the speed of spam. Don't go beyond 500.
SPAM_COUNT = 100000 # Change this to increase spam count

URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfwUwWtRlWXEoUjKZPm_uRo4_sG-3xc6g5HEK7l2kP3A7dZHQ/formResponse'

DATA = 'entry.1859015008=%D0%9C%D1%83%D0%B6%D1%81%D0%BA%D0%BE%D0%B9&entry.588683882=18-25&entry.1970350708=%D0%A1%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%82&entry.1050667952=%D0%A2%D1%8E%D0%BB%D1%8C%D0%BF%D0%B0%D0%BD%D1%8B%2C+%D0%B3%D0%B2%D0%BE%D0%B7%D0%B4%D0%B8%D0%BA%D0%B8%2C+%D0%BB%D0%B8%D0%BB%D0%B8%D0%B8&entry.896433706=%D0%91%D1%83%D0%BA%D0%B5%D1%82&entry.210249492=%D0%A0%D0%B5%D0%B4%D0%BA%D0%BE&entry.694777093=%D0%A1+%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E+%D0%BE%D0%B1%D1%8B%D1%87%D0%BD%D0%BE%D0%B3%D0%BE+%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD%D0%B0&entry.1082732336=%D0%9A%D0%B0%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE+%D0%B8+%D1%81%D0%B2%D0%B5%D0%B6%D0%B5%D1%81%D1%82%D1%8C+%D0%B1%D1%83%D0%BA%D0%B5%D1%82%D0%B0&entry.1082732336=%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D1%8C&entry.1082732336=%D0%A3%D1%80%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C+%D0%BE%D0%B1%D1%81%D0%BB%D1%83%D0%B6%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+%D0%B8+%D0%B4%D0%BE%D0%B1%D1%80%D0%BE%D0%B6%D0%B5%D0%BB%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C+%D1%81%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2&entry.1082732336=%D0%9E%D1%80%D0%B8%D0%B3%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C+%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D0%BC%D1%8B%D1%85+%D1%83%D1%81%D0%BB%D1%83%D0%B3&dlut=1679826024337&entry.1859015008_sentinel=&entry.588683882_sentinel=&entry.1970350708_sentinel=&entry.1050667952_sentinel=&entry.896433706_sentinel=&entry.210249492_sentinel=&entry.694777093_sentinel=&entry.1082732336_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-8424303833300430537%22%5D&pageHistory=0&fbzx=-8424303833300430537'

REFERER = 'https://docs.google.com/forms/d/e/1FAIpQLSfwUwWtRlWXEoUjKZPm_uRo4_sG-3xc6g5HEK7l2kP3A7dZHQ/viewform?fbzx=-8424303833300430537'

COOKIE = 'S=spreadsheet_forms=_H_WPe1OQrTuPl-YsivQVRE6e1rCVTbmqpgI4hSA2b4; COMPASS=spreadsheet_forms=CjIACWuJV6ITi5gccDo16kIhJ224f_40cZ15swaL5Ibb7DovX6EQ9nRdRH2QiBrjghwtQhDT04ChBho0AAlriVf6iSUBiL8v1dHpgxpWpA-yW2jUqXwkMNS784FQZVEMVC5uQfGS1uCHXbseFvXTXg==; NID=511=HEbVtPsvPO8tbqVvFsudzBhFnKr4_TXX2RENd0U9YOug4BpcFKoIX5yRszZDU7IbDL2Qb1GNt6gvc169mxezzxLmVJ3edCG7Wq0lP_ArHBlauRY9jVcOx38999JKzdhCLKA-0fGj8FjE86Hc93pMXiGeEQcpJMqLFWOzoYwPXoYZSJ8JFWGF4ebP7MjB0s0wVHuLwg7FX-wHZixaGafSK_SrhoxX8NSt; SID=UwjTIvHiSAsj9vBWjnZPZubxdskor7_X5ewYDfPSQBhNG8L_9NNVWdwx0WLxqDec_8m7vw.; __Secure-1PSID=UwjTIvHiSAsj9vBWjnZPZubxdskor7_X5ewYDfPSQBhNG8L_beUrYwsRhNTMw9bpskhYwg.; __Secure-3PSID=UwjTIvHiSAsj9vBWjnZPZubxdskor7_X5ewYDfPSQBhNG8L_EEYrAuEO6KhJ-v5nQFmA7A.; HSID=AUWtfxiMx1BgyiCDj; SSID=AAztMach6xIoQEJOW; APISID=Q8I0bfyIl8arLBY3/AHua7Lbce16GzJCOu; SAPISID=-TqQBUMRbw0MML8B/AJRMRYtbmlKt8aLR2; __Secure-1PAPISID=-TqQBUMRbw0MML8B/AJRMRYtbmlKt8aLR2; __Secure-3PAPISID=-TqQBUMRbw0MML8B/AJRMRYtbmlKt8aLR2; OTZ=6958632_44_44_123780_40_436260; SIDCC=AFvIBn8j4G_C-yXGxtC_dCNppatpNw2737gjFP2T9LbEA6Z1nW7J98h9UDYAZWP4_iHyU1hkuQ; __Secure-1PSIDCC=AFvIBn9TDs3Tp-C6gvg-7nTCUd2t1D2DBzpLLVwpGxpU6VUQw-lrv_kodYen2zqu6OPnJVg2K5g; __Secure-3PSIDCC=AFvIBn8rc2cABbf8A31Yh5tQMoymAVbxEk_G24HoWUhtkBPmMT-CjLw93MOvfypgeUNw34RHHQ'


HEADER = {
    'Host': 'docs.google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://docs.google.com',
    'Referer': REFERER,
    'Cookie': COOKIE,
    'Upgrade-Insecure-Requests':'1'
    }

# After 4.8K+ requests google will ask you to fill a captcha if you are not using proxy.
PROXYS = []
# PROXYS = ['144.217.101.242:3129', '192.41.71.204:3128', '192.41.13.71:3128', '104.154.143.77:3128']




def trouble():
    try:
        if len(PROXYS) > 0: # Proxies are passed
            proxy = PROXYS[random.choice([x for x in range(len(PROXYS))])]
            r = requests.post(URL, proxies={'http':proxy, 'https':proxy}, data=DATA, headers=HEADER)
        else:
            r = requests.post(URL, data=DATA, headers=HEADER)
        return r
    except Exception as e:
        raise Exception (e)


if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_calls = {executor.submit(trouble): count for count in range(SPAM_COUNT)}

        for future in as_completed(future_calls):
            try:
                result = future.result()
                print('[-] {}'.format(result.status_code))
            except Exception as e:
                print('[!] {}'.format(e))
