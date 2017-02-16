
# coding: utf-8

# In[10]:

from bs4 import BeautifulSoup
from urllib.request import urlopen 

#芸能人一覧
url = "http://www.weblio.jp/ontology/%E6%97%A5%E6%9C%AC%E3%81%AE%E8%8A%B8%E8%83%BD%E4%BA%BA_1"

# urlopen()でデータを取得 --- (※1)
res = urlopen(url)

# BeautifulSoupで解析 --- (※2)
soup = BeautifulSoup(res, "html.parser")

# 日本の芸能人一覧を抽出 --- (※1)
actor_actoress_Japan = soup.select(".subCatWordsB")


# In[12]:

#名前の取り出しと列挙
for a in actor_actoress_Japan:
    title = a.get_text()
    print(title)


# In[ ]:



