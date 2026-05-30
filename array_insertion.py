# Array Insertion Program

arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

position = int(input("Enter position (0 to 5): "))
element = int(input("Enter element to insert: "))

arr.insert(position, element)

print("Array after insertion:", arr)
