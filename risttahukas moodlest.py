l=2*int(input("Laius: "))
p=int(input("Pikkus: "))
k=int(input("Kõrgus: "))

def risttahukas(l,p,k):
    tahukas=" "*(p)+"_"*(l+1)
    if k<p:
        i=0
        while i<k:
            rida=" "*(p-i-1)+"/"+" "*l+"/"+" "*(2+(i-1)*2)+"\\"
            tahukas=tahukas+"\n"+rida
            i+=1
        i=0
        while i<p-k:
            if i==p-k-1:    rida=" "*(p-k-i-1)+"/"+"_"*l+"/"+" "*(2*k-1)+"/"
            else:           rida=" "*(p-k-i-1)+"/"+" "*l+"/"+" "*(2*k-1)+"/"
            tahukas=tahukas+"\n"+rida
            i+=1
        i=0
        while i<k:
            if i==k-1:  rida=" "*(i)+"\\"+"_"*l+"\\"+"/"
            else:       rida=" "*(i)+"\\"+" "*l+"\\"+" "*(2+(k-i-2)*2)+"/"
            tahukas=tahukas+"\n"+rida
            i+=1
            
    if k==p:
        i=0
        while i<2*k:
            if i<k-1:
                rida=" "*(p-i-1)+"/"+" "*l+"/"+" "*(2+(i-1)*2)+"\\"
            elif i==k-1:
                rida="/"+"_"*l+"/"+" "*(2+(i-1)*2)+"\\"
            elif i>=k:
                if i==2*k-1:  rida=" "*(i-k)+"\\"+"_"*l+"\\"+"/"
                else:       rida=" "*(i-k)+"\\"+" "*l+"\\"+" "*(2+(2*k-i-2)*2)+"/"
            tahukas=tahukas+"\n"+rida
            i+=1

    if k>p:
        i=0
        while i<p:
            if i==p-1:  rida="/"+"_"*l+"/"+" "*(2+(i-1)*2)+"\\"
            else:       rida=" "*(p-i-1)+"/"+" "*l+"/"+" "*(2+(i-1)*2)+"\\"
            tahukas=tahukas+"\n"+rida
            i+=1
        i=0
        while i<k-p:
            rida=" "*(i)+"\\"+" "*l+"\\"+" "*(2*p-1)+"\\"
            tahukas=tahukas+"\n"+rida
            i+=1
        i=0
        while i<p:
            if i==p-1:  rida=" "*(i+k-p)+"\\"+"_"*l+"\\"+"/"
            else:       rida=" "*(i+k-p)+"\\"+" "*l+"\\"+" "*(2+(p-i-2)*2)+"/"
            tahukas=tahukas+"\n"+rida
            i+=1
    return tahukas

print(risttahukas(l,p,k))