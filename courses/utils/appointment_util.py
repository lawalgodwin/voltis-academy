from django.http import Http404
from courses.models import User, Appointment


def book_appointment(**kwargs):
    """Book an appoint for a student with an instructor"""
    try:

        student = User.objects.get(pk=kwargs.get("student_id"))
        instructor = User.objects.get(pk=kwargs.get("instructor_id"))
        appointment_date = kwargs.get("appointment_date")
        appointment = Appointment.objects.create(student=student, instructor=instructor, appointment_date=appointment_date)
        return appointment
    except User.DoesNotExist:
        raise Http404("Instructor or student does not exist")
    except Exception as e:
        raise e
