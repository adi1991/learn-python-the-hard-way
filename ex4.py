cars = 100;
space_in_cars = 4;
drivers = 20;
passengers = 30;
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars
average_persons_per_car = passengers/cars_driven

print "There are", cars, "only available"
print "There are only", drivers, "available" 
print "There will be", cars_not_driven, "empty today"
print "We can transport",carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_persons_per_car, "in each car" 
