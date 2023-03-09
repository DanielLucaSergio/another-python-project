from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from credentials import *
from starlette.requests import Request
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers = ['*']
)

redis = get_redis_connection(
    host = "redis-11634.c300.eu-central-1-1.ec2.cloud.redislabs.com",
    port = 11634,
    password = redis_password,
    decode_responses = True
)

class Order(HashModel):
    product_id: str
    price: float
    total: float
    quantity: int
    status: str
    class Meta:
        database = redis


@app.post("/orders")
async def create(request: Request):
    body = await request.json()

    req = requests.get('http://localhost:8080/products/%s' % body['id'])
    
    return req.json()
