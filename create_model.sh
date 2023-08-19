#!/bin/bash
export OPENAI_API_KEY='YOUR API KEY HERE'

# Check if a file name is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./create_model.sh <TRAINING_DATA_FILE>"
    exit 1
fi

# Run the openai command
openai api fine_tunes.create -t "$1"
