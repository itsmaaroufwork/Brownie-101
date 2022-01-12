from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    # Brownie accounts /first method/
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    # Transact
    # call
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(5, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# /Top security method/
# account = accounts.load("myFirstAccount")
# print(account)

# /Environment method/
# account = accounts.add(config["wallets"]["from_key"])
# print(account)


def main():
    deploy_simple_storage()
