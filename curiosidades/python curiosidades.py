x = (1,2)
y = x
x = (1,2,3)

print(x,y)

############################

x = [1,2]
y = x
x[0] = 100

print(x,y)

##############################

def get_largest_numbers(numbers, n):
    numbers.sort()

    return numbers[-n:]

nums = [2,3,4,1,34,123,321,1]
print(nums)

largest = get_largest_numbers(nums, 2)
print(nums)
