# -*- coding: utf-8 -*-

# function import BeautifulSoup
from bs4 import BeautifulSoup
# genetic import codecs
import codecs
f = codecs.open("data.html", 'r', 'utf-8')
# print(f.read())


soup = BeautifulSoup(f.read(), 'html.parser')
# print(soup.prettify())


# content = soup.select('span[class=UFICommentBody] a')[1].get_text()
"""
透過 soup.select('span[class=UFICommentBody] a')，
會回傳所有class 為 UFICommentBody之 <span> 下的 <a> 。
由於結果不只一筆，所以回傳的是一個陣列。
透過for去走訪它，而我們需要的只有 <a> tag 裡的文字，
因此用 .get_text() 去取得文字。
"""

s = ""

for child in soup.select('span[class=UFICommentBody] a'):
    s = s + "\"" + child.get_text() + "\","

# print(s)

s = "var arr = [" + s + "];"
print(s)

# print content
# print str(content).decode("unicode–escape")
