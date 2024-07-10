# Arithmetic OPERATIONS

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

# 1. Addition
result = num1 + num2
print("result is: ", result)

# 2. Subtraction
result = num1 - num2
print("result is: ", result)

# 3. Multiplication
result = num1 * num2
print("result is: ", result)

# 4. Division
if num2 == 0 :
    print('division not possible (denominator = 0 )')
else :
    result = num1 / num2
    print("result is: ", round(result,2))

# 5. Floor division
if num2 == 0 :
    print('division not possible (denominator = 0 )')
else :
    result = num1 // num2
    print("result is: ", result)

# 6. Exponential
result = num1 ** num2
print("result is: ", result)
