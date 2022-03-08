#1157 단어공부

salpha=list('abcdefghijklmnopqrstuvwxyz')
balpha=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
array=[0 for _ in range(len(salpha))]
final=[]
word=input()
for i in range(len(word)):
    if word[i] in salpha:
        array[salpha.index(word[i])]+=1
    elif word[i] in balpha:
        array[balpha.index(word[i])]+=1
for i in range(len(array)):
    if array[i]==max(array):
        final.append(i)
if len(final)>1:
    print('?')
else:
    print(balpha[final[0]])











