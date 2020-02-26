from common.rest_controller import rest_controller
from service.question import QuestionService


@rest_controller()
def handler(event, context):
    question_service = QuestionService()
    questions = question_service.list_polls()

    result = []
    for question in questions:
        result.append(question.as_dict(recurse=True))
    return result
