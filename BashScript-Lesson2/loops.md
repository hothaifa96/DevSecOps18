# Bash Scripting Loops Guide

Loops are essential control structures in Bash scripting that allow you to execute commands repeatedly. This guide covers the most common loop types in Bash with practical examples for DevOps tasks.

## Table of Contents
- [For Loops](#for-loops)
- [While Loops](#while-loops)
- [Until Loops](#until-loops)
- [Loop Control](#loop-control)
- [Practical DevOps Examples](#practical-devops-examples)

## For Loops

### Basic Syntax

```bash
for variable in list
do
    # commands to execute
done
```

### Examples

#### Loop through a range of numbers

```bash
# Count from 1 to 5
for i in {1..5}
do
    echo "Number: $i"
done
```

#### Loop with step value

```bash
# Count from 0 to 10 by 2
for i in {0..10..2}
do
    echo "Even number: $i"
done
```

#### Traditional C-style for loop

```bash
# Count from 1 to 5
for ((i=1; i<=5; i++))
do
    echo "Count: $i"
done
```

### For Loops with Files

#### Iterate through files in current directory

```bash
for file in *
do
    echo "Found file: $file"
done
```

#### Iterate through specific file types

```bash
for file in *.log
do
    echo "Processing log file: $file"
done
```

#### Process files recursively

```bash
for file in $(find /path/to/directory -type f -name "*.conf")
do
    echo "Found configuration file: $file"
    # Process each file
done
```

#### Reading file content line by line

```bash
for line in $(cat config.txt)
do
    echo "Line: $line"
done
```

#### Better way to read file line by line (preserves whitespace)

```bash
while IFS= read -r line
do
    echo "Line: $line"
done < config.txt
```

## While Loops

### Basic Syntax

```bash
while [ condition ]
do
    # commands to execute
done
```

### Examples

#### Simple counter

```bash
count=1
while [ $count -le 5 ]
do
    echo "Count: $count"
    ((count++))
done
```

#### Reading file line by line

```bash
while IFS= read -r line
do
    echo "Processing: $line"
    # Do something with each line
done < data.txt
```

#### Monitoring a process

```bash
while ps -p $PID > /dev/null
do
    echo "Process $PID is still running..."
    sleep 5
done
echo "Process $PID has completed."
```

#### Reading command output

```bash
while read -r server
do
    echo "Checking server: $server"
    ssh $server "uptime"
done < servers.txt
```

#### Infinite loop with break condition

```bash
while true
do
    echo "Checking system status..."
    if [ $(df -h | grep /dev/sda1 | awk '{print $5}' | tr -d '%') -gt 90 ]; then
        echo "Disk space critical! Alerting admin..."
        break
    fi
    sleep 300
done
```

## Until Loops

The `until` loop is similar to `while` but continues until the condition becomes true.

### Basic Syntax

```bash
until [ condition ]
do
    # commands to execute
done
```

### Example

```bash
count=1
until [ $count -gt 5 ]
do
    echo "Count: $count"
    ((count++))
done
```

## Loop Control

### Break Statement

The `break` statement exits the loop immediately.

```bash
for i in {1..10}
do
    if [ $i -eq 5 ]
    then
        echo "Breaking at 5"
        break
    fi
    echo "Number: $i"
done
```

### Continue Statement

The `continue` statement skips the current iteration and continues with the next.

```bash
for i in {1..10}
do
    if [ $i -eq 5 ]
    then
        echo "Skipping 5"
        continue
    fi
    echo "Number: $i"
done
```

## Practical DevOps Examples

### 1. Batch Server Management

```bash
# servers.txt contains a list of server hostnames or IPs
while read -r server
do
    echo "=== Managing server: $server ==="
    ssh $server "uptime && df -h && free -m"
    echo "Updating packages on $server..."
    ssh $server "sudo apt update && sudo apt upgrade -y"
done < servers.txt
```

### 2. Log File Analysis

```bash
for logfile in /var/log/*.log
do
    echo "=== Analyzing $logfile ==="
    echo "Top 5 IP addresses in $logfile:"
    grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" $logfile | sort | uniq -c | sort -nr | head -5
    
    echo "Error count in $logfile:"
    grep -c "ERROR" $logfile
done
```

### 3. Docker Container Monitoring

```bash
while true
do
    echo "=== Container Status $(date) ==="
    docker ps --format "{{.Names}}: {{.Status}}"
    
    # Check for containers using high CPU
    high_cpu=$(docker stats --no-stream --format "{{.Name}}: {{.CPUPerc}}" | grep -E "[0-9]{2,3}\.[0-9]{2}%")
    
    if [ ! -z "$high_cpu" ]
    then
        echo "WARNING: High CPU detected:"
        echo "$high_cpu"
    fi
    
    sleep 60
done
```

### 4. Backup Script

```bash
# Define directories to backup
backup_dirs=("/etc" "/home/user/documents" "/var/www")
backup_dest="/backup/$(date +%Y%m%d)"

# Create destination directory
mkdir -p $backup_dest

# Backup each directory
for dir in "${backup_dirs[@]}"
do
    dir_name=$(basename $dir)
    echo "Backing up $dir to $backup_dest/$dir_name.tar.gz"
    tar -czf "$backup_dest/$dir_name.tar.gz" $dir
    
    # Verify backup was successful
    if [ $? -eq 0 ]
    then
        echo "✓ Backup of $dir completed successfully"
    else
        echo "✗ Backup of $dir failed!"
    fi
done

# Cleanup old backups (older than 7 days)
find /backup -type d -mtime +7 -exec rm -rf {} \;
```

### 5. Automated Service Restart

```bash
services=("nginx" "postgresql" "redis-server")

for service in "${services[@]}"
do
    echo "Checking status of $service..."
    if ! systemctl is-active --quiet $service
    then
        echo "Service $service is down. Attempting to restart..."
        systemctl restart $service
        
        # Wait for service to start
        sleep 5
        
        # Verify service was restarted
        if systemctl is-active --quiet $service
        then
            echo "✓ Successfully restarted $service"
        else
            echo "✗ Failed to restart $service! Alerting admin..."
            # Send alert (email, Slack, etc.)
        fi
    else
        echo "✓ Service $service is running properly"
    fi
done
```

## Best Practices

1. **Always quote variables** to handle spaces and special characters:
   ```bash
   for file in "$directory"/*
   ```

2. **Use appropriate file reading techniques** - `while read` is generally better than `for line in $(cat file)`.

3. **Set timeouts** for operations that might hang:
   ```bash
   timeout 5s command
   ```

4. **Add error handling** to your loops:
   ```bash
   for server in $(cat servers.txt); do
       ssh $server "command" || echo "Failed on $server"
   done
   ```

5. **Control resource usage** in infinite loops:
   ```bash
   while true; do
       # Do work
       sleep 1  # Prevent CPU hogging
   done
   ```