import json

class Vehicle: 
    def __init__ (self, VIN, make, model, year, mileage, color): 
        self.VIN = VIN
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

response = ''
VehicleInventory = []

def car_add():
    print('Please enter the following information in the spaces provided:')
    car_VIN = int(input('Enter car VIN: \n'))
    car_make = input('Enter car make: \n')
    car_model = input('Enter car model: \n')
    car_color = input('Enter car color: \n')
    car_year = int(input('Enter car year: \n'))
    car_mileage = int(input('Enter car mileage: \n'))
    vehicle = Vehicle(car_VIN, car_make, car_model, car_year, car_mileage, car_color)
    VehicleInventory.append(vehicle)

def car_delete(): 
    vin = int(input('What is the VIN of the car you would like to delete?'))
    for v in VehicleInventory:
        if v.VIN == vin: 
            VehicleInventory.remove(v) 
            print('Vehicle Deleted')

def car_update():
    vin = int(input('What is the VIN of the car you would like to update?'))
    for v in VehicleInventory:
        if v.VIN == vin: 
            v.make =  input('Enter car make: \n')
            v.model = input('Enter car model: \n')
            v.color = input('Enter car color: \n')
            v.year = int(input('Enter car year: \n'))
            v.mileage = int(input('Enter car mileage: \n'))
    print('Vehicle Updated')

def print_list(v):
        print('=========================')
        print('VIN: ' + str(v.VIN))
        print('make: ' + v.make)
        print('model: ' + v.model)
        print('year: ' + str(v.year))
        print('mileage: ' + str(v.mileage))
        print('color: ' + v.color) 
        print('=========================')


while response != 'Q':
    response = input('What would you like to do? Add(A), Delete(B), Update(C), View List(D), Save to Text File and Quit(Q)')
    if (response == 'A' or response == 'a'): 
        car_add()
    elif (response == 'B' or response == 'b'):
        car_delete()
    elif (response == 'C' or response == 'c'):
        car_update()
    elif (response == 'D' or response == 'd'):
        for v in VehicleInventory:
            print_list(v)

with open('file.txt', 'w') as file:
     for v in VehicleInventory:
         file.write(json.dumps(v.toJSON()))
    