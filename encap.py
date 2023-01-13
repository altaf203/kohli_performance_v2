# class User():
#     id     # attribute
#     username
#     pwd
#     sk
#     # dob


class Sensor():
    def __init__(self,name, location):
        self.name=name
        self.location=location
        self.__record_date="2023-01-10"
        self.__version="0.0112"

    def get_record_date(self):
        print(f"the record date is {self.__record_date}")

    def get_version(self):
        print(f"the version is {self.__version}")

    def set_version(self,version):
        self.__version = version
        print(f"the updated version is {self.__version}")

sensor1=Sensor(
    name="Sensor 1", location="haldia"
)
print(sensor1.name)
print(sensor1.location)

sensor1.get_record_date()             # to retrive
sensor1.get_version()
sensor1.set_version(version="0.1212")   # update version
sensor1.get_version()


# print(sensor1.__record_date)
# print(sensor1.__version)