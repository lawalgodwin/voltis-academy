from django.db import DatabaseError, IntegrityError
import graphene
from graphql import GraphQLError
from graphene_django.rest_framework.mutation import SerializerMutation
from courses.enums.user_type_enum import UserRole
from courses.models import Settings
from courses.serializers import SettingsSerializer
from courses.types.user_type import UserSettingsType, UserType
from courses.utils.user_util import create_user


class CreateUser(graphene.Mutation):

    class Arguments:
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        password = graphene.String(required=True)
        role = graphene.Argument(UserRole)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
            newUser = create_user(**kwargs)
            return CreateUser(user=newUser)
        except IntegrityError as e:
            raise GraphQLError(f"Failed to create user: {e}")


class SettingsMutation(SerializerMutation):
    class Meta:
        serializer_class = SettingsSerializer
        model_operations = ['create', 'update']
        lookup_field = 'settings_id'


class UpdateNotificationPreferences(graphene.Mutation):
    class Arguments:
        user_id = graphene.UUID(required=True)
        notification_preferences = graphene.JSONString(required=True)

    settings = graphene.Field(UserSettingsType)

    def mutate(self, info, user_id, notification_preferences):
        try:
            settings = Settings.objects.get(user=user_id)
            settings.notification_preferences = notification_preferences
            settings.save()
            return UpdateNotificationPreferences(settings=settings)
        except Settings.DoesNotExist:
            return None
