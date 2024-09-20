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

    if user == None:
        role = "user"
        date_added = datetime.now()
        password_hash = generate_password_hash(password, 'scrypt')

        try:
            print("test3")
            role = "general user"
            sql = """INSERT INTO "user" (username, email, password, role, date_added)
                    VALUES (:username, :email, :password, :role, :date_added)"""
            db.session.execute(text(sql), {"username":username, "email":email, "password":password_hash, "role":role, "date_added":date_added})
            db.session.commit()
            return login(email, password)
        except:
            return False  
    else:
        return False
    
def login(email, password):
    sql = '''SELECT password, id, role, username, date_added FROM "user" 
        WHERE email=:email'''
    result = db.session.execute(text(sql), {"email":email})
    user = result.fetchone()
    print(user)

    if user == None:
        return False

    if not check_password_hash(user[0], password):
        return False

    session["email"] = email
    session["id"] = user[1]
    session["role"] = user[2]
    session["username"] = user[3]
    session["date_added"] = user[4]
    #session["csrf_token"] = os.urandom(16).hex()
    return True

def logout():
    del session["id"]
    del session["email"]
    del session["role"]
    del session["username"]