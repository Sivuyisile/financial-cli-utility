import pytest

from database_manager import DatabaseManager


@pytest.fixture
def db_manager(tmp_path):

    #creating a temp file for the test
    db_file = tmp_path / "test_fin.db"

    manager = DatabaseManager(db_path=db_file) #I am using the real-life path here

    manager.create_tables()

    yield manager


def test_create_tables(db_manager):

    budget_table = db_manager.fetch_one(query="SELECT name FROM sqlite_master WHERE type='table' AND name='monthly_budgets'", params=())

    assert budget_table is not None
    assert budget_table["name"] == "monthly_budgets"

    expenses_table = db_manager.fetch_one(query="SELECT name FROM sqlite_master WHERE type='table' AND name='expenses'", params=())
    
    assert expenses_table is not None
    assert expenses_table["name"] == "expenses"


    