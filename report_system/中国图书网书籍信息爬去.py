# -*- coding: utf-8 -*-
import requests
import re
import os

os.chdir(r'C:\Users\super\Desktop')

url = 'http://www.bookschina.com/book_find2/?stp=python'
content = requests.get(url).text
title = re.findall('jpg" alt="(.*?)"', content)
author = re.findall('class="author">(.*?)</a>', content)
pubhouses = re.findall('class="publisher">(.*?)</a>', content)
pubtime = re.findall('title="出版时间">(.*?)&nbsp;&nbsp', content)
raw_price = re.findall('<del class="">(.*?)</del>', content)
now_price = re.findall('<span class="sellPrice">(.*?)</span>', content)
discount = re.findall('<span class="discount">\((.*?)\)</span>', content)
author[-7]='蔡立X'
file = open('books.csv', 'a', encoding='utf-8')
for i in list(range(0, 10)):
    file.write(
        ','.join((title[i], author[i], pubhouses[i], pubtime[i], raw_price[i], now_price[i], discount[i])) + '\n')
	# print(title[i],author[i],pubhouses[i],pubtime[i],ISBN[i],raw_price[i],now_price[i],jiesheng[i],discount[i])
file.close()

# BeautifulSoup方法
import requests
from bs4 import BeautifulSoup

url = 'http://www.bookschina.com/book_find2/?stp=python'
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

res = soup.find_all('div', attrs={'class': 'wordContent'})
for i in res:
    title = i.find_all('a')[0].text
    author = i.find_all('a')[1].text
    pubhouse = i.find_all('a')[2].text
    text = i.find_all('br')[2].text
    pubtime = text[text.find('：') + 1:text.find('ISBN：') - 1]
    ISBN = text[text.find('ISBN：') + 6: text.find('原价：￥')]
    raw_price = text[text.find('原价：￥') + 4: text.find('现价')]
    now_price = text[text.find('现价') + 4: text.find('现价') + 9]
    diff = text[text.find('您节省：') + 5: text.find('您节省：') + 9]
    discounts = text[-4:-1]
    print(title, author, pubhouse, pubtime, ISBN, raw_price, now_price, diff, discounts)

# 写入txt文档
import requests
from bs4 import BeautifulSoup

url = 'http://www.bookschina.com/book_find2/?stp=python'
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

res = soup.find_all('div', attrs={'class': 'wordContent'})
file = open('Chinese Lib Net.txt', 'w', encoding='utf-8')
for i in res:
    title = i.find_all('a')[0].text
    author = i.find_all('a')[1].text
    pubhouse = i.find_all('a')[2].text
    text = i.find_all('br')[2].text
    pubtime = text[text.find('：') + 1:text.find('ISBN：') - 1]
    ISBN = text[text.find('ISBN：') + 6: text.find('原价：￥')]
    raw_price = text[text.find('原价：￥') + 4: text.find('现价')]
    now_price = text[text.find('现价') + 4: text.find('现价') + 9]
    diff = text[text.find('您节省：') + 5: text.find('您节省：') + 9]
    discounts = text[-4:-1]
    file.write('\t'.join((title, author, pubhouse, pubtime, ISBN, raw_price, now_price, diff, discounts)) + '\n')
    print(title, author, pubhouse, pubtime, ISBN, raw_price, now_price, diff, discounts)
file.close()

# 写入数据库
"""
DROP TABLE IF EXISTS books ;
CREATE TABLE books(
title VARCHAR(50),
author VARCHAR(50),
pubhouse VARCHAR(20),
pubtime VARCHAR(20),
ISBN VARCHAR(20),
raw_price VARCHAR(10),
now_price VARCHAR(10),
diff VARCHAR(10),
discounts VARCHAR(10)
);
"""
# 查询语句
# SELECT * FROM books;

import requests, pymysql
from bs4 import BeautifulSoup

s1 = 'http://www.bookschina.com/book_find2/default.aspx?pageIndex='
s2 = '&stp=python&dmethod=all&sType=0'
urls = []
for i in list(range(1, 7)):
    urls.append(s1 + str(i) + s2)

for url in urls:
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    res = soup.find_all('div', attrs={'class': 'wordContent'})

    for i in res:
        title = i.find_all('a')[0].text
        author = i.find_all('a')[1].text
        pubhouse = i.find_all('a')[2].text
        text = i.find_all('br')[2].text
        pubtime = text[text.find('：') + 1:text.find('ISBN：') - 1]
        ISBN = text[text.find('ISBN：') + 6: text.find('原价：￥')]
        raw_price = text[text.find('原价：￥') + 4: text.find('现价')]
        now_price = text[text.find('现价') + 4: text.find('现价') + 9]
        diff = text[text.find('您节省：') + 5: text.find('您节省：') + 9]
        discounts = text[-4:-1]
        print(title, author, pubhouse, pubtime, ISBN, raw_price, now_price, diff, discounts)
        # 创建连接
        connect = pymysql.connect(host='localhost', user='root', password='A,378125,z', port=3306, database='mysql',
                                  charset='utf8')

        cursor = connect.cursor()
        sql = '''insert into books(title,author,pubhouse,pubtime,ISBN,raw_price,now_price,diff,discounts) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cursor.execute(sql, (title, author, pubhouse, pubtime, ISBN, raw_price, now_price, diff, discounts))
        connect.commit()
        cursor.close()
        connect.close()