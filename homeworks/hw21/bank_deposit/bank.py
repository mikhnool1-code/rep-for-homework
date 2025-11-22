from homeworks.hw21.bank_deposit.currency import CurrencyConverter


class Bank:
    def __init__(self):
        self.currency_converter = CurrencyConverter()
        self.clients = {}
        self.deposits = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            return False
        self.clients[client_id] = name
        return True

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients or client_id in self.deposits:
            return False
        if start_balance <= 0 or years <= 0:
            return False
        self.deposits[client_id] = {
            "balance": start_balance,
            "years": years,
            "interest_rate": 10
        }
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.deposits:
            return False
        deposit = self.deposits[client_id]
        balance = deposit["balance"]
        interest_rate = deposit["interest_rate"] / 100
        months = deposit["years"] * 12
        final_balance = balance * (1 + interest_rate / 12) ** months
        return round(final_balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposits:
            return False
        final_balance = self.calc_interest_rate(client_id)
        del self.deposits[client_id]
        return final_balance

    def exchange_currency(self, from_curr, amount, to_curr):
        return self.currency_converter.convert(from_curr, to_curr, amount)
