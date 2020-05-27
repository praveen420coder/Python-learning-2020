from functools import reduce
num=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda x:x%2==0,num))
print(evens)
sum=reduce(lambda x,y:x+y,num)
print(sum)
update=list(map(lambda x:x+1,num))
print(update)

