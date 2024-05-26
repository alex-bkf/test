a = 'aaf'
fl = False

for i in a:
    a = a[-1] + a[:-1]
    if a == a[::-1]:
        fl = True
        break

if fl:
    print('Ok')
else:
    print('No')

fl = False
b = set(a)
count = 0
for i in b:
    if a.count(i) % 2 == 1:
        count += 1
        if count > 1:
            fl = True
            break
if fl:
    print('No')
else:
    print('Ok')
