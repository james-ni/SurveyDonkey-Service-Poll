import functools
import json

from common.auth_error import AuthError


def rest_controller(require_auth=None):
    def controller(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            event = args[0]

            if require_auth:
                try:
                    token = get_token_auth_header(event)

                except AuthError as error:
                    return {
                        'statusCode': error.status_code,
                        'body': json.dumps({'message': error.message})
                    }

            try:
                result = {
                    'statusCode': 200,
                    'body': json.dumps(func(*args, **kwargs))
                }
            except KeyError:
                result = {
                    'statusCode': 400,
                    'body': json.dumps({'message': 'Bad request'})
                }
            except:
                result = {
                    'statusCode': 500,
                    'body': json.dumps({'message': 'Something went wrong at server side'})
                }
            return result

        return wrapper

    return controller


# Format error response and append status code
def get_token_auth_header(event):
    """Obtains the Access Token from the Authorization Header
    """
    print(event)
    try:
        auth = event['request_headers']["authorization"]
    except KeyError:
        auth = ""

    if not auth:
        raise AuthError("Authorization header is expected", 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError("Authorization header must start with"" Bearer", 401)
    elif len(parts) == 1:
        raise AuthError("Token not found", 401)
    elif len(parts) > 2:
        raise AuthError("Authorization header must be"" Bearer token", 401)

    token = parts[1]
    return token
