from django.dispatch import receiver
from courses.models import Appointment, Notification
from django.db.models.signals import post_save


@receiver(post_save, sender=Appointment)
def initialize_payment(sender, instance: Appointment, created, **kwargs):
    """Initialize payment once booking is created"""
    # appointment_date = (instance.appointment_date).date()
    # appointment_time = (instance.appointment_date).time()
    notification_title = "Video Call Appointment"
    notification_message = "We’ll send you a link to join the call at the booking details."
    if created:
        Notification.objects.create(
            receiver=instance.student,
            subject=notification_title,
            message=notification_message
        )
    # send mail to the instructor
    # send_mail_to(instructor)
