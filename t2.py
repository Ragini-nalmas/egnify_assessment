
def watertrap(arr, n) :
	sum = 0;

	for i in range(1, n - 1) :
	
		left = arr[i];
		for j in range(i) :
			left = max(left, arr[j]);
		
		
		right = arr[i];
		for j in range(i + 1 , n) :
			right = max(right, arr[j]);
		sum = sum + (min(left, right) - arr[i]);

	return sum;

arr = [0,1,0,2,1,0,1,3,2,1,2,1];
n = len(arr);
	
print(watertrap(arr, n));
	


        
    
    
