"""
#1
n = int(input())
if n == 1:
    print("1")
else:
    pass
print(n%2)

0 - 0
1 - 1
2 - 2
3 - 2
4 - 3
5 - 3
6 - 4
7 - 4
8 - 5
9 - 5
10 - 6


    QUESTION 2 NOT DONE


"""
#2
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

N = 0
B = 0
count = 0
Ndec = 0
Bdec = 0

while count != s:
    while N <= a and B <= c:
        N += 1
        B += 1
    while Ndec <= b or Bdec <= d:
        N -= 1
        B -= 1
        if Ndec != b:
            Ndec += 1
        if Bdec != d:
            Bdec += 1
    count += 2



if N > B:
    print("N")
elif B > N:
    print("B")
else:
    print("Tie")