#!/bin/bash

echo "welcom  youcef" 

echo "put your url or url file "

read url
for i in $(cat $url)
do 



subfinder -d $i 


assetfinder --subs-only  $i 



amass enum -brute -d $i  

done
