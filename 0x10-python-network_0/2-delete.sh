#!/bin/bash
#Takes an URL, sends a 'DELETE' to that URL and display the body of the response
curl -s -L -X "DELETE" $1
