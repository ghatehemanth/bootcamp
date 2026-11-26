from datetime import date
from enum import Enum

from pydantic import BaseModel, Field, field_validator

class ServiceType(str, Enum):
    INSTALLATION = "Installation"
    REPAIR = "Repair"
    MAINTENANCE = "Maintenance"


class TicketStatus(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"

class Ticket(BaseModel):
    ticket_id: int = Field(gt=0)
    customer_name: str
    service_type: ServiceType
    issue_date: date
    status: TicketStatus

    @field_validator("customer_name")
    @classmethod
    def validate_customer_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Customer name cannot be empty")

        return value

