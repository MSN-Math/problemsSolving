a=999
b=999

res=0
resA=0
resB=0

while a>99:
    while b>99:
        if "".join(reversed(str(a*b))) == str(a*b) and res<a*b:
            res=a*b
            resA=a
            resB=b
        b-=1
    a-=1
    b=999
    

print(str(resA)+"*"+str(resB)+"="+str(res))
