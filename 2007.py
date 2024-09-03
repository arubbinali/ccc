#1
w1 = int(input())
w2 = int(input())
w3 = int(input())

if (w1 > w2 and w1 < w3) or (w1 > w3 and w1 < w2):
    print(w1)
elif  (w2 > w1 and w2 < w3) or (w2 > w3 and w1 < w2):
    print(w2)
else:
    print(w3)
#2
dict = {
    "CU" : "see you"



}
key = input()
print(dict[key])