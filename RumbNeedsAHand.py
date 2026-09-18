n = int(input())
k: int = 0
a = []
for i in range(n):
    a.append(input())
b: bool = True
while b:
    b = False
    for i in range(n-1):
        if a[i]>a[i+1]:
            b = True
            a[i], a[i+1] = a[i+1], a[i]
            k+=1
if n-k>1:
    print("NO")
else:
    print("YES")
