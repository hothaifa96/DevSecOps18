#!/bin/bash


# Exercise 1: File Backup Tool
backup_file() {
    # Check if filename was provided
    if [ -z "$1" ]; then
        echo "Error: No filename provided."
        echo "Usage: backup_file <filename>"
        return 1
    fi

    filename="$1"

    # Check if the file exists
    if [ ! -f "$filename" ]; then
        echo "Error: File '$filename' does not exist."
        return 1
    fi

    # Ask if user wants to specify a custom backup location
    echo -n "Do you want to specify a custom backup location? (y/n): "
    read -r custom_location_choice

    if [[ "$custom_location_choice" =~ ^[Yy]$ ]]; then
        echo -n "Enter backup location (directory path): "
        read -r backup_dir
        
        # Check if the directory exists
        if [ ! -d "$backup_dir" ]; then
            echo "Directory does not exist. Do you want to create it? (y/n): "
            read -r create_dir
            
            if [[ "$create_dir" =~ ^[Yy]$ ]]; then
                mkdir -p "$backup_dir"
                if [ $? -ne 0 ]; then
                    echo "Error: Failed to create directory."
                    return 1
                fi
            else
                echo "Operation canceled."
                return 1
            fi
        fi
    else
        # Use current directory as backup location
        backup_dir="."
    fi

    # Get current date
    current_date=$(date +"%Y-%m-%d")
    
    # Get file extension and base name
    base_name=$(basename "$filename")
    
    # Create backup filename
    backup_filename="${backup_dir}/${base_name}.${current_date}.bak"
    
    # Create the backup
    cp "$filename" "$backup_filename"
    
    # Check if backup was successful
    if [ $? -eq 0 ]; then
        echo "Backup created successfully: $backup_filename"
    else
        echo "Error: Failed to create backup."
        return 1
    fi
    
    return 0
}

# Exercise 2: User Account Information
user_info() {
    # Check if at least one username was provided
    if [ $# -eq 0 ]; then
        echo -n "Enter a username: "
        read -r username
        display_user_info "$username"
    else
        # Process all usernames provided as arguments
        for username in "$@"; do
            display_user_info "$username"
        done
    fi
}

display_user_info() {
    username="$1"
    
    # Check if user exists
    if ! getent passwd "$username" > /dev/null; then
        echo "Error: User '$username' does not exist."
        return 1
    fi
    
    echo "=== User Information for: $username ==="
    
    # Get user's home directory
    home_dir=$(getent passwd "$username" | cut -d: -f6)
    echo "Home Directory: $home_dir"
    
    # Get user's shell
    shell=$(getent passwd "$username" | cut -d: -f7)
    echo "Shell: $shell"
    
    # Get last login time
    echo "Last Login:"
    last_login=$(last -n 1 "$username" 2>/dev/null)
    if [ -z "$last_login" ]; then
        echo "  No login records found."
    else
        echo "  $last_login"
    fi
    
    # Additional user info
    echo "UID: $(id -u "$username")"
    echo "Groups: $(groups "$username" 2>/dev/null | cut -d: -f2)"
    echo ""
    
    return 0
}

# Exercise 3: Interactive Calculator
calculator() {
    local operation=""
    local num1=""
    local num2=""
    
    # Process arguments if provided
    if [ $# -ge 1 ]; then
        operation="$1"
    fi
    
    if [ $# -ge 2 ]; then
        num1="$2"
    fi
    
    if [ $# -ge 3 ]; then
        num2="$3"
    fi
    
    # Main calculator loop
    while true; do
        # Get operation if not provided
        if [ -z "$operation" ]; then
            echo -n "Enter operation (add, subtract, multiply, divide): "
            read -r operation
        fi
        
        # Validate operation
        if [ "$operation" = "add" ] || [ "$operation" = "subtract" ] || [ "$operation" = "multiply" ] || [ "$operation" = "divide" ]; then
            # Valid operation
            :
        else
            echo "Invalid operation. Please use add, subtract, multiply, or divide."
            operation=""
            continue
        fi
        
        # Get first number if not provided
        if [ -z "$num1" ]; then
            echo -n "Enter first number: "
            read -r num1
        fi
        
        # Validate num1 is numeric
        if ! [[ "$num1" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
            echo "Invalid input. Please enter a numeric value."
            num1=""
            continue
        fi
        
        # Get second number if not provided
        if [ -z "$num2" ]; then
            echo -n "Enter second number: "
            read -r num2
        fi
        
        # Validate num2 is numeric
        if ! [[ "$num2" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
            echo "Invalid input. Please enter a numeric value."
            num2=""
            continue
        fi
        
        # Check for division by zero
        if [ "$operation" = "divide" ] && [ "$num2" = "0" ]; then
            echo "Error: Cannot divide by zero."
            num2=""
            continue
        fi
        
        # Perform calculation
        if [ "$operation" = "add" ]; then
            result=$(echo "$num1 + $num2" | bc -l)
            echo "Result: $num1 + $num2 = $result"
        elif [ "$operation" = "subtract" ]; then
            result=$(echo "$num1 - $num2" | bc -l)
            echo "Result: $num1 - $num2 = $result"
        elif [ "$operation" = "multiply" ]; then
            result=$(echo "$num1 * $num2" | bc -l)
            echo "Result: $num1 * $num2 = $result"
        elif [ "$operation" = "divide" ]; then
            result=$(echo "scale=4; $num1 / $num2" | bc -l)
            echo "Result: $num1 / $num2 = $result"
        fi
        
        # Ask if user wants to perform another calculation
        echo -n "Perform another calculation? (y/n): "
        read -r another
        
        if [[ ! "$another" =~ ^[Yy]$ ]]; then
            break
        fi
        
        # Reset variables for next calculation
        operation=""
        num1=""
        num2=""
    done
    
    echo "Calculator exited."
}

# Exercise 4: File Search and Analysis
file_search() {
    local extension=""
    local directory=""
    local action=""
    
    # Process arguments if provided
    if [ $# -ge 1 ]; then
        extension="$1"
    fi
    
    if [ $# -ge 2 ]; then
        directory="$2"
    else
        directory="."
    fi
    
    if [ $# -ge 3 ]; then
        action="$3"
    else
        action="list"
    fi
    
    # Prompt for extension if not provided
    if [ -z "$extension" ]; then
        echo -n "Enter file extension (without dot): "
        read -r extension
    fi
    
    # Validate directory
    if [ ! -d "$directory" ]; then
        echo "Error: Directory '$directory' does not exist."
        return 1
    fi
    
    # Validate action
    if [ "$action" = "count" ] || [ "$action" = "list" ] || [ "$action" = "size" ] || [ "$action" = "newest" ]; then
        # Valid action
        :
    else
        echo "Invalid action. Using default (list)."
        action="list"
    fi
    
    echo "Searching for .$extension files in $directory..."
    
    # Perform the requested action
    if [ "$action" = "count" ]; then
        count=$(find "$directory" -type f -name "*.$extension" | wc -l)
        echo "Found $count files with extension .$extension"
    elif [ "$action" = "list" ]; then
        echo "Files with extension .$extension:"
        find "$directory" -type f -name "*.$extension" | sort
    elif [ "$action" = "size" ]; then
        echo "Size of all .$extension files:"
        find "$directory" -type f -name "*.$extension" -exec du -ch {} \; | grep total$
        echo "Individual file sizes:"
        find "$directory" -type f -name "*.$extension" -exec du -h {} \; | sort -hr
    elif [ "$action" = "newest" ]; then
        echo "5 most recently modified .$extension files:"
        find "$directory" -type f -name "*.$extension" -printf "%T@ %TY-%Tm-%Td %TH:%TM:%TS %p\n" | sort -nr | head -5 | cut -d' ' -f2-
    fi
    
    return 0
}

# Exercise 5: System Resource Monitor
resource_monitor() {
    local resource_type=""
    local threshold=""
    local format=""
    
    # Process arguments if provided
    if [ $# -ge 1 ]; then
        resource_type="$1"
    else
        resource_type="all"
    fi
    
    if [ $# -ge 2 ]; then
        threshold="$2"
    else
        threshold=80
    fi
    
    if [ $# -ge 3 ]; then
        format="$3"
    else
        format="text"
    fi
    
    # Interactive mode to change settings
    echo "System Resource Monitor"
    echo "Current settings:"
    echo "  Resource type: $resource_type"
    echo "  Threshold: $threshold%"
    echo "  Output format: $format"
    
    echo -n "Change settings? (y/n): "
    read -r change_settings
    
    if [[ "$change_settings" =~ ^[Yy]$ ]]; then
        echo -n "Resource type (cpu, memory, disk, all): "
        read -r new_resource
        if [ -n "$new_resource" ]; then
            resource_type="$new_resource"
        fi
        
        echo -n "Threshold percentage (0-100): "
        read -r new_threshold
        if [[ "$new_threshold" =~ ^[0-9]+$ ]] && [ "$new_threshold" -ge 0 ] && [ "$new_threshold" -le 100 ]; then
            threshold="$new_threshold"
        else
            echo "Invalid threshold. Using $threshold%."
        fi
        
        echo -n "Output format (text, simple, detailed): "
        read -r new_format
        if [ -n "$new_format" ]; then
            format="$new_format"
        fi
    fi
    
    # Validate resource type
    if [ "$resource_type" = "cpu" ] || [ "$resource_type" = "memory" ] || [ "$resource_type" = "disk" ] || [ "$resource_type" = "all" ]; then
        # Valid resource type
        :
    else
        echo "Invalid resource type. Using 'all'."
        resource_type="all"
    fi
    
    # Check CPU usage if requested
    if [ "$resource_type" = "cpu" ] || [ "$resource_type" = "all" ]; then
        echo "=== CPU Usage ==="
        
        # Get CPU usage (may vary depending on system)
        cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
        cpu_usage_rounded=$(printf "%.0f" "$cpu_usage")
        
        if [ "$format" = "simple" ]; then
            echo "CPU: $cpu_usage_rounded%"
        else
            echo "CPU Usage: $cpu_usage_rounded%"
            
            if [ "$format" = "detailed" ]; then
                echo "CPU Details:"
                top -bn1 | head -5
            fi
        fi
        
        if [ "$cpu_usage_rounded" -gt "$threshold" ]; then
            echo "ALERT: CPU usage exceeds threshold of $threshold%"
        fi
        
        echo ""
    fi
    
    # Check memory usage if requested
    if [ "$resource_type" = "memory" ] || [ "$resource_type" = "all" ]; then
        echo "=== Memory Usage ==="
        
        # Get memory information
        mem_info=$(free -m)
        total_mem=$(echo "$mem_info" | awk '/Mem:/ {print $2}')
        used_mem=$(echo "$mem_info" | awk '/Mem:/ {print $3}')
        mem_usage=$((used_mem * 100 / total_mem))
        
        if [ "$format" = "simple" ]; then
            echo "Memory: $mem_usage%"
        else
            echo "Memory Usage: $mem_usage% ($used_mem MB / $total_mem MB)"
            
            if [ "$format" = "detailed" ]; then
                echo "Memory Details:"
                free -m
            fi
        fi
        
        if [ "$mem_usage" -gt "$threshold" ]; then
            echo "ALERT: Memory usage exceeds threshold of $threshold%"
        fi
        
        echo ""
    fi
    
    # Check disk usage if requested
    if [ "$resource_type" = "disk" ] || [ "$resource_type" = "all" ]; then
        echo "=== Disk Usage ==="
        
        # Get disk information
        if [ "$format" = "simple" ]; then
            df -h / | awk 'NR==2 {print "Disk: " $5}'
            disk_usage=$(df -h / | awk 'NR==2 {gsub("%","",$5); print $5}')
        else
            df -h / | awk 'NR==1 {print $0}; NR==2 {print $0}'
            disk_usage=$(df -h / | awk 'NR==2 {gsub("%","",$5); print $5}')
            
            if [ "$format" = "detailed" ]; then
                echo "Disk Details:"
                df -h
            fi
        fi
        
        if [ "$disk_usage" -gt "$threshold" ]; then
            echo "ALERT: Disk usage exceeds threshold of $threshold%"
        fi
        
        echo ""
    fi
    
    # Summary
    echo "=== Resource Summary ==="
    if [ "$resource_type" = "all" ]; then
        echo "CPU: $cpu_usage_rounded% | Memory: $mem_usage% | Disk: $disk_usage%"
        
        # Count alerts
        alerts=0
        [ "$cpu_usage_rounded" -gt "$threshold" ] && ((alerts++))
        [ "$mem_usage" -gt "$threshold" ] && ((alerts++))
        [ "$disk_usage" -gt "$threshold" ] && ((alerts++))
        
        echo "Alerts: $alerts"
    fi
    
    return 0
}

# Main function to handle command-line arguments
main() {
    if [ $# -eq 0 ]; then
        echo "Bash Scripting Exercises"
        echo "1. File Backup Tool"
        echo "2. User Account Information"
        echo "3. Interactive Calculator"
        echo "4. File Search and Analysis"
        echo "5. System Resource Monitor"
        echo -n "Enter exercise number (1-5): "
        read -r choice
    else
        choice="$1"
        shift
    fi
    
    if [ "$choice" = "1" ]; then
        backup_file "$@"
    elif [ "$choice" = "2" ]; then
        user_info "$@"
    elif [ "$choice" = "3" ]; then
        calculator "$@"
    elif [ "$choice" = "4" ]; then
        file_search "$@"
    elif [ "$choice" = "5" ]; then
        resource_monitor "$@"
    else
        echo "Invalid choice."
        return 1
    fi
    
    return 0
}

# Run the main function with all script arguments
main "$@"