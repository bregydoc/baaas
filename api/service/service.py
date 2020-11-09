from . import schema

# Using Starlette

from starlette.applications import Starlette
# from starlette.responses import JSONResponse
from starlette.routing import Route

# from starlette.graphql import GraphQLApp
from ariadne.asgi import GraphQL


routes = [
    Route('/graphql', GraphQL(schema=schema, debug=True))
]

app = Starlette(debug=True, routes=routes)
