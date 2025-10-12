class CurrencyConverter:
    def __init__(self):
        self.rates = {
            ("USD", "BYN"): 3.267,
            ("EUR", "BYN"): 3.399,
            ("BYN", "USD"): 1 / 3.267,
            ("BYN", "EUR"): 1 / 3.399,
            ("USD", "EUR"): 3.267 / 3.399,
            ("EUR", "USD"): 3.399 / 3.267,
        }
        self.default_currency = "BYN"

    def convert(self, from_curr, to_curr, amount):
        if from_curr not in {"USD", "BYN", "EUR"}:
            raise ValueError(f"Unsupported currency: {from_curr}")
        if to_curr not in {"USD", "BYN", "EUR"}:
            raise ValueError(f"Unsupported currency: {to_curr}")
        if to_curr is None:
            to_curr = self.default_currency
        rate = self.rates[(from_curr, to_curr)]
        converted_amount = round(amount * rate, 2)
        return converted_amount, to_curr
