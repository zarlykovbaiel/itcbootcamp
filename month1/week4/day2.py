# class Cars:
#         def notting(self):
#                 pass
# class Moto(Cars):
#         def mpting(self, world):
#                 print(world + '!')
# a = Moto()
# a.mpting('hello')

# #------------------------------------

# class Person:
#         name = 'Vlad'
#         age = '23'

#         def __setr(self, name, age):
#                 self.name = name
#                 self.age = age
# class Student(Person):
#         course = 2
# a = Student()
# a._Person__setr('Vlad', 24)
# a.course = 3
# print(a.course)


# #------------------------------------------------


# class Factory:
#         def enfgine(self):
#                 return 'Двигатель готовы'
#         def bride(self):
#                 return 'Ходовая часть готова'
# q = Factory()
# print(q.enfgine())
# print(q.bride())

# class Toyota(Factory):
#         def weels(self):
#                 return 'Колеса готовы'
#         def window(self):
#                 return 'Стекла готовы'
# w = Toyota()
# print(w.weels())
# print(w.window())
# k = [q.enfgine(), q.bride(), w.weels(), w.window()]
# print(k)

# #--------------------------------------------------------

# class Phone:
#         username = 'Baiel'
#         __number = '999-999'

#         def call(self):
#                 print('Ring- Ring')
#         def __turn_on(self):
#                 print('Num on:', self.__number)
# myphone = Phone()
# myphone._Phone__turn_on()
# print(dir(myphone))
# myphone.call()


#------------------------------------------------------


# class Zoo:
#         def __init__(self, animal_1 = "Тигр",animal_2 = "Бегемот",animal_3 = "Лев"):
#                 self.animal_1 = animal_1
#                 self.animal_2 = animal_2 
#                 self.animal_3 = animal_3
#                 self.animal_4 = [animal_2,animal_3]

# p = Zoo()
# print(p.animal_1, p.animal_2, p.animal_3,)
# p.animal_1 = "Лев"
# p.animal_3 = "Змея"
# print(p.animal_1, p.animal_2, p.animal_3,"\n",p.animal_4)



