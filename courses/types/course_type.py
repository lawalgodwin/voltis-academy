from graphene_django import DjangoObjectType

from courses.models import Course


class CourseType(DjangoObjectType):
    """GraphQL representation of the Course Model"""

    class Meta:
        model = Course
        fields = "__all__"
