import pytest
import utils
from src.loader.load_user_data import insert_user_data, users


def truncate_user_data():
    with utils.connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE housing.user')


@pytest.fixture()
def set_up_tear_down():
    truncate_user_data()
    yield
    truncate_user_data()


class TestLoadUserData:
    def test_load_user_data(self, set_up_tear_down):
        insert_user_data(users)
        with utils.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT COUNT(*) FROM housing.user')
                nrows = cursor.fetchone()
        assert nrows[0] == 2
