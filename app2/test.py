from .db import get_session, save_item, RandomDatabaseModel


def test_save_saves_to_db():
    save_item(RandomDatabaseModel(random_text="test"))

    session = get_session()

    assert len(session.query(RandomDatabaseModel).all()) == 1
