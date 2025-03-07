# Basic Linux Commands Tutorial for DevOps

## Table of Contents

1. [Introduction](#introduction)
2. [System Information Commands](#system-information-commands)
   - [uname](#uname)
   - [ps](#ps)
   - [lsof](#lsof)
3. [Package Management](#package-management)
   - [apt](#apt)
   - [apk](#apk)
4. [Network Utilities](#network-utilities)
   - [curl](#curl)
   - [ping](#ping)
   - [traceroute](#traceroute)
5. [Process Management](#process-management)
   - [kill](#kill)
6. [Help System](#help-system)
   - [man](#man)

## Introduction

Understanding basic Linux commands is essential for any DevOps engineer. These commands form the foundation for system administration, troubleshooting, and automation in Linux environments. This tutorial covers the fundamental commands that every DevOps professional should know.

## System Information Commands

### uname

The `uname` command displays system information including kernel name, network node hostname, kernel release, kernel version, machine hardware name, and operating system.

**Basic Usage:**
```bash
uname
```

**Common Options:**
- `-a`: Print all information
- `-s`: Print the kernel name
- `-n`: Print the network node hostname
- `-r`: Print the kernel release
- `-v`: Print the kernel version
- `-m`: Print the machine hardware name
- `-o`: Print the operating system

**Examples:**
```bash
# Display all system information
uname -a

# Display only the kernel version
uname -v

# Display only the machine hardware name
uname -m
```

**Use Cases:**
- Identifying the operating system and kernel version
- Checking system architecture for compatibility with software
- Troubleshooting system-specific issues

### ps

The `ps` command displays information about active processes running on the system.

**Basic Usage:**
```bash
ps
```

**Common Options:**
- `aux`: Display all processes for all users
- `-ef`: Full listing with full-format listing
- `-u [username]`: Display processes for a specific user
- `--sort=[+|-]key`: Sort output by key (e.g., -pcpu for CPU usage)

**Examples:**
```bash
# Display all processes with detailed information
ps aux

# Display all processes in a full format
ps -ef

# Display processes sorted by memory usage (descending)
ps aux --sort=-pmem

# Display processes for a specific user
ps -u username
```

**Use Cases:**
- Monitoring system processes
- Identifying resource-intensive processes
- Troubleshooting application issues
- Finding process IDs for management operations

### lsof

The `lsof` (List Open Files) command displays information about files opened by processes.

**Basic Usage:**
```bash
lsof
```

**Common Options:**
- `-i`: Display Internet connections
- `-p [PID]`: List files opened by a specific process ID
- `-u [user]`: List files opened by a specific user
- `-c [command]`: List files opened by a command
- `-t`: Display only process IDs

**Examples:**
```bash
# List all network connections
lsof -i

# List files opened by a specific process ID
lsof -p 1234

# List all network connections on a specific port
lsof -i :80

# List all files opened by a specific user
lsof -u username

# List all files opened by a specific command
lsof -c nginx
```

**Use Cases:**
- Identifying which processes have files or ports open
- Troubleshooting file locking issues
- Checking network connections and bound ports
- Diagnosing "file in use" errors

## Package Management

### apt

The `apt` (Advanced Package Tool) command is used for package management on Debian-based distributions like Ubuntu.

**Basic Usage:**
```bash
apt [options] [command] [package(s)]
```

**Common Commands:**
- `update`: Update package lists
- `upgrade`: Upgrade installed packages
- `install`: Install new packages
- `remove`: Remove packages
- `autoremove`: Remove automatically installed packages no longer needed
- `search`: Search for packages
- `show`: Show package details

**Examples:**
```bash
# Update package lists
sudo apt update

# Upgrade all installed packages
sudo apt upgrade

# Install a package
sudo apt install nginx

# Remove a package
sudo apt remove nginx

# Search for packages
apt search python3

# Show package information
apt show nginx
```

**Use Cases:**
- Installing and updating software
- Managing system dependencies
- Keeping the system up to date
- Cleaning up unused packages

### apk

The `apk` command is the package manager for Alpine Linux, commonly used in Docker containers.

**Basic Usage:**
```bash
apk [options] [command] [package(s)]
```

**Common Commands:**
- `add`: Install packages
- `del`: Remove packages
- `update`: Update package lists
- `upgrade`: Upgrade installed packages
- `search`: Search for packages
- `info`: Show package information

**Examples:**
```bash
# Update package lists
apk update

# Install a package
apk add nginx

# Remove a package
apk del nginx

# Search for packages
apk search python3

# Show package information
apk info nginx

# Upgrade all installed packages
apk upgrade
```

**Use Cases:**
- Managing packages in Alpine Linux environments
- Keeping Docker containers up to date
- Minimizing container size by controlling package installation

## Network Utilities

### curl

The `curl` command is a tool for transferring data from or to a server using various protocols (HTTP, HTTPS, FTP, etc.).

**Basic Usage:**
```bash
curl [options] [URL]
```

**Common Options:**
- `-O`: Save output to a file with the same name as remote
- `-o [filename]`: Save output to a specified file
- `-I` or `--head`: Fetch HTTP headers only
- `-X [METHOD]`: Specify HTTP method (GET, POST, PUT, DELETE)
- `-H [header]`: Specify HTTP headers
- `-d [data]`: Send data in POST request
- `-u [user:password]`: Specify username and password for authentication
- `-k`: Allow insecure SSL connections
- `-v`: Verbose output

**Examples:**
```bash
# Download a webpage and display in terminal
curl https://example.com

# Download a file and save it
curl -O https://example.com/file.zip

# Download a file and save it with a different name
curl -o myfile.zip https://example.com/file.zip

# Get HTTP headers only
curl -I https://example.com

# Send a POST request with data
curl -X POST -d "name=John&age=25" https://example.com/api

# Send a request with custom headers
curl -H "Content-Type: application/json" -H "Authorization: Bearer token123" https://api.example.com

# Download with basic authentication
curl -u username:password https://example.com/secure
```

**Use Cases:**
- Testing APIs and web services
- Downloading files
- Debugging HTTP requests
- Automating web interactions
- Checking server responses and headers

### ping

The `ping` command tests the reachability of a host on an IP network and measures round-trip time.

**Basic Usage:**
```bash
ping [options] host
```

**Common Options:**
- `-c [count]`: Stop after sending a specified number of packets
- `-i [interval]`: Wait the specified number of seconds between pings
- `-w [deadline]`: Exit after the specified number of seconds
- `-s [packetsize]`: Specify the number of data bytes to be sent

**Examples:**
```bash
# Basic ping to a host
ping google.com

# Send only 5 ping packets
ping -c 5 google.com

# Set interval between pings to 2 seconds
ping -i 2 google.com

# Set packet size to 1000 bytes
ping -s 1000 google.com

# Set deadline to 10 seconds
ping -w 10 google.com
```

**Use Cases:**
- Testing network connectivity
- Checking if a server is up
- Measuring network latency
- Diagnosing network issues

### traceroute

The `traceroute` command displays the route packets take to a network host, showing all the intermediate hops.

**Basic Usage:**
```bash
traceroute [options] host
```

**Common Options:**
- `-n`: Do not resolve IP addresses to hostnames
- `-w [seconds]`: Wait time for response
- `-m [max_ttl]`: Set maximum time-to-live (number of hops)
- `-p [port]`: Use specified port for UDP packets

**Examples:**
```bash
# Basic traceroute to a host
traceroute google.com

# Don't resolve hostnames (faster)
traceroute -n google.com

# Set maximum hops to 15
traceroute -m 15 google.com

# Set timeout to 2 seconds
traceroute -w 2 google.com
```

**Use Cases:**
- Identifying network bottlenecks
- Diagnosing routing problems
- Understanding network topology
- Troubleshooting high latency issues

## Process Management

### kill

The `kill` command sends a signal to a process, most commonly used to terminate processes.

**Basic Usage:**
```bash
kill [options] PID
```

**Common Options:**
- `-9` or `-SIGKILL`: Force kill a process
- `-15` or `-SIGTERM`: Gracefully terminate a process (default)
- `-l`: List all available signals

**Examples:**
```bash
# Terminate a process gracefully
kill 1234

# Force kill a process
kill -9 1234

# List all available signals
kill -l

# Kill multiple processes
kill 1234 5678 9012

# Send a specific signal
kill -SIGHUP 1234
```

**Common Signals:**
- `SIGTERM (15)`: Terminate process gracefully (default)
- `SIGKILL (9)`: Force kill process (cannot be caught or ignored)
- `SIGHUP (1)`: Hangup detected, often used to reload configuration
- `SIGINT (2)`: Interrupt from keyboard (Ctrl+C)
- `SIGSTOP (19)`: Stop the process (cannot be caught or ignored)
- `SIGCONT (18)`: Continue a stopped process

**Use Cases:**
- Terminating unresponsive applications
- Restarting services
- Forcing processes to release resources
- Managing process lifecycles

## Help System

### man

The `man` (manual) command displays the user manual for any command.

**Basic Usage:**
```bash
man [options] [section] command
```

**Common Options:**
- `-k [keyword]`: Search for commands related to a keyword
- `-f [command]`: Display only the description of a command
- `[section]`: Specify the section of the manual (1-9)

**Examples:**
```bash
# View the manual for the ls command
man ls

# Search for commands related to files
man -k file

# Display the description for grep
man -f grep

# View a specific section of the manual for a command
man 5 passwd
```

**Manual Sections:**
1. User commands (executable programs or shell commands)
2. System calls (functions provided by the kernel)
3. Library calls (functions within libraries)
4. Special files (usually found in /dev)
5. File formats and conventions
6. Games
7. Miscellaneous
8. System administration commands (usually for root)
9. Kernel routines

**Use Cases:**
- Learning how to use unfamiliar commands
- Understanding command options and syntax
- Finding commands for specific tasks
- Exploring system functionality