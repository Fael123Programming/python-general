'''
    This module contains some useful functions to compute operations with
    accounts of a possible bank system.
'''


def create_account(name_owner: str, number: str, agency: str, limit: float):
    return {"name_owner": name_owner, "number": number, "agency": agency, "limit": limit, "balance": 0.0}


def deposit(account: dict, quantity: float):
    if quantity < 0 or account["balance"] + quantity > account["limit"]:
        return
    account["balance"] += quantity


def withdraw(account: dict, quantity: float):
    if quantity < 0 or account["balance"] < quantity:
        return
    account["balance"] -= quantity 


def info(account: dict):
    return account
