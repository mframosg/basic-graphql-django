import graphene

class Query(graphene.ObjectType):
    men = graphene.List(graphene.String)
    women = graphene.List(graphene.String)

    def resolve_men(self, info):
        return ["Juan", "Pedro", "Pablo", "Jose"]

    def resolve_women(self, info):
        return ["Maria"]

schema = graphene.Schema(query=Query)