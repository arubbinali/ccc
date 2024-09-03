"""
#1
B = int(input())
P = 5 * B - 400
print(P)
if P < B:
    print(1)
elif P > B:
    print(-1)
else:
    print(0)

#2
N = int(input())
names = []
bids = []
for x in range(N):
    name = input()
    bid = int(input())
    names.append(name)
    bids.append(bid)
highest = bids.index(max(bids))
print(names[highest])

#3
answers = []
number_answers = []
while True:
    number = input()
    if number == "99999":
        break
    number = str(number)
    ay = number[0:2]
    first = ay[0]
    second = ay[1]
    first = int(first)
    second = int(second)
    sum = first + second
    number = str(number)
    if sum % 2 != 0:
        direction = "left"
        answers.append(direction)
        number_answers.append(number[2:])
    elif sum % 2 == 0 and sum != 0:
        direction = "right"
        answers.append(direction)
        number_answers.append(number[2:])
    elif sum == 0:
        answers.append(direction)
        number_answers.append(number[2:])
    
for _ in range(len(answers)):
    print(answers[_], number_answers[_])
"""










