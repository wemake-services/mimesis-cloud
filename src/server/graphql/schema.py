import graphene

from mimesis import Generic

from .types import MimesisType


class Mimesis(MimesisType):
    pass


class Query(graphene.ObjectType):
    mimesis = graphene.Field(
        Mimesis,
        required=True,
        locale=graphene.String(),
    )

    def resolve_mimesis(self, context, *args, **kwargs):
        return Generic(context.get('locale', 'en'))


schema = graphene.Schema(query=Query)
