num = [555,901,482,1771, 2323]
total = []
res = 0
for i in num:
    total.append(len(str(i)))

for i in total:
    if i%2 == 0:
        res += 1
print(res)