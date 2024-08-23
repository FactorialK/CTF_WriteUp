#!/bin/bash
# Using loop for a command until found a specific keyword

content=$(cat enc_flag)

while true; do
    # decode
    content=$(echo "$content" | base64 -d)

    echo "$content" | grep -q "pico"
    if [ $? -eq 0 ]; then
        echo "Found 'pico' in the decoded content:"
        echo "$content"
        break
    fi
done
