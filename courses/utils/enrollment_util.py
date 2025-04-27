from django.http import Http404
from django.shortcuts import get_object_or_404
from courses.models import User, Course, Enrollment


def enroll(**kwargs):
    """Enroll a student for a course"""
    try:
        student = get_object_or_404(User, pk=kwargs.get("student_id"))
        course = get_object_or_404(Course, pk=kwargs.get("course_id"))
        return Enrollment.objects.create(student=student, course=course)
    except User.DoesNotExist:
        raise Http404("Student does not exist")
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
