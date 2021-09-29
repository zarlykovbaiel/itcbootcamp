# class Student:
#     def __init__(self, name, lastname,department, year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance
#     def get_student_info(self):
#         print(self.name, self.lastname, "поступил в",self.year_of_entrance + str("г."), "на факультет",self.department)
# s = Student("Вася","Василий"," Инжеnер","2016")
# s.get_student_info()


# class Airplane:
#     def __init__(self,make,model,year,max_speed,odometer = 0,is_flying = False):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = 0
#         self.is_flying = is_flying

#     def dor(self):
#         self.is_flying = True
#         print(f'Самолет {self.model} взлетел, со скорость {self.max_speed} км/ч, на расстояние  {self.odometer} км')

#     def fly(self):
#         self.odometer += 1000
           
#     def land(self):
#         self.is_flying = False


# airplane = Airplane(
#     make = "Ильюшин",
#     model = "ИЛ-62",
#     year = '1967',
#     max_speed = 850
#     )

# airplane.fly()
# airplane.dor()

# class Car:
#     def __init__(self,make,model,year,fuel = 70,odometer = 0):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel
#     def drive(self):
#     	print()






class House():
    def __init__(self, typehouse, areahouse): 
        self.typehouse = typehouse
        self.areahouse = areahouse

    def get_house(self):
        self.totalarea = 0
        self.furnitures = {
            'Кравать' : 4,
            'Гардироб' : 2,
            'Стол' : 1.5
        }
        for value in self.furnitures.values():
            self.totalarea += value
        print('Тип дома: ',self.typehouse," -- Общая площадь:",self.areahouse, "\n",list(self.furnitures.keys()),"\n" "Оставшаяся площадь: " ,self.areahouse - self.totalarea) 
b = House('Квартира', 80)
b.get_house()
