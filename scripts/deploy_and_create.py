from scripts.helpful_scripts import get_account, SimpleCollectable


def main():
    account = get_account()
    simple_collectable = SimpleCollectable.deploy({"from": account})
