#!/bin/bash

python -m venv venv

source venv/bin/activate

pip install -r requirements_versions.txt

pip install -r requirements.txt

python install.py --xformers --exit --skip-torch-cuda-test