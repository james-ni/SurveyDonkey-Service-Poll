import logging
import subprocess

import cfnresponse


def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info(event)

    try:
        if event['RequestType'] == 'Delete':
            logger.info('Deleted!')
            cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
            return

        logger.info(event['RequestType'])
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
    except Exception:
        logger.exception('Signaling failure to CloudFormation.')
        cfnresponse.send(event, context, cfnresponse.FAILED, {})


def db_migrate():
    subprocess.run(['echo', 'hello'], shell=False, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    pass
