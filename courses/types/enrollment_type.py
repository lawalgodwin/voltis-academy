from graphene_django import DjangoObjectType

from courses.models import Enrollment


class EnrollmentType(DjangoObjectType):
    class Meta:
        model = Enrollment
        fields = "__all__"
