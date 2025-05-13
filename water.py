def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    binary = ""
    num = abs(decimal)  # Handle negative numbers
    
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    
    # Add negative sign if the input was negative
    if decimal < 0:
        binary = "-" + binary
        
    return binary if binary else "0"

# Get user input and convert
try:
    decimal = int(input("Enter a decimal number: "))
    result = decimal_to_binary(decimal)
    print(f"Binary representation of {decimal} is: {result}")
except ValueError:
    print("Please enter a valid integer.")