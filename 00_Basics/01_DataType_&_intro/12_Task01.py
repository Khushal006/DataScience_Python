#Q1 :- Print the given strings as per stated format.
#Data-Science-Mentorship-Program-started-By-CampusX
print("Data-Science-Mentorship-Program-started-By-CampusX")

#Q2:- Write a program that will convert celsius value to fahrenheit.
cel = int(input("Enter celsius value :"))
fah = (cel * 9/5)+32
print(fah, " is the fahrenheit value")

#Q3 Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))

num1, num2 = num2 , num1 

print("First num is :", num1)
print("Second num is :", num2)

#Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
x1, x2 = int(input("enter the x1 :")), int(input("enter the x2 :"))
y1, y2 = int(input("enter the y1 :")), int(input("enter the y2 :"))
euclidean_distance = ((x2-x1)**2+(y2-y1)**2)**0.5
print(euclidean_distance)

#Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
principle = int(input("Enter the value of principle :"))
rate = int(input("Enter the rate of interest :"))
time_period = int(input("Enter the period of interest in years :"))

Simple_interest = principle*rate*time_period/100
print(Simple_interest)

#Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
heads = int(input("Enter number of heads :"))
legs = int(input("Enter number of legs :"))

dogs = (legs - 2*heads) / 2
print("Number of dogs :", dogs)
chicken = heads - dogs
print("Number of chicken:", chicken)

#Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
n = int(input("Enter the n :"))
sum_of_sqr = n(n+1)*(2*n+1)/6
print(sum_of_sqr)

#Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
a1 = int(input("Enter the 1st num :"))
a2 = int(input("Enter the 2nd num :"))
n = int(input("Enter the nth term :"))
nth = a1 + (n-1)(a2-a1)

print("nth term is :", nth)

#Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
n1 , n2 = int(input("Enter the 1st numerator :")), int(input("Enter the 2nd numerator :"))
d1, d2 = int(input("Enter the 1st denomenator :")), int(input("Enter the 2nd denomenator :"))
sum_of_fractions = (n1*d2 + n2*d1) / (d1*d2)
print(sum_of_fractions)

#Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
height_MT = int(input("Enter the height of Milk tank :"))
breadth_MT = int(input("Enter the breadth of Milk tank :"))
length_MT = int(input("Enter the length of Milk tank :"))

vol_of_MT = height_MT*breadth_MT*length_MT

height_GL = int(input("Enter the height of milk glass :"))
radius_GL = int(input("Enter the radius of milk glass :"))

vol_of_GL = 3.14*((radius_GL)**2)*height_GL

Milk_glass = vol_of_MT/vol_of_GL

print("Number of Milk glass Milk tank can fill :", int(Milk_glass))