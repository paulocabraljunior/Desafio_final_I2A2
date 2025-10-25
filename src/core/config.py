# src/core/config.py

import os

class Config:
    """Configurações base da aplicação."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta-bem-segura'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Configurações para o ambiente de desenvolvimento."""
    DEBUG = True

class TestingConfig(Config):
    """Configurações para o ambiente de testes."""
    TESTING = True

class ProductionConfig(Config):
    """Configurações para o ambiente de produção."""
    pass

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
