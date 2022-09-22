#!/bin/bash
# Post some data to a web server
curl -sd 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
