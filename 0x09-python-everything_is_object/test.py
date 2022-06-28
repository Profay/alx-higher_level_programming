def increment(n):
    a = []
    for i in range(len(n)):
        a += [n[i] + 1]
    return a

a = [1, 2]
b = increment(a)
print(a)
print(b)