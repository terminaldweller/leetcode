#!/usr/bin/env bash

for word in $(cat ./file.txt); do echo $word;done | sort | uniq -c | sort -nr | awk '{temp=$1; $1=$2; $2=temp; print}'
