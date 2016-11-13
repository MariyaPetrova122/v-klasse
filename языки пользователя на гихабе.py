import json
import urllib.request

user = "nevmenandr"  # пользователь, про которого мы хотим что-то узнать
url = 'https://api.github.com/users/%s/repos' % user  
# по этой ссылке мы будем доставать джейсон, попробуйте вставить ссылку в браузер и посмотреть, что там

response = urllib.request.urlopen(url)  # посылаем серверу запрос и достаем ответ
text = response.read().decode('utf-8')  # читаем ответ в строку
data = json.loads(text) # превращаем джейсон-строку в объекты питона
n_language={}
for i in data:
    print(i['language'])
for i in data:
    b=i['language']
    if b in n_language:
        a =int(n_language[b])
        a+=1
        n_language[b]=str(a)
    else:
        n_language[b]="1"
    
print(n_language)
        
