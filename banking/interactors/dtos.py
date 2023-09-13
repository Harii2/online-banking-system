import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class CreateBankRequestDTO:
    bank_name: str
    ifsc_code: str
    bank_manager_email: str
    branch: str


@dataclass
class CreateBankResponseDTO:
    bank_id: int
    manager_id: int


@dataclass
class CreateAccountRequestDTO:
    bank_id: int
    name: str
    age: int
    mobile_number: str


@dataclass
class TransactionDTO:
    transaction_id: int
    transaction_type: int
    amount: int
    date_time: datetime.datetime
    to_account_id: int


@dataclass
class TransactionHistoryResponseDTO:
    transaction_history: List[TransactionDTO]


@dataclass
class MakeTransactionDTO:
    from_account_number: int
    to_account_number: int
    amount: int
    transaction_type: str


@dataclass
class GetAllTransactionsQueryParamsDTO:
    limit: int = 100
    offset: int = 0
    sort_by: str = "date_time"
    type: str = "CREDIT"


@dataclass
class MakeTransactionResponseDTO:
    transaction_id: int
    amount_paid: int
    message: str


@dataclass
class SelfTransactionRequestDTO:
    account_number: int
    amount: int
    transaction_type: str


@dataclass
class UpdateAccountRequestDTO:
    account_id: int
    name: str
    age: int
