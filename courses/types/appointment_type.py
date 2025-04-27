
from graphene_django import DjangoObjectType

from courses.models import Appointment


class AppointmentType(DjangoObjectType):

    class Meta:
        model = Appointment
        fields = "__all__"