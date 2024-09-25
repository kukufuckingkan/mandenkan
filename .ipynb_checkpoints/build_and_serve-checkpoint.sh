#!/bin/bash

# Start the local server in the background
python serve_html.py &

# Store the process ID (PID) of the server
SERVER_PID=$!

# Allow some time for the server to start
sleep 2

# Build the Jupyter Book
jupyter-book build ./ --builder pdfhtml

# Kill the server after the build is complete
kill $SERVER_PID