from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine0 = create_engine('postgresql://gui:AniTa08@128.175.112.125/anita_0116d', convert_unicode=True)
engine1 = create_engine('postgresql://gui:AniTa08@128.175.112.80/anita_0105d', convert_unicode=True)
engine2 = create_engine('postgresql://gui:AniTa08@128.175.112.80/anita_0106d', convert_unicode=True)
engine3 = create_engine('postgresql://gui:AniTa08@128.175.112.58/anita_0105d', convert_unicode=True)
engine4 = create_engine('postgresql://gui:AniTa08@128.175.112.58/anita_0106d', convert_unicode=True)
db_session0 = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine0))
db_session1 = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine1))
db_session2 = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine2))
db_session3 = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine3))
db_session4 = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine4))
Base = declarative_base()

Base.query_128_175_112_125_anita_0116d = db_session0.query_property()
Base.query_128_175_112_80_anita_0105d = db_session1.query_property()
Base.query_128_175_112_80_anita_0106d = db_session2.query_property()
Base.query_128_175_112_58_anita_0105d = db_session1.query_property()
Base.query_128_175_112_58_anita_0106d = db_session2.query_property()

# engine0 seems can be any database, does not affect the Base.query we use.
Base.metadata.bind=engine0
def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
	import app.models
    # Base.metadata.create_all(bind=engine)
    #autoload the database
    # Base.metadata.reflect(bind=engine)
