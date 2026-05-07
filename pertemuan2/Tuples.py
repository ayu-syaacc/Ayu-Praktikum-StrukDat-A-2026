#TUPLES
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple Items - Data Types
#ex 1
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#ex 2
tuple1 = ("abc", 34, True, "male")

#type
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
#ex 1
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#ex 2
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#ex 3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Negative Indexing Range
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Update Tuples
#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Items
#ex 1
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#ex 2
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Remove Items
#ex 1
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)

#ex 2
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

#Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

#ex 2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*
#ex 1
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#ex 2 
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Looping Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Looping Using Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i += 1

#join two tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

