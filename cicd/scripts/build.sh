#!/usr/bin/env bash
rm -rf output/
echo "building..."
mkdir output
cd src
zip -R ../output/${SERVICE_NAME}.zip '*.py'