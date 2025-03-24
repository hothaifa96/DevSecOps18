# Bash Scripting: Command Line Arguments

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Command Line Arguments](#basic-command-line-arguments)
   - [Positional Parameters](#positional-parameters)
   - [Special Parameters](#special-parameters)
   - [Accessing Arguments](#accessing-arguments)
3. [Argument Parsing Techniques](#argument-parsing-techniques)
   - [Simple Argument Parsing](#simple-argument-parsing)



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
