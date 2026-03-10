# Drug Information Query — OpenFDA API

A Python command-line tool that queries the OpenFDA API to retrieve
drug label information including purpose, manufacturer and adverse effects.

## Features
- Search drugs by brand name
- Displays purpose, manufacturer and adverse effects
- Handles drugs not found in the database
- Loop allowing multiple searches in the same session

## Technologies
- Python
- Requests

## API
OpenFDA Drug Label API
https://api.fda.gov/drug/label.json

## How to run
pip install requests
python drug_query.py

## Example
Enter drug name: aspirin