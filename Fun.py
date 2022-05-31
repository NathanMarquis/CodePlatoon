# import functools

# num = 11
# x = 'working' if num == 1 else 'sadness'
# print(x)

# listing = list(range(1, 11))
# # 1, 2, .. , 10

# plus_two = list(map(lambda elem: elem + 2, listing))

# def factorial(num):
#     num_list = list(range(1, num + 1))
#     answer = functools.reduce(lambda aggie, item: aggie * item, num_list)
#     return answer
# print(factorial(4))



def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)