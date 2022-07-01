# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    answer = []
    for element in numbers:
        item = str(element)
        variable_length = len(item)     
        sum = 0
        for digit in item:
            sum += int(digit)**variable_length
        if sum == element:
            answer.append(element)
            
    return answer