import logging
import subprocess
from os import getenv

import cfnresponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(event)

    try:
        if event['RequestType'] == 'Delete':
            logger.info('Deleted!')
            cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
            return

        db_migrate()
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
    except Exception:
        logger.exception('Signaling failure to CloudFormation.')
        cfnresponse.send(event, context, cfnresponse.FAILED, {})


def db_migrate():
    args = [
        '/opt/flyway-5.2.4/flyway',
        f'-url=jdbc:postgresql://{getenv("RDS_ENDPOINT")}:5432/postgres',
        f'-user={getenv("DB_USER")}',
        f'-password={getenv("DB_PASS")}',
        f'-schemas={getenv("DB_SCHEMA")}',
        f'-locations=filesystem:/opt/db',
        '-baselineOnMigrate=true',
        'migrate'
    ]

    flyway_process = subprocess.run(args=args, shell=False, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    logger.info(f'Flyway cmd STDOUT:\n{flyway_process.stdout.decode("utf-8")}')
    logger.info(f'Flyway cmd STDERR:\n{flyway_process.stderr.decode("utf-8")}')
