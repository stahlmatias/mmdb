import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DIRECTORS_PER_PAGE = 12
    MOVIES_PER_PAGE = 10
    SERIES_PER_PAGE = 10
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="",
        password="",
        hostname="",
        databasename="",
    )

