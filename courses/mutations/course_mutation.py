from django.db import DatabaseError, IntegrityError
from django.http import Http404
from graphene_django.rest_framework.mutation import SerializerMutation
import graphene
from graphql import GraphQLError
from courses.serializers import CourseSerializer
from courses.types.course_type import CourseType
from courses.utils.course_util import create_course


class CreateCourse(graphene.Mutation):
    """Course Mutations"""
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        instructor_id = graphene.UUID(required=True)
        category = graphene.String(required=True)
        duration = graphene.String(required=True)
    course = graphene.Field(CourseType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        try:
            newCourse = create_course(**kwargs)
            return CreateCourse(course=newCourse)
        except Http404 as e:
            raise GraphQLError(f"Failed to create course: {e}")
        except IntegrityError as e:
            raise GraphQLError(f"Failed to create course: {e}")
        except DatabaseError as e:
            raise GraphQLError(f"Failed to create course: {e}")


class CourseUpdateMutation(SerializerMutation):
    class Meta:
        serializer_class = CourseSerializer
        model_operations = ['update']
        lookup_field = 'course_id'
    
    @classmethod
    def perform_mutate(cls, serializer, info):
        return super().perform_mutate(serializer, info)
