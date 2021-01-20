#!/usr/bin/env python
# encoding: utf-8
# Covid19 Daily Status
# By davidhayter

import json
from bs4 import BeautifulSoup as bs
import requests


# Colors
RED = "\033[31m"
WHITE = "\033[39m"

URL = "https://covid19.saglik.gov.tr"

try:
    html = requests.get(URL)

    # Parsing operations
    parsed_html = bs(html.text, "html.parser")

    # Receiving data from script tag in HTML.
    scriptTagData = str(parsed_html.find_all("script", {"type":"text/javascript"})[-1])

    # Splitting data
    splittedData = scriptTagData.split()

    # Slicing operation to convert data to suitable format.
    lastTagData = str(splittedData[6][:-6][1:-1] )

    # Preparation phase for the transition to JSON.
    dictDataforJson = lastTagData.replace('"', "\"")

    # JSON data
    jsonData = json.loads(dictDataforJson)

    date = jsonData.get('tarih')
    dailyCaseCount = jsonData.get('gunluk_vaka')
    dailyPatientCount = jsonData.get('gunluk_hasta')
    dailyDeathCount = jsonData.get('gunluk_vefat')
    dailyHealingCount = jsonData.get('gunluk_iyilesen')

    totalPatientCount = jsonData.get("toplam_hasta").split(".")
    totalPatientCount = int("".join(totalPatientCount))

    totalHealingCount = jsonData.get("toplam_iyilesen").split(".")
    totalHealingCount = int("".join(totalHealingCount))


    print(f"{RED}[+] Tarih: {WHITE}{date}")
    print(f"{RED}[+] Açıklanan günlük vaka sayısı: {WHITE}{dailyCaseCount}")
    print(f"{RED}[+] Açıklanan günlük hasta sayısı: {WHITE}{dailyPatientCount}")
    print(f"{RED}[+] Açıklanan günlük vefat sayısı: {WHITE}{dailyDeathCount}")
    print(f"{RED}[+] Açıklanan günlük iyileşen vaka sayısı: {WHITE}{dailyHealingCount}")

    print("-" * 50)

    print(f"{RED}[+] Toplam hasta sayısı: {WHITE}{totalPatientCount - totalHealingCount}")

except Exception as errMessage:
    print(f"Error! Message: {errMessage}")
