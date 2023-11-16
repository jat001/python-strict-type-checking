# python-strict-type-checking

Testing strict type checking in Python.

FastAPI (based on Pydantic) + Strawberry (GraphQL library) + SqlAlchemy (ORM) + Pyright (static type checking) + Ruff (linting & formatting)

```shell
curl 'http://127.0.0.1:8000/graphql' \
  -X POST -H "content-type: application/json" \
  -d '{"query": "mutation { createUser ( name: \"foobar\", password: \"my_password\" ) }"}'
# {"data": {"createUser": "29a86a7e841411eea3b18cc681138fcf"}}

curl 'http://127.0.0.1:8000/graphql' \
  -X POST -H "content-type: application/json" \
  -d '{"query": "query { listUsers { id, name } }"}'
# {"data": {"listUsers": [{"id": "bc60a3f7840a11ee9a1f8cc681138fcf", "name": "foobar"}, {"id": "29a86a7e841411eea3b18cc681138fcf", "name": "foobar"}]}}

curl 'http://127.0.0.1:8000/graphql' \
  -X POST -H "content-type: application/json" \
  -d '{"query": "query { getUser ( id: \"29a86a7e841411eea3b18cc681138fcf\" ) { id, name } }"}'
# {"data": {"getUser": {"id": "29a86a7e841411eea3b18cc681138fcf", "name": "foobar"}}}
```
