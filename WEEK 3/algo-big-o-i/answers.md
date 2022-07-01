# Big O Answers

## Snippet 1 -
### Big O: O(n)
### Explanation: O(n) * 0(1); in Linear time, we have 1 constant time op
```python
def largest(array, value):
  for item in array:
    if item > value:
      return False
  return True 
```


## Snippet 2 -
### Big O: O(n)
### Explanation:  O(n) + O(n); 2 Linear time ops apart from each other. Choose 1

```python
def info_dump(customers):
  
  print('Customer Names:')
  for customer in customers: 
    print(customer['name'])
  
  print('Customer Locations:')
  for customer in customers: 
    print(customer['country'])
  
```

## Snippet 3 -
### Big O: O(1)
### Explanation: O(1); 1 Constant time op

```python
def first_element_is_red(array):
  return array[0] == 'red' 
```

## Snippet 4 -
### Big O: O(n^2)
### Explanation: O(n) * O(n) * O(1) * O(1); Nested loops with 2x Constant ops 

```python
def duplicates(array):
  for index1, item1 in enumerate(array):
    for index2, item2 in enumerate(array):
      if index1 == index2:
        continue
      if item1 == item2:
        return True
  return False
``` 

## Snippet 5 -
### Big O: O(n*m)
### Explanation: O(n) + O(m) + O(n) * O(m) * O(1); 2 Linear assignments and 2x nested loops with 1 Constant op

```python
words = ['chocolate', 'coconut', 'rainbow']
endings = ['cookie', 'pie', 'waffle']

for word in words:
  for ending in endings:
    print(word + ending)

```

## Snippet 6 -
### Big O: O(n)
### Explanation: O(n) + O(n) * O(1); 1 Linear assignment and loops with 1 Constant op

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

def print_array(array):
  for item in array:
    print(item)

```

## Snippet 7 -
### Big O: O(n^2)
### Explanation: Nested loops of same array

```python
# this is insertion sort
def insertionSort(arr): 
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >=0 and key < arr[j] : 
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key 
```

## Snippet 8 -
### Big O: O(n^2)
### Explanation: Nested loops with assignments

```python
for i in range(len(my_list)):
  min_idx = i
  for j in range(i+1, len(my_list)):
      if my_list[min_idx] > my_list[j]:
          min_idx = j

  my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
```
