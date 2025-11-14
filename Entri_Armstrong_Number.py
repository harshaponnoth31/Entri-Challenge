# Write a python program to check whether a number is an armstrong number or not

def is_armstrong_number(input_number):
    digits = str(input_number)
    length_of_digits = len(digits)

    sum_of_digits_with_power = 0

    for digit in digits:
        sum_of_digits_with_power += int(digit) ** length_of_digits

    if sum_of_digits_with_power == input_number:
        return True
    else:
        return False



def main():
    input_number = int(input("Enter a number: "))
    is_armstrong_num = is_armstrong_number(input_number)
    if is_armstrong_num:    
        print(f"{input_number} is an Armstrong number!!")
    else:
        print(f"{input_number} is not an Armstrong number!!")

# Write a program that prints all Armstrong numbers in a given range
    input_range = input("Enter the range to find Armstrong numbers separated by comma: ").split(',')

    start = int(input_range[0])
    end = int(input_range[1])

    armstrong_num_list = []

    for num in range(start, end + 1):   # include end value
        if is_armstrong_number(num):
            armstrong_num_list.append(num)

    print("\nArmstrong numbers in the range are :")
    for val in armstrong_num_list:
        print(val, end=" ")

main()
