import os
import unittest

from app import app, db
from app.config import basedir
from app.models import User, Dictionary, Chapter, Word


class TestUser(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def _refresh_db(self, *args):
        for arg in args:
            db.session.add(arg)
        db.session.commit()

    def test_create_sanity(self):
        user = User(email='test@test.com', username='test', password='test')
        self._refresh_db(user)
        assert db.session.query(User).count() == 1
        db.drop_all()

    def test_fields(self):
        user = User(email='test@test.com', username='test', password='test')
        self._refresh_db(user)
        assert user.email == 'test@test.com'
        assert user.username == 'test'
        assert user.password == 'test'
        db.drop_all()

    def test_multiple_create(self):
        user1 = User(username='test1',email='test1@test1.com', password='test1')
        user2 = User(username='test2', email='test2@test2.com', password='test2')
        self._refresh_db(user1,user2)
        yield db
        assert db.session.query(User).count() == 2
        db.drop_all()

    def test_delete_user(self):
        user = User(email='testtest@test.com', username='testtest', password='testtest')
        self._refresh_db(user)
        db.session.delete(user)
        db.session.commit()
        assert db.session.query(User).count() == 0

    def test_dictionary_single_create(self):
        user = User(email='test@test.com', username='test', password='test')
        dictionary = Dictionary(user=relationship(User), native_lang='ukrainian',foreign_lang='english')
        self._refresh_db(user,dictionary)
        assert db.session.query(Dictionary).count() == 1









if __name__ == '__main__':
    unittest.main()