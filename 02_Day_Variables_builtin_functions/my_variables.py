# Day 2: 30 Days of python programming
first_name = 'Harsimar'
last_name = 'Gurdatta'
full_name = 'Harsimar Gurdatta'
country = 'India'
city =  'New Delhi'
age = '23'
year = '2023'
is_married = 'True'
is_true = 'False'
is_light_on = 'True'
First_name, Last_name, Country,City, Age, Year = 'Harsimar', 'Gurdatta', 'India', 'New Delhi', '23', '2023'

variables = [ first_name,last_name,full_name,country,city,age,year,is_married,is_light_on]
for v in variables:
    print(v, type(v))

print(len(first_name))
print(len(first_name) >= len(last_name))
num_one = 5
num_two = 4
Total = num_one + num_two
Diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
radius = 30
pi = 3.417
area_of_circle = pi* radius**2
circumference = 2*pi* radius

radius_fancy = int(input("type:"))
fancy_area = pi* (radius_fancy**2)
print(fancy_area)
fancy_first = input("first:")
fancy_last = input("last:")
country = input("country:")
age = input("age:")
