

my_list=["zaman","rohith",3,6]


my_list.append("athul")#used to add a single element to the list.
print(my_list)

my_list.append([1,2,3])#here we add a list into a list,so itwill show as a nested list in output.
print(my_list)

my_newlist=["jessin","aswin","shahid"]
my_list.extend(my_newlist)#used to add multiple elements to a list not like append
print(my_list)


my_list.remove(6)#direct element,used to delete a specified element from the list(if two same elements are present then it will remove first)
print(my_list)

print(my_list.pop(0))#using index number,used to remove an element (if we dont specify any index number it will remove the last element)
print(my_list)


numbers=[1,44,87,23,12]
numbers.sort()#used to sort elements(it changes the orginal list)
print(numbers)
numbers.sort(reverse=True)#to get descending order
print(numbers)
numbers.reverse()#used to reversethe order of elements(it changes the list)
print(numbers)

zaman_list=[1,2,4,6,]
zaman_list.insert(-2,3)#used to insert an element at a specific index position,list_name.index(index,element),if index is greater than the list length then it will add to last
print(zaman_list)#if index is negative,it will counts from the last(if -1 is index it will add before the last element)

print(my_list[:])#slicing,here we get full list
print(my_list[2:])
print(my_list[:5])
print(my_list[::2])#here we get every second element(always add first element)
print(my_list[-3:])#here we get last 3 elements
print(my_list[::-1])#reverse the list
print(my_list[0:3:1])#start:end:step()

#print(my_list.clear())#removes all elements from the list

print(my_list.count("athul"))#used to count how many times an element is appeared(if the element is not present it return 0)

my_list=my_list.copy()#used to create a copy of the list(new list with same elements)
print(my_list.copy())

print(my_list.index("athul"))#used to show index number