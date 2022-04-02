# Python3 program to find a
# local minima in an array

# A binary search based function that
# returns index of a local minima.
def localMinUtil(arr, low, high, n):
		
	# Find index of middle element
	mid = low + (high - low) // 2
		
	# Compare middle element with its
	# neighbours (if neighbours exist)
	if(mid == 0 or arr[mid - 1] > arr[mid] and
	mid == n - 1 or arr[mid] < arr[mid + 1]):
		return mid
		
	# If middle element is not minima and its left
	# neighbour is smaller than it, then left half
	# must have a local minima.
	elif(mid > 0 and arr[mid - 1] < arr[mid]):
		return localMinUtil(arr, low, mid - 1, n)
		
	# If middle element is not minima and its right
	# neighbour is smaller than it, then right half
	# must have a local minima.
	return localMinUtil(arr, mid + 1, high, n)
	
# A wrapper over recursive function localMinUtil()
def localMin(arr, n):
	
	return localMinUtil(arr, 0, n - 1, n)
	
# Driver code
arr = [4, 3, 1, 14, 16, 40]
n = len(arr)
print("Index of a local minima is " ,
					localMin(arr, n))
					
# This code is contributed by Anant Agarwal.
