#successiue number
a= [1,2,5,9]
i=0
while i<len(a)-1:
    b=a[i+1]-a[i]
    i+=1
    print(b)