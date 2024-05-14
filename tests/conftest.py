import pytest, sys, random, py, pytest, os
from xprocess import ProcessStarter
from lib.database_connection import DatabaseConnection
from app import app

# This is a Pytest fixture.
@pytest.fixture
def db_connection():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn
