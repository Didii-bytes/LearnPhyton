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
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2 #slope
b =-2 #Y=intercept
x_intercept = -b/m

print("Slope (m): ",m)
print("Y-intercept: ",b)
print("X-intercept: ",x_intercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
y1=2
y2=10
x1=2
x2=6
Slope_m=(y2-y1)/(x2-x1)
euclidean = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(1/2)

print(Slope_m)
print(euclidean)

print(m==Slope_m)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.#