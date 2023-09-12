from django.core.exceptions import ObjectDoesNotExist


class InvalidAge(Exception):
    pass


class InvalidMobileNumber(Exception):
    pass


class InvalidAccountantName(Exception):
    pass


class IFSCCodeAlreadyExists(Exception):
    pass


class ManagerEmailAlreadyExists(Exception):
    pass


class BankNotExists(ObjectDoesNotExist):
    pass


class InvalidUserDetails(Exception):
    pass


class InvalidAmount(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class InvalidAccountId(ObjectDoesNotExist):
    pass
