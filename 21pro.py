maximum = int(raw_input())
def largest(arr,j):
    maximum = arr[0]
    for i in range(1, j):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum
arr = [2,3,1,45,5]
j = len(arr)
sol = largest(arr,j)
print (sol)
