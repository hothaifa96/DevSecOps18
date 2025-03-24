#!/bin/bash

# Lab 4: File Backup Script

echo "===== BACKUP SCRIPT ====="
echo "Date: $(date)"

# Create timestamped backup directory
timestamp=$(date +"%Y%m%d_%H%M%S")
backup_dir="/backups/${timestamp}"

# Create the backup directory
mkdir -p "$backup_dir"

# Display the backup location
echo "Backup location: $backup_dir/"

# List of configuration files to back up
config_files=(
    "/etc/nginx/nginx.conf"
    "/etc/apache2/apache2.conf"
    "/etc/mysql/my.cnf"
    "/etc/ssh/sshd_config"
    "/var/www/html"
    "/opt/application/config.json"
)

# Initialize counters
total_files=${#config_files[@]}
success_count=0
fail_count=0

# Start timing the backup
start_time=$(date +%s.%N)

# Display backup header
echo "Backing up configuration files:"

# Loop through each file/directory
for file in "${config_files[@]}"; do
    # Print file name with dots for alignment
    printf "- %s " "$file"
    dots_needed=$((30 - ${#file}))
    for ((i=0; i<dots_needed; i++)); do
        printf "."
    done
    printf " "
    
    # Check if file exists
    if [ -e "$file" ]; then
        # Create directory structure if needed
        mkdir -p "$backup_dir/$(dirname "$file")"
        
        # Perform the backup
        if [ -d "$file" ]; then
            # It's a directory, so use cp -r
            cp -r "$file" "$backup_dir$file" 2>/dev/null
        else
            # It's a file
            cp "$file" "$backup_dir$file" 2>/dev/null
        fi
        
        # Check if backup was successful
        if [ $? -eq 0 ]; then
            echo "SUCCESS"
            success_count=$((success_count + 1))
        else
            echo "FAILED (Permission denied)"
            fail_count=$((fail_count + 1))
        fi
    else
        echo "FAILED (File not found)"
        fail_count=$((fail_count + 1))
    fi
done

# Calculate elapsed time
end_time=$(date +%s.%N)
elapsed=$(echo "$end_time - $start_time" | bc)
elapsed=$(printf "%.1f" "$elapsed")

# Calculate backup size
backup_size=$(du -sh "$backup_dir" | awk '{print $1}')

# Display backup summary
echo "Backup Summary:"
echo "- Total files attempted: $total_files"
echo "- Successfully backed up: $success_count"
echo "- Failed: $fail_count"
echo "Backup completed in $elapsed seconds"
echo "Backup size: $backup_size"

# End of Lab 4