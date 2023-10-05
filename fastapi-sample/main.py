from fastapi import FastAPI

app = FastAPI()

# 実践以下

# 導入
@app.get("/hello")
async def getHello():
    return {"Message":"Hello World"}
# http://localhost:8000/hello

# パスパラメーター
@app.get("/countries/{country}")
async def get(country:str):

    return {"Message": country}
# http://localhost:8000/countries/any

# クエリパラメーター
@app.get("/countries")
async def read_item(country_name:str, city_name:str):
    return {
        "country_name":country_name,
        "city_name":city_name
    }
# http://localhost:8000/countries?country_name=any&city_name=any

