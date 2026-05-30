arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

element = int(input("Enter element to delete: "))

if element in arr:
    arr.remove(element)
    print("Array after deletion:", arr)
else:
    print("Element not found in array")
