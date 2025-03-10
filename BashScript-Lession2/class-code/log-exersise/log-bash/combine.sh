#!/bin/bash

TARGET_FILE="$(whoami).log"

if [ -f  "$TARGET_FILE" ]; then
	echo removing existing file : $TARGET_FILE
	rm $TARGET_FILE
fi

echo gathering all the log files

SOURCE_FILES=$(find . -maxdepth 1 -type f -name "*.log")

if [ -z "$SOURCE_FILES" ]; then
	echo No logs files found
fi


for file in $SOURCE_FILES;do
	echo ">>>>>>>> contents from $file <<<<<<<<<<" >> "$TARGET_FILE"
	cat "$file" >> "$TARGET_FILE"
	echo "" >> "$TARGET_FILE"
done

