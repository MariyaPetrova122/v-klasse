import json
import urllib.request

users = ("nevmenandr","elmiram","shwars","JelteF","timgraham","arogozhnikov","jasny","bcongdon","whyisjake")
num_repos={}

for i in users:
    

    url = 'https://api.github.com/users/%s/repos' % i
    
    response = urllib.request.urlopen(url)  # посылаем серверу запрос и достаем ответ
    text = response.read().decode('utf-8')  # читаем ответ в строку
    data = json.loads(text) # превращаем джейсон-строку в объекты питона
    num_repos[i]=(len(data))
print(num_repos)
