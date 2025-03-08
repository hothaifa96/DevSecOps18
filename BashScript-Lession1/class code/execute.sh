#!/bin/bash

if [ -e $1 ]; then 
	chmod +x $1
	./$1
else 
	echo file does not exist enter again:
	read path
	
	if [ -f $path ]; then
		chmod +x $path
		./$path
	else
		echo we tried to  help 
	fi
fi

