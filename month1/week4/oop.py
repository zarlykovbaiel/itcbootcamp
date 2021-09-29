# class Animal:
# 	def inits(self):
# 		print('Идет звук')
# class Cat(Animal):
# 	def kok(self):
# 		print('Мяу мяу вставай')
# class Dog(Animal):
# 	def kok(self):
# 		print('гаф гаф вставай')
# a = Cat()
# a.inits()
# a.kok()

# b = Dog()
# b.inits()
# b.kok()


#Без __init__

# class Chool:
# 	def gith(self):
# 		print('Перемена')
# class kabinet4(Chool):
# 	def et(self):
# 		print('Кабинет4 вышла на перемену')
# class director(Chool):
# 	def gt(self):
# 		print('Директор  идет')
# a = kabinet4()
# a.gith()
# a.et()

# b = director()
# b.gith()
# b.gt()


# #----С __init__


# class Call:
#         def __init__(self, name, club):
#                 self.name = name
#                 self.club = club
#         def Calls(self):
#         	print('My name is', self.name, 'my club', self.club)
# p = Call('Messi', 'psg')
# p.Calls()



# class Car:
# 	def Car(self, marka"Bmw", model = "X3", year = "2003"):
# 		self.marka = marka
# 		self.model = model
# 		self.year = year
# a = 


# class Animal:
# 	def voice(self):
# 		print('music')

# class Dog():
# 		def voice(self):
# 			print('gaf')

# class Cat():
# 	def voice(self):
# 		print('mya')

# cat1 = Cat()
# dog1 = Dog()
# a = Animal()
# farm = [cat1, dog1, a]
# for i in(cat1, dog1, a):
# 	i.voice()


# class Country:
#     def capital(self):
#         print('Capital')
#     def language(self):
#         print('Language')

# class USA(Country):
#     def capital(self):
#         print('Washington')
#     def language(self):
#         print('English')

# class Italy(Country):
#     def capital(self):
#         print('Milan')
#     def language(self):
#         print('Italian')

# obj_usa = USA()
# obj_it = Italy()
# obj_count = Country()
# for i in(obj_count, obj_usa, obj_it):
#     i.language()
#     i.capital()







# #  У меня есть класс с названием Person
# class Person:
#     #Я хочу чтобы он добавлял некие атрибуты в данном случае это имя
#     def init(self, name):   
#         # и вызываю атрибут (экземпляр класса)
#         self.name = name

# # создаю Метод и добавляю запись
#     def talk(self):             
#         return 'Lets go'
# # Тут я создаю дочерний класс и назывю Америка
# class American(Person):
#     # И беру метод точно такой же как и в родительском и  это уже называется Полиморфизмом
#     def talk(self):
#         # И даю ему запись
#         return 'Hello, Do you speak English?'
# #Создаю класс и наследуюсь от Родительского класса
# class Russian(Person):
#     # И вызываю тот же метод одноименный и это есть полиморфизм когда я называю определенный метод и перезаписываю его как хоччу
#     def talk(self):
#         # И идет запись
#         return 'Привет, а ты говоришь по русский?'

# # тут я поленился давать несколько переменных и использую одну которая будет принимать значение моего атрибута
# tourists = [American('Martin'), Russian('Григорий')]
# # Тут я прописываю цикл который пройдется по каждому указанному классу и выведет
# for tourist in tourists:
#     # name + talk  Тоесть условие которое я задаю
#     print(tourist.name + ':  ' + tourist.talk())




# class Vade:
#     def village(self):
#         print('Village')
#     def districts(self):
#         print('Districts')

# class Talas():
# 	def districts(self):
# 		print('Bakay-Ata')
# 	def village(self):
# 		print('Orlovka')

# class Street():
# 	def districts(self):
# 		print('Shkolnyi')
# 	def village(self):
# 		print('Kainazar')

# ddr_tsl = Talas()
# ddr_ste = Street()
# ddr_vad= Vade()
# for i in(ddr_vad, ddr_tsl, ddr_ste):
#     i.village()
#     i.districts()



# users = ('adinai', 'dastan', 'ermek')
# print(users[1])

# names = (1,12.5, 'Joomart', 3, 'danchik')
# print(names[4:5])