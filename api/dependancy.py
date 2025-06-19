from .apis import DolibarrAPI
from .db import DbConnector
from .config import DATABASE, DOLIBARR_BASE_URL, DOLIBARR_API_KEY

API = DolibarrAPI(DOLIBARR_BASE_URL, DOLIBARR_API_KEY)

DBCONNECTOR = DbConnector(DATABASE["host"], DATABASE["user"], DATABASE["password"], DATABASE["db_name"])