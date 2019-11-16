#!/usr/bin/env bash
echo "deploying..."
echo ${APP_NAME}

PROJECT_ROOT=$(PWD)

CONFIG_FILE="${PROJECT_ROOT}/.env-${APP_ENVIRONMENT}-${APP_VERSION}"

source ${CONFIG_FILE}

deploytime=`date +%Y%m%d%H%M%S`

CODE_PREFIX="${APP_NAME}-${APP_ENVIRONMENT}-${SERVICE_NAME}-${APP_VERSION}-${deploytime}"

aws s3 cp output/${SERVICE_NAME}.zip s3://${CODE_BUCKET}/${CODE_PREFIX}/${SERVICE_NAME}.zip
aws cloudformation deploy \
    --stack-name ${APP_NAME}-${APP_ENVIRONMENT}-${SERVICE_NAME}-${APP_VERSION}-stack \
    --template-file cfn/template.yaml \
    --s3-bucket ${CODE_BUCKET} \
    --s3-prefix ${CODE_PREFIX} \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides \
        CodeBucket=${CODE_BUCKET} \
        CodePrefix=${CODE_PREFIX} \
        AppName=${APP_NAME} \
        Environment=${APP_ENVIRONMENT} \
        ServiceName=${SERVICE_NAME} \
        ServiceVersion=${SERVICE_VERSION} \
    --no-fail-on-empty-changeset