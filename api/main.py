from typing import Dict

from fastapi import FastAPI, HTTPException
from customers.initializer import initialize as customer_initializer
from customers.enums import Regions, Classifications

app = FastAPI()

application_data: Dict = {}


@app.on_event("startup")
async def startup_event():
    application_data['Costumers'] = customer_initializer()


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.get("/customers/")
async def customers_by_region(
    country: str, region: Regions, classification: Classifications
):
    customers = application_data['Costumers']
    if not customers.get(country):
        msg = f"Não foram encontrados clientes com desse país [{country}]"
        raise HTTPException(status_code=404, detail=msg)

    if not customers[country].get(region):
        msg = f"Não foram encontrados clientes com dessa região [{region}]"
        raise HTTPException(status_code=404, detail=msg)

    if not customers[country][region].get(classification):
        msg = (
            "Não foram encontrados clientes com essa "
            f"classificação [{classification}]")
        raise HTTPException(status_code=404, detail=msg)

    return customers[country][region][classification]
