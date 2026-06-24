import logging

from login_system import log_event


def test_log_success(caplog):

    with caplog.at_level(logging.INFO):

        log_event("Andrii", "success")

    assert "Login event - Username: Andrii, Status: success" in caplog.text


def test_log_expired(caplog):

    with caplog.at_level(logging.WARNING):

        log_event("Andrii", "expired")

    assert "Login event - Username: Andrii, Status: expired" in caplog.text


def test_log_failed(caplog):

    with caplog.at_level(logging.ERROR):

        log_event("Andrii", "failed")

    assert "Login event - Username: Andrii, Status: failed" in caplog.text