#!/bin/bash

git config --global user.email "endywezy@gmail.com"
 git config --global user.name "endywezy"

# Add all files to git, commit changes, and push to the remote repository
git add . && git commit -m 'Configuration management' && git push
