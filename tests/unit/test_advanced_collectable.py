from scripts.advanced_collectable.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from brownie import network, AdvancedCollectable
import pytest


def test_can_create_advanced_collectable():
    # Deploy the contract
    # Create an NFT
    # Get a random breed back
    ## Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    ## Act
    advanced_collectable, creation_tx = deploy_and_create()
    requestId = creation_tx.events["requestedCollectable"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectable.address, {"from": get_account()}
    )
    ## Assert
    assert advanced_collectable.tokenCounter() == 1
    assert advanced_collectable.tokenIdToBreed(0) == random_number % 3
