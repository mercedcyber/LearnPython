
Ramiro Gonzalez 

Chapter 4

Gaddis, T. (2019). Starting out with Python. New York, NY: Pearson

<b> Algorithm Workbench

# Bug Collector 


```python
total = 0; 
for days in range(5):
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    bugs = int(input("How many bugs were colleceted day {}: ".format(week[days]))) # or days + 1
    total = total + bugs
print("{} bugs were collected".format(total))
```

    How many bugs were colleceted day Monday: 1
    How many bugs were colleceted day Tuesday: 1
    How many bugs were colleceted day Wednesday: 1
    How many bugs were colleceted day Thursday: 1
    How many bugs were colleceted day Friday: 1
    5 bugs were collected
    

# Calories Burned 


```python
caloriesPerMin = 4.2
for minutes in range(10,30,5):
    calories = caloriesPerMin*minutes
    print("In {} you burned {} calories".format(minutes,calories))
```

    In 10 you burned 42.0 calories
    In 15 you burned 63.0 calories
    In 20 you burned 84.0 calories
    In 25 you burned 105.0 calories
    

# Budget Analysis


```python
budget = int(input("Enter budget amount for a month: "))
total = 0 
yesno = "y"
while yesno == "y":
    expense = int(input("Enter expense: "))
    total = total + expense; 
    yesno = input("More expenses? Enter y or n:")
print(" ${} is the total amount spent. ".format(total))
if(total < budget):
    underAmount = budget - total;
    print("Underbudget by {}".format(underAmount))
```

    Enter budget amount for a month: 1
    Enter expense: 1
    More expenses? Enter y or n:1
     $1 is the total amount spent. 
    

# Distance Traveled 


```python
mph = int(input("Enter the miles per hour travelled: "))
hours = int(input("Enter number of hours travelled: "))
for travel in range(1,hours):
    distance = mph*travel; 
    print("In the {} hour the vehicle travelled {} miles".format(hours, distance))
    
```

    Enter the miles per hour travelled: 1
    Enter number of hours travelled: 1
    

# Average Rainfall


```python
yearsNum = int(input("Enter the number of years: "))
monthsInYear = 12
totalRainfall = 0
averageRainfalPerMonth = 0
for years in range(yearsNum):
    print("For year {}".format(years + 1))
    for month in range(monthsInYear):
        rainfallMonth = int(input("Enter amount of rainfall month number {} :".format(month + 1)))
        totalRainfall = totalRainfall + rainfallMonth; 
yearsToMonth = yearsNum*monthsInYear
averageRainfall = totalRainfall/yearsToMonth
print("There are {} months in {} years".format(yearsToMonth,yearsNum))
print("Total rainfal was {} inches".format(totalRainfall))
print("Average rainfall per month is {}".format(averageRainfall))
```

    Enter the number of years: 1
    For year 1
    Enter amount of rainfall month number 1 :1
    Enter amount of rainfall month number 2 :1
    Enter amount of rainfall month number 3 :1
    Enter amount of rainfall month number 4 :1
    Enter amount of rainfall month number 5 :1
    Enter amount of rainfall month number 6 :1
    Enter amount of rainfall month number 7 :1
    Enter amount of rainfall month number 8 :1
    Enter amount of rainfall month number 9 :1
    Enter amount of rainfall month number 10 :1
    Enter amount of rainfall month number 11 :1
    Enter amount of rainfall month number 12 :1
    There are 12 months in 1 years
    Total rainfal was 12 inches
    Average rainfall per month is 1.0
    

# Celsius to Fahrenheit Table 


```python
print("Celsius \t Fahrenheit")
for celsius in range(0,20,1):
    fahrenheit = (9/5.0)*celsius + 32; 
    print("{} \t\t  {} ".format(celsius,fahrenheit))
```

    Celsius 	 Fahrenheit
    0 		  32.0 
    1 		  33.8 
    2 		  35.6 
    3 		  37.4 
    4 		  39.2 
    5 		  41.0 
    6 		  42.8 
    7 		  44.6 
    8 		  46.4 
    9 		  48.2 
    10 		  50.0 
    11 		  51.8 
    12 		  53.6 
    13 		  55.400000000000006 
    14 		  57.2 
    15 		  59.0 
    16 		  60.8 
    17 		  62.6 
    18 		  64.4 
    19 		  66.2 
    

# Pennies for Pay


```python
numberOfDays = int(input("Enter number of days worked: "))
salary = 0.0
pennies = 1;
totalSalary = 0; 
for day in range(numberOfDays):
    salary = pennies
    pennies *= 2
    totalSalary = totalSalary + salary
    salaryDollars = salary/100
    print("On day {} salary is {} dollars".format(day + 1, salaryDollars))
totalSalaryDollars = totalSalary/100
print("Total pay was {} dollars".format(totalSalaryDollars))
```

    Enter number of days worked: 10
    On day 1 salary is 0.01 dollars
    On day 2 salary is 0.02 dollars
    On day 3 salary is 0.04 dollars
    On day 4 salary is 0.08 dollars
    On day 5 salary is 0.16 dollars
    On day 6 salary is 0.32 dollars
    On day 7 salary is 0.64 dollars
    On day 8 salary is 1.28 dollars
    On day 9 salary is 2.56 dollars
    On day 10 salary is 5.12 dollars
    Total pay was 10.23 dollars
    

# Sum of Numbers 


```python
sum = 0; 
userNumber = float(input("Enter a positive number or negative number to end : "))
while(userNumber >= 0):
    sum = sum + userNumber
    userNumber = float(input("Enter a positive number or negative number to end : ")) 
print("The total sum is {}".format(sum))
```

    Enter a positive number or negative number to end : .5
    Enter a positive number or negative number to end : .5
    Enter a positive number or negative number to end : -1
    The total sum is 1.0
    

# Ocean Levels 


```python
oceanRise = 1.6 #millimeters per year 
yearAmount = 25 #years
for year in range(yearAmount):
    oceanRisen = oceanRise*(year+1)
    print("In year {} ocean will have risen {} millimeters".format(year + 1,oceanRisen))

```

    In year 1 ocean will have risen 1.6 millimeters
    In year 2 ocean will have risen 3.2 millimeters
    In year 3 ocean will have risen 4.800000000000001 millimeters
    In year 4 ocean will have risen 6.4 millimeters
    In year 5 ocean will have risen 8.0 millimeters
    In year 6 ocean will have risen 9.600000000000001 millimeters
    In year 7 ocean will have risen 11.200000000000001 millimeters
    In year 8 ocean will have risen 12.8 millimeters
    In year 9 ocean will have risen 14.4 millimeters
    In year 10 ocean will have risen 16.0 millimeters
    In year 11 ocean will have risen 17.6 millimeters
    In year 12 ocean will have risen 19.200000000000003 millimeters
    In year 13 ocean will have risen 20.8 millimeters
    In year 14 ocean will have risen 22.400000000000002 millimeters
    In year 15 ocean will have risen 24.0 millimeters
    In year 16 ocean will have risen 25.6 millimeters
    In year 17 ocean will have risen 27.200000000000003 millimeters
    In year 18 ocean will have risen 28.8 millimeters
    In year 19 ocean will have risen 30.400000000000002 millimeters
    In year 20 ocean will have risen 32.0 millimeters
    In year 21 ocean will have risen 33.6 millimeters
    In year 22 ocean will have risen 35.2 millimeters
    In year 23 ocean will have risen 36.800000000000004 millimeters
    In year 24 ocean will have risen 38.400000000000006 millimeters
    In year 25 ocean will have risen 40.0 millimeters
    

# Tuition Increase


```python
percentIncrease = 3 # percent 
yearAmount = 5 # years
tuition = 8000 # Per semester 
tuitionYear = tuition*2 # Per year 
projectedTution = 0
for year in range(yearAmount):
    tuitionRate = (tuitionYear)*.03 
    projectedTution = projectedTution + (tuitionRate + tuitionYear) 
    print("In year {} projected tuition will be {}".format(year + 1, projectedTution))
    
```

    In year 1 projected tuition will be 16480.0
    In year 2 projected tuition will be 32960.0
    In year 3 projected tuition will be 49440.0
    In year 4 projected tuition will be 65920.0
    In year 5 projected tuition will be 82400.0
    

# Calculating the Factorial of a Number 


```python
number = int(input("Enter nonnegative integer n: "))
factorial = 1
for num in range(number):
    factorial = (num+1)*factorial
print("{}! is {}".format(number,factorial))
```

    Enter nonnegative integer n: 3
    3! is 6
    

# Population


```python
organismCount = int(input("Enter number of starting number of organisms: "))
averageIncrease = float(input("Enter the average daily population increase in percentage: "))
dayNumMult = int(input("Enter number of days the organism will be left to multiply: ")) 
print("Day Approximate \t Population")
increasePopulation = 0
for days in range(dayNumMult):
    organismCount = organismCount + increasePopulation
    increasePopulation = organismCount*(averageIncrease/100)
    print("{}\t\t{}".format(days + 1, organismCount))
```

    Enter number of starting number of organisms: 2
    Enter the average daily population increase in percentage: 30
    Enter number of days the organism will be left to multiply: 10
    Day Approximate 	 Population
    1		2
    2		2.6
    3		3.38
    4		4.394
    5		5.7122
    6		7.42586
    7		9.653618
    8		12.5497034
    9		16.31461442
    10		21.208998746000002
    

# Write a program that uses nested loops to draw this pattern:


```python
num_row = 7
num_col = 7
for r in range(num_row):
    for c in range(r):
        print('',end='')
    print("*"*num_col)
    num_col = num_col - 1
```

    *******
    ******
    *****
    ****
    ***
    **
    *
    

# Write a program that uses nested loops to draw this pattern: 


```python
num_row = 6 
num_col = 0
for r in range(num_row):
    for c in range(r):
        print('',end='')
    print("#{}#".format(" "*num_col))
    num_col +=1
```

    ##
    # #
    #  #
    #   #
    #    #
    #     #
    
