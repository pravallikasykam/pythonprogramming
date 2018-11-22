min = int(raw_input())
def smallest(arr,n) :
	min = arr[0]
	for i in range(1,n) :
		if arr[i] < min :
			min = arr[i]
	return min
arr = [1,2,3]
n = len(arr)
ans = smallest(arr,n)
print(ans)
