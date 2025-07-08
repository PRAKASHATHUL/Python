language="pyThon"
print(language.upper())
language.upper()#does not change the orginal string,changes are made in the new string
upper_language=language.upper()
print(upper_language)

lower_language=language.lower()#same as .upper()but converts all uppercase letters to lowecase
print(lower_language)

cap_language=language.capitalize()#converts the first character of the string to uppercase and the rest to lowecase
print(cap_language)

swap_language=language.swapcase()#upper to lower and lower to upper
print(swap_language)
"""
name=input("Enter your name:")
age=int (input("Enter your age:"))
print("My name is {} I am {} years old".format(name,age))#used to insert values using{} 
"""
strip_pgm="      python     "
print(strip_pgm.strip())#remove spaces
strip_pgm2="//python//"
result=strip_pgm2.strip("/")#we can also remove some characters
print(result)

startswith_1="It is beautiful"
print(startswith_1.startswith("It"))#used to check if a string begins with certain word or letter
print(startswith_1.startswith("it"))#case sensitive

endswith_1="It is very beautiful"
print(endswith_1.endswith("beautiful"))#used to check if a sting ends with certain word or letter


split_text="It is very beautiful"
#strip()will break a string into substrings (it will be in the form of list[])
result_text=split_text.split()#here splits all by space
print(result_text)

split_text1="apple,banana,mango,grape"
result_text1=split_text1.split(",")#here splits where ',' is present(using seperator)
print(result_text1)

result_text2=split_text1.split(",",2)#here only do 2 splits(maxsplit)
print(result_text2)


partition_text="welcome to python programming"
result_part=partition_text.partition("to")#splits into 3 parts(before the seperator,sperator,after the seperator)if there is nothing after the seperator it will return an empty string("")
print(result_part)#it is in the form of tuple()

result_part1=partition_text.partition('hi')#here the seperator is not present so it will return two empty strings after the orginal string
print(result_part1)




#Added a message
