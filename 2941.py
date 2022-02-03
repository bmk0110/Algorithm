#2941 크로아티아 알파벳
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
N= input()
cnt=0

for i in cro:
    N = N.replace(i,'*')
print(len(N))