# Simple DevOps Bash Loop Lab Exercises

## Lab 1: Service Status Checker

### Objective
Create a script that checks the status of multiple services on a server and reports their status.

### Instructions
1. Create a bash script that loops through a list of common services (nginx, apache2, mysql, ssh, etc.)
2. Check if each service is running using `systemctl status` or equivalent
3. Display the status (RUNNING/STOPPED) for each service
4. Create a summary count of running and stopped services

### Example Output
```
===== SERVICE STATUS CHECKER =====

Checking nginx............. RUNNING
Checking apache2........... STOPPED
Checking mysql............. RUNNING
Checking ssh............... RUNNING
Checking redis-server...... STOPPED
Checking mongodb........... RUNNING

===== SUMMARY =====
Total services checked: 6
Running: 4
Stopped: 2
```

## Lab 2: Log File Parser

### Objective
Create a script that scans a log file for ERROR entries and displays a summary.

### Instructions
1. Create a bash script that reads a log file line by line
2. Count the occurrences of different error types (ERROR, WARNING, INFO)
3. Extract and list the 5 most recent ERROR messages
4. Display a summary of findings

### Example Output
```
===== LOG FILE ANALYSIS =====
Log file: /var/log/application.log

Message Count:
- ERROR: 12
- WARNING: 45
- INFO: 237

Last 5 ERROR messages:
[2025-03-11 12:34:56] ERROR: Database connection failed
[2025-03-11 10:23:45] ERROR: API request timeout
[2025-03-11 09:12:34] ERROR: Invalid authentication token
[2025-03-10 18:45:23] ERROR: Configuration file not found
[2025-03-10 15:23:10] ERROR: Out of memory exception

Analysis completed in 0.8 seconds
```

## Lab 3: Disk Space Monitor

### Objective
Create a script that monitors disk space usage across multiple filesystems and alerts if usage exceeds thresholds.

### Instructions
1. Create a bash script that gets disk space information using `df`
2. Loop through each filesystem
3. Check if usage exceeds warning (70%) or critical (90%) thresholds
4. Display formatted output with appropriate warnings

### Example Output
```
===== DISK SPACE MONITOR =====
Date: Tue Mar 11 16:30:22 EDT 2025

Filesystem          Size    Used    Avail   Usage   Status
/dev/sda1           50G     15G     35G     30%     OK
/dev/sda2           100G    85G     15G     85%     WARNING
/dev/sda3           500G    120G    380G    24%     OK
/dev/sda4           1T      950G    50G     95%     CRITICAL

SUMMARY: 1 critical, 1 warning, 2 ok
Action required for /dev/sda4 - Critical space shortage!
```

## Lab 4: File Backup Script

### Objective
Create a script that backs up config files to a timestamped directory.

### Instructions
1. Create a bash script that creates a timestamped backup directory
2. Loop through a list of important configuration files/directories
3. Create a backup of each file/directory
4. Verify the backup was successful
5. Generate a backup report

### Example Output
```
===== BACKUP SCRIPT =====
Date: Tue Mar 11 17:15:45 EDT 2025
Backup location: /backups/20250311_171545/

Backing up configuration files:
- /etc/nginx/nginx.conf .......... SUCCESS
- /etc/apache2/apache2.conf ...... SUCCESS
- /etc/mysql/my.cnf .............. SUCCESS
- /etc/ssh/sshd_config ........... SUCCESS
- /var/www/html .................. SUCCESS
- /opt/application/config.json ... FAILED (File not found)

Backup Summary:
- Total files attempted: 6
- Successfully backed up: 5
- Failed: 1

Backup completed in 3.4 seconds
Backup size: 24.8 MB
```