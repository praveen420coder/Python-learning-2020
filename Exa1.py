def binarysearch(arr,l,r,x):
 while(l<=r):
  mid=l+(r-1)/2
  if(arr[mid]==x):
   return mid
  elif(arr[mid]<x):
   l=mid+1
  else:
   r=mid-1
 return -1
  
if __name__=="__main__":
 print("Enter the arry with comma sepreted.")
 arr=[int(x) for x in input().split(',')]
 x=int(input("Enter the element you want to search"))
 result=binarysearch(arr,0,len(arr)-1,x)
 if(result!=-1):
  print("Element is present at index {}".format(result))
 else:
  print("Element not found in the array.")