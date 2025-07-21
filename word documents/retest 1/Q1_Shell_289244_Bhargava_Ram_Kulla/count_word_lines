#!/bin/bash

    
    if [ "$#" -lt 2 ]; then
        echo "Usage: $0 word file1 [file2 ...]"
        exit 1
    fi

    
    search_word=$1
    shift

    
    for file in "$@"; do
        if [ -f "$file" ]; then
            
            count=$(grep -i -w "$search_word" "$file" | wc -l)
            echo "The word '$search_word' appears in $count lines of $file."
        else
            echo "File $file does not exist."
        fi
    done
