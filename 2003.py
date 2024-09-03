"""
#1
t = int(input("Enter tine length: "))
s = int(input("Enter tine spacing: "))
h = int(input("Enter handle length: "))

for x in range(t):
    for x in range(3):
        print("*", " "*(s-1), end="")
    print()

print("*" + "*"*s + "*" + "*"*s + "*")

for y in range(h):
    print(" " * (s), "*")

#2
first_num = last_num = 0
number = int(input("Enter number of pictures:\n"))
lowest_perimeter = 9999999999999
while True :
    if number == 0:
        break
    for i in range(1, number + 1):
        for j in range(number, 0, -1):
            if i * j == number:
                perimeter = 2 * (i + j)
                if perimeter < lowest_perimeter:
                    lowest_perimeter = perimeter
                    first_num = i,
                    last_num = j,
            if i == j:
                break
    first = sum(first_num)
    last = sum(last_num)
    print(f"Minimum perimeter is {perimeter} with dimensions {first} x {last}")
    number = int(input("Enter number of pictures:\n"))
"""