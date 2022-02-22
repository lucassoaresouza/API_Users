from typing import Dict

from fastapi import FastAPI, HTTPException

from customers.enums import Regions, Classifications
from customers.initializer import initialize as customer_initializer
from customers.models import Paginator
from customers.pagination import CustomerPagination

app = FastAPI()

application_data: Dict = {}


@app.on_event("startup")
async def startup_event():
    """
    Initialize the required data.
    """
    application_data['Costumers'] = customer_initializer()


@app.get("/")
def healthcheck():
    """
    Checks if the API is online.
    """
    return {"status": "ok"}


@app.get("/customers/")
async def customers_by_region(
    country: str,
    region: Regions,
    classification: Classifications,
    page: int = 0
) -> Paginator:
    """
    Read and filter Customers view.
    :param country: The string with the country code. I.e.: 'BR'
    :param region: The selected region. A Regions instance.
    :param classification: A Classification instance.
    :param page: The actual page number.
    """
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

    filtered_customers = customers[country][region][classification]
    return CustomerPagination(
        customers=filtered_customers, page_number=page).paginate()
