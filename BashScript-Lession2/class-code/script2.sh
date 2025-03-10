#!/bin/bash

# for var in list 
# do
# # commands
# done


# echo example 1 for with str
# sen="bash scripting is boring please start docker!"

# for word in $sen
# do
#     echo $word
# done


# echo example2 : for with range
# for number in {1..8..2}
# do 
#     echo the number is $number
# done


# echo example3 array-iteration
# array=( "hodi" "chen" "mor" "mike" )
# for i in "${array[@]}"
# do 
#     echo $i
# done

echo example 4

for d in $(ls /)
do
    if [ -f "/$d" ] ; then
        echo skipping $d
    else
        date > "/$d/date.txt"
    fi
done
