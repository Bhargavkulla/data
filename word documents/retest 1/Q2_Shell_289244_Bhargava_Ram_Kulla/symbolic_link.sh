#!/bin/bash
 

 
FILE="$1"
 

if [ -z "$FILE" ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi
 

if [ -L "$FILE" ]; then
    echo "'$FILE' is a symbolic link."
 
    
    if command -v readlink >/dev/null && readlink -f "$FILE" >/dev/null 2>&1; then
        TARGET=$(readlink -f "$FILE")
    else
        TARGET=$(readlink "$FILE")
    fi
 
    echo "It points to: $TARGET"
else
    echo "'$FILE' is not a symbolic link."
fi
