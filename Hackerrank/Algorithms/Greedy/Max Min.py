def maxMin(k, arr):

    # Method 1: Correct but takes a lot of time
    arr = sorted(arr)
    n = len(arr)-k+1
    grp_arr = []
    for i in range(n):
        j = 0
        ls = []
        while j<k:
            ls.append(arr[i+j])
            j += 1
        # print(ls)
        grp_arr.append(ls)
    # print(grp_arr)
    return min([max(grp_arr[i]) - min(grp_arr[i]) for i in range(len(grp_arr))])

    # i = 0
    # diff = []
    # while i<len(grp_arr):
    #     diff.append(max(grp_arr[i]) - min(grp_arr[i]))
    #     i += 1
    # # print(diff)
    # return min(diff)


    # Method 2:
    # arr.sort()
    # n = len(arr)-k+1
    # return min([arr[i+k-1]-arr[i] for i in range(n)])




n = int(input())
k = int(input())
arr = []
# for _ in range(n):
#     arr_item = int(input())
#     arr.append(arr_item)
arr = [int(input()) for _ in range(n)]

print(maxMin(k,arr))