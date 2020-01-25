#!/usr/bin/env bash
echo "deploying..."

set -x

PROJECT_ROOT=$(PWD)

CONFIG_FILE="${PROJECT_ROOT}/.env-${APP_ENVIRONMENT}-${APP_VERSION}"

source ${CONFIG_FILE}

FlywayVersion="5-2-4"
deploytime=`date +%Y%m%d%H%M%S`
CODE_PREFIX="${APP_NAME}-${APP_ENVIRONMENT}-${SERVICE_NAME}-${APP_VERSION}-${deploytime}"

aws s3 cp output/build/${SERVICE_NAME}.zip s3://${CODE_BUCKET}/${CODE_PREFIX}/${SERVICE_NAME}.zip
aws s3 cp output/build/pythonlibs.zip s3://${CODE_BUCKET}/${CODE_PREFIX}/pythonlibs.zip
aws s3 cp output/build/sqlscripts.zip s3://${CODE_BUCKET}/${CODE_PREFIX}/sqlscripts.zip

set +x
export DB_PASS=$(aws ssm get-parameter --with-decryption --name "/${APP_NAME}/${SERVICE_NAME}/${APP_ENVIRONMENT}/${APP_VERSION}/DBPass" --query "Parameter.Value" --output text)

aws cloudformation deploy \
    --stack-name ${APP_NAME}-${APP_ENVIRONMENT}-${SERVICE_NAME}-${APP_VERSION}-${APP_ENVIRONMENT} \
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
        AppVersion=${APP_VERSION} \
        FlywayLayerName=${APP_NAME}-infra-flyway-${FlywayVersion}-${APP_ENVIRONMENT}-${APP_VERSION} \
        RDSEndpoint=${RDS_ENDPOINT} \
        DBUser=${DB_USER} \
        DBPass=${DB_PASS} \
        DBSchema=${DB_SCHEMA} \
    --no-fail-on-empty-changeset