#!/bin/bash
#Takes an URL, sends a request to that URL and display the size of the body of the response
curl -s $1 --include | grep -i Content-Length | awk '{print $2}'
