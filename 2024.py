#1
cost = 0
for _ in range(3):
    i = int(input())
    if _ == 0: cost += i * 3
    elif _ == 1: cost += i * 4
    else: cost+= i * 5
print(cost)

#1 - gpt
multipliers = [3, 4, 5]
cost = sum(int(input()) * multipliers[i] for i in range(3))
print(cost)

#2
d, i = int(input()), int(input())
while d > i: d += i; i = int(input())
print(d)

#3
l = []
for _ in range(int(input())):
    l.append(int(input()))
def rem():
    c = 0
    for _ in l:
        if _ == max(l): c += 1
    for _ in range(c): del l[l.index(max(l))]
def find():
    rem(), rem()
    num, count = max(l), 0
    for _ in l:
        if _ == num: count += 1
    print(num, count)
find()

#3 - gpt
l = [int(input()) for _ in range(int(input()))]
def rem():
    max_val = max(l)
    while max_val in l: l.remove(max_val)
def find():
    rem(); rem()
    max_val = max(l)
    print(max_val, l.count(max_val))
find()

#4
