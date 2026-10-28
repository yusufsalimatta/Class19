L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List:", L)

# varible to store the sum of all numbers in the list
count = 0
for i in L:
    count += i

#divide the total elements by the number of elements in the list to get the average
avg = count / len(L)

print("sum =", count)
print("average =", avg)

#Sorting the elements of the list
L.sort()
#printing the smallest and largest number in the list
print("Smallest number in the list:", L[0])

print("Largest number in the list:", L[-1])