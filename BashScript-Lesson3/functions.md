# Bash Functions Tutorial

## Introduction

Functions in Bash are blocks of reusable code designed to perform a particular task. They help in organizing code, avoiding repetition, and making scripts more maintainable.

## Basic Syntax

There are two common ways to define functions in Bash:

```bash
# Method 1
function_name() {
    # Commands
    # ...
}

# Method 2
function function_name {
    # Commands
    # ...
}
```

Both styles are equivalent in functionality, though the first method is more commonly used and is POSIX-compliant.

## Creating and Calling Functions

### Simple Function Example

```bash
#!/bin/bash

# Define a simple greeting function
say_hello() {
    echo "Hello, world!"
}

# Call the function
say_hello
```

When you run this script, it will output: `Hello, world!`

## Function Parameters

You can pass arguments to functions just like you would with shell scripts:

```bash
#!/bin/bash

# Function that greets a person
greet() {
    echo "Hello, $1! Nice to meet you."
}

# Call the function with an argument
greet "Alice"
greet "Bob"
```

Output:
```
Hello, Alice! Nice to meet you.
Hello, Bob! Nice to meet you.
```

### Parameter Handling

Inside a function, parameters are accessed using:
- `$1`, `$2`, `$3`, etc. for individual parameters
- `$@` for all parameters as separate strings
- `$*` for all parameters as a single string
- `$#` for the number of parameters

```bash
#!/bin/bash

show_params() {
    echo "Function received $# parameters"
    echo "First parameter: $1"
    echo "Second parameter: $2"
    echo "All parameters: $@"
    
    echo "Processing all parameters individually:"
    for param in "$@"; do
        echo "- $param"
    done
}

show_params apple banana "cherry pie"
```

## Return Values

Bash functions don't return values like in other programming languages. Instead, they have two ways to provide output:

### 1. Using the return statement

The `return` statement can only return numeric exit status codes (0-255):

```bash
#!/bin/bash

is_even() {
    if (( $1 % 2 == 0 )); then
        return 0  # Success (true)
    else
        return 1  # Failure (false)
    fi
}

is_even 4
echo "Is 4 even? $?"  # $? contains the exit status of the last command

is_even 5
echo "Is 5 even? $?"
```

Output:
```
Is 4 even? 0
Is 5 even? 1
```

### 2. Capturing function output

To return strings or more complex data, output it and capture with command substitution:

```bash
#!/bin/bash

get_date() {
    echo $(date +"%Y-%m-%d")
}

today=$(get_date)
echo "Today is $today"
```

## Variable Scope

By default, variables in Bash are global. To create local variables within functions, use the `local` keyword:

```bash
#!/bin/bash

demo_scope() {
    local local_var="I'm local"
    global_var="I'm global"
    echo "Inside function: local_var = $local_var"
    echo "Inside function: global_var = $global_var"
}

demo_scope
echo "Outside function: global_var = $global_var"
echo "Outside function: local_var = $local_var"  # This will be empty
```

## Advanced Function Techniques

### Default Parameter Values

```bash
#!/bin/bash

greet() {
    local name=${1:-"Guest"} # if $1 is null give it a default name 
    echo "Hello, $name!"
}

greet           # Uses default
greet "Alice"   # Uses provided name
```

### Functions with Variable Number of Arguments

```bash
#!/bin/bash

sum_all() {
    local total=0
    for num in "$@"; do
        (( total += num ))
    done
    echo $total
}

result=$(sum_all 1 2 3 4 5)
echo "Sum: $result"
```

## Function Libraries

You can create a library of functions and source them in different scripts:

### lib_functions.sh
```bash
#!/bin/bash

# Library of useful functions

# Convert string to uppercase
to_upper() {
    echo "$1" | tr '[:lower:]' '[:upper:]'
}

# Convert string to lowercase
to_lower() {
    echo "$1" | tr '[:upper:]' '[:lower:]'
}
```

### Using the library
```bash
#!/bin/bash

# Import the function library
source lib_functions.sh
# Or use: . lib_functions.sh

echo $(to_upper "hello world")
echo $(to_lower "HELLO WORLD")
```

## Best Practices

1. **Use descriptive function names** that indicate what the function does.

2. **Document your functions** with comments explaining their purpose, parameters, and return values.

3. **Keep functions small and focused** on a single task.

4. **Use local variables** to prevent unintended side effects.

5. **Validate input parameters** at the beginning of your functions.

```bash
validate_input() {
    if [[ $# -ne 2 ]]; then
        echo "Error: Function requires exactly 2 parameters" >&2
        return 1
    fi
    
    if ! [[ $1 =~ ^[0-9]+$ ]]; then
        echo "Error: First parameter must be a number" >&2
        return 1
    fi
    
    # Proceed with function
    echo "Input validated successfully"
    return 0
}
```

## Debugging Functions

To debug functions, you can:

1. Use `set -x` to enable debug mode before calling a function:

```bash
set -x  # Enable debugging
my_function arg1 arg2
set +x  # Disable debugging
```

2. Add echo statements to trace execution flow:

```bash
complex_function() {
    echo "DEBUG: Starting complex_function with params: $@"
    # ... function code ...
    echo "DEBUG: Step 1 complete"
    # ... more code ...
    echo "DEBUG: Function complete"
}
```

## Real-World Examples

### Log Function
```bash
log() {
    local level="$1"
    shift
    local message="$*"
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] [$level] $message" >> app.log
    
    # Also print to stdout if verbose mode is enabled
    if [[ "$VERBOSE" == "true" ]]; then
        echo "[$level] $message"
    fi
}

# Usage
log "INFO" "Script started"
log "ERROR" "Failed to connect to database"
```

### Configuration Parser
```bash
parse_config() {
    local config_file="$1"
    if [[ ! -f "$config_file" ]]; then
        echo "Config file not found" >&2
        return 1
    fi
    
    while IFS='=' read -r key value; do
        # Skip comments and empty lines
        [[ "$key" =~ ^#.*$ || -z "$key" ]] && continue
        
        # Remove leading/trailing whitespace
        key=$(echo "$key" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
        value=$(echo "$value" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
        
        # Export as environment variables
        export "$key=$value"
    done < "$config_file"
    
    return 0
}

# Usage
parse_config "/path/to/config.ini"
```
