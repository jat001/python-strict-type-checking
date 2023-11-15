import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from models.strawberry import Mutation, Query


def init(app: FastAPI):
    schema = strawberry.Schema(Query, Mutation)
    graphql_app = GraphQLRouter(schema)  # pyright: ignore[reportUnknownVariableType]

    app.include_router(graphql_app, prefix="/graphql")  # pyright: ignore[reportUnknownArgumentType]
