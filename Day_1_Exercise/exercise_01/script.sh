#!/bin/bash
sha256="$(cat ./file00.txt | openssl dgst -sha256)"
printf "file00.txt\n$sha256\n" > toppointer.txt
echo $(cat ./toppointer.txt)

for i in {01..15}
do
	printf "This is data number $i." > data$i.txt
	printf "$(cat toppointer.txt)\n$(cat data$i.txt)" > file$i.txt
	newsha256="$(cat ./file$i.txt | openssl dgst -sha256)"
	printf "file$i.txt\n$newsha256\n" >> newtoppointer.txt
	printf "file$i.txt\n$newsha256" > toppointer.txt
done


