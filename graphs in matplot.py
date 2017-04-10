import matplotlib.pyplot as plt
import urllib.request
import json

req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-76982440&count=20') 
with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')

data = json.loads(result)

Y=[]

i=1
while i<20:
    Y.append(data['response'][i]['comments']['count'])
    i+=1


X = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19.20]

#size = [60, 70, 80, 90, 100, 130]
#colors = ['darkred', 'red', 'gainsboro', 'blue', 'olivedrab', 'brown']
plt.bar(X,Y, c='b')
#plt.savefig('plt.png',format='png')


#X2 = [i*2 for i in X]
#Y2 = [i*1.5 for i in Y]

plt.title('Graph')
plt.ylabel('Number of Comments')
plt.xlabel('Comment')


#plt.plot(X2, Y2)

plt.show()

#векторные форматы: eps(!), svg, pdf(если рисунок изначально был нарисован в пдф, а не растровый и вставленный туда)

#задание: скачать инф-ю о количестве постов, отображать на графике кол-во комментариев к каждому посту
