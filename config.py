import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacityp1storageacc'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'KCdKbDA8zhl/d4LI5RbJ2TLRartngu0wDoxY1WjAZUuzuaOItjLnm+5aY+aqE4F5j+ub3rRM/0wp+AStr+Kacg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacityproject1server110323.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacityproject1db110323'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'maersa123'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '1122334poMN%%'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "flE8Q~a_zG1mL-9sCRMH3ULqeIyr0sV8cPa2Scsw"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    #AUTHORITY = "https://login.microsoftonline.com/c51fa4ad-e591-483a-b180-af1a49af4665"

    CLIENT_ID = "6cfebe44-f02c-490f-804f-eb2cd547425b"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session