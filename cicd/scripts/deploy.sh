echo "deploying..."
echo ${APP_NAME}
deploytime=`date +%Y%m%d%H%M%S`
aws s3 cp output/cf-demo.zip s3://jamesni-cloudformation-demo-2019/${deploytime}/cf-demo.zip
aws cloudformation deploy \
    --stack-name cf-demo \
    --template-file cfn/template.yaml \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides \
        AppName=${APP_NAME} \
        Environment=${APP_ENVIRONMENT} \
        ServiceName=${SERVICE_NAME} \
        ServiceVersion=${SERVICE_VERSION} \
        S3Dir=${deploytime} \
    --no-fail-on-empty-changeset