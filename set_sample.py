my_set={"hii","hello","heyy",1,4,1}

my_set.add(4)#adds an element
print(my_set)

#my_set.remove(1)#removes elemets(how many times it is present it will remove all ),raises error if the specified element is not present
#print(my_set)

my_set.discard(1)#removes element(how many times it is present it will remove all ),no error if the element is not found 
print(my_set)

print(my_set.pop())#removes a random element every time we runs.returns the removed element

s=["list",1,"name",2,"age"]
my_set.update(s)#add multiple elements (from list or set)
print(my_set)

a={1,2,3,4,5,6,10,12}
b={3,2,10,7,8,9,6}

#print(a.union(b))#joins the set

print(a.intersection(b))#display same elements

print(a.difference(b))#avoid same elements(difference)and display the elemets in first set(here a)

print(a.symmetric_difference(b))#avoid same elements( display from both sets)

c={1,2,3,4}
d={1,2}

print(d.issubset(c))#checks if a set is the subset of other set(contains the all set in other)

print(c.issuperset(d))#checks if "c" contains all the elements of "d"(super set)

print(c.isdisjoint(d))#checks if they have common elemets(disjoint)