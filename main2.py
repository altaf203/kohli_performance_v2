# from my_sensor import Acceleometer, Gyro, GPS
from my_sensor import Acceleometer, Gyro, GPS
import numpy as np


acc = Acceleometer(
    name="Accelometer",
    location="Haldia",
    record_date = "2023-01-10"
)

Gyro = Gyro(
    name = "Gyroscope",
    location="kolkata",
    record_date = "2023-01-10"

)

gps = GPS(
    name = "GPS",
    location="West bengal",
    record_date = "2023-01-10"
)
# get all the dumy data
time = np.arange(10)
acc_data = np.random.randint(-10,10,10)
Gyro_data = np.random.randint(-15,15,10)
gps_data = np.random.randint(-12,12,10)

# add  data to the instance
print(acc.name)
print(acc.location)
print(acc.record_date)

acc.add_data(
    data=acc_data,
    time=time
)

print(Gyro.name)
print(Gyro.location)
print(Gyro.record_date)

Gyro.add_data(
    data=Gyro_data,
    time=time
)
print(gps.name)
print(gps.location)
print(gps.record_date)

gps.add_data(
    data=gps_data,
    time=time
)


