#!/bin/bash
#Takes an URL, send a request and displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
