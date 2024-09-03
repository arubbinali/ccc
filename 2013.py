"""
#1
Y = int(input())
M = int(input())
dif = M - Y
print(M + dif)

#2
word = input()
possibilites = ["I", "O", "S", "H", "Z", "X", "N"]
word = list(word)
correct_count = 0
for check in range(len(word)):
    if word[check] in possibilites:
        correct_count += 1

if correct_count == len(word):
    print("YES")
else:
    print("NO")
    """