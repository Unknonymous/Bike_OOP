#define class & set attributes
class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    #declare methods
    def displayInfo(self):
        print ('Price: $' + str(self.price))
        print ('Max Speed: ' + str(self.max_speed)+'mph')
        print ("Mileage: " + str(self.miles)+"mi" )
        print (" ")
        return self

    def ride(self):
        self.miles += 10
        return self

    def reverse(self):
        if (self.miles < 5):
            self.miles = 0
        else:
            self.miles -= 5
        return self

# create 3 instances of bike objects
bike1 = Bike(200, 25, 0)
bike2 = Bike(350, 27, 0)
bike3 = Bike(375, 33, 0)

#have the first instance ride 3 times, reverse once, and have it displayInfo()
bike1.ride().ride().ride().reverse().displayInfo()

#have the second instance ride twice, reverse twice and have it displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()

#have the third instance reverse three times and displayInfo()
bike3.reverse().reverse().reverse().displayInfo()