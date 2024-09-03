#1
#2
word = input()
while word != "quit!":
    if len(word) > 4:
        print(word.replace("or", "our"))
    else:
        print(word)
    word = input()
