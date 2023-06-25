#INITIALIZATION
#SUM
''''x=10.0
y=10
print(x+y) 
print(type(x)) #FOR_DATATYPE
print(type(y)) #FOR_DATATYPE

x=y=23
print(x+y)

x,y=20,40
print(x+y)'''

#OPERATORS
'''
operator- symbols which are used to operate on variables
types of operation:
1. arithmetic +,-,*,/,%
2. logical and,or,nor,nand,
3. incremental ++,--
4. relational <,>,=>,==
5. assignment =
6. membership (Membership operators are used to test if a sequence is presented in an object:)
in       Returns True if a sequence with the specified value is present in the object        x in y    
not in   Returns True if a sequence with the specified value is not present in the object    x not in y
'''

#EXAMPLE THAT SHOWS LOCATION
'''a=1
print(id(a))
b=2
print(id(b))
c=3
print(id(c))
d=1
print(id(d))
e=10
print(id(e))'''

#EXAMPLE FOR OPERATORS
''''a=1
b=2
c=3
d=10
output=a+b*(d/b)**b-a
print(output)
output2=a%b
print(output2)
output3=a//c #floored division
print(output3)'''


#BODMASS RULE
'''this will be done based on bodmass rule
BODMASRULE:
op:1+2*(10/2)**2-1
op:1+2*5**2-1
op:1+2*25-1
op:1+50-1
op:51-1
op:50
if we give / it will be decimal, if we give // it will round off i.e=a/b'''
'''output= 1 and 0
print(output) #logical operator (we can combine multiple operators)'''

#print(3==2) relational operator

#control flow statement
'''
The flow control statements are divided into three categories
1.Conditional statements (if,if-else,if-elif-else,nested if-else)
2.looping statements. (for loop,while loop,while-do,do-while)
3.sequential statements'''

#EXAMPLE FOR IF STATEMENT
''''a=1
b=1
if b>0:
    if a>0:
        b=b+1
        print(b)
    a=a+1
    print(a+2)
    
elif a>0:
    print("oooooo")

else:
    print("end")
    
print("Thank you")'''

#example program for largest of three numbers 
#example program using type casting
'''a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
c=int(input("Enter the number c: "))
output=a+b+c
print("The sum is:",output)
if  a>=b and a>=c:
    print("Largest number is:" ,a)
elif b>=c and b>=a:
    print("Largest number is:" ,b)
else:
    print("Largest number is:" ,c) '''



    