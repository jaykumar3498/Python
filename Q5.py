x= [ 1,2,3,4,5]
y = [6,7,8,9,10]
lis = []
for i in x:
  if i%2!=0:
    lis.append(i)
for i in y:
  if i%2==0:
    lis.append(i)
print(lis)
