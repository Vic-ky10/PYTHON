import sys
from pathlib import Path
sys.path.insert(0, r"c:\Users\vigne\OneDrive\Desktop\PYTHON\banck")
import pytest
import bank_project


def test_deposit_and_balance(capsys):
    a = bank_project.BankAccount(10, 'TestA')
    a.deposit(15)
    assert pytest.approx(a.get_balance(), rel=1e-9) == 25.0


def test_withdraw_success(capsys):
    a = bank_project.BankAccount(50, 'TestB')
    a.withdraw(20)
    assert pytest.approx(a.get_balance(), rel=1e-9) == 30.0


def test_withdraw_insufficient_funds(capsys):
    a = bank_project.BankAccount(5, 'TestC')
    with pytest.raises(bank_project.BalanceException):
        a.withdraw(10)


def test_transfer_success():
    a = bank_project.BankAccount(100, 'Alice')
    b = bank_project.BankAccount(0, 'Bob')
    a.transfer_to(b, 40)
    assert pytest.approx(a.get_balance(), rel=1e-9) == 60.0
    assert pytest.approx(b.get_balance(), rel=1e-9) == 40.0


def test_transfer_insufficient_funds():
    a = bank_project.BankAccount(10, 'Small')
    b = bank_project.BankAccount(0, 'Receiver')
    with pytest.raises(bank_project.BalanceException):
        a.transfer_to(b, 100)


def test_transfer_invalid_target():
    a = bank_project.BankAccount(20, 'Source')
    with pytest.raises(TypeError):
        a.transfer_to('not an account', 5)


def test_deposit_negative():
    a = bank_project.BankAccount(0, 'Z')
    with pytest.raises(ValueError):
        a.deposit(-5)


def test_transfer_negative_amount():
    a = bank_project.BankAccount(20, 'Source')
    b = bank_project.BankAccount(0, 'Receiver')
    with pytest.raises(ValueError):
        a.transfer_to(b, -10)
