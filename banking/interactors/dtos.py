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
