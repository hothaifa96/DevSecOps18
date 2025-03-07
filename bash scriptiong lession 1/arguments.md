# Bash Scripting: Command Line Arguments

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Command Line Arguments](#basic-command-line-arguments)
   - [Positional Parameters](#positional-parameters)
   - [Special Parameters](#special-parameters)
   - [Accessing Arguments](#accessing-arguments)
3. [Argument Parsing Techniques](#argument-parsing-techniques)
   - [Simple Argument Parsing](#simple-argument-parsing)
   - [Using getopts](#using-getopts)
   - [Manual Argument Parsing](#manual-argument-parsing)



## Introduction

Command line arguments allow users to pass information to a script when they execute it. They enable scripts to be more flexible and reusable by accepting parameters that customize their behavior. This tutorial explains how to work with command line arguments in Bash scripts, from basic usage to advanced techniques.

## Basic Command Line Arguments

### Positional Parameters

In Bash, command line arguments are stored in special variables called positional parameters:

- `$0` - The name of the script itself
- `$1` - The first argument
- `$2` - The second argument
- `$3` - The third argument
- And so on...

### Special Parameters

Bash also provides special parameters for working with all arguments:

- `$#` - The number of arguments passed to the script
- `$@` - All arguments as separate strings: `"$1" "$2" "$3" ...`
- `$*` - All arguments as a single string: `"$1 $2 $3 ..."`
- `$$` - The process ID (PID) of the script
- `$?` - The exit status of the last command
- `$!` - The process ID of the last background command

### Accessing Arguments

Here's a simple script that demonstrates how to access command line arguments:

```bash
#!/bin/bash

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: $3"
echo "Number of arguments: $#"
echo "All arguments: $@"
```

If you save this as `args.sh` and run it with `./args.sh apple banana cherry`, the output would be:

```
Script name: ./args.sh
First argument: apple
Second argument: banana
Third argument: cherry
Number of arguments: 3
All arguments: apple banana cherry
```

## Argument Parsing Techniques

### Simple Argument Parsing

For scripts with a few fixed positional arguments, you can use direct parameter references:

```bash
#!/bin/bash

# Check if required arguments are provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 <source_file> <destination_file>"
    exit 1
fi

source_file="$1"
destination_file="$2"

echo "Copying from $source_file to $destination_file"
cp "$source_file" "$destination_file"
```

### Using getopts

For scripts with optional flags and arguments, the `getopts` built-in command provides structured option parsing:

```bash
#!/bin/bash

# Default values
verbose=0
output_file=""

# Parse options
while getopts ":vo:h" opt; do
    case $opt in
        v)
            verbose=1
            ;;
        o)
            output_file="$OPTARG"
            ;;
        h)
            echo "Usage: $0 [-v] [-o output_file] [-h] input_file"
            echo "  -v             Enable verbose mode"
            echo "  -o output_file Specify output file"
            echo "  -h             Display this help message"
            exit 0
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
            ;;
    esac
done

# Shift to remaining arguments (non-options)
shift $((OPTIND-1))

# Check for input file
if [ $# -lt 1 ]; then
    echo "Error: Input file is required."
    echo "Usage: $0 [-v] [-o output_file] [-h] input_file"
    exit 1
fi

input_file="$1"

# Display parsed information
echo "Input file: $input_file"
echo "Output file: ${output_file:-"(standard output)"}"
echo "Verbose mode: $([[ $verbose -eq 1 ]] && echo "enabled" || echo "disabled")"

# Process the file
if [ $verbose -eq 1 ]; then
    echo "Processing file $input_file..."
fi

if [ -n "$output_file" ]; then
    cat "$input_file" > "$output_file"
    echo "Results written to $output_file"
else
    cat "$input_file"
fi
```

This script accepts:
- `-v` flag for verbose output
- `-o filename` to specify an output file
- `-h` flag to display help
- A required input file as the last argument

### Manual Argument Parsing

For more complex argument patterns, you can implement custom parsing:

```bash
#!/bin/bash

# Initialize variables
source=""
destination=""
recursive=0
verbose=0
dry_run=0

# Function to display usage
usage() {
    echo "Usage: $0 [OPTIONS] --source SOURCE --destination DEST"
    echo "Options:"
    echo "  --source SOURCE       Source directory"
    echo "  --destination DEST    Destination directory"
    echo "  --recursive           Copy directories recursively"
    echo "  --verbose             Display detailed progress"
    echo "  --dry-run             Show what would be done without doing it"
    echo "  --help                Display this help message"
    exit 1
}

# Parse arguments
while [ $# -gt 0 ]; do
    case "$1" in
        --source)
            source="$2"
            shift 2
            ;;
        --destination)
            destination="$2"
            shift 2
            ;;
        --recursive)
            recursive=1
            shift
            ;;
        --verbose)
            verbose=1
            shift
            ;;
        --dry-run)
            dry_run=1
            shift
            ;;
        --help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

# Validate required arguments
if [ -z "$source" ] || [ -z "$destination" ]; then
    echo "Error: Source and destination directories are required."
    usage
fi

# Display configuration
echo "Configuration:"
echo "  Source: $source"
echo "  Destination: $destination"
echo "  Recursive: $([[ $recursive -eq 1 ]] && echo "Yes" || echo "No")"
echo "  Verbose: $([[ $verbose -eq 1 ]] && echo "Yes" || echo "No")"
echo "  Dry run: $([[ $dry_run -eq 1 ]] && echo "Yes" || echo "No")"

# Build the copy command
cmd="cp"
if [ $recursive -eq 1 ]; then
    cmd="$cmd -r"
fi
if [ $verbose -eq 1 ]; then
    cmd="$cmd -v"
fi

# Execute or simulate
if [ $dry_run -eq 1 ]; then
    echo "Would execute: $cmd \"$source\" \"$destination\""
else
    eval "$cmd \"$source\" \"$destination\""
fi
```

