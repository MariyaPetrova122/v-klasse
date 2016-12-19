import re
a = open('input.txt','r', encoding='UTF-8').read()
reg = re.compile('[a-яА-Я0-9]+|[.,;:?!]')
k = reg.findall(a)
print(k)

