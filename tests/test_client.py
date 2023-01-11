
import pytest
import socket


def test_valid_commands():
    commands = ['ping', 'who am i', 'hello server']
    assert set(commands) == set(['ping', 'who am i', 'hello server'])
