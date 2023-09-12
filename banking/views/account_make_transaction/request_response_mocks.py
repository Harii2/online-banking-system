

REQUEST_BODY_JSON = """
{
    "account_number": 1,
    "amount": 1,
    "transaction_type": "string"
}
"""


RESPONSE_201_JSON = """
{
    "transaction_id": 1,
    "amount_paid": 1,
    "message": "string"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_ACCOUNT_ID"
}
"""

