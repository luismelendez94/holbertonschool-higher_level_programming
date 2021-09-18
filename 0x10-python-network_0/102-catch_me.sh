#!/bin/bash
#Send JSON POST to an URL passed as the first argument, displays the body of the response
curl -s -L -d "You got me!" -X 'PUT' "0.0.0.0:5000/catch_me"
