from sanic_graphql import GraphQLView

from server.graphql.schema import schema

view = GraphQLView.as_view(schema=schema, graphiql=True)
