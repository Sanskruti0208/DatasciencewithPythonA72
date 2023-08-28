# Dictionary and its fun

d={'ashish':10,'sanskruti':20,'pihu':30}
d

type(d)
len(d)
print(d)
d

#extracting keys from dictionary
d={'ashish':10,'sanskruti':20,'pihu':30}
d.keys()

# extracting values from dictionary
d.values()

# changing an exsisting element 
d={'ashish':10,'sanskruti':20,'pihu':30}
d['pihu']=55
print(d)

#adding new element 
d={'ashish':10,'sanskruti':20,'pihu':30}
d['sans']=15
d

# update one exsisting dict with another dict
d1={'sam':11,'kasturi':12,'shreyaa':13}
d2={'shruti':14,'aabha':15,'shravni':16}
d1.update(d2)
d1

#poping
d={'ashish':10,'sanskruti':20,'pihu':30}
d.pop('pihu')
d.pop()
