from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine0 = create_engine('postgresql://gui:AniTa08@128.175.112.58:54320/anita_1206d', convert_unicode=True)
# engine0 = create_engine('postgresql://gui:AniTa08@128.175.112.80/anita_1125d', convert_unicode=True)
Base = declarative_base()
# engine0 seems can be any database with the tables we need, does not affect the Base.query we use.
Base.metadata.bind=engine0
def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
	import app.models
    # Base.metadata.create_all(bind=engine)
    #autoload the database
    # Base.metadata.reflect(bind=engine)
