nums = [4, 5, 3, 4]
arr1 = sorted(nums)
arr2 = sorted(list(set(nums)))
answer = arr1 == arr2

print(not answer)
