from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

engine0 = create_engine('postgresql://'+ url.username +':' + url.password + '@' + url.hostname + '/' + url.path[1:], convert_unicode=True)
# engine0 = create_engine('postgresql://gui:AniTa08@128.175.112.125/anita_0116d', convert_unicode=True)
Base = declarative_base()
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
