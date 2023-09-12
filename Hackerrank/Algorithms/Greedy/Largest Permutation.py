def largestPermutation(k, arr):

# Method 1 : Applicable for all types of values but takes more time and space
    # new_arr = []
    # if k > len(arr):
    #     k = len(arr)
    # # print(k)
    # i = 0
    # count = 0
    # while count<k and i<len(arr):
    #     maximum = max(arr)
    #     index = arr.index(maximum)
    #     # print(index)
    #     # print(maximum)
    #     if index == i:
    #         new_arr.append(arr[i])
    #         arr.remove(maximum)
    #     else:
    #         # swapping
    #         arr[index],arr[i] = arr[i],arr[index]
    #         # adding at the end of new list
    #         new_arr.append(arr[i])
    #         # removing from the old list
    #         arr.remove(maximum)
    #         count += 1
    # new_arr.extend(arr)
    # return new_arr


# Method 2: Uses dictionary to decrease time complexity
    d = {}
    i = 0
    while i<len(arr):
        d[arr[i]] = i
        i+=1
    print(d)
    j = 0
    n = len(arr)
    while k>0 and n>0:
        # print(j)
        if arr[j]<n:
            max_index = d[n]
            # swapping in list
            arr[max_index],arr[j] = arr[j],arr[max_index]
            # swapping indices
            d[arr[j]], d[arr[max_index]] = d[arr[max_index]], d[arr[j]]
            print(d)
            #  Swapping using temp
            # tmp = d[n]
            # arr[d[n]] = arr[i]
            # arr[i] = n
            # tmp = d[arr[d[n]]]
            # d[arr[d[n]]] = d[n]
            # d[n] = tmp
            k -= 1
            print(k)
        n -= 1
        j += 1
    return arr

            




t = 6
a = [4,2,3,5,1]
result = largestPermutation(t, a)
print(' '.join(map(str,result)))
print(result)


# Input
# nk = input().split()
# n = int(nk[0])
# k = int(nk[1])
# arr = list(map(int, input().rstrip().split()))
# result = largestPermutation(k, arr)