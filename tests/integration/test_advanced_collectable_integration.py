from scripts.advanced_collectable.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network
import pytest
import time


def test_can_create_advanced_collectable_integration():
    # Deploy the contract
    # Create an NFT
    # Get a random breed back
    ## Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    ## Act
    advanced_collectable, creation_tx = deploy_and_create()
    time.sleep(60)
    ## Assert
    assert advanced_collectable.tokenCounter() == 1
