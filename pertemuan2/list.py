thislist = ["apple", "banana", "cherry"]
print(thislist)

#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
#ex 1
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#ex 2
list1 = ["abc", 34, True, 40, "male"]

#Type of List
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
#ex 1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#ex 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#ex 3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Negative Indexing Range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#change a Range of Item Values
#ex 1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#ex 2
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#ex 3
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add list items
#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove List Items
#Remove Specified Item
#ex 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#ex 2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#ex 1
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#ex 2
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#ex 3
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#ex 4
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Lists
#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
#ex 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#ex 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

#the syntax
#(Condition)
#ex 1 
newlist = [x for x in fruits if x != "apple"]

#ex 2
newlist = [x for x in fruits]

#(iterable)
#ex 1
newlist = [x for x in range(10)]

#ex 2
newlist = [x for x in range(10) if x < 5]

#(expression)
#ex 1
newlist = [x.upper() for x in fruits]

#ex 2
newlist = ['hello' for x in fruits]

#ex 3
newlist = [x if x != "banana" else "orange" for x in fruits]

#Sort Lists
#Sort List Alphanumerically
#ex 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#ex 2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
#ex 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#ex 2
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort
#ex 1
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#ex 2
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy list
#Use the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#use the slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# join lists
#Join Two Lists
#ex 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#ex 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#ex 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#list methode
