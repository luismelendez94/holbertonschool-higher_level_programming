#!/bin/bash
#Send JSON POST to an URL passed as the first argument, displays the body of the response
curl -sL -X PUT -d "You got me!" -H "0.0.0.0:5000/catch_me"
