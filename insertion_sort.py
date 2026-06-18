def binary_insertion_sort(arr):
    # Loop from the second element up to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Binary search to find the correct index for 'key'
        low = 0
        high = i - 1
        
        while low <= high:
            mid = (low + high) // 2
            if key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        # Shift all elements to the right to make room for 'key'
        for j in range(i, low, -1):
            arr[j] = arr[j - 1]
        
        # Insert the element at its calculated position
        arr[low] = key
        
    return arr

# Example Usage
if __name__ == "__main__":
    data = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    print("Original array:", data)
    
    sorted_data = binary_insertion_sort(data)
    print("Sorted array:  ", sorted_data)

def binary_insertion_sort(arr):
    # Loop from the second element up to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Binary search to find the correct index for 'key'
        low = 0
        high = i - 1
        
        while low <= high:
            mid = (low + high) // 2
            if key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        # Shift all elements to the right to make room for 'key'
        for j in range(i, low, -1):
            arr[j] = arr[j - 1]
        
        # Insert the element at its calculated position
        arr[low] = key
        
    return arr

# Example Usage
if __name__ == "__main__":
    data = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    print("Original array:", data)
    
    sorted_data = binary_insertion_sort(data)
    print("Sorted array:  ", sorted_data)
