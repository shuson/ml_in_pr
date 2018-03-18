# coding=utf-8

import requests
from bs4 import BeautifulSoup
import codecs
import csv

r = requests.get("http://sg--pr.appspot.com/tableList.jsp")
r.encoding = "utf-8"

"""
since source code of has invalid html <a> tag, replace them
"""
c = r.content.replace(b'</a>', b'')

bs = BeautifulSoup(c, 'html.parser')
trs = bs.select("tr")

f = open('data.csv','w+', encoding="utf-8", newline='')
writer = csv.writer(f)

i = 0
for tr in trs[1:]:
    i+=1
    tds = tr.select('td')
    if len(tds) < 7: continue
    con = tds[5].text.strip().replace('\n', ' ').replace('\r', '')
    result = tds[6].text.strip().replace('\n', ' ').replace('\r', '')
    if len(con) < 4: continue
    if len(result) < 1 or result not in ['通过', '失败']: continue
    
    writer.writerow([con, result])

f.close()
