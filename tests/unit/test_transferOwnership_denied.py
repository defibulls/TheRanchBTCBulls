from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, TheRanchBullsAirDrop, MockedTokens_DAI, MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from scripts.deploy_mint import deploy_mint_contract
from scripts.deploy_AirDrop import deploy_AirDrop_contract
from web3 import Web3
import time, pytest
import pprint




def test_transferOwnership_denial():
    owner = get_account()
    actor = get_account(index=2)
    theRanchMint = deploy_mint_contract()
    assert theRanchMint.owner() == owner
    assert theRanchMint.owner() != actor

    theRanchMint.transferOwnership(actor, {"from": owner})

    assert theRanchMint.owner() == owner
    assert theRanchMint.owner() != actor



    theRanchAirDrop = deploy_AirDrop_contract()

    assert theRanchAirDrop.owner() == owner
    assert theRanchAirDrop.owner() != actor

    theRanchAirDrop.transferOwnership(actor, {"from": owner})

    assert theRanchAirDrop.owner() == owner
    assert theRanchAirDrop.owner() != actor



