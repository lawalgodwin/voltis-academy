import graphene

from courses.models import Course, Enrollment
from courses.types.course_type import CourseType
from courses.types.enrollment_type import EnrollmentType


class CourseQuery(graphene.ObjectType):
    """Course Querries"""
    all_courses = graphene.List(CourseType)
    courses_by_author = graphene.List(CourseType, instructor_id=graphene.UUID(required=True))

    def resolve_all_courses(self, info):
        return Course.objects.all()

    def resolve_courses_by_author(self, info, instructor_id):
        return Course.objects.filter(instructor=instructor_id)
