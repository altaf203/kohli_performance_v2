# class Acc(Sensor):
#     def show_type(self):
#         print("  ")
#     def precisionAcc(self):
    

#     class 2D():                 class 3D():

#         class Gyro(Acc):
#             def show_type(self):
#                 print("  ")

# super() --init--()




class Sensor():
    def __init__(self,name,location,record_date):
        self.name=name
        self.location=location
        self.record_date=record_date
        self.data={}

    def add_data(self, data, time):
        self.data["data"]=data
        self.data["time"]=time
        print("data points addess sucessful ")
    def clear_data(self):
        self.data={}
        print("data removed succesfull")




import numpy as np

sensor1  = Sensor(name ="sensor1", location="haldia", record_date="2023-01-09")
data = np.random.randint(-10,10,10)
time=np.arange(10)

sensor1.add_data(data=data, time=time)
print(sensor1.data)  # .data is dict

class Acceleometer(Sensor):
    def show_sensor_type(self):
        print(f"this is {self.name} ")




import numpy as np
acc_data = np.random.randint(-10,10,10)
acc_time=np.arange(10)



acc = Acceleometer(
    name="acceleometer",
    location="haldia",
    record_date="2023-01-09"
)

acc.add_data(
    data = acc_data,
    time= acc_time
)


class Gyro(Acceleometer):
    def show_sensor_type(self):
        print(f"this is {self.name} and the location is {self.location}")

Gyro_data=np.random.randint(-15,15,10)
Gyro_time=np.arange(10)

Gyro = Gyro(
    name="Gyroscope",
    location="kolkata",
    record_date="2023-01-10"
)

Gyro.add_data(time=Gyro_time,data=Gyro_data)
acc.show_sensor_type()
Gyro.show_sensor_type()
# print(data)
# print(time)

# GPS attribute :
# name
# location
# record date
# brand

class GPS(Sensor):
    def __init__(self,name,location,record_date,brand):
        super().__init__(
            name,location,record_date
        )
        self.brand=brand

gps = GPS(
    name="GPS",
    location="Haldia",
    record_date="2023-01-10",
    brand="Altaf"
)
print(gps.name)
print(gps.location)
print(gps.record_date)
print(gps.brand)

