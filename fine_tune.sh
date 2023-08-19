#!/bin/bash

# Check if a file name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./fine_tune.sh 'training filename'"
    exit 1
fi

# Run the openai command
openai tools fine_tunes.prepare_data -f "$1"
