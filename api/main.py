from typing import Dict

from fastapi import FastAPI
from customers.initializer import initialize as customer_initializer


app = FastAPI()

application_data: Dict = {}


@app.on_event("startup")
async def startup_event():
    application_data['Costumers'] = customer_initializer()


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.get("/customers")
async def all_customers():
    return application_data['Costumers']


@app.get("/customers/{item_id}")
async def read_customers(item_id: str):
    return application_data['Costumers'][int(item_id)-1]
