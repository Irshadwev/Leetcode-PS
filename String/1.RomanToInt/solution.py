s = 'MCMXCIV'

def romantonumerals(s):
    symbol_str = {'I' : 1, 'V' : 5, 
                  'X' : 10, 'L' : 50, 
                  'C' : 100, 'D' : 500, 'M' : 1000}
    
    previous_str = 0
    result = 0
    for i in range(-1, -len(s) -1, -1):
        current_str = symbol_str[s[i]]
        if (current_str < previous_str):
            result = result - current_str
        if (current_str >= previous_str):
            result = result + current_str
            previous_str = current_str

    return result

print(romantonumerals(s))