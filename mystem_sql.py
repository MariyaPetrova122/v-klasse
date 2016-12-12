import os
os.system(r'D:\Downloads\mystem.exe -nid C:\input.txt C:\output.txt')

f = open('output.txt', 'r')
a = f.readlines()
f.close()
s_q_l = open('tablemain.sql','w')


