import json
from unittest import TestCase

from handlers.list_polls import handler
from service.question import QuestionService


class Test(TestCase):
    def test_happy_path(self):
        service = QuestionService()
        result = service.list_polls()

        question = result[0]
        self.assertEqual(question.title, "What is your favourite car brand?")

    def test_handler(self):
        print(handler({}, {}))
