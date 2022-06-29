

from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from web3 import Web3
import time, pytest
import pprint



def deploy_usdc():


    #owner = accounts[0]
    owner = get_account()

    mocked_usdc = MockedTokens_USDC.deploy(50_000 * 10 ** 6, {"from": owner})



def main():
    deploy_usdc()





