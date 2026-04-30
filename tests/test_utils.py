import json

from src.utils import load_operations


def test_load_operations_success(tmp_path):
    file = tmp_path / "test.json"
    data = [{"id": 1}, {"id": 2}]

    file.write_text(json.dumps(data), encoding="utf-8")

    result = load_operations(str(file))

    assert result == data


def test_load_operations_file_not_found():
    result = load_operations("no_file.json")
    assert result == []


def test_load_operations_not_list(tmp_path):
    file = tmp_path / "test.json"
    file.write_text(json.dumps({"id": 1}), encoding="utf-8")

    result = load_operations(str(file))

    assert result == []


def test_load_operations_empty_file(tmp_path):
    file = tmp_path / "test.json"
    file.write_text("", encoding="utf-8")

    result = load_operations(str(file))

    assert result == []
