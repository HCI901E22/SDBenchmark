#!/bin/bash

python -m venv venv

source venv/bin/activate

pip install Pillow

echo "Starting api"

./webui.sh --xformers --skip-install --listen --enable-insecure-extension-access

#echo "Starting generation"

#python main.py