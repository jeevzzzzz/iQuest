#from the given list take even numbers and make another list 

'''
a=[1,2,3,4,5,6,8,9,10]
b=[]
c=[]
for x in a:
    if x%2==0:
        b.append(x) #for even
    else:
        c.append(x) #for odd
print(b)
print(c)
''' 

'''
a=[1,2,3,4,5,6,8,9,10] #this is list comprension(above code reduced into 1 line
b=[x for x in a if x%2==0]
print(b)
'''

'''
----------------------------------------------------------------------------
TUPLE    
we can create empty set
tuple is heterogenous
access by index,slicing operator
we can give dublicate items
it  is immutable

HW
use membership operator
----------------------------------------------------------------------------
'''
'''
a=(1,2,3,4,5,6,7,8,8,'jeev')
'''

'''
print(a[3])
print(a[0:9]) #full list
print(a[0:10:2]) #start,stop,step
print(a[::-1]) #reverse list
'''
'''
a[4]=9 #they are immutable
print(a) #we can replace the list (mutable) (\/)
'''

'''
print(len(a)) #display the number of elements (\/)
print(a.count(8))  #count (\/)
'''

'''
for x in a:
    print(x,a.count(x)) #(\/)
 #to count the elements in list with value
 '''
 
'''
a.append(15) #tuple has no append attribute
#print(a)
'''

'''
a.insert(0,40) #tuple' object has no attribute 'insert'
print(a)
'''

'''
f=a.copy() #'tuple' object has no attribute 'copy'
print(f)
'''

'''
a.extend(c) #'tuple' object has no attribute 'extend'
print(a)
'''

'''
a.pop(0) #'tuple' object has no attribute 'pop'
print(a)
'''

'''
a.sort() 'tuple' object has no attribute 'sort'
print(c)
'''
'''
a=[1,2,3,4,5,6,8,9,10] #this is list comprension(above code reduced into 1 line
b=[x for x in a if x%2==0]
print(b)
'''
'''
-----------------------------------------------------------------
SETS
it cannot be empty , if empty it will be dictonary
accessing cannot be done through index
it is heterogeneous
-----------------------------------------------------------------
'''

a={3,4,5,6,7,8,'jeev','hiii'}

#print(a)
print(len(a)) #it will show the length

'''
print(count(a)) #cannot count
'''

'''
a=[1,2,3,4,5,6,8,9,10] #this is list comprension(above code reduced into 1 line
b=[x for x in a if x%2==0]
print(b)
'''

a.add(121) #for adding element to the list
print(a)

a.pop() #first element will pop
print(a)

'''
a.pop(7)
print(a) #set.pop() takes no arguments (1 given)
'''

print(list(a)[1]) #accessing

'''
a.append(234) 'set' object has no attribute 'append'
print(a)
'''