from unittest import TestCase
from persistence.db_connection import ConnectionDb


class TestConnection(TestCase):
    def test_connection(self):
        connection = ConnectionDb()
        conn = connection.connect()
        print(conn)                
        self.assertIsNotNone(conn)