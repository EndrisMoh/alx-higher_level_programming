#!/bin/bash
# A Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
curl -sX POST -d "email=test@gmal.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
