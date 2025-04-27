import graphene

from courses import models


class UserRole(graphene.Enum):
    MENTEE = "mentee"
    MENTOR = "mentor"
