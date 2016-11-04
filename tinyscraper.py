#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import urllib, urllib2, re
from cookielib import CookieJar
from bs4 import BeautifulSoup
'''
Test code for obtaining web page
Thanks to: https://github.com/luzhijun/weiboSA
'''
# email = raw_input('Email: ')
# passwd = raw_input('Passwd: ')
# login_data = urllib.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'weibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# 
# req = urllib2.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# try:
#     response = urllib2.urlopen(req, data=login_data.encode('utf-8'))
# except urllib2.HTTPError as e:
#     print 'The server couldn\'t fulfill the request.'
#     print 'Error code: ', e.code
# except urllib2.URLError as e:
#     print 'We failed to reach a server.'
#     print 'Reason: ', e.reason
# else:
#     the_page = response.read()
#     print the_page

'''
Test code for Cookiejar
'''
# cookie = CookieJar()
# cookie_support = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(cookie_support)
# opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+':'+item.value)

'''
Test code for getting cookie from xici
'''
headers=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome'),
        ('Host', 'www.xicidaili.com'),
        ('Referer', 'http://www.xicidaili.com/n')]
def getCookie():
    cookie = CookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookie_support)
    opener.addheaders = headers
    opener.open('http://www.xicidaili.com/')
    return cookie

'''
Test code for BeautifulSoup
'''
html = urllib2.urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html,"lxml")
for pic in bs.find_all('img', {'src':re.compile(".*\.jpg$")}):
    print(pic['src'])

'''
Extract ips from Xici & save to local proxy.txt
'''
cookie = getCookie()
# Get the proxy
with open('proxy.txt', 'w') as f:
    for page in range(1,1103):
        if page%50 == 0: # Refresh cookie every 50 pages
            print 'Refresh cookie and now starting crawling page%d' %(page)
            cookie = getCookie()
        url = 'http://www.xicidaili.com/nn/%s' %page
        cookie_support = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookie_support)
        urllib2.install_opener(opener)
        req = urllib2.Request(url, headers=dict(headers))
        content = urllib2.urlopen(req)
        soup = BeautifulSoup(content, "lxml")
        trs = soup.find('table', id="ip_list").findAll('tr')
        for tr in trs[1:]:
            tds = tr.findAll('td')
            ip = tds[1].text.strip()
            port = tds[2].text.strip()
            protocol = tds[5].text.strip()
            f.write('%s://%s:%s\n' %(protocol, ip, port))
