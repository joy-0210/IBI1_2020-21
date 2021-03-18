a=1
b=1
n=2 #count the number
print(a)
print(b)

while n<13 :
    n=n+1
    c=b #save the number of (n-1); now a=(n-2), b=(n-1)
    b=a+b #calculate the number of n; now a=(n-2), b=n
    a=c #now a=(n-1), b=n
    print(b) 
     
