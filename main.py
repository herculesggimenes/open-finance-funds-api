from typing import Optional

import uvicorn
from fastapi import FastAPI

from base_service import BaseService

app = FastAPI()
base_service = BaseService()

@app.get("/")
def read_root():
    df_fundos = base_service.get_fundos()
    return df_fundos.to_dict(orient='list')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8999)