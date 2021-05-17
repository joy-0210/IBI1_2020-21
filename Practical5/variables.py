#task 3.1
a=291201
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
print("d="+str(d))
print("e="+str(e))

if d==e:
    print ("d=e")
elif d<=e:
    print ("d<e")
else :
    print ("d>e")


#task 3.2
print("set X as true or false")
X=input()
print("set Y as true or false")
Y=input()
Z=(X and not Y) or (Y and not X)
W=X!=Y
print("Z",Z)
print("W",W)
