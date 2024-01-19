import graphene
import graphql_jwt
from graphene_django.types import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from .models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = "__all__"


class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(self, info):
        request = info.context

        if not request.user.is_authenticated:
            raise GraphQLError('User is not authenticated')

        return Todo.objects.filter(user=request.user)


class CreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        completed = graphene.Boolean(required=True)
        priority = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    @login_required
    def mutate(self, info, title, description, completed, priority):
        request = info.context

        if not request.user.is_authenticated:
            raise GraphQLError('User is not authenticated')

        todo = Todo(user=request.user, title=title, description=description,
                    completed=completed,
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

    @login_required
    def mutate(self, info, id, title=None, description=None,
               completed=None, priority=None):
        request = info.context

        if not request.user.is_authenticated:
            raise GraphQLError('User is not authenticated')

        todo = Todo.objects.get(user=request.user, id=id)

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

    @login_required
    def mutate(self, info, id):
        request = info.context

        if not request.user.is_authenticated:
            raise GraphQLError('User is not authenticated')

        todo = Todo.objects.get(user=request.user, id=id)

        todo.delete()
        return DeleteMutation(success=True)


class Mutation(graphene.ObjectType):
    create = CreateMutation.Field()
    update = UpdateMutation.Field()
    delete = DeleteMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
