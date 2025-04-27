from graphene_django import DjangoObjectType
from courses.models import Settings, User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("user_id", "first_name", "last_name", "email", "role")
        convert_choices_to_enum = False


class UserSettingsType(DjangoObjectType):
    class Meta:
        model = Settings
        fields = "__all__"
        convert_choices_to_enum = False
