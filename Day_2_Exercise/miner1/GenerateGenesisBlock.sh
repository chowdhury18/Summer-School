#!/bin/bash
while true
do
	file="$(openssl rand -hex 4)\n$(cat $1)"
	sha256="$(echo $file | openssl dgst -sha256 | awk '{print $2}')"
	if [[ $sha256 == 000* ]]
	then
		printf "GenesisMessage.txt\n$sha256\n" > toppointer.txt
		break
	fi
done