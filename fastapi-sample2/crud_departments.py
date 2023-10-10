from sqlalchemy.orm import Session
from sqlalchemy.sql import text

#departments
#get
# 全データを取得する
def get_departments(db: Session):
    sql = text("select * from departments;")
    return db.execute(sql).all()

# 一部データのみ取得する
def get_department(id:int, db:Session):
    sql = text(f"select * from departments where id = {id}")
    return db.execute(sql).one()


#post
def insert_department(name:str, db:Session):
    sql = text(f"insert into departments (name) values('{name}');")
    db.execute(sql)
    db.commit()

    sql2 = text("select * from departments order by id desc")

    return db.execute(sql2).first()