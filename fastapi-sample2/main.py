from fastapi import FastAPI,Depends,HTTPException

from database_config import SessionLocal
from crud_departments import (get_department as g_dept, get_departments as g_depts, insert_department as i_dept)
from crud_users import ( get_users as g_users, get_user as g_user, insert_user as i_users)
from sqlalchemy.orm import Session
import validation
from typing import List

app = FastAPI()

# DB接続
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#departments

# get
@app.get("/departments",response_model=List[validation.Departments])
async def get_departments(db:Session=Depends(get_db)):
 
    """
        crud_departments.pyの関数でsqlを実行する
        http://localhost:8000/departments
    """
    return g_depts(db=db)



@app.get("/departments/{departments_id}",response_model=validation.Departments)
async def get_department(departments_id:int,db:Session=Depends(get_db)):
    
    """
        crud_departments.pyの関数でsqlを実行する
        パスパラメーターで指定したdepartments_idを使用してレコードを指定する
        http://localhost:8000/departments/any
    """
    try:
        result = g_dept(id=departments_id,db=db)
        if result == None:
            raise HTTPException(status_code=422, detail=f"{departments_id}:Negative values are not accepted")
        return result
    except:
        raise HTTPException(status_code=404,detail= f'{departments_id} is 404 not found')

# insert
@app.post("/departments",response_model=validation.Departments)
async def insert_department(name:str,db:Session=Depends(get_db)):
    """
        crud_departments.pyの関数でsqlを実行する
        POSTで指定したnameでdepartmentsに新たに追加する

        curl -X POST "http://localhost:8000/departments?name=any" -H "accept: application/json"

    """
    return i_dept(name=name,db=db)


#users

# get
@app.get("/users",response_model=List[validation.Users])
async def get_users(db:Session=Depends(get_db)):
 
    """
        crud_users.pyの関数でsqlを実行する
        http://localhost:8000/users
    """
    return g_users(db=db)



@app.get("/users/{users_id}",response_model=validation.Users)
async def get_user(users_id:int,db:Session=Depends(get_db)):
    
    """
        crud_users.pyの関数でsqlを実行する
        パスパラメーターで指定したusers_idを使用してレコードを指定する
        http://localhost:8000/users/any
    """
    try:
        result = g_user(id=users_id,db=db)
        if result == None:
            raise HTTPException(status_code=422, detail=f"{users_id}:Negative values are not accepted")
        return result
    except:
        raise HTTPException(status_code=404,detail= f'{users_id} is 404 not found')
    

# insert
@app.post("/users",response_model=validation.UsersInsert)
async def insert_user(user_name:str, departments_id:int, db:Session=Depends(get_db)):
    """
        crud_users.pyの関数でsqlを実行する
        POSTでクエリパラメーターで指定したnameとdepartments_idで新たに追加する

        curl -X POST "http://localhost:8000/users?user_name=any&departments_id=1" -H "accept: application/json"

    """
    return i_users(user_name=user_name, departments_id=departments_id, db=db)


