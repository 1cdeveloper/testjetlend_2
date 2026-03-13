from __future__ import annotations

from pathlib import Path

import pytest
from django.core.management import call_command

from openpyxl import Workbook

from mailings.models import MailingRecord


def _create_xlsx(tmp_path: Path, rows: list[dict[str, str]]) -> Path:
    wb = Workbook()
    ws = wb.active
    headers = ["external_id", "user_id", "email", "subject", "message"]
    ws.append(headers)
    for row in rows:
        ws.append([row[h] for h in headers])
    path = tmp_path / "mailings.xlsx"
    wb.save(path)
    return path


@pytest.mark.django_db
def test_import_mailings_creates_records_and_skips_duplicates(tmp_path, monkeypatch):
    
    def fake_send_email(*, user_id: str, email: str, subject: str, message: str) -> None:
        return None

    monkeypatch.setattr(
        "mailings.management.commands.import_mailings.send_email",
        fake_send_email,
    )

    path = _create_xlsx(
        tmp_path,
        [
            {
                "external_id": "1",
                "user_id": "42",
                "email": "user1@example.com",
                "subject": "Hello",
                "message": "World",
            },
            {
                "external_id": "1",  # дубликат
                "user_id": "43",
                "email": "user2@example.com",
                "subject": "Hi",
                "message": "There",
            },
        ],
    )

    call_command("import_mailings", str(path))

    assert MailingRecord.objects.count() == 1
    record = MailingRecord.objects.get()
    assert record.external_id == "1"
    assert record.email == "user1@example.com"

