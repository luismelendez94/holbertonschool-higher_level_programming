#!/bin/bash
#Takes an URL, sends a 'GET' to that URL and display the body of the response
curl -s -I -L -o -X GET $1 -eq 200
