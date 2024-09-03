"""
#1
R = int(input())
S = int(input())
cupcakes = (R * 8) + (S * 3)
students = 28
leftover = cupcakes % students
print(leftover)

#2
N = int(input())
scores = []
count = 0
for x in range(N):
    w = int(input())
    l = int(input())
    w = w * 5
    l = l * 3
    net = w - l
    scores.append(net)

for y in range(N):
    if scores[y] > 40:
        count += 1

if count == N:
    count = str(count)
    print(count + "+")
else:
    print(count)
"""








#3
instruction = 'AFB+8HC-4'

both = instruction.replace('+', ' tighten ').replace('-', ' loosen ')

l=[both]
print(l)

for _ in both:
    if _.isdigit() == True:
        print("rf")
        both.split(_)

print(both)



#AFB tighten 8HC loosen 4


#for char in both:
#    if char.isdigit() == True:
#    #    both.replace(char, f' {char} ')
#        print(char)


#print(both)






















