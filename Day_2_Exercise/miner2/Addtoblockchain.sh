#!/bin/bash
while true
do
 rand=$(openssl rand -hex 4)
 toppointer=$(cat ~/Day_2_Exercise/miner2/toppointer.txt)
 content=$(cat $1)
 file="${rand}\n${toppointer}${content}"
 sha256=$(echo $file | openssl dgst -sha256 | awk '{print $2}')
 if [[ $sha256 == 000* ]]
 then
  echo -e "$file" > $1
  printf "$1\n$sha256\n$(date +%s)\n" > ~/Day_2_Exercise/miner2/toppointer.txt
  break
 fi
done
