digit = [int(input("Enter the Digit: "))] 
digits_in_str = ''
result = []
for i in range(-1, -len(digit)-1, -1):
    b = str(digit[i])
    digits_in_str = b + digits_in_str
digits_in_int = int(digits_in_str) + 1
for i in str(digits_in_int):
    result.append(int(i))

print(result)