import requests
import time
import threading
import random

"""
Change This fields and Your are set to Rock! (Script works, but you may have difficulty finding correct details, only 4 needed. Make an issue, I will help.)
url: your form url # URL must be response URL, sample is provided
Referer: Take by Filling a response
Cookie: Take by filling a response
DATA: Fill a form and find it :)
proxys: fresh proxys (Use fastProxy library from PyPi... made my me :))
"""


URL = 'https://docs.google.com/forms/d/e/1FAIpQLScV70rqvGjDwLnPUJ-YdMNF0I_gVTXpT0_hLtVRL_yLb4ljBA/formResponse'
#'https://docs.google.com/forms/d/e/1FAIpQLScV70rqvGjDwLnPUJ-YdMNF0I_gVTXpT0_hLtVRL_yLb4ljBA/formResponse'
DATA = 'entry.1893802898_sentinel=&entry.1893802898=Option+1&entry.1893802898=Option+3&entry.1436081212=Option+2&entry.2046702074=short+answer+goes+here&fvv=1&draftResponse=%5Bnull%2Cnull%2C%22-5913095039686218102%22%5D%0D%0A&pageHistory=0&fbzx=-5913095039686218102'
#'entry.2046702074=answer2&fvv=1&draftResponse=%5Bnull%2Cnull%2C%22700526258680781707%22%5D%0D%0A&pageHistory=0&fbzx=700526258680781707'
REFERER = 'https://docs.google.com/forms/d/e/1FAIpQLScV70rqvGjDwLnPUJ-YdMNF0I_gVTXpT0_hLtVRL_yLb4ljBA/viewform?fbzx=-5913095039686218102'
#'https://docs.google.com/forms/d/e/1FAIpQLScV70rqvGjDwLnPUJ-YdMNF0I_gVTXpT0_hLtVRL_yLb4ljBA/viewform?fbzx=700526258680781707'
COOKIE ='S=spreadsheet_forms=BXegCHIeTgQU35TMDuO3W3FH3gtwNp9-iSHEQzpAbBk; NID=204=0FF1LfU_6hGdFzv1hsouk65EaU5Be-thZaJpwAIsXsCRMdSoVc7AY_7zicFPrJGdz7bv4Z9ootULJZSaTs91yy4-qAsqVNUEbLCHGR14rIP2hzfnPUIvaXftvt8N1d-AbZY8ZoZSyGB5uTeursGLP7tjGwVUdd_oJcuvFikuzfw'
#'S=spreadsheet_forms=BXegCHIeTgQU35TMDuO3W3FH3gtwNp9-iSHEQzpAbBk; NID=204=ecClXfGHi-YRCDrpb8AbnBtxNexVQUE-ypUTe-fnrRz27zOesoZ0rWzdVxibZn9Ous_oekVOdLsLmsHMWCJwfmJEZkbfXPugn-wZgzhWjgC_trelE25Dt7hZ4lsgadBy6SJEhwbC_FD-6i_ckwpgBzFjsSacjA0pUpoE8lNtfu8; 1P_JAR=2020-05-23-16'


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


proxys = ['144.217.101.242:3129', '192.41.71.204:3128', '192.41.13.71:3128', '104.154.143.77:3128', '205.126.14.166:8009', \
           '205.126.14.170:8009', '205.126.14.171:8009', '163.172.189.32:8811', '134.122.67.188:3128', '51.158.180.179:8811', \
           '163.172.136.226:8811', '80.187.140.26:8080', '205.126.14.167:8009', '51.158.107.202:8811', '51.158.78.179:8811', \
           '163.172.146.119:8811', '51.158.68.26:8811', '188.165.16.230:3129', '51.158.186.242:8811', '95.179.200.239:30963', \
           '139.180.184.204:3128', '91.202.240.208:51678', '81.16.10.141:38132', '82.200.233.4:3128', '202.40.177.69:80', \
           '139.162.47.109:143', '91.230.227.168:3128', '51.158.123.35:8811', '103.81.114.182:53281']




def trouble():
    try:
        proxy = proxys[random.choice([x for x in range(len(proxys))])]
        r = requests.post(URL, proxies={'http':proxy, 'https':proxy}, data=DATA, headers=HEADER)
        print(r.status_code)
    except Exception as e:
        print(str(e))

while True:
    threading.Thread(target=trouble).start()
