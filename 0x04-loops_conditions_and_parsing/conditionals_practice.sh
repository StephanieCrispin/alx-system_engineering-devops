#!/usr/bin/env bash
#A bash script that determines the greatest number

# a=1
# b=2
# c=3

# if [ $c -ge $b ] && [ $c -ge $b ];then
#     echo "C is the greatest"
# fi

echo -n "Enter Number: "
read x

if [ $((x%2)) == 0 ];then
    echo "This is an even number"
else
    echo "This is an odd number"
fi
