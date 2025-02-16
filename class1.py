# Declare your age as integer variable
# # age=23
# # 
# Declare your height as a float variable
# # height=1.67
# # 
# Declare a variable that store a complex number
# # ComplexNumber=2+3j
# # 
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# # Base=int(input("Enter base: "))
# # Height=int(input("Enter height: "))
# # Area=(1/2)*(Base*Height)
# # print("The area of the triangle is: ", Area)
# # 
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# # Side_a=int(input("Enter side a: "))
# # Side_b=int(input("Enter side b: "))
# # Side_c=int(input("Enter side c: "))
# # Perimeter=Side_a+Side_b+Side_c
# # print("The perimeter of the triangle is: ",Perimeter)
# # 
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# # lenght=int(input("Enter side Lenght: "))
# # Width=int(input("Enter Width: "))
# # Rec_Area=lenght*Width
# # Rec_Perimeter= 2*(lenght+Width)
# # print("The Area of the Rectangle is: ",Rec_Area)
# # print("The Perimeter of the Rectangle is: ",Rec_Perimeter)
# # 
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# # Radius_circle=int(input("Enter radius of Circle: "))
# # Circle_area=(Radius_circle**2)*3.14
# # Circle_circum=Radius_circle*3.142*2
# # print("The Area of Circle: ",Circle_area)
# # print("The Circumference of Circle:  ",Circle_circum)
# # 
# # Calculate the slope, x-intercept and y-intercept of y = 2x -2
# # m = 2 #slope
# # b =-2 #Y=intercept
# # x_intercept = -b/m
# # 
# # print("Slope (m): ",m)
# # print("Y-intercept: ",b)
# # print("X-intercept: ",x_intercept)
# # 
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# # y1=2
# # y2=10
# # x1=2
# # x2=6
# # Slope_m=(y2-y1)/(x2-x1)
# # euclidean = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(1/2)
# # 
# # print(Slope_m)
# # print(euclidean)
# # 
# # print(m==Slope_m)
# # 
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# 
# A=1
# B=6
# C=9
# 
# x1=((-B)+(B**2-4*A*C)**(1/2))/(2*A)
# x2=((-B)-(B**2-4*A*C)**(1/2))/(2*A)
# print(x1)
# print(x2)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# String1="Phyton"
# String2="Dragon"
# lenght1=len(String1)
# lenght2=len(String2)
# CompareLenght=lenght1 != lenght2
# print(CompareLenght)
# 
# #Use and operator to check if 'on' is found in both 'python' and 'dragon'
# substring="on"
# CompareON=(substring in String1) and (substring in String2)
# print(CompareON)
# 
##I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# String3="I hope this course is not full of jargon."
# Substring2="jargon"
# CheckWord1= Substring2 in String3
# print(CheckWord1)
# 
##There is no 'on' in both dragon and python
# CompareNoOn=(substring not in String1) and (substring not in String2)
# print(CompareNoOn)
# 
##Find the length of the text python and convert the value to float and convert it to string
# 
# Float1=float(lenght1)
# FloatToString=str(Float1)
# print(FloatToString)
# 
##Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# number = int(input("Enter a number: "))  # Taking input from the user and converting it to an integer
# is_even = number % 2 == 0
# print(f"The number {number} is even: {is_even}")  # This will print whether the number is even or not
# 
##Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
# 
# Result= 7 // 3
# value= 2.7
# 
# CompareInt= Result == value
# print(CompareInt)
# 
##Check if type of '10' is equal to type of 10
# value2=10
# String4="10"
# Compare10= value == String4
# print(Compare10)
# 
##Check if int('9.8') is equal to 10
# String5=int(float('9.8'))
# Compare9=value2=String5

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

Hours=int(input("Enter Hours: "))
Rate=int(input("Enter Rate per Hours: "))
Earning=Hours*Rate
print("Your Weekly Earning is",Earning)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

Live_number=int(input("Enter number of years you have lived: "))
Convert=Live_number*31557600
print("You have lived for",Convert,"seconds")


#Write a Python script that displays the following table

# Manually print each row

# print("Row | Col 1 | Col 2 | Col 3 | Col 4 | Col 5")
# print("-----|-------|-------|-------|-------|-------")
# print(f"  1  |   1   |   1   |   1   |   1   |   1   ")
# print(f"  2  |   1   |   2   |   4   |   8   |  16   ")
# print(f"  3  |   1   |   3   |   9   |  27   |  81   ")
# print(f"  4  |   1   |   4   |  16   |  64   |  256  ")
# print(f"  5  |   1   |   5   |  25   | 125   |  625  ")







