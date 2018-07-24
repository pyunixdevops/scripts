#!/bin/sh

name="Sankar"
if [ $# -ge 9 ]; then
    echo "'\$#' is $$ --$@--'$name' $# "
fi

echo ${12}
echo ${11}
echo ${10}

echo $1 $2 $3

shift 5

echo $1 $2 $3 
