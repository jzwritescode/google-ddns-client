#!/bin/bash

# Clear existing virtual environemnt
rm -Rf .env

# Create virtual environment and activate
python3 -m venv .env
source .env/bin/activate

# Install python dependencies
pip install -r requirements.txt