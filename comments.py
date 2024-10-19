from datetime import datetime
from flask import session
from sqlalchemy.sql import text
from app import app
from db import db

def add_comment(content, post_id):
    author_id = session["id"]
    date_added = datetime.now()
    try:   
        sql = """INSERT INTO comment (content, author_id, post_id, date_added)
          VALUES (:content, :author_id, :post_id, :date_added)"""
        db.session.execute(text(sql), {"content":content, "author_id":author_id, "post_id":post_id, "date_added":date_added})
        db.session.commit()
    except:
        return False  
    return True   

def delete_comment(id):
    try:   
        sql = "DELETE FROM comment WHERE id=:id;"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True
    except:
        return False

def get_comment(id):
    sql = '''SELECT c.id, c.content, c.date_added, c.author_id, c.post_id, u.username 
            FROM comment c JOIN "user" u ON c.author_id=u.id WHERE c.id=:id'''
    result = db.session.execute(text(sql), {"id":id})
    comments = result.fetchone()
    return comments

def get_comments(post_id):
    sql = '''SELECT c.id, c.content, c.date_added, c.author_id, u.username 
        FROM comment c JOIN "user" u ON c.author_id=u.id WHERE c.post_id=:post_id ORDER BY c.date_added DESC'''
    result = db.session.execute(text(sql), {"post_id":post_id})
    comments = result.fetchall()
    return comments

def get_user_comments(id):
    sql = '''SELECT c.id, c.content, c.date_added, c.author_id, c.post_id, u.username 
        FROM comment c JOIN "user" u ON c.author_id=u.id WHERE c.author_id=:id ORDER BY c.date_added DESC'''
    result = db.session.execute(text(sql), {"id":id})
    comments = result.fetchall()
    return comments