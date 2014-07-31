# -*- coding: utf-8 -*-
from components import db

# Database connection
db_host = "localhost"
db_name = "bourani"
db_user = "bourani"
db_password = "slaughterhouse"
db = db.Db(db_host, db_user, db_password, db_name)
