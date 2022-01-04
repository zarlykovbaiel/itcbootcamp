# abjektive = input('Введите прилагательное: ')
# noun = input('введите глагол в прошедшим времени: ')
# print('Этот ', abjektive, noun, 'на ленивию рыжую собаку. ' )

# import turtle
# t = turtle.Pen()
# for x in range(100):
#     t.forward(x)
#     t.left(90)

# from turtle import *
# color ('black')
# begin_fill()
# pensize(3)
# left(20)
# forward(133)
# circle(50, 200)
# right(140)
# circle(50, 200)
# forward(133)
# end_fill()


# from turtle import *
# import turtle
# t = turtle.Turtle()
# t.penup()
# t.goto(0, -90)
# t.pendown()
# t.color('purple')
# style = ('Courieer', 60, 'italic')
# t.write('i miss you', font=style, align='left', move=True)
# t.hideturtle()
# color ('red')
# begin_fill()
# pensize(3)
# left(-300)
# forward(133)
# circle(50, 200)
# right(140)
# circle(50, 200)
# forward(133)
# end_fill()
# turtle.done()

# ===============================================================================

# import random
# die1 = random.randint(1, 6)
# die2 = random.randrange(6)+1
# total = die1 + die2
# print('при вашем броске выпало', die1, 'and', die2, 'очков. в сумме', total)
  
# password
# print('Добро пожаловать к нам в ООО "Системы безопасности". ')
# print('-- Безопасность наше второе имя\n')
# password = input('Введите пароль: ')
# if password == '123':
#     print('Доступ otкрыт')
# else:
#     print('доступ закрыт')


# import random
# print("я ощущаю вашу энергетикую. от моего экрана не скрыто ни одного из ваших чувств.")
# print('и так ваше настроение..')
# mood = random.randint(1, 3)
# if mood == 1:
#     print("радостое")
# elif mood == 2:
#     print('так себе')
# elif mood == 3:
#     print('прескверное')
# else:
#     print('не бывает таеого настроение! (должно быть вы совершенно не в себе.)')
#     print("...Но это только сегодня")


# print("\t добро пожаловать в программу 'симулятор трехлетнего ребенка'\n")
# print("Имутируется рвзговор с маленьким ременком.")
# print("Попробуйте прекратить этот кошмар.") 
# response = ''
# while response != "прекрати":
#     response = input("почему?\n")
# print("а ладно.")


# print("\U0001F917")
# print("\U0001F623")
# print("\U0001F623")
# print('\U0001F618')


# a = 'Hello world'
# print(a)


# import qrcode
# im = qrcode.make("https://files.fm/u/kjx6w8dhw#/view/59gun698u")
# print(type(im))
# im.save('proba1.png')


# ==========================DJANGO==================================
# | 1. СОЗДАНИЕ ПРОЕКТА В ДЖАНГО
# |django-admin startproject nameproject  
# |
# | 2. СОЗДАНИЕ СТАРТ APP
# |python3 manage.py startapp namestartapp
# |
# | 3. СОЗДАНИЕ ВИРТАЛЬНАЯ ОКРУЖЕНИЕ 
# |virtualenv venv
# |
# | 4. АКТИВАЦИЯ
# |source venv/bin/activate
# |
# | 5. ПЕРВАЯ МИГРАЦИЯ
# |python3 manage.py makemigrations
# |
# | 6. ВТОРАЯ МИГРАЦИЯ
# |python manage.py migrate 
# |
# | 7. СОЗДАТЬ ПОЛЬЗОВАТЕЛЯ
# |python manage.py createsuperuser
# |
# | 8. ЗАПУСК СЕРВЕРА
# |python manage.py runserver
# ================================================================


# import dateparser
# from datetime import datetime

# print(dateparser.parse('1 января 2000 года'))
# print(dateparser.parse('через 3 дня'))
# print(dateparser.parse('20 дней назад '))




# a = ('hello')
# print(a)






# a = 'HELLO'
# b = 'jox'
# print(a.lower(), b.upper())



# a = input('Ваше имя: ')
# print('Здравствуйте ' +a, '!')
# b = input('Ваш возраст: ')
# v = input('Какой фильм вам нравится ?: ')
# print('Классный фильм ' +v, '!')






# import turtle
# t = turtle.Turtle()
# t.penup()
# t.goto(0, -90)
# t.pendown()
# t.color('purple')
# style = ('Courieer', 60, 'italic')
# t.write('i miss you', font=style, align='left', move=True)
# t.hideturtle()
# turtle.bgcolor('white')
# turtle.pensize(2)

# def curve():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(1)
# turtle.speed(0)
# turtle.color('red', 'red')

# turtle.begin_fill()
# turtle.left(140)
# turtle.forward(111.65)
# curve()

# turtle.left(120)
# curve()
# turtle.forward(111.65)
# turtle.end_fill()
# turtle.hideturtle()
# turtle.done()


# a = [1, 4, 7, 9, 2, 3, 5, 0]
# b = sorted(a)
# print(b)


# print('Добро пожаловать к нам в ООО "Системы безопасности". ')
# password = ''
# while password != '123':
#     print('Доступ закрыт!')
#     password = input('Введите пароль: ')
# else:
#     print('Доступ открыт!')
    



# a = 17
# b = 30
# c = 15

# while a < 23:
#     print(a)
# while b > c:
#     print(b, ">", c)



a = 40
print(a)
