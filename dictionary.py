my_dict={"name":"man","age":0,"place":"earth",11:11}

my_dict.update({"num":2})#here the key:value pair is new so it adds it to the dict
print(my_dict)

my_dict.update({"name":"human"})#here the key already exits so it will update the key with new value
print(my_dict)#it can accept another dictionary or a tuple with(key,value)

print(my_dict.pop("num"))#changes the orginal dict.shows the value of removed key.
print(my_dict)
hii=my_dict.pop("hii","Not Found")#here "hi"is the key to remove but it is not there so we should give a default value that like" not found"if the key is not present to avoid key error
print(hii)

a=my_dict.popitem()#here it will remove the last item(key:value pair) from the dict(lifo)
print(a)#also changes the orginal dict

#b=my_dict.popitem("place")#
#print(b)

print(my_dict.get("name","not found"))#here it will show the value of key("name").if the key("name")is not in the dict it will show not found 

print(my_dict.keys())#show all keys

print(my_dict.values())#show all values

print(my_dict.items())#here it will show key:value pair in tuples(key,value)



my_dict[1]="number"
print(my_dict)

#print(my_dict[4])