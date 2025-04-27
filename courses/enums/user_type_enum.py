import graphene


class UserRole(graphene.Enum):
    MENTEE = "mentee"
    MENTOR = "mentor"
