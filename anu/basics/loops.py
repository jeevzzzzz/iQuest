#one of the syntax
'''for x in range(0,6):  #it will print 0,1,2...,5
    print(x)'''
    
#one of the syntax for skip
'''for x in range(0,6,2): #it will print 0,2,4
    print(x)'''

'''for x in range(0,6): 
    print(x,end=' ') #it will print in single line'''

#for pyramid
'''for x in range (0,6):
    print("*" * x)'''
    
#output
'''
*
**
***
****
*****
'''
    
#for reverse pyramid    
'''for x in range (6,0,-1):
    print("*" * x)'''
    
#output
'''
*****
****
***
**
*
'''

#it start from =ve and -ve.. it will accept -ve only
    #if the start point is lesser than end point
'''for x in range(-6,-1):  
    print(x)'''
    
#if we have for x in range(-10,6,-2) it will not execute
#because it will move left side as it is in range -10 to 6
#but -12 is not possible...
#if we have for x in range(-10,6,2) then it will move right
#it will print -10,-8....6

#factorial of numbers
'''
num = int(input("Enter a number: "))
fact=1
while num<0:
    print("enter the valid number")
    num = int(input("Enter a number: "))
if num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       fact = fact*i
   print("The factorial of",num,"is",fact)
'''

#fibonacci

'''n1 = 0
n2 = 1
num = int(input("Enter a number:"))
while num < 0:
    print("negative not found")
    num = int(input("Enter a number:"))
if num==0:
    print(n1)
elif num==1:
     print(n1)
     print(n2)
else:
    print(n1)
    print(n2)
    for i in range(2,num+1):
        num = n1 + n2
        print(num)
        n1=n2
        n2=num
'''

#continue
'''for x in range(8):
    print(x)
    if x==4:
        print(x is four)
        continue
'''
        
#assignment for multiply 2 with even numbers and print odd numbers as it is
n = int(input("Enter a number:"))
for x in range (0,n):
    if x % 2 == 0:
        print(x*2)
        continue
    else:
        print(x)
   
        
      

    