import graphene

from courses.models import Enrollment, User
from courses.types.course_type import CourseType
from courses.types.enrollment_type import EnrollmentType


class EnrollmentQuery(graphene.ObjectType):
    """Enrollment Queries"""

    all_enrollments = graphene.List(EnrollmentType)
    my_courses = graphene.List(EnrollmentType)

    def resolve_all_enrollments(self, info):
        """All enrollments"""
        print(info.context.user)
        return Enrollment.objects.all()

    def resolve_my_courses(self, info):
        student = info.context.user
        if student.is_anonymous:
            return None
        my_course_enrollments = Enrollment.objects.filter(student=student, student__role=User.Role.MENTEE)
        return my_course_enrollments