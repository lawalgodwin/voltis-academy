from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from courses.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        MENTEE = "mentee",
        MENTOR = "mentor"

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True)
    role = models.CharField(choices=Role, default=Role.MENTEE, max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email


class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    enrollment_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course.title}"


class Appointment(models.Model):

    class AppointmentStatus(models.TextChoices):
        SCHEDULED = "scheduled",
        CONFIRM = "confirm",
        CANCELLED = "cancelled",
        COMPLETED = "completed"

    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, related_name='instructor_appointments', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(choices=AppointmentStatus, default=AppointmentStatus.SCHEDULED, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment with {self.instructor.first_name} {self.instructor.last_name}"


class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    receiver = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    # sender = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.receiver.email}: {self.receiver.first_name} {self.receiver.last_name}"


class Settings(models.Model):
    settings_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, related_name='settings', on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)
    date_format = models.CharField(max_length=50)
    notification_preferences = models.JSONField(default=dict)

    def __str__(self):
        return f"Settings for {self.user.email}: {self.user.first_name} {self.user.last_name}"
