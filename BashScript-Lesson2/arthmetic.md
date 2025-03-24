# Bash Arithmetic Operations Guide

Bash provides several ways to perform arithmetic operations. This guide covers the various methods with examples for common scenarios in DevOps and system administration.

## Table of Contents
- [Basic Syntax Options](#basic-syntax-options)
- [Arithmetic Operators](#arithmetic-operators)
- [Variables and Calculations](#variables-and-calculations)
- [Comparison Operators](#comparison-operators)
- [Bitwise Operators](#bitwise-operators)
- [Practical Examples](#practical-examples)

## Basic Syntax Options

Bash offers multiple ways to perform arithmetic operations:

### 1. The `expr` Command
```bash
result=$(expr 5 + 3)
echo $result  # Outputs: 8
```

### 2. Double Parentheses `(( ))`
```bash
(( result = 5 + 3 ))
echo $result  # Outputs: 8
```

### 3. `$((expression))` Syntax
```bash
result=$((5 + 3))
echo $result  # Outputs: 8
```

### 4. The `let` Command
```bash
let result=5+3
echo $result  # Outputs: 8
```

### 5. Using `bc` for Floating-Point Arithmetic
```bash
result=$(echo "5.5 + 3.2" | bc)
echo $result  # Outputs: 8.7
```

## Arithmetic Operators

### Basic Operators
| Operator | Description     | Example                  |
|----------|-----------------|--------------------------|
| `+`      | Addition        | `echo $((5 + 3))`        |
| `-`      | Subtraction     | `echo $((5 - 3))`        |
| `*`      | Multiplication  | `echo $((5 * 3))`        |
| `/`      | Division        | `echo $((15 / 3))`       |
| `%`      | Modulus         | `echo $((10 % 3))`       |
| `**`     | Exponentiation  | `echo $((2 ** 3))`       |

### Assignment Operators
| Operator | Description                   | Example         |
|----------|-------------------------------|-----------------|
| `=`      | Simple assignment             | `a=5`           |
| `+=`     | Addition assignment           | `((a += 2))`    |
| `-=`     | Subtraction assignment        | `((a -= 2))`    |
| `*=`     | Multiplication assignment     | `((a *= 2))`    |
| `/=`     | Division assignment           | `((a /= 2))`    |
| `%=`     | Modulus assignment            | `((a %= 2))`    |

### Increment and Decrement
```bash
a=5
((a++))    # Post-increment: a becomes 6
((++a))    # Pre-increment: a becomes 7
((a--))    # Post-decrement: a becomes 6
((--a))    # Pre-decrement: a becomes 5
```

## Variables and Calculations

### Using Variables in Arithmetic
```bash
x=10
y=5
sum=$((x + y))
echo "Sum: $sum"  # Outputs: Sum: 15

product=$((x * y))
echo "Product: $product"  # Outputs: Product: 50

# Multiple operations
result=$((x + y * 2))
echo "Result: $result"  # Outputs: Result: 20 (follows order of operations)
```

### Order of Operations
Bash follows standard mathematical order of operations (PEMDAS):
```bash
result=$((2 + 3 * 4))
echo $result  # Outputs: 14 (not 20)

result=$(((2 + 3) * 4))
echo $result  # Outputs: 20
```

## Comparison Operators

In arithmetic contexts (inside `(( ))` or `$(( ))`):

| Operator | Description                  | Example                       |
|----------|------------------------------|-------------------------------|
| `<`      | Less than                    | `((5 < 10))`                  |
| `<=`     | Less than or equal to        | `((5 <= 5))`                  |
| `>`      | Greater than                 | `((10 > 5))`                  |
| `>=`     | Greater than or equal to     | `((10 >= 10))`                |
| `==`     | Equal to                     | `((5 == 5))`                  |
| `!=`     | Not equal to                 | `((5 != 10))`                 |

### Example: Conditional with Arithmetic Comparison
```bash
age=25

if ((age >= 18)); then
    echo "Adult"
else
    echo "Minor"
fi
```

## Bitwise Operators

| Operator | Description         | Example          |
|----------|---------------------|------------------|
| `<<`     | Left shift          | `((1 << 2))`     |
| `>>`     | Right shift         | `((8 >> 2))`     |
| `&`      | Bitwise AND         | `((5 & 3))`      |
| `\|`     | Bitwise OR          | `((5 \| 3))`     |
| `^`      | Bitwise XOR         | `((5 ^ 3))`      |
| `~`      | Bitwise NOT         | `((~5))`         |

### Example: Bitwise Operations
```bash
# Binary: 101 & 011 = 001
result=$((5 & 3))
echo "5 & 3 = $result"  # Outputs: 1

# Binary: 101 | 011 = 111
result=$((5 | 3))
echo "5 | 3 = $result"  # Outputs: 7

# Left shift: 1 << 3 = 8 (binary: 1 → 1000)
result=$((1 << 3))
echo "1 << 3 = $result"  # Outputs: 8
```

## Practical Examples

### 1. Calculating Disk Usage Percentage
```bash
# Get used and total disk space in KB
used=$(df -k / | tail -1 | awk '{print $3}')
total=$(df -k / | tail -1 | awk '{print $2}')

# Calculate percentage
percent=$(( used * 100 / total ))

echo "Disk usage: $percent%"

if ((percent > 90)); then
    echo "Warning: Disk space critical!"
fi
```

### 2. Sequential Filename Generation
```bash
prefix="backup_"
suffix=".tar.gz"

for ((i=1; i<=5; i++)); do
    filename="${prefix}$(printf "%03d" $i)${suffix}"
    echo "Generated filename: $filename"
done
```

### 3. Simple Calculator Function
```bash
calculate() {
    if [ "$#" -ne 3 ]; then
        echo "Usage: calculate <number> <operator> <number>"
        echo "Operators: +, -, *, /, %, **"
        return 1
    fi
    
    num1=$1
    op=$2
    num2=$3
    
    case $op in
        "+") result=$((num1 + num2)) ;;
        "-") result=$((num1 - num2)) ;;
        "*") result=$((num1 * num2)) ;;
        "/") 
            if ((num2 == 0)); then
                echo "Error: Division by zero"
                return 1
            fi
            result=$((num1 / num2))
            ;;
        "%") result=$((num1 % num2)) ;;
        "**") result=$((num1 ** num2)) ;;
        *)
            echo "Invalid operator: $op"
            return 1
            ;;
    esac
    
    echo "$num1 $op $num2 = $result"
}

# Usage
calculate 10 + 5
calculate 10 "*" 5  # Asterisk needs quoting or escaping in shell
calculate 10 / 3
```

### 4. Averaging Values
```bash
sum=0
count=0

# Read numbers from file, one per line
while read -r num; do
    ((sum += num))
    ((count++))
done < numbers.txt

if ((count > 0)); then
    average=$((sum / count))
    echo "Average: $average"
else
    echo "No numbers found"
fi
```

### 5. Countdown Timer
```bash
countdown() {
    seconds=$1
    
    while ((seconds > 0)); do
        echo -ne "Time remaining: $seconds seconds\r"
        sleep 1
        ((seconds--))
    done
    
    echo -e "\nTime's up!"
}

countdown 10
```

### 6. Advanced Example: Working with Binary and Hexadecimal
```bash
# Binary to decimal
binary="1101"
decimal=$((2#$binary))
echo "Binary $binary = Decimal $decimal"  # Outputs: Binary 1101 = Decimal 13

# Hexadecimal to decimal
hex="1A"
decimal=$((16#$hex))
echo "Hex $hex = Decimal $decimal"  # Outputs: Hex 1A = Decimal 26

# Decimal to binary (using bc)
decimal=13
binary=$(echo "obase=2; $decimal" | bc)
echo "Decimal $decimal = Binary $binary"  # Outputs: Decimal 13 = Binary 1101

# Decimal to hexadecimal (using printf)
decimal=26
hex=$(printf "%X" $decimal)
echo "Decimal $decimal = Hex $hex"  # Outputs: Decimal 26 = Hex 1A
```

## Floating-Point Arithmetic with `bc`

Bash doesn't natively support floating-point arithmetic, but you can use the `bc` command:

### Basic `bc` Usage
```bash
echo "5.5 + 3.2" | bc
# Outputs: 8.7

echo "scale=3; 10 / 3" | bc
# Outputs: 3.333
```

### Function for Float Calculations
```bash
float_calc() {
    echo "scale=2; $1" | bc
}

result=$(float_calc "10.5 / 4")
echo "10.5 / 4 = $result"  # Outputs: 10.5 / 4 = 2.62
```

### Combining with Variables
```bash
price=10.99
quantity=3
total=$(echo "scale=2; $price * $quantity" | bc)
echo "Total: \$$total"  # Outputs: Total: $32.97
```

## Best Practices

1. **Use `$((expression))` for integer arithmetic** - it's the most modern and readable syntax

2. **Use `bc` for floating-point calculations**:
   ```bash
   # Not: result=$((10 / 3))
   result=$(echo "scale=2; 10 / 3" | bc)
   ```

3. **Prevent division by zero**:
   ```bash
   divisor=0
   if ((divisor != 0)); then
       result=$((10 / divisor))
   else
       echo "Error: Division by zero"
   fi
   ```

4. **Use parentheses to clarify order of operations**:
   ```bash
   result=$(((x + y) * z))
   ```

5. **Initialize variables before arithmetic operations**:
   ```bash
   count=0
   ((count++))  # Safe increment
   ```

6. **Use numeric validation when working with user input**:
   ```bash
   if [[ $input =~ ^[0-9]+$ ]]; then
       result=$((input * 2))
   else
       echo "Error: Not a number"
   fi
   ```