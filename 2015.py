"""
#1
month = int(input())
day = int(input())
if month == 2 and day == 18:
    print("Special")
elif month < 3 and day < 18:
    print("Before")
else:
    print("After")

#2
message = input()
happy = message.count(":-)")
sad = message.count(":-(")
if happy == 0 and sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
else:
    print("unsure")
"""
#3
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word = input()
for letter in word:
    position = alphabets.index(letter)
    for _ in range(len(alphabets)):
        pass
