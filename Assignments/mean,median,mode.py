x = list(map(int,input().split()))

res=sum(x)/len(x)
print("mean: ",round(res,2))

x.sort()
n=len(x)
if n% 2 == 0: 
	median1 = x[n//2] 
	median2 = x[n//2 - 1] 
	median = (median1 + median2)/2
else: 
	median = x[n//2] 
print("Median is: " ,median)

d = {}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

maxi = 0
for value in d.values():
    if value > maxi:
        maxi = value

modes = [key for key, value in d.items() if value == maxi]

print("MODES ARE:", modes)
print("FREQUENCY OF MODES IS:", maxi)
