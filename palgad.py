nimed=[]
vanused=[]
palgad=[]
töötajad=[]
f=open("palgad.txt")
for line in f:
    töötajad=line.split(";")
    nimed.append(töötajad[0])
    vanused.append(töötajad[1])
    palgad.append(töötajad[2])

def kõrgeim_palk():
    n=0
    max_palk=0
    for i in range(len(palgad)):
        if int(palgad[i])>max_palk:
            max_palk=int(palgad[i])
            n=i
    return nimed[n]+": "+str(max_palk) +" eurot"

def keskmine_palk():
    s=0
    for i in palgad:
        s=int(i)+s
    return s/len(palgad)

def keskmisest_rohkem():
    k=keskmine_palk()
    n=0
    for i in palgad:
        i=int(i)
        if i>k: n+=1
    return n

def keskmisest_vähem():
    k=keskmine_palk()
    n=0
    for i in palgad:
        i=int(i)
        if i<=k: n+=1
    return n

def keskmine_vanus():
    
print(kõrgeim_palk())
print(keskmine_palk())
print(keskmisest_rohkem())
