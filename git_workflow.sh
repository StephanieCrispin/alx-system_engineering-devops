#!/usr/bin/env sh

git status

git add .

read -p "Enter your commit message: " commit_message

git commit -m $commit_message

git push

echo "Git workflow completed successfully"