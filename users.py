from app import app
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from sqlalchemy.sql import text

print(generate_password_hash('test', 'scrypt'))

def is_logged_in():
    try:
        session["id"]
        return True
    except:
        return False

def get_user(id):
    sql = '''SELECT * FROM "user" WHERE id=:id'''
    result = db.session.execute(text(sql), {"id":id})
    user = result.fetchone()
    if user:
        return True
    return False

def check_email(email):
    sql = 'SELECT id FROM "user" WHERE email=:email'
    result = db.session.execute(text(sql), {"email":email})
    user = result.fetchone()
    if user != None:
        return False
    return True

def signup(username, email, password):
    sql = 'SELECT id FROM role WHERE role_name=:role_name'
    result = db.session.execute(text(sql), {"role_name":'general user'})
    role_id = result.fetchone()
    date_added = datetime.now()
    password_hash = generate_password_hash(password, 'scrypt')

    try:
        sql = """INSERT INTO "user" (username, email, password, role_id, date_added)
                VALUES (:username, :email, :password, :role_id, :date_added)"""
        db.session.execute(text(sql), {"username":username, "email":email, "password":password_hash, "role_id":role_id[0], "date_added":date_added})
        db.session.commit()
        return login(email, password)
    except:
        return False  

    
    
def login(email, password):
    sql = '''SELECT u.password, u.id, r.role_name, u.username, u.date_added FROM "user" u JOIN role r ON u.role_id=r.id
        WHERE email=:email'''
    result = db.session.execute(text(sql), {"email":email})
    user = result.fetchone()

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

"""def edit_user(id, username, email):
    if id == session["id"]:
        try:
            print("1")
            sql = "UPDATE "user" SET email = :email, username = :username WHERE id = :id"
            db.session.execute(text(sql), {"email":email, "username":username, "id":id})
            db.session.commit()
            print("5")
            session["email"] = email
            session["username"] = username
            return True
        except:
            return False
        
    return False"""