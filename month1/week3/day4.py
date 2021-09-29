# def rec(x):
# 	print(x)
# 	rec(x+1)
# rec(1)


# def rec(x):
# 		if x<10:
# 				print(x)
# 				print(x+1)
# 				print(x)
# rec(1)


# import sys
# print(sys.getrecursionlimit())


# def itc(x):
# 	if x<=1:
# 		return 1
# 	else:
# 		return x * itc(x-1)
# c = itc(int(input('vedite chislo: ')))
# print(c)


# пример ламбда
# a = (lambda x,b:(x+b))(10,5)
# print(a)


# def ok(x):
# 	def ot():
# 			print('start....')
# 			x()
# 			print('stop...')
# 	return ok
# @ok
# def ki():
# 	print('step...')
# ki()
#-------------------------------



# a = (lambda x,b,t:(x*b*t))(10,5,7)
# print(a)


# a = (lambda c:(223))
# print(a)


# gh = (lambda a, b: a-b) (365, 223)
# print('до нг осталось:', gh)



# a = int(input('ведите число: '))
# print(all([int(x)%2!=0 for x in str(a)]))


# def num(a):
# 	print(a)
# 	if a % 2 ==0:
# 		return a
# 	else:
# 		num(a+2)
# num(1)


# def fil(a):
# 	print(a)
# 	if a == set():
# 		return a
# 	else:
# 		a.pop()
# 		return fil(a)
# d = {'btr, 2e'}
# fil(d)


# def avtorizatsiy(x):
#   login = input("Ведите логин : ")
  # password = input(" Ведите пороль: ")
#   x(login,password)
# @avtorizatsiy
# def regist(login,password):
#   k = 0
#   for i in login:
#     print(k+ord(i))
#     break
#   for i in password:
#     print(k+ord(i))
#     break


# import random 
# from random import randint
# def gen():
# 	listt = []
# 	i = 0
# 	for i in range(100):
# 		a = random.randint(10, 50)
# 		listt.append(a)
# 		i+=1
# 	print(listt)
# gen() 