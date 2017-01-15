#!/bin/bash
git init
git add .
git commit -m "$1"
git remote add origin https://github.com/sunq-run/nekospider.git
git push -u origin master


