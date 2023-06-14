from graphene import Schema
from .query import Query
from .mutation import Mutation
#from models.query import Query
#from models.mutation import Mutation

schema = Schema(query=Query, mutation=Mutation)
