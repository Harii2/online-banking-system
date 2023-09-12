

REQUEST_BODY_JSON = """
{
    "bank_name": "string",
    "ifsc_code": "string",
    "bank_manager_email": "string",
    "branch": "string"
}
"""


RESPONSE_201_JSON = """
{
    "bank_id": 1,
    "manager_id": 1
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_IFSC_CODE"
}
"""

