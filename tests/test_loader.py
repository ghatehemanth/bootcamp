
from tickets.loader import load_tickets


def test_load_valid_ticket(tmp_path):
    csv_file = tmp_path / "valid_tickets.csv"

    csv_file.write_text(
        "ticket_id,customer_name,service_type,issue_date,status\n"
        "1001,Rahul Sharma,Repair,2026-11-20,Open\n",
        encoding="utf-8"
    )

    valid, invalid = load_tickets(csv_file)

    assert len(valid) == 1
    assert len(invalid) == 0
    assert valid[0].ticket_id == 1001


def test_missing_field(tmp_path):
    csv_file = tmp_path / "missing_field.csv"

    csv_file.write_text(
        "ticket_id,customer_name,service_type,issue_date\n"
        "1001,Rahul Sharma,Repair,2026-11-20\n",
        encoding="utf-8"
    )

    valid, invalid = load_tickets(csv_file)

    assert len(valid) == 0
    assert len(invalid) == 1


def test_invalid_date(tmp_path):
    csv_file = tmp_path / "invalid_date.csv"

    csv_file.write_text(
        "ticket_id,customer_name,service_type,issue_date,status\n"
        "1001,Rahul Sharma,Repair,not-a-date,Open\n",
        encoding="utf-8"
    )

    valid, invalid = load_tickets(csv_file)

    assert len(valid) == 0
    assert len(invalid) == 1


def test_invalid_enum(tmp_path):
    csv_file = tmp_path / "invalid_enum.csv"

    csv_file.write_text(
        "ticket_id,customer_name,service_type,issue_date,status\n"
        "1001,Rahul Sharma,Cleaning,2026-11-20,Open\n",
        encoding="utf-8"
    )

    valid, invalid = load_tickets(csv_file)

    assert len(valid) == 0
    assert len(invalid) == 1


def test_empty_csv(tmp_path):
    csv_file = tmp_path / "empty.csv"

    csv_file.write_text(
        "ticket_id,customer_name,service_type,issue_date,status\n",
        encoding="utf-8"
    )

    valid, invalid = load_tickets(csv_file)

    assert len(valid) == 0
    assert len(invalid) == 0

