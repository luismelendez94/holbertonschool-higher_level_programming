#!/bin/bash
#Send JSON POST to an URL passed as the first argument, displays the body of the response
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
