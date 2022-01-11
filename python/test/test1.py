
# for i in range(10):
#     for j in range(10):
#         print((i+1)*(j+1), end='\t')
#     print()

sum = 0
for i in range(1, 10):
    for j in range(1, i+1):
        if i % j == 0:
            sum += j
print(sum)
