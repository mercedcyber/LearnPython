
Ramiro Gonzalez 

Chapter 3

Gaddis, T. (2019). Starting out with Python. New York, NY: Pearson

# Day of the week


```python
number = int(input("Enter a number between 1 and 7: "))
if(number == 1):
    print('Monday')
elif(number == 2):
    print('Tuesday')
elif(number == 3):
    print('Wednesday')
elif(number == 4):
    print('Thrusday')
elif(number == 5):
    print('Friday')
elif(number == 6):
    print('Saturday')
elif(number == 7):
    print('Sunday')
else:
    print("Out of range")
        
```

    Enter a number between 1 and 7: 4
    Thrusday
    

# Areas of Rectangles


```python
lenRect1 = float(input('Enter length of first rectangle. '))
widthRect1 = float(input('Enter width of first rectangle. '))
lenRect2 = float(input('Enter length of second rectangle. '))
widthRect2 = float(input('Enter width of second rectangle. '))
rect1Area = lenRect1*widthRect1
rect2Area = lenRect2*widthRect2
if(rect1Area > rect2Area):
    print("Area of the first rectangle is greater than second rectangle.")
elif(rect1Area < rect2Area):
    print("Area of the second rectangle is greater than first rectangle. ")
else:
    print("Area of the second rectangle is the same as first rectangle. ")
```

    Enter length of first rectangle. 4
    Enter width of first rectangle. 4
    Enter length of second rectangle. 4
    Enter width of second rectangle. 4
    Area of the second rectangle is the same as first rectangle. 
    

# Age Classifier 


```python
age = int(input("Enter the person's age"))
if(age < 1):
    print("The person is an infant.")
if(age >= 1 and age < 13):
    print("The person is a child.")
if(age >= 13 and age < 20):
    print("The person is a teenager.")
if(age >= 20):
    print("The person is an adult.")

```

    Enter the person's age34
    The person is an adult.
    

# Roman Numerals


```python
number = int(input('Enter a number between 1 and 10 (inclusive): '))
if(number == 1):
    print("I")
elif(number == 2):
    print("II")
elif(number == 3):
    print("III")
elif(number == 4):
    print("IV")
elif(number == 5):
    print("V")
elif(number == 6):
    print("VI")
elif(number == 7):
    print("VII")
elif(number == 8):
    print("VIII")
elif(number == 9):
    print("IX")
elif(number == 10):
    print("X")
else:
    print("Out of range: ")
        
```

    Enter a number between 1 and 10 (inclusive): 3
    III
    

# Mass and Weight


```python
mass = float(input("Enter the object's mass: "))
weight = mass*9.8;
if(weight >= 500):
    print("The object is too heavy.")
if(weight <= 100):
    print("The object is too light. ")

```

    Enter the object's mass: 4
    The object is too light. 
    

# Magic Dates


```python
month = int(input("Enter a month (numeric): "))
day = int(input("Enter a day"));
year2 = int(input("Enter a two digit year"))
if(month*day == year2):
    print("The date is magic ")
else:
    print("The date is not magic ")
```

    Enter a month (numeric): 4
    Enter a day4
    Enter a two digit year4
    The date is not magic 
    

# Color Mixer


```python
colorPrimary1 = input("Enter name of first primary color: ")
colorPrimary2 = input("Enter name of second primary color: ")
if(colorPrimary1 == 'red' and colorPrimary2 == 'blue' or 
   colorPrimary1 == 'blue' and colorPrimary2 == 'red'):
    print("When you mix " + colorPrimary1 + " and " + 
          colorPrimary2 + ", you get purple")
elif(colorPrimary1 == 'red' and colorPrimary2 == 'yellow' or
     colorPrimary1 == 'yellow' and colorPrimary2 == 'red'):
    print("When you mix " + colorPrimary1 + " and " + colorPrimary2 + 
          ", you get orange")
elif(colorPrimary1 == 'blue' and colorPrimary2 == 'yellow' or 
     colorPrimary1 == 'yellow' and colorPrimary2 == 'blue'):
    print("When you mix " + colorPrimary1 + " and " + colorPrimary2 + 
          ", you get green")
else:
    print("Error, secondary color not found")
    
```

    Enter name of first primary color: 34
    Enter name of second primary color: 43
    Error, secondary color not found
    

# Hotdog Cookout Calculator 


```python
people = int(input("Enter number of people attending: "))
hotDogs = 10; 
hotDogBuns = 8; 
minHotDogs = (int)(people/10)
print("Minimum number of packages of hot dogs:", minHotDogs)
minHotDogBuns = (int)(people/8)
print("Minimum number of packages of hot dog buns:",minHotDogBuns)
leftHotDogs = people - minHotDogs*hotDogs
print("Number of hot dogs left:",leftHotDogs)
leftHotDogBuns = people - minHotDogBuns*hotDogBuns; 
print("Number of hot dog buns left:", leftHotDogBuns)

```

    Enter number of people attending: 34
    Minimum number of packages of hot dogs: 3
    Minimum number of packages of hot dog buns: 4
    Number of hot dogs left: 4
    Number of hot dog buns left: 2
    

# Roulette Wheel Colors


```python
pocketNum = int(input("Enter a pocket number: "))
if(pocketNum == 0):
    print("Pocket 0 is green ")
elif(pocketNum >= 1 and pocketNum <= 10):
    if(pocketNum%2 != 0):
        print("Pocket {} is red".format(pocketNum))
    if(pocketNum%2 == 0):
        print("Pocket {} is black".format(pocketNum))
elif(pocketNum >= 11 and pocketNum >= 18):
    if(pocketNum%2 != 0):
        print("Pocket {} is black".format(pocketNum))
    if(pocketNum%2 == 0):
        print("Pocket {} is red".format(pocketNum))
elif(pocketNum >= 19 and pocketNum >= 28):
    if(pocketNum%2 != 0):
        print("Pocket {} is red".format(pocketNum))
    if(pocketNum%2 == 0):
        print("Pocket {} is black".format(pocketNum))
elif(pocketNum >= 29 and pocketNum >= 36):
    if(pocketNum%2 != 0):
        print("Pocket {} is black".format(pocketNum))
    if(pocketNum%2 == 0):
        print("Pocket {} is red".format(pocketNum))
else:
    print("Out of range")
```

    Enter a pocket number: 43
    Pocket 43 is black
    

# Money Counting Game


```python
pennies = int(input("Enter number of pennies: "))
nickles = int(input("Enter number of nickles: "))
dimes = int(input("Enter number of dimes: "))
quarters = int(input("Enter number of quarters: "))
money = pennies*1 + nickles*5 + dimes*10 + quarters*25 
if(money == 100):
    print("One Dollar! ")
elif(money > 100):
    print("More than one dollar")
elif(money < 100):
    print("Less than a dollar")
else:
    print("An error has occurred! ")
```

    Enter number of pennies: 34
    Enter number of nickles: 34
    Enter number of dimes: 43
    Enter number of quarters: 43
    More than one dollar
    

# Book Club Points


```python
purchaseAmount = int(input("Enter the number of books purchased this month: "))
if(purchaseAmount == 0):
    print("0 points awarded.")
elif(purchaseAmount == 2):
    print("5 points awarded")
elif(purchaseAmount == 4):
    print("15 points awarded")
elif(purchaseAmount == 6):
    print("30 points awarded")
elif(purchaseAmount >= 8):
    print("60 points awarded")
else:
    print("Unknown points awarded")
```

    Enter the number of books purchased this month: 43
    60 points awarded
    

# Software Sales


```python
quantity = int(input("Enter the number of packages purchased."))
price = 99; 
if(quantity >= 10 and quantity <= 19 ):
    discount = price*.10; 
    total = price - discount
    print("Discount is {} and total price is {}".format(discount,total))
elif(quantity >= 20 and quantity <=49):
    discount = price*.20; 
    total = price - discount
    print("Discount is {} and total price is {}".format(discount,total))
elif(quantity >= 50 and quantity <=99):
    discount = price*.30; 
    total = price - discount
    print("Discount is {} and total price is {}".format(discount,total))
elif(quantity >= 100):
    discount = price*.40; 
    total = price - discount
    print("Discount is {} and total price is {}".format(discount,total))
else:
    print("No discount")
```

    Enter the number of packages purchased.34
    Discount is 19.8 and total price is 79.2
    

# Shipping Charges


```python
wPackage = int(input("Enter the weight of a package: "))
if(wPackage <= 2):
    charge = wPackage*1.50
    print("Shipping charge is ${}".format(charge))
elif(wPackage > 2 and wPackage <= 6):
    charge = wPackage*3.00
    print("Shipping charge is ${}".format(charge))
elif(wPackage > 6 and wPackage <= 10):
    charge = wPackage*4.00
    print("Shipping charge is ${}".format(charge))
elif(wPackage > 10):
    charge = wPackage*4.75
    print("Shipping charge is ${}".format(charge))

```

    Enter the weight of a package: 34
    Shipping charge is $161.5
    

# Body Mass Index


```python
weight = int(input("Enter weight in pounds: "))
height = int(input("Enter height in inches: "))
bmi = weight*703/(height*height)
if(bmi >= 18.5 and bmi <= 25):
    print("Optimal")
elif(bmi < 18.5):
    print("Underweight")
elif(bmi > 25):
    print("Overweight")

```

    Enter weight in pounds: 432
    Enter height in inches: 43
    Overweight
    

# Time Calculator


```python
seconds = int(input("Enter number of seconds: "))
if(seconds >= 60):
    minutes = seconds/60;
    print("{} minutes".format(minutes))
elif(seconds >= 3600):
    hours = seconds/3600;
    print("{} hours".format(hours))
if(seconds >= 86400):
    days = seconds/86400;
    print("{}".format(days))
```

    Enter number of seconds: 324
    5.4 minutes
    
