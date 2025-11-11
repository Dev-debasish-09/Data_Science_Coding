# def show_alternative(string, num):
#     new_str = string
#     for i in range(1, num):
#         new_str += string
#     for j in range(1, num):
#         update_Str = ''
#         for i in range(0,len(new_str), 2):
#             update_Str += new_str[i]
#         new_str = update_Str
#     return new_str

# input1 = 'j#k&h'
# input2 = 5
# result = show_alternative(input1, input2)
# print(result)


def show_alternative(string, num):
    n = len(string) * num    
    # Josephus problem: survivor position for k=2
    # The survivor index in 1-based indexing is: 2*(n - 2^floor(log2(n))) + 1
    # Convert to 0-based: subtract 1   
    # Find the largest power of 2 <= n
    power = 1
    while power * 2 <= n:
        power *= 2
    
    survivor_1_based = 2 * (n - power) + 1
    survivor_0_based = survivor_1_based - 1
    
    # Map back to original string
    original_index = survivor_0_based % len(string)
    
    return string[original_index]

# Test
input1 = 'a'
input2 = 1
result = show_alternative(input1, input2)
print(f"Input: '{input1}', {input2} -> Output: '{result}'")

input1 = 'j#k&h'
input2 = 5
result = show_alternative(input1, input2)
print(f"Input: '{input1}', {input2} -> Output: '{result}'")
