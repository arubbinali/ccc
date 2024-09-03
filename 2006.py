"""
#1
cal = 0
print("Welcome to Chip's Fast Food Emporium")
b = int(input("Please enter a burger choice: "))
s = int(input("Please enter a side order choice: "))
dr = int(input("Please enter a drink choice: "))
d = int(input("Please enter a dessert choice: "))

if b == 1:
    cal = cal + 461
elif b == 2:
    cal = cal + 431
elif d == 3:
    cal = cal + 420

if s == 1:
    cal = cal + 100
elif s == 2:
    cal = cal + 57
elif d == 3:
    cal = cal + 70

if dr == 1:
    cal = cal + 130
elif dr == 2:
    cal = cal + 160
elif dr == 3:
    cal = cal + 118

if d == 1:
    cal = cal + 167
elif d == 2:
    cal = cal + 266
elif d == 3:
    cal = cal + 75
cal = str(cal)
print("Your total Calorie count is", cal + ".")

#2

m = int(input("Enter m: "))
n = int(input("Enter n: "))
count = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i + j == 10:
            count += 1

if count == 1:
    print("There is 1 way to get the sum 10.")
else:
    print(f"There are {count} ways to get the sum 10.")
"""







