
#1 Declare your age as integer variable
Age=10

#2 Declare your height as a float variable
height=15.0

#3 Declare a variable that store a complex number
Complex_Number=(1 + 1j)

#4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
Base=float(input("Enter Base : "))
Length=0.5
Height=float(input("Enter Heigth : "))
Area_Triangle= Length * (Base) * (Height)
print('The Triangle Area is :',Area_Triangle)

#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Side_a=float(input('Enter side a:'))
Side_b=float(input('Enter side b:'))
Side_c=float(input('Enter side c:'))
Perimeter_Triangle=Side_a+Side_b+Side_c
print("The perimeter of the triangle is ",Perimeter_Triangle)

#6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_rectangle=float(input('Enter Length of Rectangle: '))
width_rectangle=float(input('Enter Width of Rectangle: '))
Area_rectangle=length_rectangle * width_rectangle
Perimeter_rectangle=2*(length_rectangle+width_rectangle)
print("Area rectangle : ",Area_rectangle)
print("Perimeter rectangle :",Perimeter_rectangle)

#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi=3.14
Radius_Circle=float(input('Enter Radius for Circle: '))
Area_Circle=pi*(Radius_Circle**2)
Circumference_Circle=2*pi*Radius_Circle
print("Area of circle : ",Area_Circle)
print("Circumference of circle :",Circumference_Circle)

#8 Calculate the slope, x-intercept and y-intercept of y = 2x -2 | y = mx + c
y=2
slope=2
x_Intercept=2/2
y_intercept=-2

#9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
y2=10
y1=2
x1=2
x2=6
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(1/2)
print(f"Slope: {slope}");
print(f"Euclidean Distance: {distance:.2f}")

#10 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x_Values=float(input("x values :"))
y_Values= x_Values**2 + 6*x_Values +9

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') == len('adragon'))  # False

#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'adragon') 

#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon'in'I hope this course is not full of jargon.')

#15 print('on' in 'python' and 'on' in 'adragon') 
print('on' not in 'python' and 'on' not in 'adragon') 

#16 Find the length of the text python and convert the value to float and convert it to string
Text_1='python'
length_Text_1=len(Text_1)
float_Text_1=float(length_Text_1)
str_Text_1=str(float_Text_1)

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division=7 // 3
converted_value=int(2.7)
is_equal=floor_division==converted_value

#19 Check if type of '10' is equal to type of 10
str_10= '10'
int_10= 10
compare=type(str_10)==type(int_10)

#20 Check if int('9.8') is equal to 10
int_value=int(9.8)
compare1=int_value==int_10

#21 Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Hours=float(input('Enter hours: '))
Rate_PerHours=float(input('Enter rate per hour: '))
Earning=Hours*Rate_PerHours
print("Your weekly earning is ",Earning)

#21 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Years=float(input('Enter number of years you have lived: '))
Lived=31536000*Years
print(f'You have lived for {Lived} seconds.')
