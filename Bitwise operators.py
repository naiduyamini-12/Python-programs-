string = "1A0B0C1"
result = int(string[0])
for i in range(1, len(string), 2):
    operator = string[i]
    num = int(string[i + 1])
    
    if operator == 'A':  # 'a' means bitwise AND
        result &= num
    elif operator == 'B':  # 'b' means bitwise OR
        result |= num
    elif operator == 'C':  # 'c' means bitwise XOR
        result ^= num

print("Result:", result)
