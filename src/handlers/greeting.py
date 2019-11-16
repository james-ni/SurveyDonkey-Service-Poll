from common.rest_controller import rest_controller


@rest_controller(require_auth=True)
def handler(event, context):
    print(event)
    try:
        greeting = f'hello, {event["request_uri_args"]["name"]}!'
    except KeyError as ex:
        raise ex

    return {'message': greeting}
