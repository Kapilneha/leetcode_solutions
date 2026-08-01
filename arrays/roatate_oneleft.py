def rotate(arr):
    res= []
    for i in range(1,len(arr)):
        res.append(arr[i])

    res.append(arr[0])

    return res

arr=list(map(int,input().split()))
print(rotate(arr))