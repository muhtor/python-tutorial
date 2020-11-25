

class PaycomException(Exception):

    def __init__(self, request_id, message, code, data=None) -> None:
        self.request_id = request_id
        self.message = message
        self.code = code
        self.data = data
        self.error = {}

        if self.message:
            self.error['message'] = self.message

        if self.data:
            self.error['data'] = self.data

    ERROR_INTERNAL_SYSTEM = -32400
    ERROR_INSUFFICIENT_PRIVILEGE = -32504
    ERROR_INVALID_JSON_RPC_OBJECT = -32600
    ERROR_METHOD_NOT_FOUND = -32601
    ERROR_INVALID_AMOUNT = -31001
    ERROR_TRANSACTION_NOT_FOUND = -31003
    ERROR_INVALID_ACCOUNT = -31050
    ERROR_COULD_NOT_CANCEL = -31007
    ERROR_COULD_NOT_PERFORM = -31008

