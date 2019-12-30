import os
import time as t

cur_dir_1 = os.getcwd()
print(cur_dir_1)
dir = input("Insert the directory path: ")
os.chdir(dir)
cur_dir_2 = os.getcwd()
print(cur_dir_2)
os.mkdir('new_dir_by_python')
os.chdir(cur_dir_1)
t.sleep(5)
os.rename('D:/Practise/Docker/Training/Day 2 Labs.txt','Day_2_lab.txt')




