#import  my_module.py
#print('Я функция из my_module.py')
#print(my_module.py2)


#import random
#names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
#print(random.sample(names, 4))


#import sys
#print(sys.platform)


#def func():
#     pass
#print(func())


#import os
#import random
#os.mkdir('kole')
#i = 0
#while i<5:
#	o=random.randint(0,100)
#	os.mknod(f'/home/baiel/kole/1{o}txt')
#	i = i+1
#	print(i)



from random import sample
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
i = 0
while i < 4:
	o = (sample(names,13))
	i+=1
	print(o)