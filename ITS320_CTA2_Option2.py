print('Please enter the following information in the spaces provided:')
car_brand = input('Enter car brand: \n')
car_model = input('Enter car model: \n')
car_year = int(input('Enter car year: \n'))
start_odo = int(input('Enter starting odometer: \n'))
end_odo = int(input('Enter ending odometer: \n'))
est_mpg = int(input('Enter estimated MPG: \n'))
vehicle_information = {
    'Car Brand': car_brand, 
    'Car Model' : car_model,
    'Car Year' : car_year,
    'Starting Odometer' : start_odo,
    'Ending Odometer' : end_odo,
    'Estimated MPG' : est_mpg}
print('The vehicle information is' , vehicle_information)
car_mileage = int((end_odo - start_odo)/est_mpg)
print('The estimated gallons of gasoline used during this trip was' , car_mileage)

