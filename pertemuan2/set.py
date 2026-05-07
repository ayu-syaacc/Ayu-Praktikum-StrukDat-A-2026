#set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates Not Allowed
#ex 1
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#ex 2
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#ex 3
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set Items - Data Types
#ex 1
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#ex 2
set1 = {"abc", 34, True, 40, "male"}

#type
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round
print(thisset)

#Access Items
#ex 1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#ex 2
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#ex 3
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset)

#Remove Item
#ex 1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#ex 2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#ex 3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#ex 4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#ex 5
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) 

#loop set
#loop items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets
#ex 1
#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#ex 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#Join Multiple Sets
#ex 1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#ex 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

#Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection
#ex 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#ex 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#ex 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#ex 4
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#difference
#ex 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#ex 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1
print(set3)

#ex 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#symmetric difference
#ex 1
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#ex 2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)

#ex 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

#Creating a frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

