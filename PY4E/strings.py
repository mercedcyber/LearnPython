str1 = "Hello"
str2 = 'there' 
bob = str1 + str2 
print(bob) 
str3 = '123' 
#Error cannot concatentate string and int objects
str3 = str2 + 1
x = int(str3) + 1
print(x) 
name = input('Enter: ')
print(name) 
apple = input('Enter: ')
# input gives us back a string 
x = apple - 10 
fruit = 'banana'
letter = fruit[1] 
print(letter)
x = 3 
w = fruit[x-1]
print(w)
fruit = 'banana'
print(len(fruit))

fruit = 'banana'
index = 0
while(index < len(fruit)): 
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for letter in fruit: 
    print(letter)

word = 'banana'
count = 0
for letter in word: 
    if(letter == 'a'): 
        count = count + 1
print(count) 

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])