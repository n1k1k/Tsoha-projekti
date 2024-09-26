from datetime import datetime
from app import app
from db import db
from sqlalchemy.sql import text

def add_comment(content, author_id, post_id):
    date_added = datetime.now()
    try:   
        sql = """INSERT INTO comment (content, author_id, post_id, date_added)
          VALUES (:content, :author_id, :post_id, :date_added)"""
        db.session.execute(text(sql), {"content":content, "author_id":author_id, "post_id":post_id, "date_added":date_added})
        db.session.commit()
    except:
        return False  
    return True


def get_comments(post_id):
    sql = 'SELECT c.content, c.date_added, c.author_id, u.username FROM comment c JOIN "user" u ON c.author_id=u.id WHERE c.post_id=:post_id'
    result = db.session.execute(text(sql), {"post_id":post_id})
    comments = result.fetchall()
    return comments

def add_post(title, content, author, author_id):
    date_added = datetime.now()
    try:   
        sql = """INSERT INTO post (title, content, author, author_id, date_added)
          VALUES (:title, :content, :author, :author_id, :date_added)"""
        db.session.execute(text(sql), {"title":title, "content":content, "author":author, "author_id":author_id, "date_added":date_added})
        db.session.commit()
    except:
        return False  
    return True

def edit_post(id, title, content):
    try:   
        sql = """UPDATE post SET title = :title, content = :content WHERE id = :id"""
        db.session.execute(text(sql), {"title":title, "content":content, "id":id})
        db.session.commit()
    except:
        return False
    return True

def delete_post(id):
    try:   
        sql = "DELETE FROM post WHERE id=:id;"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
    except:
        return False
    return True

def get_posts():
    sql = "SELECT id, title, content, author, author_id,  date_added FROM post"
    result = db.session.execute(text(sql))
    posts = result.fetchall()
    return posts

def get_user_posts(id):
    sql = "SELECT id, title, content, author, author_id,  date_added FROM post WHERE author_id=:id"
    result = db.session.execute(text(sql), {"id":id})
    posts = result.fetchall()
    return posts
 
def get_post(id):
    sql = "SELECT id, title, content, author, author_id, date_added FROM post WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    post= result.fetchone()
    return post