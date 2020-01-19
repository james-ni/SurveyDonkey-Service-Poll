import json

from common.rest_controller import rest_controller


@rest_controller()
def handler(event, context):
    return {
        'id': '',
        'description': '',
        'status': '',
        'user_id': '',
        'created_at': '',
        'updated_at': ''
    }
