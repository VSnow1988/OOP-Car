class Car():
    def  __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (self.price > 10,000):
            tax = "15%"
        else:
            tax = "12%"
    def displayall(self):
        print "Price is " + str(self.price) + ", speed is " + str(self.speed) + " mph, fuel is " + str(self.fuel) + " mpg, mileage is " + str(self.mileage)
        return self
        
Car(30000,20,200,700).displayall()
Car(999,6002,888,5555).displayall()
Car(7,400,18,141414).displayall()
Car(400000000,99,3,5).displayall()
Car(1234567,26,240,40).displayall()
Car(777,13,1,0).displayall()
