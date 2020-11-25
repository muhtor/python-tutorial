import base64


class PaycomAuthorization:

    """https://developer.help.paycom.uz/ru/protokol-merchant-api/skhema-vzaimodeystviya"""

    def authorization(self):
        merchant_id = '5e3bd952ffc8c568202be70f'
        merchant_secret = 'JTfSg3tejuROy2OdcweeScwSNYChJZhG4wp9'
        encoded_data = base64.b64encode(bytes(f"{merchant_id}:{merchant_secret}", "ISO-8859-1")).decode("ascii")
        # headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic ' + encoded_data}
        headers = {'Content-type': 'application/json', 'X-Auth': '5e3bd952ffc8c568202be70f'}
        return headers