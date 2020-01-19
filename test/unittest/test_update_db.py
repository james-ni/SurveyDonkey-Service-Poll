from unittest import TestCase
from handlers.update_db import db_migrate

class TestUpdateDB(TestCase):
    def test_db_migrate(self):
        db_migrate()


        pass