# data_structures.py
# PLP Week Two - Python Built-in Data Structures assignment

# 1. Create an empty list called my_list.
my_list = []

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Insert the value 15 at the second position in the list.
#    (second position means index 1, since Python is 0-indexed)
my_list.insert(1, 15)

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

# 5. Remove the last element from my_list.
my_list.pop()  # removes 70

# 6. Sort my_list in ascending order.
my_list.sort()

# 7. Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)

# Print results (these are the outputs your grader will check)
print("Final my_list:", my_list)
print("Index of 30:", index_of_30)

# Optional sanity checks to guarantee correctness
assert my_list == [10, 15, 20, 30, 40, 50, 60], f"Unexpected final list: {my_list}"
assert index_of_30 == 3, f"Expected index 3 for 30, got {index_of_30}"
