from app import app
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from sqlalchemy.sql import text

def signup(username, email, password):
    print("test1")
    sql = 'SELECT id FROM "user" WHERE email=:email'
    result = db.session.execute(text(sql), {"email":email})
    user = result.fetchone()
    print("test2")

    if user == None:
        role = "user"
        date_added = datetime.now()
        try:
            print("test3")
            role = "general user"
            sql = """INSERT INTO "user" (username, email, password, role, date_added)
                    VALUES (:username, :email, :password, :role, :date_added)"""
            db.session.execute(text(sql), {"username":username, "email":email, "password":password, "role":role, "date_added":date_added})
            db.session.commit()
            print("test4")
            return login(email, password)
        except:
            return False  
    else:
        return False
    
def login(email, password):
    return True

def logout():
    pass