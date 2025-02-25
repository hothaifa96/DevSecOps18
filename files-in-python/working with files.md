# Working with Files in Python

Python makes file operations straightforward with its built-in functions and libraries. This tutorial covers essential file operations you'll need for most projects.

## Basic File Operations

### Opening and Closing Files

```python
# Opening a file
file = open('example.txt', 'r')  # 'r' for read mode

# Always close files when done
file.close()

# Better approach using with statement (automatically closes file)
with open('example.txt', 'r') as file:
    # Operations with the file
    content = file.read()
```

### Common File Modes

- `'r'` - Read (default)
- `'w'` - Write (creates new file or truncates existing)
- `'a'` - Append (adds to end of file)
- `'r+'` - Read and write
- `'b'` - Binary mode (add to other modes, e.g., `'rb'`)

## Reading Files

```python
# Read entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Read all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
```

## Writing Files

```python
# Write to a file (overwrites existing content)
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.')

# Append to a file
with open('output.txt', 'a') as file:
    file.write('\nThis line is appended.')
```

## Working with CSV Files

```python
import csv

# Reading CSV
with open('data.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

# Writing CSV
data = [
    ['Name', 'Age', 'Country'],
    ['Alice', '25', 'USA'],
    ['Bob', '30', 'Canada']
]
with open('new_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Using DictReader and DictWriter
with open('data.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old from {row['Country']}")

# Writing with DictWriter
data = [
    {'Name': 'Charlie', 'Age': '35', 'Country': 'UK'},
    {'Name': 'Diana', 'Age': '28', 'Country': 'Australia'}
]
with open('dict_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'Country']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

## Working with JSON Files

```python
import json

# Reading JSON
with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data)

# Writing JSON
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'languages': ['Python', 'JavaScript', 'Java']
}
with open('new_data.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Pretty printing JSON
print(json.dumps(data, indent=4, sort_keys=True))
```

## File and Directory Management

```python
import os
import shutil

# Check if file exists
if os.path.exists('example.txt'):
    print('File exists')

# Get file information
file_size = os.path.getsize('example.txt')
modified_time = os.path.getmtime('example.txt')

# List directory contents
files = os.listdir('.')
print(files)

# Create a directory
os.mkdir('new_directory')

# Create nested directories
os.makedirs('parent/child/grandchild', exist_ok=True)

# Copy a file
shutil.copy('source.txt', 'destination.txt')

# Copy a directory and its contents
shutil.copytree('source_dir', 'destination_dir')

# Move/rename a file
os.rename('old_name.txt', 'new_name.txt')

# Delete a file
os.remove('unwanted.txt')

# Delete an empty directory
os.rmdir('empty_directory')

# Delete a directory and all its contents
shutil.rmtree('directory_to_delete')
```

## Error Handling for File Operations

```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File does not exist')
except PermissionError:
    print('No permission to read file')
except Exception as e:
    print(f'An error occurred: {e}')
```

## Working with Binary Files

```python
# Reading binary files
with open('image.jpg', 'rb') as file:
    binary_data = file.read()

# Writing binary files
with open('copy.jpg', 'wb') as file:
    file.write(binary_data)
```

## Working with Paths

```python
import os.path

# Join path components
full_path = os.path.join('directory', 'subdirectory', 'file.txt')

# Get file parts
dirname = os.path.dirname(full_path)
filename = os.path.basename(full_path)
name, ext = os.path.splitext(filename)

# Get absolute path
abs_path = os.path.abspath('relative/path/file.txt')

# Check if path is a file or directory
is_file = os.path.isfile('path')
is_dir = os.path.isdir('path')
```

## Path Operations with Pathlib (Modern Approach)

```python
from pathlib import Path

# Create a Path object
path = Path('directory/file.txt')

# Join paths
new_path = Path('directory') / 'subdirectory' / 'file.txt'

# Get parent directory
parent = path.parent

# Get filename
filename = path.name

# Get stem and suffix
stem = path.stem  # filename without extension
suffix = path.suffix  # extension with dot

# Check if exists
exists = path.exists()

# Create directories
Path('new/nested/directory').mkdir(parents=True, exist_ok=True)

# List directory contents
for file in Path('directory').iterdir():
    print(file)

# Find files by pattern
python_files = list(Path('directory').glob('*.py'))
all_py_files = list(Path('directory').rglob('*.py'))  # recursive

# Reading and writing text
text = Path('file.txt').read_text()
Path('output.txt').write_text('Hello, World!')

# Reading and writing binary
data = Path('file.bin').read_bytes()
Path('output.bin').write_bytes(data)
```

## Reading and Writing to Temporary Files

```python
import tempfile
import os

# Create a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp:
    temp.write(b'Temporary data')
    temp_path = temp.name

# Work with the temporary file
with open(temp_path, 'rb') as file:
    data = file.read()
    print(data)

# Delete when done
os.unlink(temp_path)

# Temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, 'file.txt')
    with open(path, 'w') as file:
        file.write('Temporary file in temporary directory')
    # Directory is automatically deleted when context exits
```

## Reading Large Files in Chunks

```python
def read_in_chunks(file_path, chunk_size=1024):
    """Read a file in chunks to avoid loading large files into memory."""
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Example usage
for chunk in read_in_chunks('large_file.bin'):
    # Process each chunk
    print(f"Processing {len(chunk)} bytes")
```

## File Encoding Handling

```python
# Specify encoding when opening files
with open('file.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Handle encoding errors
with open('file_with_errors.txt', 'r', encoding='utf-8', errors='replace') as file:
    content = file.read()  # Replaces invalid characters with �

# Write with specific encoding
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('International text: 你好, 안녕하세요, Привет')
```

## Working with Compressed Files

```python
import gzip
import zipfile
import tarfile

# Reading/writing gzip files
with gzip.open('file.txt.gz', 'wt', encoding='utf-8') as f:
    f.write('Compressed content')

with gzip.open('file.txt.gz', 'rt', encoding='utf-8') as f:
    content = f.read()

# Working with ZIP files
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')

with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extraction_dir')
    # List contents
    print(zipf.namelist())
    # Read a specific file
    content = zipf.read('file1.txt')

# Working with TAR files
with tarfile.open('archive.tar.gz', 'w:gz') as tar:
    tar.add('file1.txt')
    tar.add('directory')

with tarfile.open('archive.tar.gz', 'r:gz') as tar:
    tar.extractall('extraction_dir')
    # List contents
    print(tar.getnames())
```

## File Watching and Monitoring

```python
import time
import os

def watch_file(file_path, interval=1.0):
    """Simple file watcher that checks for changes."""
    last_modified = os.path.getmtime(file_path)

    while True:
        time.sleep(interval)
        current_modified = os.path.getmtime(file_path)

        if current_modified > last_modified:
            print(f"File {file_path} has been modified!")
            last_modified = current_modified

# Example usage
try:
    watch_file('log.txt')
except KeyboardInterrupt:
    print("Stopping file watcher")
```
