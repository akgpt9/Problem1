list = ['star', 'sky', 'apple', 'lemon', 'sky', 'sky', 'lemon', 'star', 'star', 'star']
f = [None] * len(list)
x = -1

for i in range(0, len(list)):
    count = 1
    for j in range(i + 1, len(list)):
        if (list[i] == list[j]):
            count += 1
            f[j] = x

    if (f[i] != x):
        f[i] = count

print(" WORD    -     Frequency")
for i in range(0, len(f)):
    if (f[i] != x):
        print(" " + str(list[i]) + "   -   " + str(f[i]))