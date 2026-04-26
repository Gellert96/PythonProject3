

import pytest

from src.decorators import log

# =========================
# ТЕСТ УСПЕШНОГО ВЫЗОВА (консоль)
# =========================


def test_log_success_console(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(1, 2)

    captured = capsys.readouterr()

    assert result == 3
    assert "add ok" in captured.out


# =========================
# ТЕСТ ОШИБКИ (консоль)
# =========================

def test_log_error_console(capsys):
    @log()
    def fail():
        raise ValueError("boom")

    with pytest.raises(ValueError):
        fail()

    captured = capsys.readouterr()

    assert "fail error: ValueError" in captured.out


# =========================
# ТЕСТ ЗАПИСИ В ФАЙЛ (успех)
# =========================


def test_log_success_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def add(x, y):
        return x + y

    add(2, 3)

    content = log_file.read_text(encoding="utf-8")

    assert "add ok" in content


# =========================
# ТЕСТ ЗАПИСИ В ФАЙЛ (ошибка)
# =========================

def test_log_error_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def fail():
        raise RuntimeError("oops")

    with pytest.raises(RuntimeError):
        fail()

    content = log_file.read_text(encoding="utf-8")

    assert "fail error: RuntimeError" in content
