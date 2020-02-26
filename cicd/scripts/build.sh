#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${SCRIPT_DIR}/../..
PROJECT_DIR=$(pwd)
echo ${PROJECT_DIR}

PROJECT_SRC_DIR=${PROJECT_DIR}/src

OUTPUT_DIR=${PROJECT_DIR}/output

if [[ -d ${OUTPUT_DIR} ]]; then
    rm -rf ${OUTPUT_DIR}
fi

mkdir -p "${OUTPUT_DIR}/build"
mkdir -p "${OUTPUT_DIR}/lib"
echo "building..."

# build python libraries
cd ${PROJECT_DIR}
pip3 install -r requirements.txt -t ${OUTPUT_DIR}/lib
cd ${OUTPUT_DIR}/lib
zip -r ${OUTPUT_DIR}/build/pythonlibs.zip .
rm -rf lib

# build src code
cd ${PROJECT_SRC_DIR}
zip -R ${OUTPUT_DIR}/build/${SERVICE_NAME}.zip '*.py'

cd ${PROJECT_DIR}
if [[ -d ${PROJECT_DIR}/db ]]; then
    zip -r ${OUTPUT_DIR}/build/sqlscripts.zip ./db -i '*.sql'
fi

