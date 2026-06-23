class Config:
    DATABASE = "banking.db"
    TESTING = False


class TestConfig(Config):
    TESTING = True