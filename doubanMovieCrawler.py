#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from urllib2 import urlopen, HTTPError
from bs4 import BeautifulSoup
import datetime, random, re

pages = set()

'''
Getting movies from Douban using DFS
'''
def getLinks_dfs(pageUrl):
    global pages
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    for link in bsObj.find_all("a", href=re.compile("^(https:\/\/movie\.douban\.com\/subject).*(from=subject-page)$")):
        # We have encountered a new page
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("-----------------\n"+newPage)
                print("Movie Name: %s" %(link.find_all("img")[0].attrs['alt']))
                pages.add(newPage)
                getLinks_dfs(newPage)

getLinks_dfs("https://movie.douban.com/subject/4944008/?tag=%E7%83%AD%E9%97%A8&from=gaia")
