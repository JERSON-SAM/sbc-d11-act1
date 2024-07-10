def bubble_sort(arr):
    n = len(arr)
    step = 1  # Initialize step counter
    for i in range(n):
        # Outer loop: passes through the array
        swapped = False
        for j in range(0, n - i - 1):
            # Inner loop: compares adjacent elements
            print(f"Pass {i + 1}, Step {step}: {arr}")  # Print current state of the array
            if arr[j] > arr[j + 1]:
                # Swap if the current element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"  swap: {arr}")  # Print when elements are swapped
            else:
                print("  no swap")  # Print when no swap is made
            step += 1  # Increment step counter
        if not swapped:
            break  # Exit loop if no swaps were made in a pass
        print(f"End of pass {i + 1}: {arr}\n")  # Print after each pass
    return arr

# Predefined list
arr = ['Q', 'S', 'A', 'M', 'Z', 'A']

# Sorting the list
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
