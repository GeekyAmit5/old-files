
class Car:
    def __init__(self,speed=300,color="Black"):
        self.__speed=speed
        self.__color=color

    def set_speed(self,speed):
        self.__speed=speed

    def get_speed(self):
        return self.__speed

bugati = Car()
audi = Car( )
ford = Car()
audi.__speed=100            # this does not work bcz speed is private 
audi.set_speed(500)          # this works

print(audi.get_speed())
