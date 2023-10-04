from fastapi import FastAPI

app = FastAPI()

# json読み込み準備
import json
with open('./sample.json', 'r') as temp:
    sample_data = json.load(temp)



# モックを使ってデータ処理以下


# 型チェック用の定義
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    Message: str

class Items(BaseModel):
    data:List[Item]

# データの取得

@app.get("/items",response_model=Items)
async def get_messages():
    """
        型チェック(Items)をしてデータを返す

        http://localhost:8000/items
    """
    return sample_data


@app.get("/item/{id}",response_model=Item)
async def get_item(id:int):
    """
        jsonデータからパスパラメーターで要素を指定して返す    
    
    
        http://localhost:8000/item/0
        http://localhost:8000/item/1
        http://localhost:8000/item/2
    """

    return sample_data["data"][id]


# データの挿入

@app.post("/item/append",response_model=Item)
async def create(item:Item):
    """
        postをするとsample_dataに追加して送られたものを返す

        curl -X 'POST' \
        'http://localhost:8000/item/append' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{"Message": "ここに追加したいメッセージを入れる"}'


    """

    sample_data["data"].append({"Message":item.Message})

    return {"Message":item.Message}


# データの更新

@app.patch("/item/update/{id}",response_model=Item)
async def update(id:int, item: Item):
    """
        パスパラメーターで変更したい箇所を受け取り、
        sample_data変数を更新してその箇所を返す

        curl -X 'PATCH' \
        'http://localhost:8000/item/update/1' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{"Message": "更新後のメッセージ内容"}'

    """

    sample_data["data"][id] = {"Message": item.Message}

    return sample_data["data"][id]

# データの削除

@app.delete("/item/delete/{id}",response_model=Items)
async def delete(id:int):
    """
        パスパラメーターで削除したい箇所を受け取り
        削除してsample_data変数を返す

        curl -X 'DELETE' \
        'http://localhost:8000/item/delete/1' \
        -H 'accept: application/json'

    """

    sample_data["data"].pop(id)

    return sample_data