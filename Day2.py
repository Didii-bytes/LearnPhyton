#Day 2 of 30DaysOfPython

print("Day 2: 30 Days of python programming")
first_name = 'Danial'
last_name = 'Damanhuri'
country = 'Malaysia'
city = 'Selangor'
age = 22
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Danial',
   'lastname':'Damanhuri',
   'country':'Malaysia',
   'city':'Selangor'
   }

print(type(first_name ))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(person_info))

length_first_name = len(first_name) 
length_last_name = len(last_name)

num_one=5
num_two=4

total=num_one + num_two
diff =num_one - num_two
product=num_one * num_two
division=num_one / num_two
remainder=num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
radius=30
area_of_circle=3.142*(radius**2)
circum_of_circle=2*(3.142*radius)

radius_user=float(input('enter the radius : '))
area_of_circle_user=3.142*(radius_user**2)
circum_of_circle_user=2*(3.142*radius_user)
print("Area of Circle :",area_of_circle_user)
print("Circumference of Circle :",circum_of_circle_user)

first_name=input('Enter your first name : ')
last_name=input('Enter your last name : ')
country=input("Enter your Country : ")
age=input("Enter your age : ")

print(first_name,last_name,country,age)

length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)