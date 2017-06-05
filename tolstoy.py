import urllib.request
import re
'''
f = open('tolstoy.txt','a',encoding='utf-8')

def download_page(req):
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        #print(html[:1000])
    f.write(html)

commonUrl = 'http://tolstoy.ru/online/90/'
for i in range(10,20):
    req = commonUrl + str(i)
    download_page(req)
    print(i)

f.close()
'''
f = open('tolstoy.txt','r',encoding='utf-8')
words = f.read()
f.close()

new_words = re.sub('<+?>','',words)
reg = re.compile('[a-яА-Я]+')
clean_words = reg.findall(new_words)
print(clean_words[:1000])
