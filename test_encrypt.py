import pytest
import encrypt
from unittest.mock import MagicMock


@pytest.fixture()
def mock_input():
    return MagicMock()


def test_return_value_from_encrypt_message_for_single_message(mock_input, monkeypatch):
    mock_input.side_effect = ["1", "3 A"]
    monkeypatch.setattr('builtins.input', mock_input)
    assert encrypt.encrypt_message() == ['A']


def test_return_value_from_encrypt_message_for_multi_message(mock_input, monkeypatch):
    mock_input.side_effect = ["2", "3 A", "-1 A"]
    monkeypatch.setattr('builtins.input', mock_input)
    assert encrypt.encrypt_message() == ['A', '295']

