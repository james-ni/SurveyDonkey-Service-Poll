#curl -X PUT http://localhost:8001/plugins/awslambda-plugin-greeting \
#    --data "name=aws-lambda"  \
#    --data-urlencode "config.aws_key=AKIAT2QT7NLQ42SACD3T" \
#    --data-urlencode "config.aws_secret=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" \
#    --data "config.aws_region=ap-southeast-2" \
#    --data "config.function_name=Greeting"

curl -X PUT http://localhost:8001/routes/greeting \
    --data "name=greeting" \
    --data "paths[]=/greeting" \
    --data "methods[]=GET" \
    --data "service.id=474d928c-bbbd-4491-83f5-85e4da8f2b3c"


