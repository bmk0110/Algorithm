#2908 상수

A, B = map(str,input().split())
nA= ''
nB= ''
for i in range(len(A)):
    nA+=A[2-i]
for i in range(len(B)):
    nB+=B[2-i]
nA = int(nA)
nB = int(nB)
if nA>nB:
    print(nA)
else:
    print(nB)