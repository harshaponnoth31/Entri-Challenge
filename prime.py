def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2,num):
            if num%i == 0:
                return False            
        return True
        

def main():
    print("Enter the range to check prime number")
    start = int(input("Enter the start value : "))
    end = int(input("Enter the end value : "))
    prime_num = []
    for num in range(start,end+1):
        if is_prime(num):
            prime_num.append(num)
    if len(prime_num) == 0:
        print(f"No prime numbers between the range {start} and {end}")
    else:
        for val in prime_num:
            print(val,end=" ")

main()