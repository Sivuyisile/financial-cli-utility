import pytest

from decimal import Decimal

from income import get_income

def test_get_income_valid_first_attempt(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda prompt: '35080.50')

    result = get_income()

    assert isinstance(result, Decimal), 'A decimal value is expected.'
    assert result == Decimal('35080.50'), f'Expected 35080.50, got {result}'


def test_get_income_negative_then_valid(monkeypatch):

    simulated_income_inputs = iter(['-10234','21020'])

    monkeypatch.setattr('builtins.input', lambda prompt: next(simulated_income_inputs))

    result = get_income()

    #assert that 'condition', and if not, then message
    assert isinstance(result, Decimal), 'A decimal value is expected'
    assert result >= Decimal('0.00'), f'Expected 0.00, got {result}'


def test_get_income_string_then_valid(monkeypatch):

    simulated_income_inputs = iter(['nunya', '1500.50'])

    monkeypatch.setattr('builtins.input', lambda prompt: next(simulated_income_inputs))

    result = get_income()

    assert isinstance(result, Decimal), 'A decimal value is expected.'
    assert result == Decimal('1500.50'), f'Expected 1500.50, got {result}'


def test_get_income_decimal_precision(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda prompt: '35080.58')

    result = get_income()

    assert result.as_tuple().exponent == -2, f'A 2 decimal precision number expected, got {result}'
    assert result == Decimal('35080.58'), f'Expected 35080.58, got {result}'
