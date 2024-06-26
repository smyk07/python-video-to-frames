#!/bin/bash

echo "Downloading python3 modules (ez_setup, moviepy, PIL, numpy)"

pip install ez_setup

pip install moviepy pillow numpy

echo --------------------

echo "Downloading script.py"

curl -o script.py https://raw.githubusercontent.com/smyk07/python-video-to-frames/master/script.py

echo --------------------

echo "Running script.py"

python3 script.py

echo --------------------

echo "Deleting script.py"

rm ./script.py

echo --------------------

echo "Thanks for using smyk07/"
