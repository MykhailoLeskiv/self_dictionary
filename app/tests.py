import os
import unittest

from app import app, db
from app.config import basedir
from app.models import User, Dictionary, Chapter, Word


class ModelTestMixin(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def refresh_db(self, *args):
        for arg in args:
            db.session.add(arg)
        db.session.commit()


class TestUser(ModelTestMixin):

    def test_create_sanity(self):
        user = User(email='test@test.com', username='test', password='test')
        self.refresh_db(user)
        assert db.session.query(User).count() == 1
        db.drop_all()

    def test_fields(self):
        user = User(email='test@test.com', username='test', password='test')
        self.refresh_db(user)
        assert user.email == 'test@test.com'
        assert user.username == 'test'
        assert user.password == 'test'
        db.drop_all()

    def test_multiple_create(self):
        user1 = User(username='test1', email='test1@test1.com', password='test1')
        user2 = User(username='test2', email='test2@test2.com', password='test2')
        self.refresh_db(user1, user2)
        yield db
        assert db.session.query(User).count() == 2
        db.drop_all()

    def test_delete_user(self):
        user = User(email='testtest@test.com', username='testtest', password='testtest')
        self.refresh_db(user)
        db.session.delete(user)
        db.session.commit()
        assert db.session.query(User).count() == 0


class TestDictionary(ModelTestMixin):

    def setUp(self):
        self.user = User(email='test@test.com', username='test', password='test')
        super().setUp()

    def test_dictionary_single_create(self):
        dictionary = Dictionary(user=self.user, native_lang='ukrainian', foreign_lang='english')
        self.refresh_db(self.user, dictionary)
        yield db
        assert db.session.query(Dictionary).count() == 1

    def test_dictionary_multiple_create(self):
        dictionary_1 = Dictionary(user=self.user, native_lang='spanish', foreign_lang='english')
        dictionary_2 = Dictionary(user=self.user, native_lang='ukrainian', foreign_lang='french')
        self.refresh_db(dictionary_1, dictionary_2, self.user)
        yield db
        assert db.session.query(Dictionary) == 2

    def test_dictionary_filds(self):
        dictionary = Dictionary(user=self.user, native_lang='ukrainian', foreign_lang='english')
        self.refresh_db(dictionary)
        yield db
        assert dictionary.native_lang == 'ukrainian'
        assert dictionary.foreign_lang == 'english'

    def test_delete_dictionary(self):
        dictionary = Dictionary(user=self.user, native_lang='spanish', foreign_lang='english')
        self.refresh_db(dictionary)
        db.session.delete(dictionary)
        db.session.commit()
        yield db
        assert db.session.query(Dictionary).count() == 0


class TestChapter(ModelTestMixin):

    def setUp(self):
        self.user = User(email='test@test.com', username='test', password='test')
        self.dictionary = Dictionary(user=self.user, native_lang='spanish', foreign_lang='english')
        super().setUp()

    def test_chapter_single_create(self):
        chapter = Chapter(dictionary=self.dictionary, chapter_name='food')
        self.refresh_db(chapter)
        yield db
        assert db.session.query(Chapter).count() == 1

    def test_chapter_multiple_create(self):
        chapter_1 = Chapter(dictionary=self.dictionary, chapter_name='food')
        chapter_2 = Chapter(dictionary=self.dictionary, chapter_name='hobby')
        self.refresh_db(chapter_1, chapter_2, self.dictionary)
        yield db
        assert db.session.query(Chapter) == 2


class TestWord(ModelTestMixin):

    def setUp(self):
        self.user = User(email='test@test.com', username='test', password='test')
        self.dictionary = Dictionary(user=self.user, native_lang='spanish', foreign_lang='english')
        self.chapter = Chapter(dictionary=self.dictionary, chapter_name='food')
        super().setUp()

    def test_word_single_create(self):
        word = Word(chapter=self.chapter, word='їжа', translation='food')
        self.refresh_db(word)
        yield db
        assert db.session.query(Word).count() == 1

    def test_word_multiple_create(self):
        word_1 = Word(chapter=self.chapter, word='їжа', translation='food')
        word_2 = Word(chapter=self.chapter, word='хліб', translation='bread')
        self.refresh_db(word_1, word_2, self.chapter)
        yield db
        assert db.session.query(Word) == 2

    def test_delete_word(self):
        word = Word(chapter=self.chapter, word='хліб', translation='bread')
        self.refresh_db(word)
        db.session.delete(word)
        db.session.commit()
        yield db
        assert db.session.query(Word).count() == 0


if __name__ == '__main__':
    unittest.main()
