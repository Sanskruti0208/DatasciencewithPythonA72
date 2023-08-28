# DAY 4 Set and its functions

#create a set
s={10,'sanskruti',True}
print(s)

# unorderd
s

#duplicates not allowed
s={10,'sanskruti',True,10}
s

#get the length of set
len(s)

# datatype
type(s)

# unchangable
s={10,'sanskruti',True}
s[0]=30
s

# addition is used
s={10,'sanskruti',True,10}
s.add('pihu')
s

#remove
s={10,'sanskruti',True}
s.remove(10)
s

# updating multipule elements
s={10,20,30}
s.update([1,2,3])
s

#union
s1={1,2,3}
s2={10,20,30}
s2.union(s1)

# intersection
s1={1,2,3}
s2={10,3,20}
s1.intersection(s2)

