import functools
import json
from six.moves.urllib.request import urlopen
from jose import jwt
import requests

from common.auth_error import AuthError

AUTH0_DOMAIN = 'nilab.auth0.com'
API_AUDIENCE = 'nilab.surveydonkey'
ALGORITHMS = ["RS256"]


def rest_controller(require_auth=None):
    def controller(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            event = args[0]

            if require_auth:
                try:
                    token = get_token_auth_header(event)
                    validate_token(token)

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
        auth = event['request_headers']["Authorization"]
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


def validate_token(token):
    jsonurl = requests.get("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json", verify=False)
    jwks = json.loads(jsonurl.text)
    try:
        unverified_header = jwt.get_unverified_header(token)
    except jwt.JWTError:
        raise AuthError({"code": "invalid_header",
                         "description":
                             "Invalid header. "
                             "Use an RS256 signed JWT Access Token"}, 401)
    if unverified_header["alg"] == "HS256":
        raise AuthError({"code": "invalid_header",
                         "description":
                             "Invalid header. "
                             "Use an RS256 signed JWT Access Token"}, 401)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://" + AUTH0_DOMAIN + "/"
            )
        except jwt.ExpiredSignatureError:
            raise AuthError({"code": "token_expired",
                             "description": "token is expired"}, 401)
        except jwt.JWTClaimsError:
            raise AuthError({"code": "invalid_claims",
                             "description":
                                 "incorrect claims,"
                                 " please check the audience and issuer"}, 401)
        except Exception:
            raise AuthError({"code": "invalid_header",
                             "description":
                                 "Unable to parse authentication"
                                 " token."}, 401)

        # _request_ctx_stack.top.current_user = payload
        return payload
    raise AuthError({"code": "invalid_header",
                     "description": "Unable to find appropriate key"}, 401)
