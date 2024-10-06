from datetime import datetime
from app import app
from db import db
from sqlalchemy.sql import text

def add_post(title, content, author_id):
    date_added = datetime.now()
    try:   
        sql = """INSERT INTO post (title, content, author_id, date_added)
          VALUES (:title, :content, :author_id, :date_added)"""
        db.session.execute(text(sql), {"title":title, "content":content, "author_id":author_id, "date_added":date_added})
        db.session.commit()
    except:
        return False  
    return True

def edit_post(id, title, content):
    try:   
        sql = """UPDATE post SET title = :title, content = :content WHERE id = :id"""
        db.session.execute(text(sql), {"title":title, "content":content, "id":id})
        db.session.commit()
        return True
    except:
        return False

def delete_post(id):
    try:   
        sql = "DELETE FROM post WHERE id=:id;"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True
    except:
        return False

def get_posts():
    sql = '''SELECT p.id, p.title, p.content, p.author_id, p.date_added, u.username 
            FROM post p JOIN "user" u ON p.author_id=u.id ORDER BY p.date_added DESC'''
    result = db.session.execute(text(sql))
    posts = result.fetchall()
    return posts

def get_user_posts(id):
    sql = '''SELECT p.id, p.title, p.content, p.author_id, p.date_added, u.username 
            FROM post p JOIN "user" u ON p.author_id=u.id WHERE p.author_id=:id ORDER BY p.date_added DESC'''
    result = db.session.execute(text(sql), {"id":id})
    posts = result.fetchall()
    return posts
 
def get_post(id):
    sql = '''SELECT p.id, p.title, p.content, p.author_id, p.date_added, u.username 
            FROM post p JOIN "user" u ON p.author_id=u.id WHERE p.id=:id'''
    result = db.session.execute(text(sql), {"id":id})
    post= result.fetchone()
    return post

def get_followed_posts(id):
    sql = '''SELECT p.id, p.title, p.content, p.author_id, p.date_added, u.username 
            FROM post p JOIN "user" u ON p.author_id=u.id INNER JOIN following f on p.author_id=f.followed_id WHERE f.follower_id=:id ORDER BY p.date_added DESC'''
    result = db.session.execute(text(sql), {"id":id})
    posts = result.fetchall()
    return posts

def get_searched_posts(searched):
    searched = "%" + searched + "%"
    sql = '''SELECT p.id, p.title, p.content, p.author_id, p.date_added, u.username 
            FROM post p JOIN "user" u ON p.author_id=u.id WHERE p.content ILIKE :searched OR p.title ILIKE :searched ORDER BY p.date_added DESC'''
    result = db.session.execute(text(sql), {"searched":searched})
    posts = result.fetchall()
    return posts