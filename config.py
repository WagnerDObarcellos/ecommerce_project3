import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'minha-chave-secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///ecommerce.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    