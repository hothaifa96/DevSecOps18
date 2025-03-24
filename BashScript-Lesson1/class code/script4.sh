#!/bin/bash

echo enter a number
read num

if [ $num -ge 16 ] || [ $num -lt 100 ]; then
	echo the number is greater than 16
elif [ $num -gt 5 ]; then
	echo the number greter than 5
else
	echo the number is less or equals to 5 or greter than 100
fi