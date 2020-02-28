import math


result = 0


def calc_test(arg1, arg2):
    global result
    result = arg1 + arg2
    


print(result)
calc_test(4,6)
print(result)

# Declaring a list 
L = [1, "new", "quarry", 1+5]
print("Printing list (L): ")
print L
L.append(123)
print L
L.pop()
print L
print("End of list...")

# Declare Touples
T = (1, "new", "touple", 2+3)
print("Printing touple: ")
print T

print("# ==== ====")

# ============  ============

print("While i < 6 loop: ")
i = 1
while ( i < 6 ):
    i = i + 1
    print i,

print("---")

print("For i in \"String\" loop: ")
s = "String"
for j in s:
    print j




