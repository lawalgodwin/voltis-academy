import graphene

from courses.mutations.appointment_mutation import AppointmentMutation, AppointmentUpdateMutation
from courses.mutations.auth_mutation import AuthMutation
from courses.mutations.enrollment_mutation import EnrollmentMutation
from courses.mutations.user_mutation import SettingsMutation, UpdateNotificationPreferences
from courses.queries.appointment_query import AppointmentQuery
from courses.queries.enrollment_query import EnrollmentQuery
from courses.queries.user_query import UserQuery

from .queries.course_query import CourseQuery
from .mutations.course_mutation import CourseUpdateMutation, CreateCourse


class Query(
    CourseQuery,
    UserQuery,
    EnrollmentQuery,
    AppointmentQuery
):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    create_course = CreateCourse.Field()
    enroll_for_course = EnrollmentMutation.Field()
    book_appointment = AppointmentMutation.Field()
    update_appointment = AppointmentUpdateMutation.Field()
    update_course = CourseUpdateMutation.Field()
    create_or_update_settings = SettingsMutation.Field()
    update_notification_preferences = UpdateNotificationPreferences.Field()
    pass
