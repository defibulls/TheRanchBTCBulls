
from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions
from web3 import Web3
import time, pytest
import pprint



def test_wbtc():


    #owner = accounts[0]
    owner = get_account()

    person_1 = accounts[1]


    mocked_wbtc = MockedTokens_WBTC.deploy(10 * 10 ** 8, {"from": owner})



 

    print(f'owner WBTC Balance: {mocked_wbtc.balanceOf(owner) / 10**8}')
 
 
  
    assert (mocked_wbtc.balanceOf(owner) / 10**8) == 10


    #########################################################
    ####       Transfer USDC and DAI to each person      ####
    #########################################################
    
    mocked_wbtc.transfer(person_1, 4 * 10 ** 8, {"from": owner})


    print(f'person_1 WBTC Balance: {mocked_wbtc.balanceOf(person_1)}')
 
    assert (mocked_wbtc.balanceOf(owner) / 10**8) == 6
    assert (mocked_wbtc.balanceOf(person_1) / 10**8) == 4
   
