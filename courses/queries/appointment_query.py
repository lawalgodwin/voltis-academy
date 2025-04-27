import graphene

from courses.models import Appointment
from courses.types.appointment_type import AppointmentType


class AppointmentQuery(graphene.ObjectType):
    """Appointment Queries"""
    all_appointments = graphene.List(AppointmentType)

    def resolve_all_appointments(self, info):
        return Appointment.objects.all()