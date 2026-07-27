lst = [10,20,30,40,50]

for x in lst:
    print(x)

st = "Welcome"
for x in st:
    print(x)

for x in range (5):
    print(x, end="")
print("\n")

for x in range(10,15):
    print(x, "\t", end ="")
print("\n")

for x in range(20,30,3):
    print(x, "\t", end ="")


for r in range(4):
    for c in range(4):
        if ((r == 0) or (r == 3) or (c == 0) or (c == 3)):
            print("*", end ="")

        else:
            print(" ", end ="")

    print()