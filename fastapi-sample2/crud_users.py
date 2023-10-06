from sqlalchemy.orm import Session
from sqlalchemy.sql import text


#users
#get
# 全データを取得する
def get_users(db: Session):
    sql = text("select * from users;")
    return db.execute(sql).all()

# 一部データのみ取得する
def get_user(id:int, db:Session):
    sql = text(f"select * from users where id = {id}")
    return db.execute(sql).one()


#post
def insert_user(user_name:str,departments_id:int, db:Session):
    sql = text(f"insert into users (user_name,departments_id) values('{user_name}','{departments_id}');")
    db.execute(sql)
    db.commit()

    sql2 = text("select * from users order by id desc")

    return db.execute(sql2).first()


