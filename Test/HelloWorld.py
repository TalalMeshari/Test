#k
print("hello there")
x = 5
y  = 6 
z = "hi there"
q = 1.23
#the str() function below is used to change the numbers x and y to strings.

"""
3 quotes for multiple lines comments
"""

print(str(x+y)+z)

print(type(x))
print(type(z))
print(type(q))

"""
for casting:
    int(...), float(...), str(...)
"""

a = "Hello, World!"
print(a[2:5]) #it prints from position 2 to 5

b = "talal, adel"
c = b.split(",")
d = c[0]
e = c[1]
print(b)
print(c)
print(d)
print(e.strip())


#taking an input:
print("Hi there!\n i'm Talal what's your name?")
#n = input() #the input function/method allows to take a user input.
#print("oh ", n) #or print("oh " + n)

"""
LISTS:
ordered and changable, allows duplicates
"""
#Lists are writter in square brackets:
firstList = ["Fruit", "Meat"]
print(firstList)
#can access the list items by the index number
print(firstList[0])
#loops through a list:
for x in firstList:
    print(x)
#check if something exists
if "Apple" in firstList:
    print("Apple exists in the list")
else: 
    print("Apple doesn't exists in the list")
#firstList.append(...) adds an item at the end of the list
firstList.append("Apple")
#to add an item to the list at a specific index we use insert(index number, item to add)
"""
using pop() deletes the item at the end of the list if the index is not specified
or if the index is specified then the indexed item will be deleted
"""
#clear() empties the list

#del firstList[1] deletes the item on index 1. It can deleted the entire list by: del firstList

"""
TUPLE:
ordered and unchangable, allows duplicates
"""
#Tuples uses round brackets
print("\n")
firstTuple = ("Banana", "Raspberry", "Orange")
print(firstTuple)

print(firstTuple[2])

#The following cannot be done because Tuples are unchangable

#firstTuple[0] = "Apple"

for x in firstTuple:
    print(x)

#tuples are unchangable so you cannot change an item like: firstTuple[1] = "yellow" can't do that
#cannot remove an item from a tuple

del firstTuple #this will delete the entire Tuple.


"""
SETS:
are unordered and unindexed
"""
firstSet = {"Hi", "Hello"}

#use a for loop to access the set same way as a tuple or a list
print("Hi" in firstSet)

#Once a set is created items cannot be changed but new items can be added later on ...

firstSet.add("Hi There!")#to add a single item
print(firstSet)
firstSet.update(["Banana","Orange"])#to add multiple items
print(firstSet)

#firstSet.remove(..) to remove an item


"""
DICTIONARIES:
unordered, changable and indexed
"""
print("\n")
firstDic = {
"fruit1":"orange",
"fruit2":"banana",
"randomNumber":"4"
}
print(firstDic)

#assigning a value from the dic into a variable.
g = firstDic["fruit1"] #you could use the get(): g = firstDic.get("fruit1")

#2 different loops are used in dics

#1- to get the "keys"
for x in firstDic:
    print(x)
#2- to get the value inside the key
for x in firstDic:
    print(firstDic[x]) #OR:
for x in firstDic.values():
    print(x)
#You can look for both keys and values
for x,y in firstDic.items():
    print (x,y)

#adding to a dictionary is done by simply adding a new index/key
firstDic["new"] = "shoes"

#to delete an item
firstDic.pop("new")#OR: del firstDic("new")

"""
IF STATEMENTS
"""
if condition:
    pass
elif expression:
    pass
else:
    pass


"""
FOR LOOPS
"""
for x in range(6): #it will loop 6 times. values 0 to 6 - range(2,6) means values from 2 but not
                    #including 6 - range(2,30,3) the last number = increment by 3 default is 1
    print("hi")
else:#after the loop ends the else statement will run
    print("something")

#NESTED LOOPS
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)



"""
Arrays:
very similar to Lists
"""
#adding to an array:
cars = ["Honda", "Toyota", "BMW"]
cars.append("Ferrari")
cars.pop(2) #deleted the 3rd element in the array
cars.remove("Honda")#removes by the item's name
#