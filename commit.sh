#!/bin/bash

git add -u
git commit -m "$1"
git push -u thesis2 master
#scp * $ASIMOV:/home/jamiec/PANTHEON/
