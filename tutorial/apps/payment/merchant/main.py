from .credentials import PaycomAuthorization
import requests


class MerchantAPI(PaycomAuthorization):

    def __init__(self) -> None:
        self.URL = "https://checkout.test.paycom.uz/api"

    def card_create(self, number, expire):
        payload = {
            "method": "cards.create",
            "params": {
                "card": {"number": number, "expire": expire},
                "amount": 0,
                "save": True
            }
        }
        response_data = requests.post(self.URL, json=payload, headers=self.authorization())
        response = response_data.json()
        if 'error' in response:
            return response
        # token = response['result']['card']['token']
        return response

    def check_perform_transaction(self):

        return dict(allow=True, auth=self.AUTH)

    def create_transaction(self):
        pass

    def perform_transaction(self):
        pass

    def cancel_transaction(self):
        pass

    def check_transaction(self):
        pass

    def change_password(self):
        pass

    def get_statement(self):
        pass