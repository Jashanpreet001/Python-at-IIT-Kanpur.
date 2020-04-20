##Assignment-1: Arithmetic Operators.
##1.WAP to swap two numbers inputted by user without usind third variable.
a = int (input("input first number into num1\n"))
b = int (input("input second number into num2\n"))
a=a+b
b=a-b
a=a-b

print("The num1 is now =",a,"The num2 is now =",b)

##2.WAP to input temperature in Celsius, covert it into Fahrenheit using the Formula:
Fahrenheit = (9/5)* Celsius + 32.

temperatureC = int (input("Enter the temperature in celsius"))
temperatureF = (9/5)*temperatureC+32

print(temperatureC,"celsius =",temperatureF,"Fahrenheit")

##3.WAP to calculate sum of digits of any integer between 1 to 1000.

num= int (input("Enter a number between 1 to 1000\n"))

sum=0

while (num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10

print("The sum of the digits is",sum)



##4.WAP to inpput marks scored by a student in 3 subjects and compute the percentage obtained.

marks1=int(input("enter the marks obtained in first subject"))
marks2= int (input("enter the marks obtaind in second subject"))
marks3= int (input("enter the marks obtaind in the third subject"))

total= int (input("Enter the sum of the total marks of the three subjects"))
percentage=(marks1+marks2+marks3)/total*100

print("The percenateg obtained is",percentage)

##Random, separating the digits of any number.
num= int(input("Enter the number\n"))
while num!=0:
    rem=num%10
    print(rem)
    num=num//10


##area of an equilateral triangle.
import math
side=int(input('Enter the Side the equilateral triangle\n'))

semi=3*side/2

area=math.sqrt(semi*3*(semi-side))

print(area)


## reversing a number

num = int(input("Enter the number you want to reverse:\n"))
reverse=0
while num!=0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

print("reverse is",reverse)
    
##5.WAP to covert time given in seconds into hours minutes and seconds.

time = int (input("Enter the total time in seconds\n"))

hours = time//3600
time = time%3600
minutes = time//60
seconds = time % 60

print(hours,'hours, ',minutes,'minutes, ',seconds,'seconds ')


##6.WAP to input radius and calsulate area of a circle.
import math
rad = int(input("Enter the radius of the circle.\n"))

area = math.pi*rad**2
print("area of the circle is ", area)


##7.Wap to determine the binary octdecimal and hexadecimal of a given integer.

num = int(input("Enter the decimal form of the number.\n"))
temp = num
binary = 0
while(num!=0):
    rem=num%2
    binary = binary*10 + rem
    num = num // 2

print("number in binary =",binary)

num = temp
octa = 0
while(num!=0):
    rem=num%8
    octa = octa*10 + rem
    num = num // 8

print("number in octa-decimal form =", octa)

num = temp
hexa = ''
while(num!=0):
    rem=num%16
    if(rem<10):
        hexa =  str(rem) + hexa
    else:
        if(rem==10):
            rem='A'
        if(rem==11):
            rem='B'
        if(rem == 12):
            rem='C'
        if(rem == 13):
            rem = 'D'
        if(rem == 14):
            rem = 'E'
        if(rem == 15):
            rem = 'F'

        hexa = str(rem) + hexa

    num = num // 16

print("number in hexadecimal form = ", str(hexa))    


##8.WAP to swap two numbers using a third variable.

num1=int(input("Enter the first number\n"))
num2=int(input("Enter the second number\n"))
num3=num2
num2=num1
num1=num3
print("now the first number is",num1,"and the second number is ", num2)

##9.
WAP to accpect time, principal amount , rata and calculate the principle intrest.

prin_amt =int(input("Enter the principle amount\n"))
time = int(input("Enter the time in years\n"))
rate = int(input("Enter the annual rate of interest\n"))

simple_interest = prin_amt*(1+rate*time)

print("Simple interest = ",simple_interest)

#10
#Wap to accept three nummber from a user and calculate their mean.
num1=int(input("Enter the first number:\n"))
num2=int(input("Enter the second number:\n"))
num3=int(input("Enter the third number:\n"))

mean = (num1+num2+num3)/3

print("The mean of the three numbers is:",mean)

#11
#WAP to accept to accept marks of 5 subjects and calculate the percentage.

marks1=int(input("Enter the marks of the first subject:\n"))
marks2=int(input("Enter the marks of the second subject:\n"))
marks3=int(input("Enter the marks of the third subject:\n"))
marks4=int(input("Enter the marks of the forth subject:\n"))
marks5=int(input("Enter the marks of the fifth subject:\n"))

percentage = (marks1+marks2+marks3+marks4+marks5)/500*100

print("The percentage obatained = ",percentage)

##12
WAP to accept a number from the user and print its square and cube.

num = int(input("Enter the number"))

square = num*num
cube = num*num*num

print("The square of the number is:\n",square,"The cube of the number is:\n", cube)

#13
#WAP to program to accept a number from the user and calculate its square root.
num = int(input("Enter the number"))
import math

sqr_root = math.sqrt(num)
print("The square root of the number is:\n", sqr_root)

##14
wap to accept coeffiencts of a quadratic equation and calculate its roots.
import math
a = int(input("Enter the coefficient of x^2:\n"))
b = int(input("Enter the coefficient of x^1"))
c = int(input("Enter the coefficient of x^0"))

d = b*b-4*a*c
if(d<0):
    print("no real roots exists")
else:
    x1 = (-b+ math.sqrt(d))/2*a
    x2 = (-b-math.sqrt(d))/2*a

print("The roots of the equation are:\n", x1,x2)
