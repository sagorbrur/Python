def search(array,key):
    begin=0
    end=len(array)-1
    index = None
    while begin<=end
    mid=(begin+end)/2
    if key==array[mid]:
        index=mid
        break
    elif key>array[mid]: begin=mid+1
    elif key<array[mid]: end=mid-1
   return index

info=[100,2,10,50,20,500,100,200,1000,100]
info=sorted(info)
while True:
    key=int(raw_input())
    print search(info,key)
