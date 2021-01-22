import numpy, scipy,matplotlib, sympy, math
from scipy import linalg, special
import matplotlib.pyplot as plt
import numpy as np
#Functions
def add(x , y):
    return x + y
def sub(x, y):
    return x - y
def multi(x, y):
    return x * y
def divide(x, y):
    return x  / y
def reset():
    restart=input("restart?")
    if restart == "yes":
         pro()
    else:
        exit()
def axis(x,y):
   return y * x /2
def max(x,y,z):
    return z - y * y /4*x
#Programme
def pro():
    print ("This is a calculator")
    print ("Select sections:")
    print("1.Basic calculations")
    print("2.Advanced calculations")
    a = input()
    # Basic
    if a == "1":
        print ("Choose your calculation:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        b= input()
        if b in ("1","2","3","4"):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
    # 程序
            if b == "1":
                print(add(num1,num2))
            elif b == "2":
                print(sub(num1,num2))
            elif b == "3":
                print(multi(num1,num2))
            elif b == "4":
                print(divide(num1,num2))
            reset()
    elif a == "2":
         print ("Choose your calculation:")
         print("1.Algebra")
         print("2.Trigomentary")
         print("3. Chart")
         c= input()
         if c in("1","2"):
            print ("Not done yet")
         elif c == "3":
             print("Choose the type of chart you want to do:")
             print("1.Plot")
             print("2.Pie Chart")
             print("3.Graph")
             print("4.Bar Chart")
             d= input()
             if d == "1":
                 print("Which type of plot?")
                 print("1.Normal")
                 print("2.Quadraic Equation")
                 e= input()
             elif d == "2":
                   print ("Is there a fifth array?")
                   g=input()
                   if g == "yes":
                         aa=input("Enter first array:")
                         ab=input("Enter second array:")
                         ac=input("Enter third array:")
                         ad=input("Enter fourth array:")
                         ae=input("Enter fifth array:")
                         sizes = ([aa, ab, ac ,ad, ae])
                         fig1, ax1 = plt.subplots()
                         ax1.pie (sizes)
                         plt.pie(sizes)
                         plt.show() 
                   else:   
                       aa=input("Enter first array:")
                       ab=input("Enter second array:")
                       ac=input("Enter third array:")
                       ad=input("Enter fourth array:")
                       sizes = ([aa, ab, ac ,ad])
                       fig1, ax1 = plt.subplots()
                       ax1.pie (sizes)
                       plt.pie(sizes)
                       plt.show() 
             if e == "1":
                 xa =float(input("Enter first data in the x axis"))
                 xb =float(input("Enter second data in the x axis"))
                 xc = float(input("Enter third data in the x axis"))
                 xd =float(input("Enter fourth data in the x axis"))
                 ya =float(input("Enter first data in the y axis"))
                 yb =float(input("Enter second data in the y axis"))
                 yc =float(input("Enter third data in the y axis"))
                 yd= float(input("Enter fourth data in the y axis"))
                 plt.plot([xa,xb,xc,xd], [ya,yb,yc,yd])
                 plt.title("Plot")
                 plt.show() #Remember this when making a plot!
                 reset()
             elif e == "2":
                y=int( input("Y intercept?"))
                x=int(input("X intercept?"))
                funcx=int(input("Any coefficent in the x infront of the equation? If not, its 1"))
                funcy=int(input("Whats the coefficient in the middle part/number of the equation?"))
                aos= (axis(funcx,funcy))   
                print ("Axis of symmetry", aos) #print () is needed to call a function
                print("For  minimum point, substitute the axis of symmetry to x")
                print("For maximum point")
                up= int(input("The coeffcient of the last number of the equation"))
                mid=int(input(" The coefficient of the number in the middle of the equation"))
                dow=int(input("The coefficient of the first number in the front of the equation"))
                print(max(dow,mid,up))
#Actual running
pro()        


