from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .merchant.main import MerchantAPI
from paycomuz.views import MerchantAPIView
from paycomuz.methods_subscribe_api import Paycom
# Create your views here.


class CreateInvoiceView(APIView):

    """http://127.0.0.1:8000/payment/invoce"""

    def get(self, request):
        merchant = MerchantAPI()
        number = "8600 0609 2109 0842"
        expire = "03/99"
        auth = merchant.card_create(number=number, expire=expire)
        print("Auth.....", auth, type(auth))

        return Response({"": ""})


class CheckOrder(Paycom):

    order = 'bu yerda Order ID buladi'
    account = 'bu yerga qaysi account ni yozish kerak?'

    def check_order(self, amount, account):
        return self.ORDER_FOUND

    # result = check_order(amount=order, account=account)


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder
