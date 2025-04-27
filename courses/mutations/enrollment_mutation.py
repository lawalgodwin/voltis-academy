from django.http import Http404
import graphene
from graphql import GraphQLError

from courses.types.enrollment_type import EnrollmentType
from courses.utils.enrollment_util import enroll


class EnrollmentMutation(graphene.Mutation):
    """Enrollment Mutation"""

    class Arguments:
        course_id = graphene.UUID(required=True)
        student_id = graphene.UUID(required=True)

    enrollment = graphene.Field(EnrollmentType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
            enrollment = enroll(**kwargs)
            return EnrollmentMutation(enrollment=enrollment)
        except Http404 as e:
            raise GraphQLError(f"Course enrollment failed: {e}")
