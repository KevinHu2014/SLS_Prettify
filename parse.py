# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml

import codecs
f=codecs.open("data.html", 'r', 'utf-8')
#print f.read()

soup = BeautifulSoup(f.read(),'lxml')

#content = soup.select('span[class=UFICommentBody] a')[1].get_text()
s = ""
i = 0
# # #可以抓到所有的u tag
for child in  soup.select('span[class=UFICommentBody] a'):
     #print (child.get_text()) #檢查URL 用
     i = i + 1
     #print i
     s = s + "\"" + child.get_text() + "\","

# print (s)

s = "var arr = [" + s + "];"
print (s)

#print content
#print str(content).decode("unicode–escape")
