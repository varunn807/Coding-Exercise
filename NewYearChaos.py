def minimumBribes(q,n):
    arr=q
    n=n
    big=-1
    small=n+1
    prev=0
    sum=0
    for i in range(len(arr)):

        if arr[i]!=i+1:
            d=arr[i]-(i+1)
            d=abs(d)

            if arr[i]>prev:
                sum=sum+d
                prev=arr[i]
    return sum


print(minimumBribes([2,3,4,5,6,7,1],7))




