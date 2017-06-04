import graphene

from elizabeth import Generic

from .types import ElizabethType


class Elizabeth(ElizabethType):
    pass


class Query(graphene.ObjectType):
    elizabeth = graphene.Field(
        Elizabeth,
        required=True,
        locale=graphene.String(),
    )

    def resolve_elizabeth(self, context, *args, **kwargs):
        return Generic(context.get('locale', 'en'))


schema = graphene.Schema(query=Query)
