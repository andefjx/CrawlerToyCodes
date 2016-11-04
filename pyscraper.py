#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Toy codes from the book Web Scraping with Python
'''
from urllib2 import urlopen, HTTPError
from bs4 import BeautifulSoup
import datetime, random, re

'''
Toy example from the book showing basic moves
'''
# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html, "lxml")
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
# 
# title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)

'''
Toy example of HTML Parsing
'''
# random.seed(datetime.datetime.now()) # Set random number generator seed with the current system time, ensuring a nwe random path through Wikipedia articles every time the program is run
# def getLinks(articleUrl):
#     try:
#         html = urlopen("http://en.wikipedia.org"+articleUrl)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html, "lxml")
#     except AttributeError as e:
#         return None
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
# 
# links = getLinks("/wiki/Kevin_Bacon")
# 
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)

# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html, "lxml")
#     for link in bsObj.find_all("a", href=re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 # We have encountered a new page
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
# getLinks("")
