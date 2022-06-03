import functools
def sum_pairs(num_list, num):
    ans_arr = []
    for idx1,val1 in enumerate(num_list):
        for idx2,val2 in enumerate(num_list):
            if (val1 + val2 == num) and idx1 != idx2:
                ans_arr.append([val1, val2])
        #print(val1)
    if ans_arr:
        arr_len = int(len(ans_arr)/2)
        #print(ans_arr, arr_len)
        return ans_arr[:arr_len]
    else:
        return 'Unable to find pairs. ;('
#print(sum_pairs([1, 2, 3, 4, 5, 6, 7, 7], 7))

#print(sum_pairs([1, 2, 3, 4, 5, 6, 7, 7], 15))
print(sum_pairs([1, 2, 3, 4, 5, 6, 7, 15, 3, 2, 7, 8, 0, 11], 12))
#print(sum_pairs([1, 2, 3, 4, 5, 6, 8, 7], 50))
#print(sum_pairs([1, 2, 3, 4, 5, 6, 100, 7], 4))




# def sum_pairs(num_list, num):
#     ans_arr = []
    # for idx1,val1 in enumerate(num_list):
    #     for idx2,val2 in enumerate(num_list):
    #         if (val1 + val2 == num) and idx1 != idx2:
    #             ans_arr.append([val1, val2])
    #     num_list.pop(0)
#     if ans_arr:
#         return ans_arr
#     else:
#         return 'Unable to find pairs. ;('
# print(sum_pairs([1, 2, 3, 4, 5, 6, 7, 7], 7))