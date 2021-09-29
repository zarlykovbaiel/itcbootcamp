			#OOP

# class Car:
	# name='camry55'
	# make='Toyota'
# 	model='2015'
# 	def start(self):
# 		print('Заводим двигатель')
# 	def stop(self):
# 		print('Останавливается')
# car_a=Car()
# print(car_a.start)




# class Laptop:
#     def __init__(self, model_name):
#         self.model = model_name
#         self.kharakteristics = []
#         self.processor()
#         self.ram()
#         self.video_card()
#         self.HDD()
#         self.display_size()

#     def processor(self):
#         self.kharakteristics.append('AMD® A6-9220 radeon r4, 5 compute cores 2c+3g × 2 ')

#     def ram(self):
#         self.kharakteristics.append('8 Гб DDR4')

#     def video_card(self):
#         self.kharakteristics.append('AMD® Stoney')

#     def HDD(self):
#         self.kharakteristics.append('SSD 500 Гб')
    
#     def display_size(self):
#         self.kharakteristics.append('16,6 FHD')
    
# laptop = Laptop(model_name='Acer')
# print(laptop.model)
# print(laptop.kharakteristics)


colors = {
    "black": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,255,255,1],
    "hex": "#000"
    }
    },
    "white": {
    "category": "value",
    "code": {
    "rgba": [0,0,0,1],
    "hex": "#FFF"
    }
    },
    "red": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,0,0,1],
    "hex": "#FF0"
    }
    },
    "blue": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [0,0,255,1],
    "hex": "#00F"
    }
    },
    "yellow": {
    "category": "hue",
    "type": "primary",
    "code": {
    "rgba": [255,255,0,1],
    "hex": "#FF0"
    }
    },
    "green": {
    "category": "hue",
    "type": "secondary",
    "code": {
    "rgba": [0,255,0,1],
    "hex": "#0F0"
    }
    }
    }
class Plat:
    def init(self ,colors ):
        self.colors = colors

    def get_keys_tuple(self):
        s = colors.keys()
        t = tuple(s)
        return t
    def get_values_tuple(self):
        r = colors.values()
        t = tuple(r)
        return t

    def get_keys_list(self):
        s = colors.keys()
        t = list(s)
        return t
    def get_values_list(self):
        r = colors.values()
        t = list(r)
        return t

    def get_keys_set(self):
        s = colors.keys()
        t = set(s)
        return t
    def get_values_set(self)
        r = colors.values()
        t = set(r)
        return t


d = Plat(colors)
print(d.get_keys_tuple())
print(d.get_values_tuple())
print(d.get_keys_list())
print(d.get_values_list())
print(d.get_keys_set())
print(d.get_values_set())