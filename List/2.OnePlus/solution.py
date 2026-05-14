digits = [9] 
digits_in_str = ''
result = []
for i in range(-1, -len(digits)-1, -1):
    b = str(digits[i])
    digits_in_str = b + digits_in_str
digits_in_int = int(digits_in_str) + 1
for i in str(digits_in_int):
    result.append(int(i))

print(result)