import calculator

result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(10, 4)
result_multiply = calculator.multiply(2, 6)
result_divide = calculator.divide(8, 2)
result_divide_zero = calculator.divide(7, 0)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")
print(f"Division by zero: {result_divide_zero}")
