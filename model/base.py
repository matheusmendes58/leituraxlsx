from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class DatabaseConection:

    @classmethod
    def get_engine(cls):
        cls.user = 'root'
        cls.passoword = '12345'
        cls.host = 'localhost'
        cls.db ='003_'

        mysql = "mysql+mysqlconnector://%s:%s@%s/%s" % (cls.user,
                                                     cls.passoword,
                                                     cls.host,
                                                     cls.db)
        return mysql


ENGINE_ALCHEMY = create_engine(DatabaseConection.get_engine(), echo=False)
DBSession = scoped_session(sessionmaker(bind=ENGINE_ALCHEMY, expire_on_commit=False))
Base = declarative_base()


def create_all():
    from model.tables import DataCorrectionDb
    Base.metadata.create_all(ENGINE_ALCHEMY)
