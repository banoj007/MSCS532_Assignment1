# insertion_sort_desc.py

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    numbers = [12, 11, 13, 5, 6]
    print("Original:", numbers)
    print("Sorted (Descending):", insertion_sort_desc(numbers))
