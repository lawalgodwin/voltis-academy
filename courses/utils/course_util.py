from django.db import DatabaseError, IntegrityError
from django.http import Http404
from courses.models import Course, User
from django.shortcuts import get_object_or_404


def create_course(**kwargs):
    """Create a course and save to database"""
    instructor_id = kwargs.get("instructor_id")
    description = kwargs.get("description")
    title = kwargs.get("title")
    category = kwargs.get("category")
    duration = kwargs.get("duration")
    try:
        instructor = get_object_or_404(User, pk=instructor_id)
        newCourse = Course.objects.create(
            title=title,
            category=category,
            description=description,
            duration=duration,
            instructor=instructor
        )
    except User.DoesNotExist:
        raise Http404("Instructor does not exist")
    except IntegrityError as e:
        if "courses_course.title" in str(e):
            raise IntegrityError("A Course with this Title already exists")
        raise e
    except DatabaseError as e:
        raise e
    return newCourse
