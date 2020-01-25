#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${SCRIPT_DIR}/../..
PROJECT_DIR=$(pwd)
echo ${PROJECT_DIR}

PROJECT_SRC_DIR=${PROJECT_DIR}/src

OUTPUT_DIR=${PROJECT_DIR}/output/build

if [[ -d ${OUTPUT_DIR} ]]; then
    rm -rf ${OUTPUT_DIR}
fi

mkdir -p "${OUTPUT_DIR}"
echo "building..."

# build python libraries
cd ${PROJECT_DIR}
pip3 install -r requirements.txt -t ${PROJECT_DIR}/output/lib
cd ${PROJECT_DIR}/output/lib
zip -r ${OUTPUT_DIR}/pythonlibs.zip .
rm -rf lib

# build src code
cd ${PROJECT_SRC_DIR}
zip -R ${OUTPUT_DIR}/${SERVICE_NAME}.zip '*.py'

cd ${PROJECT_DIR}
if [[ -d ${PROJECT_DIR}/db ]]; then
    zip -r ${OUTPUT_DIR}/sqlscripts.zip ./db -i '*.sql'
fi

