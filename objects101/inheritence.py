class Car(object):
    def __init__(self,make,model,mpg):
        self.make = make
        self.model = model
        self.mpg = mpg
    def startCar(self):
        print "%s goes Vroom" % self.model
myCar = Car('Ford','Focus',40)
myCar.startCar()

class ElecrtricCar(Car):
    # call this object's constructor
    def __init__(self,make,model,batteryLife):
        # call super class constructor        
        super(ElecrtricCar,self).__init__(make,model,"N/A")
        self.batteryLife = batteryLife
    # we can override a super method
    def startCar(self):
        print "%s goes ..." % self.model

car1 = Car("Toyota","Camry",35)
car2 = ElecrtricCar("Tesla","S","100kh")
# print car1.model
print car2.mpg
car2.startCar()