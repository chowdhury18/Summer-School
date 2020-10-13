#!/bin/bash
i=0
while true
do
	printf "$(openssl rand -hex 4)\n$(cat ./toppointer.txt)$(cat $1)" > $1
	sha256="$(cat $1 | openssl dgst -sha256 | awk '{print $2}')"
	if [[ $sha256 == 000* ]]
	then
		printf "$1\n$sha256" > toppointer$(date +%s).txt
		if [[ $i == 10 ]]
        then
            break
        fi
        i=i+1
	fi
done