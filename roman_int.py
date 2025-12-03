def roman_to_int(input_roman):
    prev = 0
    total = 0
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    for char in reversed(input_roman):
        value = roman[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

input_roman = input("Enter the roman numeral : ").upper()
print(roman_to_int(input_roman))