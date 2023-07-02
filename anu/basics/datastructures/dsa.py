'''
1.tuple ( ) 
2.list [ ] 
3.dictionaries {key:value}
4.sets { }
'''
from test.crashers.mutation_inside_cyclegc import lst
from pip._vendor.pyparsing.core import empty
from itertools import count

'''

#simple checks
'''
 #list
'''
a=[1,2,3,4,5,6,8,8,9,'jeev']
'b=() #tuple
c={1,2} #set
d={1:1,2:2,3:3} #dict
e= 1,2,3 #tupple
'''

'''print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
'''

'''
----------------------------------------------------------------------------------
1.list 
we can create empty set
access by index,slicing operator
we can give dublicate items
list is heterogenous(it can take strings also)
list can be mutable
---------------------------------------------------------------------------------
'''

'''
print(a[3])
print(a[0:10]) #full list
print(a[0:10:2]) #start,stop,step
print(a[::-1]) #reverse list
a[2]=12
print(a[3])
print(a) #we can replace the list (mutable)
print(len(a)) #display the number of elements
print(a.count(8))        #count
for x in a:
print(x,a.count(x)) #to count the elements in list with value
a.append(15) #will add element to the end of list
print(a)
'''

'''
a.insert(0,40) #it will add 40 to the index that is specified
print(a)
'''

'''
f=a.copy() #it will copy a to f
print(f)
'''

'''
a.append(c) #it will be adding the the entire list as single element
print(a) #c will be added to a
print(a[10]) #it will print entire a
'''

'''
a.extend(c) #it will add list c to a seperately
print(a)
print(a[11])
'''

'''
a.pop(0) #it will pop the element based on index
print(a)
'''

'''
c.sort()
print(c)
'''

'''
a.remove(2) #it will remove element based on value
print(a)
'''

'''
a.pop() #it will pop the element in end
print(a)
'''

'''
a.remove() #list.remove() takes exactly one argument (0 given)
print(a)
'''
              
'''
--------------------------------------------------------------------
tuple

'''




