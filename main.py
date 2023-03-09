from fastapi import FastAPI
from redis_om import get_redis_connection
from credentials import redis_password

app = FastAPI()



redis = get_redis_connection(
    host = "redis-11634.c300.eu-central-1-1.ec2.cloud.redislabs.com",
    port = 11634,
    password = redis_password,
    decode_responses = True
)

