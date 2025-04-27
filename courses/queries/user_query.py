import graphene

from courses.models import User, Settings
from courses.types.user_type import UserType, UserSettingsType


class UserQuery(graphene.ObjectType):
    """GraphQL representation of the User Model"""
    all_users = graphene.List(UserType)
    user_settings = graphene.Field(UserSettingsType)

    def resolve_all_users(self, info):
        """Fetch all users"""
        return User.objects.all()

    def resolve_user_settings(self, info):
        """Fetch user settings"""
        user = info.context.user
        if user.is_anonymous:
            return None
        try:
            return user.settings
        except Settings.DoesNotExist:
            return None
