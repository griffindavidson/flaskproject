import os

class Config(object):
    SECRET_KY = os.environ('SECRET_KEY') or "secret_string"