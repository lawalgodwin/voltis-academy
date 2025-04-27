from django.http import Http404
import graphene
from graphene_django.rest_framework.mutation import SerializerMutation
from graphql import GraphQLError
from courses.serializers import AppointmentSerializer
from courses.types.appointment_type import AppointmentType
from courses.utils.appointment_util import book_appointment


class AppointmentMutation(graphene.Mutation):

    class Arguments:
        student_id = graphene.UUID(required=True)
        instructor_id = graphene.UUID(required=True)
        appointment_date = graphene.DateTime(required=True)
    
    appointment = graphene.Field(AppointmentType)
    
    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
            appointment = book_appointment(**kwargs)
            return AppointmentMutation(appointment=appointment)
        except Http404 as e:
            raise GraphQLError(f"Appointment booking failed {e}")
        except Exception as e:
            raise GraphQLError(f"Appointment booking failed {e}")


class AppointmentUpdateMutation(SerializerMutation):
    class Meta:
        serializer_class = AppointmentSerializer
        model_operations = ['update']
        lookup_field = 'appointment_id'
    
    @classmethod
    def perform_mutate(cls, serializer, info):
        return super().perform_mutate(serializer, info)
