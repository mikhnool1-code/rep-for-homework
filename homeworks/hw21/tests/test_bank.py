import pytest
from loguru import logger
from homeworks.hw21.bank_deposit.bank import Bank
from homeworks.hw21.bank_deposit.currency import CurrencyConverter


@pytest.fixture()
def bank_fixture():
    return Bank()


def test_client_can_be_registered(bank_fixture):
    logger.info("Registering new client with id=1, name=Vasyl")
    result = bank_fixture.register_client("1", "Vasyl")

    logger.debug(f"Current clients: {bank_fixture.clients}")
    assert result is True
    assert bank_fixture.clients["1"] == "Vasyl"


def test_register_existing_client(bank_fixture):
    bank_fixture.register_client("1", "Vasyl")
    logger.info("Trying to register existing client with id=1 again")
    result = bank_fixture.register_client("1", "Maria")

    assert result is False
    assert bank_fixture.clients["1"] == "Vasyl"


def test_open_deposit_success(bank_fixture):
    bank_fixture.register_client("1", "Vasyl")
    result = bank_fixture.open_deposit_account("1", start_balance=1000, years=2)

    logger.debug(f"Opened deposits: {bank_fixture.deposits}")
    assert result is True
    assert "1" in bank_fixture.deposits

    deposit = bank_fixture.deposits["1"]
    assert deposit["balance"] == 1000
    assert deposit["years"] == 2
    assert deposit["interest_rate"] == 10


def test_calc_interest_rate_without_deposit(bank_fixture):
    logger.info("Testing interest rate calculation without deposit")
    result = bank_fixture.calc_interest_rate(1)
    assert result is False


def test_close_deposit_without_deposit(bank_fixture):
    result = bank_fixture.close_deposit(1)
    assert result is False


@pytest.fixture()
def converter_fixture():
    return CurrencyConverter()


def test_currency_is_valid(converter_fixture):
    result, currency = converter_fixture.convert("USD", "BYN", 10)
    logger.debug(f"Converted 10 USD to {result} {currency}")

    assert result == round(10 * 3.267, 2)
    assert currency == "BYN"


def test_currency_is_not_valid(converter_fixture):
    with pytest.raises(ValueError, match="Unsupported currency: CNY"):
        converter_fixture.convert("USD", "CNY", 10)
