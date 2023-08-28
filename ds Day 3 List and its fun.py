# DAY 3 List and its functions

#creating list
l=[10,22.5,True, 'sanskruti']
l
len(l)
type(l)
l[0] #i.e. it is orderd
l[-2]
l[2]
l[1:]
l[:-1]
l[1:3]

#changing the index value i.e. lists are mutable
l=[10,22.5,True, 'sanskruti']
l[0]=100
l

# appending the elements in list (push,pop)
l.pop() # start from last
l.pop()
l=[10,22.5,True, 'sanskruti']

l.append('pihu') # add element i.e push element
l

# to reverse the element of list
l=[60,10,83,90,45]
l.reverse()
l

l=[60,10,83,90,45]
l.sort()
l
l.reverse()
l

# to insert element in list
l=[60,10,83,90,45]
l.insert(0,'pihu')
l

#concatinating two lists
x=[1,2,3]
y=[4,5,6]
x,y
x+y

# repeating elements of list
x*3
y*6

