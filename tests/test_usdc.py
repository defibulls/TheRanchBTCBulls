
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

    person_1 = accounts[1]


    mocked_usdc = MockedTokens_USDC.deploy(100_000 * 10 ** 6, {"from": owner})
    mocked_dai = MockedTokens_DAI.deploy(100_000 * 10 ** 18, {"from": owner})


 

    print(f'owner USDC Balance: {mocked_usdc.balanceOf(owner) / 10**6}')
    print(f'owner DAI Balance: {mocked_dai.balanceOf(owner) / 10**18}')
 
  
    assert (mocked_usdc.balanceOf(owner) / 10**6) == 100_000
    assert (mocked_dai.balanceOf(owner) / 10**18) == 100_000


    #########################################################
    ####       Transfer USDC and DAI to each person      ####
    #########################################################
    
    mocked_usdc.transfer(person_1,10_000, {"from": owner})
    mocked_dai.transfer(person_1,10_000, {"from": owner})


    print(f'person_1 USDC Balance: {mocked_usdc.balanceOf(person_1)}')
    print(f'person_1 DAI  Balance: {mocked_dai.balanceOf(person_1)}')

    assert (mocked_usdc.balanceOf(owner) / 10**6) == 100_000
    assert (mocked_dai.balanceOf(owner) / 10**18) == 100_000

