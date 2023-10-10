from fastapi import FastAPI,Depends,HTTPException

from database_config import SessionLocal
from crud_departments import (get_departments, get_department, insert_department)
from crud_users import ( get_users, get_user, insert_user)
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
async def index_departments(db:Session=Depends(get_db)):
 
    """
        crud_departments.pyの関数でsqlを実行する
        http://localhost:8000/departments
    """
    return get_departments(db=db)



@app.get("/departments/{departments_id}",response_model=validation.Departments)
async def index_department(departments_id:int,db:Session=Depends(get_db)):
    
    """
        crud_departments.pyの関数でsqlを実行する
        パスパラメーターで指定したdepartments_idを使用してレコードを指定する
        http://localhost:8000/departments/any
    """
    try:
        result = get_department(id=departments_id,db=db)
        if result == None:
            raise HTTPException(status_code=422, detail=f"{departments_id}:Negative values are not accepted")
        return result
    except:
        raise HTTPException(status_code=404,detail= f'{departments_id} is 404 not found')

# insert
@app.post("/departments",response_model=validation.Departments)
async def index_department(name:str,db:Session=Depends(get_db)):
    """
        crud_departments.pyの関数でsqlを実行する
        POSTで指定したnameでdepartmentsに新たに追加する

        curl -X POST "http://localhost:8000/departments?name=any" -H "accept: application/json"

    """
    return insert_department(name=name,db=db)


#users

# get
@app.get("/users",response_model=List[validation.Users])
async def index_users(db:Session=Depends(get_db)):
 
    """
        crud_users.pyの関数でsqlを実行する
        http://localhost:8000/users
    """
    return get_users(db=db)



@app.get("/users/{users_id}",response_model=validation.Users)
async def index_user(users_id:int,db:Session=Depends(get_db)):
    
    """
        crud_users.pyの関数でsqlを実行する
        パスパラメーターで指定したusers_idを使用してレコードを指定する
        http://localhost:8000/users/any
    """
    try:
        result = get_user(id=users_id,db=db)
        if result == None:
            raise HTTPException(status_code=422, detail=f"{users_id}:Negative values are not accepted")
        return result
    except:
        raise HTTPException(status_code=404,detail= f'{users_id} is 404 not found')
    

# insert
@app.post("/users",response_model=validation.UsersInsert)
async def index_user(user_name:str, departments_id:int, db:Session=Depends(get_db)):
    """
        crud_users.pyの関数でsqlを実行する
        POSTでクエリパラメーターで指定したnameとdepartments_idで新たに追加する

        curl -X POST "http://localhost:8000/users?user_name=any&departments_id=1" -H "accept: application/json"

    """
    return insert_user(user_name=user_name, departments_id=departments_id, db=db)


