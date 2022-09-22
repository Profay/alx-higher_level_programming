#!/bin/bash
# Send custom header with GET request
curl -sH 'X-School-User-Id:98' "$1"
