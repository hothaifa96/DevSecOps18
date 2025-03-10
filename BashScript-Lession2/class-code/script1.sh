#!/bin/bash

# +
# -
# *
# /
# %
# **

echo $(( 10 ** 3 ))

x=11
let "x *= 2"
echo $x


a=1
b=5

sum=$(( a + b ))
(( sum=a+b ))
echo sum=$sum