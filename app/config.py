import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Ud7w6Wgb36t7FAHEapfknMPWFnbvhbx90sKAW'
