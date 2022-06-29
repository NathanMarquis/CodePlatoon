import random

values = random.sample(list(range(1,10000)), 1000)
values.sort() # We now have a sorted list of 1000 unique values between 1 and 10,000

def binary_search(num, num_list):
  lower_limit = 0
  upper_limit = len(num_list) - 1
  split_char = 0

  while lower_limit <= upper_limit:
    split_char = ((upper_limit + lower_limit) / 2)
    # If x is greater, ignore left half
    if num_list[split_char] < num:
        lower_limit = split_char + 1
    # If x is smaller, ignore right half
    elif num_list[split_char] > num:
        upper_limit = split_char - 1
    # means x is present at split_char
    else:
        return split_char
  # If we reach here, then the element was not present
  return -1

print(( binary_search(1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == 1)
