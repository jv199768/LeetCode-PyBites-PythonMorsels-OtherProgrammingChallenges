def numRollsToTarget(self, n: int, k: int, target: int)
    num_ways=0
    if((n>=1) and (k<=30) and(1<=target<=1000)):
        if(n==1):
            num_ways=1
        elif(n==2):
            num_ways=6
        else:
            num_ways=(math.pow(6,n-1)%(math.pow(10,9)+7))
    return num_ways
