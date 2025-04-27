import graphene


class AppointmentStatus(graphene.Enum):
    SCHEDULED = "scheduled",
    CANCELLED = "cancelled",
    COMPLETED = "completed"
