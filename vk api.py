import urllib.request
import json

req = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id=-55284725&post_id=332258&count=10') 
with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')

data = json.loads(result)



f = open('com.sql','w', encoding='UTF-8')

f.write('CREATE TABLE comments (id_post INTEGER,cid INTEGER,uid INTEGER,text VARCHAR);'+'\n') #создаем таблицy
r=1

while (r<11):
    comment_id = data['response'][r]['cid']
    user_id=data['response'][r]['uid']
    post_id=332258
    comment=data['response'][r]['text']
    f.write('INSERT INTO comments(id_post,cid,uid,text) VALUES ('+str(post_id)+','+str(comment_id)+','+str(user_id)+',"'+str(comment)+'");'+'\n')#добавляем значения в поля
    r+=1

f.close()

