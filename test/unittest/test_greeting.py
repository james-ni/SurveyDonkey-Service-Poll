import json
from unittest import TestCase

from handlers.greeting import handler

HAPPY_EVENT = {
    'request_method': 'GET',
    'request_uri': '/greeting?name=James',
    'request_body': '',
    'request_headers': {
        'host': 'localhost:8000',
        'content-type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9VWXdOa0UyUXprM05UazRSREZHTkRneFJrUkNPVFF6UmpReE5rVkJSakZCTkRaRU5ETTBSZyJ9.eyJpc3MiOiJodHRwczovL25pbGFiLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1YThhNWZkZmY1YzgyMTNjYjI3Y2RhZjciLCJhdWQiOlsibmlsYWIuc3VydmV5ZG9ua2V5IiwiaHR0cHM6Ly9uaWxhYi5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTg1MzgxMzM2LCJleHAiOjE1ODU0Njc3MzYsImF6cCI6Ijd1Rk9xdXljSm5WOGhISjMwVkxrSXNiT1NNSWx6ZTdJIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.gwgYINlAzVYnnySGaTK5lGw8Ax6sRLDZVYfFXxjl22R_3SbDQJqEyah_PCKkmig39O7h4GoeElsFfaWAqLXv5N_oP-JNUyCQeBlAUqUsLf2M6FhrOJmxQdQLPfmf0XL64nftjXSypYi_wMZFgfSDsRBLQCaFl33ExD4sHhXLDK5pnkThv4WsPewL6PGUQV693o87Jwl6miL8TyVj4wMPvzw9zS6jNGKqW7w_yLkuZIOMZLvtB18NjpKd4uyXkAAEU0oD60u-VStwLuUKBp7ATnPaULYcIoHZzzMzVBoW-BNiBufrlw-OUR3yhYjXFbrIdTA0PupBOzy2yxbS0d7kxQ',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'accept-encoding': 'gzip, deflate',
        'user-agent': 'PostmanRuntime/7.1.1',
        'auth': '123',
        'connection': 'keep-alive'
    },
    'request_uri_args': {
        'name': 'James'
    }
}

BAD_REQUEST_400_EVENT = {
    'request_headers': {
        'host': 'localhost:8000',
        'content-type': 'application/json',
        'Authorization': 'Bearer xiE1sqwcvbUBmPtRLL1Vww1OqqRJWpH8',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'accept-encoding': 'gzip, deflate',
        'user-agent': 'PostmanRuntime/7.1.1',
        'connection': 'keep-alive'
    },
}

AUTH_HEADER_NOT_FOUND_EVENT = {}

HAPPY_RESPONSE = {
    'statusCode': 200,
    'body': json.dumps({'message': 'hello, James!'})
}

BAD_REQUEST_RESPONSE = {
    'statusCode': 400,
    'body': json.dumps({'message': 'Bad request'})
}

AUTH_HEADER_NOT_FOUND_RESPONSE = {
    'statusCode': 401,
    'body': json.dumps({'message': 'Authorization header is expected'})
}


class Test(TestCase):
    def test_happy_path(self):
        result = handler(HAPPY_EVENT, {})
        self.assertEqual(HAPPY_RESPONSE, result)

    def test_bad_request_path(self):
        result = handler(BAD_REQUEST_400_EVENT, {})
        self.assertEqual(BAD_REQUEST_RESPONSE, result)

    def test_auth_header_path(self):
        result = handler(AUTH_HEADER_NOT_FOUND_EVENT, {})
        self.assertEqual(AUTH_HEADER_NOT_FOUND_RESPONSE, result)