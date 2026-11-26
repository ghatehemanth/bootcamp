import csv
import logging
from pathlib import Path

from pydantic import ValidationError

from .models import Ticket

logger = logging.getLogger(__name__)

def load_tickets(file_path: Path) -> tuple[list[Ticket], list[dict]]:
    valid_tickets = []
    invalid_rows = []
    with file_path.open(mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row_number, row in enumerate(reader, start=2):
            try:
                ticket = Ticket(**row)
                valid_tickets.append(ticket)
                logger.info("Valid ticket: %s", ticket.ticket_id)
            except ValidationError as error:
                invalid_rows.append({
                    "row": row_number,
                    "error": str(error)
                })
                logger.warning("Invalid row %s: %s", row_number, error)
    return valid_tickets, invalid_rows

    