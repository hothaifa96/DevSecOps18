# Bash Date Command Guide

The `date` command in Bash is a powerful tool for working with dates and times. It can display the current date and time, format dates in different ways, perform date calculations, and convert between different date formats.

## Table of Contents
- [Basic Usage](#basic-usage)
- [Date Formatting Options](#date-formatting-options)
- [Setting Dates](#setting-dates)
- [Date Calculations](#date-calculations)
- [Working with Timestamps](#working-with-timestamps)
- [Time Zones](#time-zones)
- [Parsing Dates](#parsing-dates)
- [Practical Examples](#practical-examples)

## Basic Usage

### Display Current Date and Time
```bash
date
# Output example: Tue Mar 11 14:23:45 EDT 2025
```

### Custom Format
```bash
date "+%Y-%m-%d %H:%M:%S"
# Output example: 2025-03-11 14:23:45
```

## Date Formatting Options

The `date` command uses format specifiers that start with `%`:

### Common Format Specifiers

| Specifier | Description | Example Output |
|-----------|-------------|----------------|
| `%a` | Abbreviated weekday name | Mon, Tue, ... |
| `%A` | Full weekday name | Monday, Tuesday, ... |
| `%b` | Abbreviated month name | Jan, Feb, ... |
| `%B` | Full month name | January, February, ... |
| `%d` | Day of month (01-31) | 01, 02, ..., 31 |
| `%D` | Date in MM/DD/YY format | 03/11/25 |
| `%e` | Day of month (1-31), space-padded | 1, 2, ..., 31 |
| `%F` | Date in YYYY-MM-DD format | 2025-03-11 |
| `%H` | Hour (00-23) | 00, 01, ..., 23 |
| `%I` | Hour (01-12) | 01, 02, ..., 12 |
| `%j` | Day of year (001-366) | 001, 002, ..., 366 |
| `%m` | Month (01-12) | 01, 02, ..., 12 |
| `%M` | Minute (00-59) | 00, 01, ..., 59 |
| `%p` | AM or PM | AM, PM |
| `%r` | 12-hour clock time (hh:mm:ss AM/PM) | 02:55:02 PM |
| `%R` | 24-hour hour and minute (HH:MM) | 14:55 |
| `%S` | Second (00-60) | 00, 01, ..., 60 |
| `%T` | 24-hour time (HH:MM:SS) | 14:55:02 |
| `%u` | Day of week (1-7, 1=Monday) | 1, 2, ..., 7 |
| `%U` | Week number (00-53, Sunday as first day) | 00, 01, ..., 53 |
| `%V` | ISO week number (01-53) | 01, 02, ..., 53 |
| `%w` | Day of week (0-6, 0=Sunday) | 0, 1, ..., 6 |
| `%W` | Week number (00-53, Monday as first day) | 00, 01, ..., 53 |
| `%x` | Locale's date representation | 03/11/25 |
| `%X` | Locale's time representation | 14:55:02 |
| `%y` | Year, last two digits (00-99) | 00, 01, ..., 99 |
| `%Y` | Year in 4-digit format | 2025 |
| `%z` | Timezone offset | -0400, +0530 |
| `%Z` | Timezone abbreviation | EDT, UTC, ... |

### Format Examples

```bash
# ISO 8601 date format (YYYY-MM-DD)
date +%F
# Output: 2025-03-11

# Custom date and time format
date "+Date: %Y-%m-%d | Time: %H:%M:%S"
# Output: Date: 2025-03-11 | Time: 14:55:02

# Day name and day of year
date "+Today is %A, day %j of the year %Y"
# Output: Today is Tuesday, day 070 of the year 2025

# Format for filenames
date "+backup_%Y%m%d_%H%M%S.tar.gz"
# Output: backup_20250311_145502.tar.gz

# RFC 3339 format (for logs)
date --rfc-3339=seconds
# Output: 2025-03-11 14:55:02-04:00
```

## Setting Dates

### Set System Date and Time (requires root privileges)
```bash
sudo date --set="2025-03-11 15:30:00"
```

### Set Date Without Changing System Time (for testing)
```bash
date -d "2025-03-11 15:30:00"
# Output: Tue Mar 11 15:30:00 EDT 2025
```

## Date Calculations

The `-d` or `--date` option allows you to perform date calculations:

```bash
# Tomorrow's date
date -d "tomorrow" +%F
# Output: 2025-03-12

# Yesterday's date
date -d "yesterday" +%F
# Output: 2025-03-10

# Next month
date -d "next month" +%F
# Output: 2025-04-11

# Last week
date -d "last week" +%F
# Output: 2025-03-04
```

### Adding or Subtracting Time Periods

```bash
# 3 days from now
date -d "+3 days" +%F
# Output: 2025-03-14

# 2 weeks ago
date -d "-2 weeks" +%F
# Output: 2025-02-25

# 1 year and 3 months from now
date -d "+1 year +3 months" +%F
# Output: 2026-06-11

# 6 hours from now
date -d "+6 hours" +%T
# Output: 20:55:02
```

### Specific Day Calculation

```bash
# Next Friday
date -d "next friday" +%F
# Output depends on current date

# First day of next month
date -d "next month" +%Y-%m-01
# Output: 2025-04-01

# Last day of current month
date -d "$(date +%Y-%m-01) +1 month -1 day" +%F
# Output depends on current month
```

## Working with Timestamps

### Convert Date to Unix Timestamp
```bash
# Current time as Unix timestamp
date +%s
# Output example: 1741874102

# Specific date to Unix timestamp
date -d "2025-03-11 15:00:00" +%s
# Output example: 1741875600
```

### Convert Unix Timestamp to Date
```bash
# Convert Unix timestamp to date
date -d @1741875600
# Output: Tue Mar 11 15:00:00 EDT 2025

# Format the converted date
date -d @1741875600 +"%Y-%m-%d %H:%M:%S"
# Output: 2025-03-11 15:00:00
```

## Time Zones

### Display Time in a Different Time Zone
```bash
# Set timezone using the TZ environment variable
TZ="UTC" date
# Output: Tue Mar 11 18:55:02 UTC 2025

# Other timezone examples
TZ="America/Los_Angeles" date
# Output: Tue Mar 11 10:55:02 PDT 2025

TZ="Asia/Tokyo" date
# Output: Wed Mar 12 02:55:02 JST 2025

# Format with timezone indication
TZ="Europe/London" date "+%F %T %Z"
# Output: 2025-03-11 18:55:02 GMT
```

### List Available Time Zones
```bash
# List all available time zones
ls /usr/share/zoneinfo/

# List time zones for a region
ls /usr/share/zoneinfo/Europe/
```

## Parsing Dates

### Parse Various Date Formats
```bash
# ISO 8601 format
date -d "2025-03-11T15:30:45" +%s
# Output: 1741877445

# US format (MM/DD/YYYY)
date -d "03/11/2025 15:30:45" +%s
# Output: 1741877445

# Text description
date -d "March 11, 2025 15:30:45" +%s
# Output: 1741877445
```

## Practical Examples

### 1. Create Timestamped Backups

```bash
#!/bin/bash

# Create a backup with timestamp
backup_dir="/var/backups"
timestamp=$(date +%Y%m%d_%H%M%S)
backup_file="${backup_dir}/backup_${timestamp}.tar.gz"

# Create the backup
tar -czf "$backup_file" /path/to/data

echo "Backup created: $backup_file"
```

### 2. Log with Timestamps

```bash
#!/bin/bash

log_file="application.log"

log_message() {
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] $1" >> "$log_file"
}

log_message "Application started"
sleep 2
log_message "Processing data..."
sleep 1
log_message "Application finished"
```

### 3. Calculate Time Difference

```bash
#!/bin/bash

# Record start time
start_time=$(date +%s)

# Do something time-consuming
sleep 5

# Record end time
end_time=$(date +%s)

# Calculate elapsed time
elapsed=$((end_time - start_time))

echo "Operation took $elapsed seconds"

# Format elapsed time if it's longer
if ((elapsed > 60)); then
    minutes=$((elapsed / 60))
    seconds=$((elapsed % 60))
    echo "That's $minutes minutes and $seconds seconds"
fi
```

### 4. Check If File is Older Than X Days

```bash
#!/bin/bash

file="/path/to/file.txt"
days_threshold=30

# Get file's last modification date in seconds since epoch
file_time=$(stat -c %Y "$file")

# Get current time minus threshold in seconds
threshold_time=$(date -d "-$days_threshold days" +%s)

if ((file_time < threshold_time)); then
    echo "File $file is older than $days_threshold days"
    echo "Last modified: $(date -d @$file_time '+%Y-%m-%d %H:%M:%S')"
else
    echo "File $file is less than $days_threshold days old"
fi
```

### 5. Create Date-Based Directory Structure

```bash
#!/bin/bash

# Create year/month/day directory structure
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)

backup_path="/backups/$year/$month/$day"

# Create directory if it doesn't exist
mkdir -p "$backup_path"

echo "Created directory structure: $backup_path"
```

### 6. Run Task on Specific Day of Week

```bash
#!/bin/bash

# Run weekly maintenance task on Sunday
day_of_week=$(date +%u)  # 1-7, where 1 is Monday

if ((day_of_week == 7)); then  # Sunday
    echo "Running weekly maintenance task on $(date +%A)"
    # Run task...
else
    echo "Today is $(date +%A), skipping weekly task"
fi
```

### 7. Get First and Last Day of Month

```bash
#!/bin/bash

# Get first day of current month
first_day=$(date +%Y-%m-01)
echo "First day of month: $first_day"

# Get last day of current month
last_day=$(date -d "$(date +%Y-%m-01) +1 month -1 day" +%Y-%m-%d)
echo "Last day of month: $last_day"

# Get first and last day of next month
next_month_first=$(date -d "$(date +%Y-%m-01) +1 month" +%Y-%m-%d)
echo "First day of next month: $next_month_first"

next_month_last=$(date -d "$(date +%Y-%m-01) +2 months -1 day" +%Y-%m-%d)
echo "Last day of next month: $next_month_last"
```

### 8. Generate a Date Range

```bash
#!/bin/bash

# Generate dates between start and end date
start_date="2025-03-01"
end_date="2025-03-10"

current_date="$start_date"

while [[ "$current_date" <= "$end_date" ]]; do
    echo "$current_date"
    current_date=$(date -d "$current_date +1 day" +%Y-%m-%d)
done
```

### 9. Schedule a Future Task

```bash
#!/bin/bash

# Schedule a task to run 5 minutes from now
run_at=$(date -d "+5 minutes" +"%H:%M")
echo "Task scheduled to run at $run_at"

# Create an at job
echo "echo 'Scheduled task running' >> /tmp/scheduled_task.log" | at $run_at
```

### 10. Find Files Modified in Last 24 Hours

```bash
#!/bin/bash

# Find files modified in the last 24 hours
find /path/to/search -type f -mtime -1 | while read file; do
    mod_time=$(stat -c "%y" "$file" | cut -d. -f1)
    echo "[$mod_time] $file"
done
```

## Best Practices

1. **Always quote format strings** to prevent shell interpretation:
   ```bash
   date "+%Y-%m-%d %H:%M:%S"  # Good
   ```

2. **Use ISO 8601 format** for machine-readable dates:
   ```bash
   date -I  # Same as date +%F
   date --rfc-3339=seconds  # More precise with timezone
   ```

3. **Use %F for dates and %T for times** as shortcuts for common formats:
   ```bash
   date +%F  # Same as +%Y-%m-%d
   date +%T  # Same as +%H:%M:%S
   ```

4. **Consider timezone effects** when scheduling or comparing dates:
   ```bash
   TZ="UTC" date  # Use UTC for consistency
   ```

5. **Handle leap years and daylight saving time** by using date's built-in calculation:
   ```bash
   # Don't calculate days manually for date differences
   date -d "2024-02-29 +1 year" +%F  # Handles leap year correctly
   ```

6. **Format timestamps in logs consistently** for easier parsing:
   ```bash
   # ISO 8601 with timezone is ideal for logs
   log_timestamp=$(date --rfc-3339=seconds)
   ```

7. **Use seconds since epoch for calculations** to avoid timezone and DST issues:
   ```bash
   date_diff=$(($(date -d "tomorrow" +%s) - $(date +%s)))
   echo "Seconds until tomorrow: $date_diff"
   ```