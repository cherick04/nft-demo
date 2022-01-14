from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import AdvancedCollectable, network, config


def main():
    deploy_and_create()


def deploy_and_create():
    account = get_account()
    # We want to be able to use the deployed contracts if we're not on a testnet
    # Otherwise, we want to deploy some mocks and use those in Rinkeby
    advanced_collectable = AdvancedCollectable.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=True,
    )
    fund_with_link(advanced_collectable.address)
    creating_tx = advanced_collectable.createCollectable({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
