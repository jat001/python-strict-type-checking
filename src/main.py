from fastapi import FastAPI

from apps import graphql

app = FastAPI()
graphql.init(app)
