# from banking.interactors.dtos import CreateAccountRequestDTO, CreateBankRequestDTO, GetAllTransactionsQueryParamsDTO, \
#     TransactionHistoryResponseDTO, MakeTransactionRequestDTO, MakeTransactionResponseDTO
# from banking.interactors.storage_interfaces.storage_interface import StorageInterface
#
#
# class DynamoStorage(StorageInterface):
#     def validate_debit_user_balance(self, account_id: int, amount: int):
#         pass
#
#     def make_transaction(self, make_transaction_dto: MakeTransactionRequestDTO) -> MakeTransactionResponseDTO:
#         pass
#
#     def validate_amount(self, amount: int):
#         pass
#
#     def get_transaction_history(self, account_id: int,
#                                 query_params_dto: GetAllTransactionsQueryParamsDTO) -> TransactionHistoryResponseDTO:
#         pass
#
#     def get_accountant_balance(self, account_id: int):
#         pass
#
#     def validate_account_id(self, account_id: int):
#         pass
#
#     def validate_ifsc_code(self, ifsc_code: str):
#         pass
#
#     def manager_already_exists(self, manager_email: str):
#         pass
#
#     def create_bank(self, create_bank_request_dto: CreateBankRequestDTO) -> int:
#         pass
#
#     def create_manager_for_bank(self, bank_id: int, manager_email: str) -> int:
#         pass
#
#     def validate_bank_id(self, bank_id: int):
#         pass
#
#     def validate_user_details(self, create_account_request_dto: CreateAccountRequestDTO):
#         pass
#
#     def create_account(self, create_account_request_dto: CreateAccountRequestDTO) -> int:
#         pass
