#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

touch $DIR/temp.out
echo

sudo pip install --upgrade $DIR &> temp.out
sudo pip3 install --upgrade $DIR &> temp.out

echo 'Python 2.7 run'
python $DIR/test_scoria.py #&> temp.out
echo

echo 'Python 3 run'
sudo python3 $DIR/test_scoria.py #&> temp.out
echo

rm temp.out
