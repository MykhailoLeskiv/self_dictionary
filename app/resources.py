from flask_restful import Resource

from app.models import Dictionary, DictionarySchema

dictionary_schema = DictionarySchema()


class DictionaryList(Resource):

    def get(self):
        dictionaries = Dictionary.query.all()
        dictionaries = dictionary_schema.dump(dictionaries).data
        return {'status': 'success', 'data': dictionaries}, 200
