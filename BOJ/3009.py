#3009 네 번째 점
arra=[]
arrb=[]
final=[]
for _ in range(3):
    a,b = map(int, input().split())
    arra.append(a)
    arrb.append(b)
arra.sort()
arrb.sort()
if arra[0] == arra[1]:
    final.append(arra[2])
else:
    final.append(arra[0])
if arrb[0]==arrb[1]:
    final.append(arrb[2])
else:
    final.append(arrb[0])
for i in range(2):
    print(final[i], end=' ')