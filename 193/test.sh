#!/usr/bin/bash

# while IFS= read -r line; do
#   echo "$line" | grep -Eo "^(\([0-9]{3}\)\s|[0-9]{3}-)[0-9]{3}-[0-9]{4}$"
# done < ./file.txt

grep -e "^[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}$" -e "^([0-9]\{3\}) [0-9]\{3\}\-[0-9]\{4\}$" file.txt
