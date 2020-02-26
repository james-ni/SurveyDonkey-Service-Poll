from common.service_base import ServiceBase
from entity.question import Question


class QuestionService(ServiceBase):
    def __init__(self):
        super().__init__()
        self._init_connection()

    def list_polls(self):
        return self.get_session().query(Question).all()
