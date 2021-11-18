import random

def readf(fn):#读取文件
    with open(fn,"r") as f:
        l=list(f.readlines())
        l=[i.rstrip() for i in l]
    return l

text=readf("广播稿文本.txt")
print("语料库大小:%d条"%len(text))

famous=readf("名言.txt")
famous=[i.split("——") for i in famous]
before=readf("名言前缀.txt")
after=readf("名言后缀.txt")

get=lambda l:l.pop(random.randint(0,len(l)-1))

def get_famous():
    f=get(famous)
    return f[1]+get(before)+"——“"+f[0]+"”"+get(after)

n=random.randint(2,3)
ll=[]
for i in range(n):
    s=""
    famoused=0#名言计数，理论上一段文字最多出现一次名言
    while len(s)<200//n:
        rn=random.randint(0,99)
        if rn<80:
            s+=get(text)#正常屁话
        elif not famoused:
            s+=get_famous()#来点名言
            famoused=1
    ll.append("  %s\n"%s)


ssss="".join(ll)
print("总长度%d"%len(ssss))
print("========")
print(ssss)
input()
