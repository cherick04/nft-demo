from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy_and_create import deploy_and_create
from brownie import network
import pytest


def test_can_create_simple_collectable():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectable = deploy_and_create()
    assert simple_collectable.ownerOf(0) == get_account()
