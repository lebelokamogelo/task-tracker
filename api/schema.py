import graphene
from graphene_django.types import DjangoObjectType

from .models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = "__all__"


class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(self, info):
        request = info.context

        return Todo.objects.filter(user=request.user)


schema = graphene.Schema(query=Query)
