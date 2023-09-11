from dataclasses import dataclass


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
