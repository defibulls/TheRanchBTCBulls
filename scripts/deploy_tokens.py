

from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, TheRanchBullsAirDrop, MockedTokens_DAI, MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from scripts.deploy_mint import deploy_mint_contract
from scripts.deploy_AirDrop import deploy_AirDrop_contract
from web3 import Web3
import time, pytest
import pprint



def test_usdc():


    #owner = accounts[0]
    owner = get_account()

    mocked_usdc = MockedTokens_USDC.deploy(100_000_000 * 10**6, {"from": owner})



def main():
    test_usdc()




