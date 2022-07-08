

from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions
from web3 import Web3
import time, pytest
import pprint



def deploy_wbtc():


    #owner = accounts[0]
    owner = get_account()

    mocked_wbtc= MockedTokens_WBTC.deploy(15 * 10 ** 8, {"from": owner})



def main():
    deploy_wbtc()





