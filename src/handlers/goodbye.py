from common.rest_controller import rest_controller


@rest_controller()
def handler(event, context):
    print(event)

    try:
        goodbye = f'Goodbye, {event["request_uri_args"]["name"]}!'
    except KeyError as ex:
        raise ex

    return {'message': goodbye}
