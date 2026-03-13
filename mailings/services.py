from __future__ import annotations

import logging
from random import randint
from time import sleep

logger = logging.getLogger(__name__)


def send_email(*, user_id: str, email: str, subject: str, message: str) -> None:
    """
    Имитация отправки письма.

    В реальной системе здесь была бы интеграция с почтовым провайдером.
    Для целей задания делаем задержку и пишем сообщение в лог.
    """
    delay = randint(5, 20)
    sleep(delay)
    logger.info(
        "Send EMAIL to %s (user_id=%s) with subject=%r after %s seconds. Message: %s",
        email,
        user_id,
        subject,
        delay,
        message,
    )

