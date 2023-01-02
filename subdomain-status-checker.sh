#!/bin/bash

read -p "Enter the name of the file with the URLs: " file

while read -r url; do
status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
if [[ "$status" == "200" ]]; then
message="$url is returning a 200 status."
elif [[ "$status" == "404" ]]; then
message="$url is returning a 404 status."
elif [[ "$status" == "500" ]]; then
message="$url is returning a 500 status."
elif [[ "$status" == "502" ]]; then
message="$url is returning a 502 status."
elif [[ "$status" == "503" ]]; then
message="$url is returning a 503 status."
elif [[ "$status" == "504" ]]; then
message="$url is returning a 504 status."
else
message="$url is experiencing a connection timeout, SSL certificate error, redirect loop, slow loading, or broken links."
fi

echo "$message" >> status.txt
sleep 5
done < "$file"