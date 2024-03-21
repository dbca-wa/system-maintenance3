#!/bin/bash

wget -q -O - "http://localhost:8080/"
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start wget: $status"
  exit 1
fi
exit 0
