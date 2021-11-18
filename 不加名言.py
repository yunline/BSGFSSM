import random

with open("广播稿文本.txt","r") as f:
    l=list(f.readlines())

l=[i.rstrip() for i in l]

print("语料库大小:%d条"%len(l))


n=random.randint(2,4)
ll=[]
for i in range(n):
    s=""
    while len(s)<150//n:
        s+=l.pop(random.randint(0,len(l)-1))
    ll.append("  %s\n"%s)


ssss="".join(ll)
print("总长度%d"%len(ssss))
print("========")
print(ssss)
input()
