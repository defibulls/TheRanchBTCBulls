
from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from web3 import Web3
from scripts.deploy_usdc import deploy_usdc
import time, pytest
import pprint



def test_wbtc():


    #owner = accounts[0]
    owner = get_account()

    person_1 = accounts[1]


    mocked_usdc = MockedTokens_USDC.deploy(1000 * 10 ** 6, {"from": owner})


    print(mocked_usdc)



 

    print(f'owner WBTC Balance: {mocked_usdc.balanceOf(owner) / 10**6}')
 
 
  
    assert (mocked_usdc.balanceOf(owner) / 10**6) == 1000


    #########################################################
    ####       Transfer USDC and DAI to each person      ####
    #########################################################
    
    mocked_usdc.transfer(person_1, 4 * 10 ** 6, {"from": owner})


    print(f'person_1 WBTC Balance: {mocked_usdc.balanceOf(person_1)}')
 
    assert (mocked_usdc.balanceOf(owner) / 10**6) == 996
    assert (mocked_usdc.balanceOf(person_1) / 10**6) == 4
   
