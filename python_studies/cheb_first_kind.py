# multiplies by x
def f1(x):
    y=str()
    i=0
    while i<len(x):
        if x[i]=="^":
            p=i+1
            while p<len(x) and x[p].isdigit():
                p=p+1
            y=y+"^"+str(int(x[i+1:p])+1)
            i=p
        else:
            y=y+x[i]
            i=i+1
    return(y)

# multiplies by r
def f2(x,r):
    y=str()
    i=0
    while i<len(x):
        if x[i]=='+' or x[i]=='-':
            p=i+1
            while x[p].isdigit():
                p=p+1
            if r*int(x[i:p])>=0:
                y=y+"+"+str(r*int(x[i:p]))
            else:
                y=y+str(r*int(x[i:p]))
            i=p
        else:
            y=y+x[i]
            i=i+1
    return(y)



# simplifies polynomial of degree q
def f3(x,q):
    y=str()
    for k in range(q+1):
        s=0
        for i in range(len(x)):
            if (x[i]=='x' and x[i+1]=='^'):
                l=i+2
                while l<len(x) and x[l].isdigit():
                    l=l+1
                if int(x[i+2:l])==k:
                    p=i-1
                    while x[p].isdigit():
                        p=p-1
                    s=s+int(x[p:i])
        if s>=0:
            y=y+"+"+str(s)+"x^"+str(k)
        else:
            y=y+str(s)+"x^"+str(k)
    return(y)

# simplifies further ignoring terms like 0x^...
def fsimplify(x):
    y=str()
    i=0
    while i<len(x):
        if x[i]=="+" and x[i+1]=="0":
            p=i+2
            while p<len(x) and x[p]!='+' and x[p]!='-':
                p=p+1
            i=p
        else:
            y=y+x[i]
            i=i+1
    return(y)




n=int(input())
a='+1x^1'
b='+2x^2-1x^0'


if n==1:
    print(a)
elif n==2:
   print(b)
       #elif n==3:
       # i=2
#print(f3(f2(f1(b),2)+f2(a,-1),i+1))
elif n>2:
    for i in range(n-2):
        a , b = b , f3(f2(f1(b),2)+f2(a,-1),i+3)
    print(fsimplify(b))



