def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Assume the current position holds the minimum element
        min_index = i
        
        # Scan the remaining unsorted portion to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
numbers = [64, 25, 12, 22, 11, 64, 25, 12, 22, 11, 64, 25, 12, 22, 11]
print("Original list:", numbers)

selection_sort(numbers)
print("Sorted list:  ", numbers)
