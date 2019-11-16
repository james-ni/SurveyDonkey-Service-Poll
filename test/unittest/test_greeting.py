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
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9VWXdOa0UyUXprM05UazRSREZHTkRneFJrUkNPVFF6UmpReE5rVkJSakZCTkRaRU5ETTBSZyJ9.eyJpc3MiOiJodHRwczovL25pbGFiLmF1dGgwLmNvbS8iLCJzdWIiOiJPVnZFUzBaak51V0pYRjJMbTRvUjBxNm1DaXZxS21YZEBjbGllbnRzIiwiYXVkIjoibmlsYWIuc3VydmV5ZG9ua2V5IiwiaWF0IjoxNTczNDY5ODg5LCJleHAiOjE1NzM1NTYyODksImF6cCI6Ik9WdkVTMFpqTnVXSlhGMkxtNG9SMHE2bUNpdnFLbVhkIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.UIUL2MxQmd5abSwV6B_pbqyOHuaYsvHG-OZXDhdcvwEiCBpbWvpmKHny71BlF2iK22piT5ghMfc30sp4QX7wtct1GAeuTsRRpHleDMxaSlm_4zO9O072kLiCe7sHjknHsGpkb5WpxyQIPpfag44gJInxccoJmCTx5qAcQK8n-ceWcxC4DN-gPJtyTleY_pfW19greqp5hTgAQBzoR9hUry8MdKlG9Wj7HsT6ysRB4vak6EXwLK_RmXatmCYmFGEUS51MgAIoKsAjO76QWF8bAdX_9LiaZNY70zscQ9ZKWjZObrN6wl3OlCjvt6uUmcp_YuFuXuJtjPfYsxRrASVaZQ',
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
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9VWXdOa0UyUXprM05UazRSREZHTkRneFJrUkNPVFF6UmpReE5rVkJSakZCTkRaRU5ETTBSZyJ9.eyJpc3MiOiJodHRwczovL25pbGFiLmF1dGgwLmNvbS8iLCJzdWIiOiJPVnZFUzBaak51V0pYRjJMbTRvUjBxNm1DaXZxS21YZEBjbGllbnRzIiwiYXVkIjoibmlsYWIuc3VydmV5ZG9ua2V5IiwiaWF0IjoxNTczNDY5ODg5LCJleHAiOjE1NzM1NTYyODksImF6cCI6Ik9WdkVTMFpqTnVXSlhGMkxtNG9SMHE2bUNpdnFLbVhkIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.UIUL2MxQmd5abSwV6B_pbqyOHuaYsvHG-OZXDhdcvwEiCBpbWvpmKHny71BlF2iK22piT5ghMfc30sp4QX7wtct1GAeuTsRRpHleDMxaSlm_4zO9O072kLiCe7sHjknHsGpkb5WpxyQIPpfag44gJInxccoJmCTx5qAcQK8n-ceWcxC4DN-gPJtyTleY_pfW19greqp5hTgAQBzoR9hUry8MdKlG9Wj7HsT6ysRB4vak6EXwLK_RmXatmCYmFGEUS51MgAIoKsAjO76QWF8bAdX_9LiaZNY70zscQ9ZKWjZObrN6wl3OlCjvt6uUmcp_YuFuXuJtjPfYsxRrASVaZQ',
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