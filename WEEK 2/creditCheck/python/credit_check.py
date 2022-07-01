def credit_check(num_str):
    working_list = list(num_str)
    #for x in range(-2, len(working_list) * -1, -2):
    sum = 0
    for i,x in enumerate(working_list[-2::-2]):
        x = int(x)*2
        if x > 9:
            mini_sum = 0
            for element in str(x):
                mini_sum += int(element)
            x = mini_sum
        working_list[(i + 1) * -2] = x
    for item in working_list:
        sum+= int(item)
    print(working_list)
    if sum % 10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"
    #print(range(-2, len(working_list) * -1, -2))
    return working_list

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

print(credit_check('5541808923795240'))

#print(range(-2, len(working_list) * -1, -2))