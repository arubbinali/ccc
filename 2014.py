"""
#1
a = int(input())
b = int(input())
c = int(input())
sum = a + b + c
if a == b and b == c:
    print("Equilateral")
elif sum == 180 and (a == b or b == c):
    print("Isosceles")
elif sum == 180 and (a != b and b != c):
    print("Scalene")
else:
    print("Error")

#2
V = int(input())
to = input()
a = to.count("A")
b = to.count("B")
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")
"""
