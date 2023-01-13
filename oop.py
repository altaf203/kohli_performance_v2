# DAY 4 (9-01-23)
# how can declare a method in python
# class superHeros():
#     def __init__(self,name,superpower):
#         self.name=name
#         self.superpower=superpower
#     def get_superpower(self):
#         print("{self.name}")

# class SuperHero():
#     def __init__(self,name,superpower):
#         self.name=name
#         self.superpower=superpower
#         # print("i am {self.name} and my power is {self.superpower}")
#     def get_superpower(self):
#         print(f"i am {self.name} and my power is {self.superpower}")
    
# ironMan= SuperHero(
#     name="iron man",
#     superpower="suit"
# )
# ironMan.get_superpower()

# inheritance

# class Sensor():
#     def __init__(self,name,loc):
#         self.name=name
#         self.loc=loc
#     def add_data()

#     class Accelero(Sensor)
#     def get_name(def):


# class SuperHeroes():
# 	def __init__(self, name, superpower):
# 			self.name = name
# 			self.superpower = superpower

# 	def get_superpower():
# 			print("I am {} and My power is {}".format(self.name, self.superpower))

# ironMan = SuperHeroes(name="Ironman", superpower="Suit")
# print(ironMan.get_superpower())

# """
# Output:
# I am Ironman and My power is Suit
# """

#if you want to access name and superpower of the object ironMan
#you can just write the following lines of code
# name = ironMan.name
# superpower = ironMan.superpower

# #if you want to access the method get_superpower() , here's
# #the following lines of code
# ironMan.get_superpower()

# thor = SuperHeroes(name="Thor", superpower="Mjolnir")
# print(thor.name)
# print(thor.superpower)
# print("I am the God of Thunder, {} and I am worthy of {}".format(thor.name, thor.superpower))


# Inheritance

# class Sensor():
#     def __init__(self, name, location, record_date):
#         self.name = name
#         self.location = location
#         self.record_date = record_date
#         self.data = {}
        
#     def add_data(self, t, data):
#         self.data['time'] = t
#         self.data['data'] = data
#         print(f'We have {len(data)} points saved')        
        
#     def clear_data(self):
#         self.data = {}
#         print('Data cleared!')

# import numpy as np

# sensor1 = Sensor('sensor1', 'Berkeley', '2019-01-01')
# data = np.random.randint(-10, 10, 10)
# sensor1.add_data(np.arange(10), data)
# print(sensor1.data)

# """
# Output:
# We have 10 points saved
# {'time': array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#  'data': array([-4, -7,  2, -3, -8,  6,  4,  3,  5, -9])}
# """


# class Accelerometer(Sensor):
    
#     def show_type(self):
#         print('I am an accelerometer!')
        
# acc = Accelerometer('acc1', 'Oakland', '2019-02-01')
# acc.show_type()
# data = np.random.randint(-10, 10, 10)
# acc.add_data(np.arange(10), data)
# print(acc.data)

# """
# Output:
# I am an accelerometer!
# We have 10 points saved

# {'time': array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#  'data': array([ -2,   2, -10,   6,   2,  -8,   2,   3,   7,  -6])}
# """


# Inherit and method overriding

# class UCBAcc(Accelerometer):
    
#     def show_type(self):
#         print(f'I am {self.name}, created at UC Berkeley!')
        
# acc_ucb = UCBAcc('UCBAcc', 'Berkeley', '2019-03-01')
# acc_ucb.show_type()

# """
# Output:
# I am UCBAcc, created at UC Berkeley!
# """


# Inherit and update attributes with super

# class NewSensor(Sensor):
#     def __init__(self, name, location, record_date, brand):
#         self.name = name
#         self.location = location
#         self.record_date = record_date
#         self.brand = brand
#         self.data = {}
        
# new_sensor = NewSensor('OK', 'SF', '2019-03-01', 'XYZ')
# print(new_sensor.brand)

# """
# Output:
# 'XYZ'
# """


# class NewSensor(Sensor):
#     def __init__(self, name, location, record_date, brand):
#         super().__init__(name, location, record_date)
#         self.brand = brand
        
# new_sensor = NewSensor('OK', 'SF', '2019-03-01', 'XYZ')
# print(new_sensor.brand)

# """
# Output:
# 'XYZ'
# """





# class SuperHeroes():
# 	def __init__(self, name, superpower):
# 			self.name = name
# 			self.superpower = superpower

# 	def get_superpower():
# 			print("I am {} and My power is {}".format(self.name, self.superpower))

# ironMan = SuperHeroes(name="Ironman", superpower="Suit")
# print(ironMan.get_superpower())

# """
# Output:
# I am Ironman and My power is Suit
# """


#  Encapsulation

# class Sensor():
#     def __init__(self, name, location):
#         self.name = name
#         self._location = location
#         self.__version = '1.0'
    
#     # a getter function
#     def get_version(self):
#         print(f'The sensor version is {self.__version}')
    
#     # a setter function
#     def set_version(self, version):
#         self.__version = version

# sensor1 = Sensor('Acc', 'Berkeley')
# print(sensor1.name)
# print(sensor1._location)
# print(sensor1.__version)

# """
# Output:
# Acc
# Berkeley

# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-8-ca9b481690ba> in <module>
#       2 print(sensor1.name)
#       3 print(sensor1._location)
# ----> 4 print(sensor1.__version)

# AttributeError: 'Sensor' object has no attribute '__version'
# """


# sensor1.get_version()

# """
# Output:
# The sensor version is 1.0
# """

# sensor1.set_version('2.0')
# sensor1.get_version()

# """
# Output:
# The sensor version is 2.0
# """

# Polymorphism

# class Sensor():
#     def __init__(self, name, location, record_date):
#         self.name = name
#         self.location = location
#         self.record_date = record_date
#         self.data = {}

#     def add_data(self, time, data):
#         self.data["data"] = data
#         self.data["time"] =  time
#         print(
#             f"Received {len(data)} point"
#         )

#     def clear_data(self):
#         self.data = {}
#         print("Data cleared!!")

# import numpy as np

# sensor1 = Sensor(
#     name="sensor1",
#     location="Haldia",
#     record_date="2023-01-09"    
# )
# print(sensor1.name, sensor1.location, sensor1.record_date)

# #generating random data points list of length 10
# data = np.random.randint(-10, 10, 10)
# #generating random time in seconds corresponding to the data points above
# time = np.arange(10)

# #adding the generated data points into the sensor object
# sensor1.add_data(
#     time=time,
#     data=data
# )

# #printing the sensor dictionary within the class
# print(sensor1.data)

# print(" -------------------------------- ")
# class Accelerometer(Sensor):
#     def show_type(self):
#         print(f"I am an {self.name}")

# acc = Accelerometer(
#     "accelerometer",
#     "Haldia",
#     "2023-01-09"
# )

# acc.show_type()

# #generating random data points list of length 10
# data = np.random.randint(-10, 10, 10)
# #generating random time in seconds corresponding to the data points above
# time = np.arange(10)
# acc.add_data(data=data, time=time)
# print(acc.data)