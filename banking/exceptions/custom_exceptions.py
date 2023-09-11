from django.core.exceptions import ObjectDoesNotExist


class IFSCCodeAlreadyExists(Exception):
    pass


class ManagerEmailAlreadyExists(Exception):
    pass


class BankNotExists(ObjectDoesNotExist):
    pass


class InvalidUserDetails(Exception):
    pass


class InvalidAccountId(ObjectDoesNotExist):
    pass
