#!/bin/bash

# Simulate reading from CSV and creating user folders
INPUT="users.csv"

if [ ! -f "$INPUT" ]; then
  echo "Error: users.csv not found!"
  exit 1
fi

mkdir -p home_dirs

tail -n +2 "$INPUT" | while IFS=',' read -r full_name email department
do
  username=$(echo "$full_name" | tr '[:upper:]' '[:lower:]' | sed 's/ /./g')
  user_dir="home_dirs/$username"
  mkdir -p "$user_dir"
  echo "Created directory: $user_dir"
done
