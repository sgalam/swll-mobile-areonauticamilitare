#!/bin/bash
cp -r /app/backend/html_resources/* /dist/
mkdir -p /dist/am_charts/ 
python main.py