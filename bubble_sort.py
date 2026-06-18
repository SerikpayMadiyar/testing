def advanced_bubble_sort(arr):
    n = len(arr)
    
    # Continue looping as long as there is an unsorted segment
    while n > 1:
        last_swap_index = 0
        
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements using Python tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Track the position where the last swap occurred
                last_swap_index = j + 1
                
        # Optimization: everything past the last swap index is already sorted
        if last_swap_index == 0:
            break
            
        n = last_swap_index
        
    return arr

def bubble_sort(arr):
    n = len(arr)
    # Outer loop to traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Inner loop for adjacent comparisons
        # Last i elements are already in place, so we skip them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

# Example Usage
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90]
    print("Original list:", test_list)
    
    sorted_list = advanced_bubble_sort(test_list)
    print("Sorted list:  ", sorted_list)
    
    def advanced_bubble_sort(arr):
    n = len(arr)
    
    # Continue looping as long as there is an unsorted segment
    while n > 1:
        last_swap_index = 0
        
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements using Python tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Track the position where the last swap occurred
                last_swap_index = j + 1
                
        # Optimization: everything past the last swap index is already sorted
        if last_swap_index == 0:
            break
            
        n = last_swap_index
        
    return arr

def bubble_sort(arr):
    n = len(arr)
    # Outer loop to traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Inner loop for adjacent comparisons
        # Last i elements are already in place, so we skip them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

# Example Usage
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90,64, 34, 25, 12, 22, 11, 90]
    print("Original list:", test_list)
    
    sorted_list = advanced_bubble_sort(test_list)
    print("Sorted list:  ", sorted_list)