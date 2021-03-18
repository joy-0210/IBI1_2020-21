print("set the average number of individual infected by individual with the virus")
r=input()
r=float(r) #turn r from str into float so that it can do subsequent calculates
n=84
x=0 # count the round of infection

while x<5:
    n=n*r+n #each round n people inferct n*r people
    x=x+1 #the times of round +1
print("r="+str(r)+" n="+str(n))
