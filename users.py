from datetime import datetime
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from app import app
from db import db

def followed_accounts(follower_id):
    sql = '''SELECT u.id, u.username FROM "user" u JOIN following f on
        u.id=f.followed_id WHERE f.follower_id=:follower_id'''
    result = db.session.execute(text(sql), {"follower_id":follower_id})
    accounts = result.fetchall()
    return accounts

def check_following(followed_id):
    follower_id = session["id"]
    sql = '''SELECT u.id, u.username FROM "user" u JOIN following f on
        u.id=f.followed_id WHERE f.follower_id=:follower_id AND
        f.followed_id=:followed_id'''
    result = db.session.execute(text(sql), {"follower_id":follower_id, "followed_id":followed_id})
    account = result.fetchone()

    if account is not None:
        return True
    return False

def follow(followed_id):
    follower_id = session["id"]
    if follower_id != followed_id:
        try:
            sql = '''INSERT INTO following (follower_id, followed_id)
                    VALUES (:follower_id, :followed_id)'''
            db.session.execute(text(sql), {"follower_id":follower_id, "followed_id":followed_id})
            db.session.commit()
            return True
        except:
            return False
    return False

def unfollow(followed_id):
    follower_id = session["id"]
    if follower_id != followed_id:
        try:
            sql = '''DELETE FROM following WHERE follower_id=:follower_id AND
                followed_id=:followed_id'''
            db.session.execute(text(sql), {"follower_id":follower_id, "followed_id":followed_id})
            db.session.commit()
            return True
        except:
            return False
    return False

def is_logged_in():
    try:
        session["id"]
        return True
    except:
        return False

def delete_user(id):
    try:
        sql = 'DELETE FROM "user" WHERE id=:id;'
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True
    except:
        return False

def check_email(email):
    sql = 'SELECT id FROM "user" WHERE email=:email'
    result = db.session.execute(text(sql), {"email":email})
    user = result.fetchone()
    if user is not None:
        return False
    return True

def signup(username, email, password):
    sql = 'SELECT id FROM role WHERE role_name=:role_name'
    result = db.session.execute(text(sql), {"role_name":'general user'})
    role_id = result.fetchone()
    date_added = datetime.now()
    password_hash = generate_password_hash(password, 'scrypt')

    try:
        sql = '''INSERT INTO "user" (username, email, password, role_id, date_added)
            VALUES (:username, :email, :password, :role_id, :date_added)'''
        db.session.execute(text(sql), {"username":username, "email":email,
            "password":password_hash, "role_id":role_id[0], "date_added":date_added})
        db.session.commit()
        return login(email, password)
    except:
        return False

def login(email, password):
    sql = '''SELECT u.password, u.id, r.role_name, u.username, u.date_added, u.bio
        FROM "user" u JOIN role r ON u.role_id=r.id WHERE email=:email'''
    result = db.session.execute(text(sql), {"email":email})
    user = result.fetchone()

    if not user:
        return False

    if not check_password_hash(user[0], password):
        return False

    session["email"] = email
    session["id"] = user[1]
    session["role"] = user[2]
    session["username"] = user[3]
    session["date_added"] = user[4]
    session["bio"] = user[5]
    #session["csrf_token"] = os.urandom(16).hex()
    return True

def logout():
    del session["id"]
    del session["email"]
    del session["role"]
    del session["username"]

def edit_user(id, username, email, bio):
    if id == session["id"]:
        try:
            sql = 'UPDATE "user" SET email=:email, username=:username, bio=:bio WHERE id=:id'
            db.session.execute(text(sql), {"email":email, "username":username, "bio":bio, "id":id})
            db.session.commit()
            session["email"] = email
            session["username"] = username
            session["bio"] = bio
            return True
        except:
            return False
    return False

def get_users():
    sql = '''SELECT u.id, u.username, u.email, u.date_added, r.role_name
            FROM "user" u JOIN role r on u.role_id=r.id ORDER BY u.date_added DESC'''
    result = db.session.execute(text(sql), {"id":id})
    users = result.fetchall()
    return users

def get_user(id):
    sql = '''SELECT id, username, email, bio, date_added FROM "user" WHERE id=:id'''
    result = db.session.execute(text(sql), {"id":id})
    user = result.fetchone()
    return user

def get_searched_user(searched):
    searched="%"+searched+"%"
    sql = '''SELECT u.id, u.username, u.email, u.date_added, r.role_name
            FROM "user" u JOIN role r on u.role_id=r.id WHERE u.username
            ILIKE :searched OR u.id::text LIKE :searched ORDER BY u.date_added DESC'''
    result = db.session.execute(text(sql), {"searched":searched})
    users = result.fetchall()
    return users
