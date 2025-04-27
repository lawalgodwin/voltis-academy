from django.db import DatabaseError, IntegrityError
from courses.models import User


def create_user(**kwargs) -> User:
    """create a user"""
    try:
        user = User(**kwargs)
        user.set_password(kwargs.get('password'))
        user.save()
        return user
    except IntegrityError as e:
        if "courses_user.email" in str(e):
            raise IntegrityError("Account with the email address already exist")
        raise e
    except DatabaseError as e:
        raise e