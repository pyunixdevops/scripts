omplete the function below.

def  medians(arr):
    #print(sorted(arr))
    arr_len=len(arr)
    loop=1
    items=[]
    while arr_len > 0:
        items.extend(arr[0:loop])
        #print(items)
        if len(items)%2==0:
            index1=int(len(items)/2)
            #print(index1)
            median=int((sorted(items)[index1-1] + sorted(items)[index1])/2)
            print(median)
        else:
            if len(items)==1:
                median=items[0]
                print(median)
            else:
                index1=int((len(items)-1)/2)
                median=int(sorted(items)[index1])
                print(median)
        arr.pop(0)
        arr_len=len(arr)
