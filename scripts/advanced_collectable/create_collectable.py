from scripts.helpful_scripts import get_account, fund_with_link
from brownie import AdvancedCollectable
from web3 import Web3


def main():
    account = get_account()
    advanced_collectable = AdvancedCollectable[-1]
    fund_with_link(advanced_collectable.address, amount=Web3.toWei(0.1, "ether"))
    creation_tx = advanced_collectable.createCollectable({"from": account})
    creation_tx.wait(1)
    print("Collectable created!")
