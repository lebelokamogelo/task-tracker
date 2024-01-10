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


class CreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        completed = graphene.Boolean(required=True)
        priority = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    def mutate(self, info, title, description, completed, priority):
        todo = Todo(user=info.context.user, title=title, description=description, completed=completed,
                    priority=priority)
        todo.save()

        return CreateMutation(todo=todo)


class UpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        description = graphene.String()
        completed = graphene.Boolean()
        priority = graphene.String()

    todo = graphene.Field(TodoType)

    def mutate(self, info, id, title=None, description=None, completed=None, priority=None):
        todo = Todo.objects.get(user=info.context.user, id=id)

        todo.title = title if title else todo.title
        todo.description = description if description else todo.description
        todo.completed = completed if completed else todo.completed
        todo.priority = priority if priority else todo.priority
        todo.save()

        return UpdateMutation(todo=todo)


class DeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(self, info, id):
        todo = Todo.objects.get(user=info.context.user, id=id)

        todo.delete()
        return DeleteMutation(success=True)


class Mutation(graphene.ObjectType):
    create = CreateMutation.Field()
    update = UpdateMutation.Field()
    delete = DeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
