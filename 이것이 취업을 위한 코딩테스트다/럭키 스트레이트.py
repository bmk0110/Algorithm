import sys
input=sys.stdin.readline
N = str(input().rstrip())
lc=0
rc=0
for i in range(len(N)//2):
    lc+=int(N[i])
for i in range(len(N)//2,len(N)):
    rc+=int(N[i])
if lc == rc:
    print('LUCKY')
else:
    print('READY')