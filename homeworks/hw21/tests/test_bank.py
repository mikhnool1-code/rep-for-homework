import pytest
from loguru import logger
from homeworks.hw21.bank_deposit.bank import Bank
from homeworks.hw21.bank_deposit.currency import CurrencyConverter


@pytest.fixture()
def bank():
    return Bank()


def test_client_can_be_registered(bank):
    logger.info("Registering new client with id=1, name=Vasyl")
    result = bank.register_client("1", "Vasyl")

    logger.debug(f"Current clients: {bank.clients}")
    assert result is True
    assert bank.clients["1"] == "Vasyl"


def test_register_existing_client(bank):
    bank.register_client("1", "Vasyl")
    logger.info("Trying to register existing client with id=1 again")
    result = bank.register_client("1", "Maria")

    assert result is False
    assert bank.clients["1"] == "Vasyl"


def test_open_deposit_success(bank):
    bank.register_client("1", "Vasyl")
    result = bank.open_deposit_account("1", start_balance=1000, years=2)

    logger.debug(f"Opened deposits: {bank.deposits}")
    assert result is True
    assert "1" in bank.deposits

    deposit = bank.deposits["1"]
    assert deposit["balance"] == 1000
    assert deposit["years"] == 2
    assert deposit["interest_rate"] == 10


def test_calc_interest_rate_without_deposit(bank):
    logger.info("Testing interest rate calculation without deposit")
    result = bank.calc_interest_rate(1)
    assert result is False


def test_close_deposit_without_deposit(bank):
    result = bank.close_deposit(1)
    assert result is False


@pytest.fixture()
def converter():
    return CurrencyConverter()


def test_currency_is_valid(converter):
    result, currency = converter.convert("USD", "BYN", 10)
    logger.debug(f"Converted 10 USD to {result} {currency}")

    assert result == round(10 * 3.267, 2)
    assert currency == "BYN"


def test_currency_is_not_valid(converter):
    with pytest.raises(ValueError, match="Unsupported currency: CNY"):
        converter.convert("USD", "CNY", 10)
