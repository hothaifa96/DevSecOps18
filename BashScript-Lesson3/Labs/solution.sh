#!/bin/bash


##########################
# EASY EXERCISES
##########################

# Exercise 1: Hello Function
# -------------------------
say_hello() {
    echo "Hello, World!"
}

##########################
# USAGE EXAMPLES
##########################

# Demo function to show how to use the solutions
demo_functions() {
    echo "Select a function to demonstrate:"
    echo "1. Hello Function"
    echo "2. Personalized Greeting"
    echo "3. Simple Calculator"
    echo "4. File Checker"
    echo "5. Temperature Converter"
    echo "6. Word Counter"
    echo "7. Log Parser"
    echo "8. Directory Size Analyzer"
    echo "9. Backup Script"
    echo "10. System Monitor"
    echo "11. Interactive Menu Framework"
    echo "12. Bash Utils Library"
    
    read -p "Enter your choice (1-12): " choice
    
    case $choice in
        1)
            say_hello
            ;;
        2)
            greet "Alice"
            greet "Bob"
            ;;
        3)
            calculate 10 + 5
            calculate 10 - 5
            calculate 10 '*' 5
            calculate 10 / 5
            calculate 10 / 0
            ;;
        4)
            # Create test files with different permissions
            echo "Test file" > test_file.txt
            chmod 644 test_file.txt
            
            echo "#!/bin/bash" > test_script.sh
            echo "echo 'Hello'" >> test_script.sh
            chmod 755 test_script.sh
            
            check_file test_file.txt
            check_file test_script.sh
            check_file nonexistent_file.txt
            
            # Clean up
            rm -f test_file.txt test_script.sh
            ;;
        5)
            # Simulate user input for temperature converter
            temp_converter
            ;;
        6)
            # Create a test file
            cat > test_count.txt << EOF
This is a test file
for the word counter function.
It has multiple lines
and several words to count.
EOF
            
            count_text test_count.txt
            count_text nonexistent_file.txt
            
            # Clean up
            rm -f test_count.txt
            ;;
        7)
            # Create a test log file
            cat > test_log.txt << EOF
2023-04-12 14:32:45 INFO User logged in successfully
2023-04-12 14:33:12 WARNING Failed login attempt
2023-04-12 14:35:22 ERROR Database connection failed
2023-04-12 14:37:01 INFO User logged out
2023-04-12 14:40:15 ERROR Failed to connect to server
EOF
            
            parse_log test_log.txt "ERROR"
            
            # Clean up
            rm -f test_log.txt
            ;;
        8)
            # Create test directory structure
            mkdir -p test_dir/subdir
            dd if=/dev/zero of=test_dir/file1.bin bs=1M count=5 2>/dev/null
            dd if=/dev/zero of=test_dir/file2.bin bs=1M count=10 2>/dev/null
            dd if=/dev/zero of=test_dir/subdir/file3.bin bs=1M count=15 2>/dev/null
            
            dir_size test_dir false
            dir_size test_dir true
            
            # Clean up
            rm -rf test_dir
            ;;
        9)
            # Create test directory for backup
            mkdir -p test_backup_source
            echo "Test file 1" > test_backup_source/file1.txt
            echo "Test file 2" > test_backup_source/file2.txt
            mkdir -p test_backup_dest
            
            # Run backup with simulated parameters
            run_backup "test_backup_source" "test_backup_dest" "password123"
            
            # Clean up
            rm -rf test_backup_source test_backup_dest backup.log
            ;;
        10)
            echo "Running system monitor (press Ctrl+C to stop)..."
            # Run monitor for just one cycle by modifying the function internally
            run_system_monitor_demo() {
                local cpu_threshold=80
                local mem_threshold=60
                local disk_threshold=80
                
                clear
                local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
                echo "SYSTEM MONITORING REPORT - $timestamp"
                echo ""
                
                # Check CPU
                local cpu=$(check_cpu)
                if [ "$cpu" -gt "$cpu_threshold" ]; then
                    echo "CPU: ${cpu}% [WARNING]"
                    cpu_alert=1
                else
                    echo "CPU: ${cpu}% [OK]"
                    cpu_alert=0
                fi
                
                # Check Memory
                local mem=$(check_memory)
                if [ "$mem" -gt "$mem_threshold" ]; then
                    echo "Memory: ${mem}% [WARNING]"
                    mem_alert=1
                else
                    echo "Memory: ${mem}% [OK]"
                    mem_alert=0
                fi
                
                # Check Disk
                local disk=$(check_disk)
                if [ "$disk" -gt "$disk_threshold" ]; then
                    echo "Disk: ${disk}% [WARNING]"
                    disk_alert=1
                else
                    echo "Disk: ${disk}% [OK]"
                    disk_alert=0
                fi
                
                # Check Network
                local network=$(check_network)
                echo "Network: $network [OK]"
                
                echo ""
                echo "TOP PROCESSES:"
                check_processes
                
                echo ""
                echo "ALERTS:"
                if [ "$cpu_alert" -eq 1 ]; then
                    echo "- CPU usage above threshold (${cpu}% > ${cpu_threshold}%)"
                fi
                if [ "$mem_alert" -eq 1 ]; then
                    echo "- Memory usage above threshold (${mem}% > ${mem_threshold}%)"
                fi
                if [ "$disk_alert" -eq 1 ]; then
                    echo "- Disk usage above threshold (${disk}% > ${disk_threshold}%)"
                fi
                
                if [ "$cpu_alert" -eq 0 ] && [ "$mem_alert" -eq 0 ] && [ "$disk_alert" -eq 0 ]; then
                    echo "- No alerts at this time."
                fi
            }
            
            run_system_monitor_demo
            ;;
        11)
            echo "Running interactive menu demo (press Ctrl+C to stop)..."
            echo "This will clear the screen and start a full interactive session."
            echo "Press Enter to continue or Ctrl+C to cancel..."
            read
            
            # Run a simplified version of the menu demo
            run_menu_demo_simple() {
                # Setup menu options
                add_option "main" "Say Hello" "function_hello" "Displays a greeting message"
                add_option "main" "Show Date" "function_date" "Shows the current date and time"
                
                # Display menu once
                display_menu "main" "Simple Menu Demo"
                echo "This is a simplified demo. The full version is interactive."
            }
            
            run_menu_demo_simple
            ;;
        12)
            # Demonstrate a few utility functions
            echo "Original string: '  Hello World  '"
            echo "Trimmed: '$(trim "  Hello World  ")'"
            echo "Uppercase: '$(to_uppercase "Hello World")'"
            echo "Lowercase: '$(to_lowercase "Hello World")'"
            
            echo ""
            echo "Validating email: valid@example.com"
            validate_email "valid@example.com"
            echo "Exit code: $?"
            
            echo "Validating email: invalid@email"
            validate_email "invalid@email"
            echo "Exit code: $?"
            
            echo ""
            echo "Color text examples:"
            color_text "This is red text" "red"
            color_text "This is green text" "green"
            color_text "This is blue text" "blue"
            
            echo ""
            echo "Progress bar example:"
            for i in {1..10}; do
                progress_bar $i 10 40
                sleep 0.2
            done
            echo ""
            ;;
        *)
            echo "Invalid choice."
            ;;
    esac
}

# Run the demo if this script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    demo_functions
fi

# Exercise 2: Personalized Greeting
# --------------------------------
greet() {
    echo "Hello, $1!"
}

# Exercise 3: Simple Calculator
# ---------------------------
calculate() {
    local num1=$1
    local num2=$3
    local operator=$2
    
    case $operator in
        add|+)
            echo "$num1 + $num2 = $(( num1 + num2 ))"
            ;;
        subtract|-)
            echo "$num1 - $num2 = $(( num1 - num2 ))"
            ;;
        multiply|*)
            echo "$num1 * $num2 = $(( num1 * num2 ))"
            ;;
        divide|/)
            if [ "$num2" -eq 0 ]; then
                echo "Cannot divide by zero!"
            else
                echo "$num1 / $num2 = $(( num1 / num2 ))"
            fi
            ;;
        *)
            echo "Invalid operator. Use add, subtract, multiply, or divide."
            ;;
    esac
}

##########################
# INTERMEDIATE EXERCISES
##########################

# Exercise 4: File Checker
# -----------------------
check_file() {
    local file="$1"
    
    if [ -e "$file" ]; then
        echo "File $file exists:"
        
        # Check if readable
        if [ -r "$file" ]; then
            echo "- Readable: yes"
        else
            echo "- Readable: no"
        fi
        
        # Check if writable
        if [ -w "$file" ]; then
            echo "- Writable: yes"
        else
            echo "- Writable: no"
        fi
        
        # Check if executable
        if [ -x "$file" ]; then
            echo "- Executable: yes"
        else
            echo "- Executable: no"
        fi
    else
        echo "File $file does not exist."
    fi
    
    echo ""
}

# Exercise 5: Temperature Converter
# -------------------------------
celsius_to_fahrenheit() {
    local celsius=$1
    local fahrenheit=$(echo "scale=1; ($celsius * 9/5) + 32" | bc)
    echo $fahrenheit
}

fahrenheit_to_celsius() {
    local fahrenheit=$1
    local celsius=$(echo "scale=1; ($fahrenheit - 32) * 5/9" | bc)
    echo $celsius
}

temp_converter() {
    echo -n "Enter temperature: "
    read temp
    
    echo -n "Current unit (C/F): "
    read unit
    
    case $unit in
        [Cc])
            fahrenheit=$(celsius_to_fahrenheit $temp)
            echo "${temp}°C = ${fahrenheit}°F"
            ;;
        [Ff])
            celsius=$(fahrenheit_to_celsius $temp)
            echo "${temp}°F = ${celsius}°C"
            ;;
        *)
            echo "Invalid unit. Use C or F."
            ;;
    esac
}

# Exercise 6: Word Counter
# ----------------------
count_text() {
    local file="$1"
    
    if [ ! -f "$file" ]; then
        echo "Error: File $file does not exist."
        return 1
    fi
    
    local lines=$(wc -l < "$file")
    local words=$(wc -w < "$file")
    local chars=$(wc -m < "$file")
    
    echo "File: $file"
    echo "- Lines: $lines"
    echo "- Words: $words"
    echo "- Characters: $chars"
}

##########################
# ADVANCED EXERCISES
##########################

# Exercise 7: Log Parser
# --------------------
parse_log() {
    local log_file="$1"
    local search_term="$2"
    
    if [ ! -f "$log_file" ]; then
        echo "Error: Log file $log_file does not exist."
        return 1
    fi
    
    echo "Searching for '$search_term' in $log_file:"
    echo "----------------------------------------"
    
    grep "$search_term" "$log_file" | while read -r line; do
        # Extract timestamp (assuming format: YYYY-MM-DD HH:MM:SS)
        local timestamp=$(echo "$line" | grep -o '[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} [0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}')
        
        # Extract log level (INFO, WARNING, ERROR)
        local level=$(echo "$line" | grep -o 'INFO\|WARNING\|ERROR')
        
        # Extract message (everything after the log level)
        local message=$(echo "$line" | sed "s/.*$level //")
        
        echo "[$timestamp] [$level] $message"
    done
}

# Exercise 8: Directory Size Analyzer
# ---------------------------------
dir_size() {
    local dir_path="$1"
    local recursive="$2"
    
    if [ ! -d "$dir_path" ]; then
        echo "Error: Directory $dir_path does not exist."
        return 1
    fi
    
    local size_bytes
    if [ "$recursive" = true ]; then
        size_bytes=$(du -sb "$dir_path" | cut -f1)
        echo "Directory (recursive): $dir_path"
    else
        size_bytes=$(find "$dir_path" -maxdepth 1 -type f -exec du -bc {} \; | grep total$ | cut -f1)
        echo "Directory: $dir_path"
    fi
    
    # Convert to human-readable format
    if [ "$size_bytes" -lt 1024 ]; then
        echo "Size: ${size_bytes} B"
    elif [ "$size_bytes" -lt 1048576 ]; then
        echo "Size: $(echo "scale=1; $size_bytes/1024" | bc) KB"
    elif [ "$size_bytes" -lt 1073741824 ]; then
        echo "Size: $(echo "scale=1; $size_bytes/1048576" | bc) MB"
    else
        echo "Size: $(echo "scale=1; $size_bytes/1073741824" | bc) GB"
    fi
}

# Exercise 9: Backup Script
# -----------------------
check_space() {
    local source_dir="$1"
    local backup_dir="$2"
    
    # Get source directory size
    local source_size=$(du -sb "$source_dir" | cut -f1)
    
    # Get available space in backup directory
    local backup_space=$(df -B1 --output=avail "$backup_dir" | tail -n1)
    
    # Need at least 1.5x the source size for temporary files
    local needed_space=$(echo "$source_size * 1.5" | bc | cut -d. -f1)
    
    if [ "$backup_space" -lt "$needed_space" ]; then
        echo "Not enough space. Need: $needed_space bytes, Available: $backup_space bytes."
        return 1
    else
        echo "Checking available space... OK"
        return 0
    fi
}

create_archive() {
    local source_dir="$1"
    local archive_name="$2"
    
    tar -czf "$archive_name" -C "$(dirname "$source_dir")" "$(basename "$source_dir")"
    
    if [ $? -eq 0 ]; then
        echo "Creating archive of $source_dir... OK"
        return 0
    else
        echo "Failed to create archive."
        return 1
    fi
}

encrypt_file() {
    local file="$1"
    local password="$2"
    
    # Using OpenSSL for encryption
    openssl enc -aes-256-cbc -salt -in "$file" -out "${file}.enc" -pass "pass:$password"
    
    if [ $? -eq 0 ]; then
        echo "Encrypting $file... OK"
        return 0
    else
        echo "Failed to encrypt file."
        return 1
    fi
}

transfer_file() {
    local file="$1"
    local destination="$2"
    
    # Check if destination is local or remote
    if [[ "$destination" =~ ^[a-zA-Z0-9_-]+@ ]]; then
        # Remote destination
        scp "$file" "$destination"
    else
        # Local destination
        cp "$file" "$destination"
    fi
    
    if [ $? -eq 0 ]; then
        echo "Transferring $file to $destination... OK"
        return 0
    else
        echo "Failed to transfer file."
        return 1
    fi
}

cleanup() {
    local files=("$@")
    
    for file in "${files[@]}"; do
        if [ -e "$file" ]; then
            rm "$file"
        fi
    done
    
    echo "Cleaning up temporary files... OK"
    return 0
}

log_action() {
    local message="$1"
    local log_file="$2"
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    
    echo "[$timestamp] $message" >> "$log_file"
}

run_backup() {
    local source_dir="$1"
    local backup_dir="$2"
    local password="$3"
    local log_file="backup.log"
    
    local timestamp=$(date "+%Y-%m-%d_%H-%M-%S")
    local archive_name="backup_${timestamp}.tar.gz"
    
    echo "Starting backup at $(date "+%Y-%m-%d %H:%M:%S")"
    log_action "Starting backup of $source_dir" "$log_file"
    
    # Check space
    check_space "$source_dir" "$backup_dir"
    if [ $? -ne 0 ]; then
        log_action "ERROR: Not enough space for backup" "$log_file"
        echo "Backup failed. See $log_file for details."
        return 1
    fi
    log_action "Space check passed" "$log_file"
    
    # Create archive
    create_archive "$source_dir" "$archive_name"
    if [ $? -ne 0 ]; then
        log_action "ERROR: Failed to create archive" "$log_file"
        echo "Backup failed. See $log_file for details."
        return 1
    fi
    log_action "Archive created: $archive_name" "$log_file"
    
    # Encrypt archive
    encrypt_file "$archive_name" "$password"
    if [ $? -ne 0 ]; then
        log_action "ERROR: Failed to encrypt archive" "$log_file"
        cleanup "$archive_name"
        echo "Backup failed. See $log_file for details."
        return 1
    fi
    log_action "Archive encrypted: ${archive_name}.enc" "$log_file"
    
    # Transfer file
    transfer_file "${archive_name}.enc" "$backup_dir"
    if [ $? -ne 0 ]; then
        log_action "ERROR: Failed to transfer archive" "$log_file"
        cleanup "$archive_name" "${archive_name}.enc"
        echo "Backup failed. See $log_file for details."
        return 1
    fi
    log_action "Archive transferred to $backup_dir" "$log_file"
    
    # Cleanup
    cleanup "$archive_name" "${archive_name}.enc"
    log_action "Temporary files cleaned up" "$log_file"
    
    echo "Backup completed successfully at $(date "+%Y-%m-%d %H:%M:%S")"
    echo "Log written to $log_file"
    log_action "Backup completed successfully" "$log_file"
    return 0
}

# Exercise 10: System Monitor
# -------------------------
check_cpu() {
    # Get CPU usage using top
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    local cpu_usage_rounded=$(printf "%.0f" $cpu_usage)
    
    echo "$cpu_usage_rounded"
}

check_memory() {
    # Get memory usage using free
    local mem_info=$(free | grep Mem)
    local total=$(echo $mem_info | awk '{print $2}')
    local used=$(echo $mem_info | awk '{print $3}')
    local usage_percent=$(echo "scale=0; $used * 100 / $total" | bc)
    
    echo "$usage_percent"
}

check_disk() {
    # Get disk usage using df
    local disk_info=$(df -h / | tail -1)
    local usage_percent=$(echo $disk_info | awk '{print $5}' | tr -d '%')
    
    echo "$usage_percent"
}

check_network() {
    # Sample network usage for 1 second
    local net_dev="/proc/net/dev"
    local interface=$(grep -v "lo" $net_dev | grep ":" | head -1 | cut -d: -f1 | tr -d ' ')
    
    local start_in=$(grep $interface $net_dev | awk '{print $2}')
    local start_out=$(grep $interface $net_dev | awk '{print $10}')
    
    sleep 1
    
    local end_in=$(grep $interface $net_dev | awk '{print $2}')
    local end_out=$(grep $interface $net_dev | awk '{print $10}')
    
    local in_bytes=$((end_in - start_in))
    local out_bytes=$((end_out - start_out))
    
    # Convert to MB/s
    local in_mb=$(echo "scale=1; $in_bytes / 1048576" | bc)
    local out_mb=$(echo "scale=1; $out_bytes / 1048576" | bc)
    
    echo "In: ${in_mb} MB/s, Out: ${out_mb} MB/s"
}

check_processes() {
    # Get top 5 processes by CPU and memory usage
    local processes=$(ps aux --sort=-%cpu,-%mem | head -6 | tail -5)
    local i=1
    
    while read -r line; do
        local user=$(echo $line | awk '{print $1}')
        local pid=$(echo $line | awk '{print $2}')
        local cpu=$(echo $line | awk '{print $3}')
        local mem=$(echo $line | awk '{print $4}')
        local command=$(echo $line | awk '{print $11}')
        
        local mem_mb=$(echo "scale=0; $(free -m | grep Mem | awk '{print $2}') * $mem / 100" | bc)
        
        echo "$i. $command (PID $pid): CPU ${cpu}%, MEM ${mem_mb}MB"
        ((i++))
    done <<< "$processes"
}

run_system_monitor() {
    local cpu_threshold=80
    local mem_threshold=60
    local disk_threshold=80
    local interval=300  # 5 minutes in seconds
    
    while true; do
        clear
        local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
        echo "SYSTEM MONITORING REPORT - $timestamp"
        echo ""
        
        # Check CPU
        local cpu=$(check_cpu)
        if [ "$cpu" -gt "$cpu_threshold" ]; then
            echo "CPU: ${cpu}% [WARNING]"
            cpu_alert=1
        else
            echo "CPU: ${cpu}% [OK]"
            cpu_alert=0
        fi
        
        # Check Memory
        local mem=$(check_memory)
        if [ "$mem" -gt "$mem_threshold" ]; then
            echo "Memory: ${mem}% [WARNING]"
            mem_alert=1
        else
            echo "Memory: ${mem}% [OK]"
            mem_alert=0
        fi
        
        # Check Disk
        local disk=$(check_disk)
        if [ "$disk" -gt "$disk_threshold" ]; then
            echo "Disk: ${disk}% [WARNING]"
            disk_alert=1
        else
            echo "Disk: ${disk}% [OK]"
            disk_alert=0
        fi
        
        # Check Network
        local network=$(check_network)
        echo "Network: $network [OK]"
        
        echo ""
        echo "TOP PROCESSES:"
        check_processes
        
        echo ""
        echo "ALERTS:"
        if [ "$cpu_alert" -eq 1 ]; then
            echo "- CPU usage above threshold (${cpu}% > ${cpu_threshold}%)"
        fi
        if [ "$mem_alert" -eq 1 ]; then
            echo "- Memory usage above threshold (${mem}% > ${mem_threshold}%)"
        fi
        if [ "$disk_alert" -eq 1 ]; then
            echo "- Disk usage above threshold (${disk}% > ${disk_threshold}%)"
        fi
        
        if [ "$cpu_alert" -eq 0 ] && [ "$mem_alert" -eq 0 ] && [ "$disk_alert" -eq 0 ]; then
            echo "- No alerts at this time."
        fi
        
        echo ""
        echo "Next check in $(($interval / 60)) minutes."
        
        sleep $interval
    done
}

##########################
# EXPERT CHALLENGE
##########################

# Exercise 11: Interactive Menu Framework
# -------------------------------------
declare -A menu_options
declare -A menu_help
declare -A menu_functions
current_menu="main"
menu_stack=()

display_menu() {
    local menu_name=$1
    local title=${2:-"Menu"}
    
    clear
    echo "===== $title ====="
    echo ""
    
    # Display breadcrumb if we're in a submenu
    if [ ${#menu_stack[@]} -gt 0 ]; then
        echo -n "Location: "
        for i in "${menu_stack[@]}"; do
            echo -n "$i > "
        done
        echo "$menu_name"
        echo ""
    fi
    
    # Display options
    local i=1
    IFS=","
    for option in ${menu_options[$menu_name]}; do
        echo "$i) $option"
        ((i++))
    done
    
    echo ""
    echo "h) Help"
    echo "q) Quit" 
    echo ""
}

get_user_choice() {
    local menu_name=$1
    local num_options=$(echo ${menu_options[$menu_name]} | tr ',' ' ' | wc -w)
    
    while true; do
        echo -n "Enter your choice: "
        read choice
        
        if [[ $choice == "q" || $choice == "Q" ]]; then
            return 0
        elif [[ $choice == "h" || $choice == "H" ]]; then
            return -1
        elif [[ $choice =~ ^[0-9]+$ && $choice -ge 1 && $choice -le $num_options ]]; then
            return $choice
        else
            echo "Invalid choice. Please try again."
        fi
    done
}

show_help() {
    local menu_name=$1
    
    clear
    echo "===== Help: $menu_name ====="
    echo ""
    
    local i=1
    IFS=","
    for option in ${menu_options[$menu_name]}; do
        local help_text=${menu_help[$menu_name,$option]:-"No help available."}
        echo "$i) $option: $help_text"
        ((i++))
    done
    
    echo ""
    echo "Press Enter to continue..."
    read
}

run_option() {
    local menu_name=$1
    local choice=$2
    
    local options=($(echo ${menu_options[$menu_name]} | tr ',' ' '))
    local selected=${options[$choice-1]}
    
    local function_name=${menu_functions[$menu_name,$selected]}
    
    # Check if this option leads to a submenu
    if [[ $function_name == SUBMENU:* ]]; then
        local submenu=${function_name#SUBMENU:}
        menu_stack+=("$menu_name")
        current_menu=$submenu
    else
        # Run the associated function
        $function_name
        
        echo ""
        echo "Press Enter to continue..."
        read
    fi
}

add_option() {
    local menu_name=$1
    local option_name=$2
    local function_name=$3
    local help_text=$4
    
    # Check if menu exists, create if it doesn't
    if [ -z "${menu_options[$menu_name]}" ]; then
        menu_options[$menu_name]="$option_name"
    else
        menu_options[$menu_name]="${menu_options[$menu_name]},$option_name"
    fi
    
    menu_functions[$menu_name,$option_name]="$function_name"
    menu_help[$menu_name,$option_name]="$help_text"
}

remove_option() {
    local menu_name=$1
    local option_name=$2
    
    # Remove the option from the options list
    local options=$(echo ${menu_options[$menu_name]} | tr ',' '\n' | grep -v "^$option_name$" | tr '\n' ',' | sed 's/,$//')
    menu_options[$menu_name]="$options"
    
    # Remove the function and help text
    unset menu_functions[$menu_name,$option_name]
    unset menu_help[$menu_name,$option_name]
}

create_submenu() {
    local parent_menu=$1
    local option_name=$2
    local submenu_name=$3
    local help_text=$4
    
    # Add option to parent menu that points to submenu
    add_option "$parent_menu" "$option_name" "SUBMENU:$submenu_name" "$help_text"
}

back_to_parent() {
    if [ ${#menu_stack[@]} -gt 0 ]; then
        current_menu=${menu_stack[${#menu_stack[@]}-1]}
        unset menu_stack[${#menu_stack[@]}-1]
    fi
}

run_menu() {
    while true; do
        display_menu "$current_menu" "Interactive Menu Demo"
        
        get_user_choice "$current_menu"
        local choice=$?
        
        if [ $choice -eq 0 ]; then
            # User selected quit
            if [ ${#menu_stack[@]} -eq 0 ]; then
                # We're in the main menu, exit the program
                clear
                echo "Goodbye!"
                exit 0
            else
                # We're in a submenu, go back to parent
                back_to_parent
            fi
        elif [ $choice -eq -1 ]; then
            # User selected help
            show_help "$current_menu"
        else
            # User selected an option
            run_option "$current_menu" $choice
        fi
    done
}

# Example functions for the menu demo
function_hello() {
    echo "Hello, World!"
}

function_date() {
    echo "Current date and time: $(date)"
}

function_calendar() {
    cal
}

function_user() {
    echo "Current user: $(whoami)"
}

function_add_dynamic() {
    echo -n "Enter the name of the new option: "
    read option_name
    
    add_option "main" "$option_name" "function_dynamic" "Dynamically added option"
    echo "Option added successfully!"
}

function_remove_dynamic() {
    echo "Available options to remove:"
    local options=($(echo ${menu_options[$current_menu]} | tr ',' ' '))
    local i=1
    for option in "${options[@]}"; do
        echo "$i) $option"
        ((i++))
    done
    
    echo -n "Enter the number of the option to remove: "
    read choice
    
    if [[ $choice =~ ^[0-9]+$ && $choice -ge 1 && $choice -le ${#options[@]} ]]; then
        remove_option "$current_menu" "${options[$choice-1]}"
        echo "Option removed successfully!"
    else
        echo "Invalid choice."
    fi
}

function_dynamic() {
    echo "This is a dynamically added function!"
}

function_sub1() {
    echo "This is function 1 in the submenu!"
}

function_sub2() {
    echo "This is function 2 in the submenu!"
}

setup_demo_menu() {
    # Main menu options
    add_option "main" "Say Hello" "function_hello" "Displays a greeting message"
    add_option "main" "Show Date" "function_date" "Shows the current date and time"
    add_option "main" "Show Calendar" "function_calendar" "Displays a calendar for the current month"
    add_option "main" "Add Option" "function_add_dynamic" "Adds a new option to the menu dynamically"
    add_option "main" "Remove Option" "function_remove_dynamic" "Removes an option from the menu"
    
    # Create a submenu
    create_submenu "main" "Tools Submenu" "tools" "Opens a submenu with additional tools"
    
    # Add options to the submenu
    add_option "tools" "Show Current User" "function_user" "Displays the current user"
    add_option "tools" "Function 1" "function_sub1" "Example function 1"
    add_option "tools" "Function 2" "function_sub2" "Example function 2"
    
    # Set starting menu
    current_menu="main"
}

run_menu_demo() {
    setup_demo_menu
    run_menu
}

##########################
# BONUS CHALLENGE
##########################

# Exercise 12: Library Management
# -----------------------------
# This would typically be implemented as a separate file: bash_utils.sh
# Below is a comprehensive utility library with documentation:

# String manipulation functions
trim() {
    local string="$1"
    echo "$string" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//'
}

to_uppercase() {
    local string="$1"
    echo "$string" | tr '[:lower:]' '[:upper:]'
}

to_lowercase() {
    local string="$1"
    echo "$string" | tr '[:upper:]' '[:lower:]'
}

# File handling functions
safe_copy() {
    local source="$1"
    local destination="$2"
    
    if [ ! -f "$source" ]; then
        echo "Error: Source file does not exist."
        return 1
    fi
    
    if [ -f "$destination" ]; then
        echo -n "File $destination already exists. Overwrite? (y/n): "
        read confirmation
        
        if [[ ! $confirmation =~ ^[Yy]$ ]]; then
            echo "Operation cancelled."
            return 0
        fi
    fi
    
    cp "$source" "$destination"
    echo "File copied successfully."
    return 0
}

# Input validation functions
validate_number() {
    local input="$1"
    local min="${2:-}"
    local max="${3:-}"
    
    if ! [[ $input =~ ^[0-9]+$ ]]; then
        echo "Error: Input must be a number."
        return 1
    fi
    
    if [ -n "$min" ] && [ "$input" -lt "$min" ]; then
        echo "Error: Input must be at least $min."
        return 1
    fi
    
    if [ -n "$max" ] && [ "$input" -gt "$max" ]; then
        echo "Error: Input must be at most $max."
        return 1
    fi
    
    return 0
}

validate_email() {
    local email="$1"
    
    if [[ $email =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$ ]]; then
        return 0
    else
        echo "Error: Invalid email address."
        return 1
    fi
}

# Logging functions
LOG_LEVEL_DEBUG=0
LOG_LEVEL_INFO=1
LOG_LEVEL_WARNING=2
LOG_LEVEL_ERROR=3
LOG_LEVEL_CRITICAL=4

LOG_LEVEL=$LOG_LEVEL_INFO
LOG_FILE="app.log"
MAX_LOG_SIZE=1048576  # 1MB

log_rotate() {
    local log_file="$1"
    
    if [ -f "$log_file" ] && [ $(stat -c%s "$log_file") -gt $MAX_LOG_SIZE ]; then
        mv "$log_file" "${log_file}.1"
        touch "$log_file"
    fi
}

log() {
    local level="$1"
    local message="$2"
    local level_name
    
    case $level in
        $LOG_LEVEL_DEBUG)
            level_name="DEBUG"
            ;;
        $LOG_LEVEL_INFO)
            level_name="INFO"
            ;;
        $LOG_LEVEL_WARNING)
            level_name="WARNING"
            ;;
        $LOG_LEVEL_ERROR)
            level_name="ERROR"
            ;;
        $LOG_LEVEL_CRITICAL)
            level_name="CRITICAL"
            ;;
    esac
    
    if [ $level -ge $LOG_LEVEL ]; then
        local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
        echo "[$timestamp] [$level_name] $message" >> "$LOG_FILE"
        
        log_rotate "$LOG_FILE"
    fi
}

# UI functions
progress_bar() {
    local current="$1"
    local total="$2"
    local width="${3:-50}"
    
    local percentage=$((current * 100 / total))
    local completed=$((width * current / total))
    local remaining=$((width - completed))
    
    printf "\r["
    printf "%${completed}s" | tr " " "#"
    printf "%${remaining}s" | tr " " " "
    printf "] %3d%%" $percentage
}

color_text() {
    local text="$1"
    local color="$2"
    
    case $color in
        black)   echo -e "\033[0;30m$text\033[0m" ;;
        red)     echo -e "\033[0;31m$text\033[0m" ;;
        green)   echo -e "\033[0;32m$text\033[0m" ;;
        yellow)  echo -e "\033[0;33m$text\033[0m" ;;
        blue)    echo -e "\033[0;34m$text\033[0m" ;;
        magenta) echo -e "\033[0;35m$text\033[0m" ;;
        cyan)    echo -e "\033[0;36m$text\033[0m" ;;
        white)   echo -e "\033[0;37m$text\033[0m" ;;
    esac
}

spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\'
    
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf "\r[%c] " "$spinstr"
        local spinstr=$temp${spinstr%???}
        sleep $delay
    done
    printf "\r   \r"
}