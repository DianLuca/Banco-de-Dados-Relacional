n = 10

for i in range (n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    
for i in range (n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    

# lista = []

# n = '*'

# for i in range (5 + 1):
#     print(n)
#     lista.append(n)
#     n += '*'


# nova = lista[::-1]

# for r in nova:
#     print(r)
