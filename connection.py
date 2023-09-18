from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# import sqlite3 as sql # import the sqlite3 module and assign it with an alias (sql) hm

# # To use the sqlite3 (sql) module: Create a DB connection object (variable).
# # dbCon is a variable that is assigned everything on the right (sql.connect())
# dbCon = sql.connect("filmflix.db") # sqlite3(sql).connect() = create a db or open(if one exists) a DB


# # Create a cursor object(variable) and pass/assign it to the cursor method
# dbCursor = dbCon.cursor()