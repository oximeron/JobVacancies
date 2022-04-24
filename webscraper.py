#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:50:22 2022

@author: lastcoder
Web-Scraper 0.0.2
TODO: implement statistics by websites about vacancies in internet(jooble, 
dou, work, rabota, etc)

"""
import matplotlib.pyplot as plt
import urllib.parse
import requests
from bs4 import BeautifulSoup

"""JOOBLE SCRAPER"""
vac_info_dict = {}
vacancies = []
lang_reqs = ['python','java','scala','c#','c++','javascript','c',
             'r','ruby','swift', 'go', 'sql']
for l in range(len(lang_reqs)):
    lang_reqs[l] = urllib.parse.quote_plus(lang_reqs[l])
    
sites = [f"https://ua.jooble.org/SearchResult?ukw={i} developer" for i in lang_reqs]
  
#Start scraping
for site in sites:
    req = requests.get(site)
    status = req.status_code
    if status == 200:
        print("[Requesting web page: OK]")
        soup = BeautifulSoup(req.content, "html.parser")    
        vacancie = soup.find("div",class_= "_303e9a")
        lang = urllib.parse.unquote_plus(lang_reqs[sites.index(site)])
        vacancies.append(f"""{vacancie.text[:6]} - {lang}""")
        value = str(vacancie.text[:2]) + str(vacancie.text[3:6])
        vac_info_dict[lang] = int(value)
    else:
        print(f"[Requesting web page: Error:Code {status}]")
        continue
    
text = "".join([f"{i}\n" for i in vacancies])
print(text)
"""END OF JOOBLE SCRAPER"""

"""MAKE PLOT"""

def make_plot_info(names, values, label_name, size):
    plt.figure(figsize=(size[0], size[1]))
    plt.ylabel(label_name)
    plt.bar(names, values)
    
names = vac_info_dict.keys()
values = vac_info_dict.values()
label = "Jooble.com Vacancies" 
size = (9, 3)   
    
make_plot_info(names, values, label, size)