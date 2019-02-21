from flask import request
from flask_restful import Resource

from app import db
from app.models import Dictionary, DictionarySchema, User, UserSchema, Chapter, ChapterSchema, WordSchema, Word

dictionaries_schema = DictionarySchema(many=True)
dictionary_schema = DictionarySchema()
users_schema = UserSchema(many=True)
user_schema = UserSchema()
chapters_schema = ChapterSchema(many=True)
chapter_schema = ChapterSchema
words_schema = WordSchema(many=True)
word_schema = WordSchema()



class DictionaryApi(Resource):

    def get(self, user_id):
        dictionaries = Dictionary.query.filter_by(user=user_id)
        dictionaries = dictionaries_schema.dump(dictionaries).data
        return {'status': 'success', 'data': dictionaries}, 200

    def post(self, user_id):
        json_data = request.get_json(force=True)
        dictionary = Dictionary(
            user=user_id, native_lang=json_data['native_lang'], foreign_lang=json_data['foreign_lang']
        )
        db.session.add(dictionary)
        db.session.commit()
        result = dictionary_schema.dump(dictionary).data
        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        dictionary = Dictionary.query.filter_by(id=json_data['id']).first()
        if not dictionary:
            return {'message': 'Category does not exist'}, 400
        dictionary.native_lang = json_data['native_lang']
        dictionary.foreign_lang = json_data['foreign_lang']
        db.session.commit()
        result = dictionary_schema.dump(dictionary).data
        return {"status": 'success', 'data': result}, 200

    def delete(self, user_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        Dictionary.query.filter_by(id=json_data['id']).delete()
        db.session.commit()

        return {"status": 'success', 'data': {}}, 204


class UserApi(Resource):
    def get(self):
        users = User.query.all()
        users = users_schema.dump(users).data
        return {'status': 'success', 'data': users}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        user = User.query.filter_by(username=data['username']).first()
        if user:
            return {'message': 'Category already exists'}, 400
        user = User(
            username=json_data['username'], email=json_data['email'], password=json_data['password']
        )
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user).data
        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        user = User.query.filter_by(id=json_data['id']).first()
        if not user:
            return {'message': 'User does not exist'}, 400
        user.username = json_data['username']
        user.email = json_data['email']
        user.password = json_data['password']
        db.session.commit()
        result = dictionary_schema.dump(user).data
        return {"status": 'success', 'data': result}, 200

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        User.query.filter_by(id=json_data['id']).delete()
        db.session.commit()
        return {"status": 'success', 'data': {}}, 204


class GetUserApi(Resource):

    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        user = user_schema.dump(user).data
        return {'status': 'success', 'data': user}, 200


class ChapterApi(Resource):

    def get(self, user_id, dictionary_id):
        chapters = Chapter.query.filter_by(dictionary=dictionary_id)
        chapters = chapters_schema.dump(chapters).data
        return {'status': 'success', 'data': chapters}, 200

    def post(self, dictionary_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        chapter = Chapter.query.filter_by(id=json_data['id']).first()
        if chapter:
            return {'message': 'Chapter already exists'}, 400
        chapter = Chapter(
            dictionary=dictionary_id, chapter_name=json_data['chapter_name'])

        db.session.add(chapter)
        db.session.commit()
        result = chapter_schema.dump(chapter).data
        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        chapter = Chapter.query.filter_by(id=json_data['id']).first()
        if not chapter:
            return {'message': 'Chapter does not exist'}, 400
        chapter.chapter_name = json_data['chapter_name']
        db.session.commit()
        result = chapter_schema.dump(chapter).data
        return {"status": 'success', 'data': result}, 200

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        Chapter.query.filter_by(id=json_data['id']).delete()
        db.session.commit()
        return {"status": 'success', 'data': {}}, 204


class WordApi(Resource):
    def get(self, user_id, dictionary_id, chapter_id):
        words = Word.query.filter_by(chapter=chapter_id)
        words = words_schema.dump(words).data
        return {'status': 'success', 'data': words}, 200

    def post(self, user_id, dictionary_id, chapter_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        word = Word.query.filter_by(id=data['id']).first()
        if word:
            return {'message': 'Word already exists'}, 400
        word = Word(
            chapter=json_data['chapter'], word=json_data['word'], translation=json_data['translation'])

        db.session.add(word)
        db.session.commit()
        result = word_schema.dump(word).data
        return {"status": 'success', 'data': result}, 201

    def put(self, user_id, dictionary_id, chapter_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        word = Word.query.filter_by(id=json_data['id']).first()
        if not word:
            return {'message': 'Word does not exist'}, 400
        word.word = json_data['word']
        word.translation = json_data['transtalion']
        db.session.commit()
        result = chapter_schema.dump(word).data
        return {"status": 'success', 'data': result}, 200

    def delete(self, user_id, dictionary_id, chaper_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        Word.filter_by(id=json_data['id']).delete()
        db.session.commit()
        return {"status": 'success', 'data': {}}, 204