from curses import use_env
from curses.ascii import FF
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintReward, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_haveTheyMintedBefore():

    fund_deposited = 80_000

    #owner = accounts[0]
    TheRanchBullsMintAndReward = deploy_contract()


    person_1 = accounts[1]
    person_2 = accounts[2]
    person_3 = accounts[3]
    person_4 = accounts[4]

    
    coinbase = accounts[10001]
    defender_wallet = accounts[10002]
    multisig = accounts[10003]

    btcMinersSafe = accounts[10006]
    hostingSafe = accounts[10007]







    TheRanchBullsMintAndReward = deploy_contract()
    deployer = TheRanchBullsMintAndReward.owner.call()

    coreTeam1 = TheRanchBullsMintAndReward.coreTeam_1.call()
    coreTeam2 = TheRanchBullsMintAndReward.coreTeam_2.call()


 
    ################################################################
    ## assert the deployer can transfer ownership of the contract ##
    ################################################################

    tx_transfer_ownership = TheRanchBullsMintAndReward.transferOwnership(multisig)
    print(tx_transfer_ownership.info())

    assert TheRanchBullsMintAndReward.owner.call() != deployer
    assert TheRanchBullsMintAndReward.owner.call() == multisig




    assert TheRanchBullsMintAndReward.paused.call() == True


    mocked_usdc = MockedTokens_USDC.deploy(1_000_000_000 * 10**6, {"from": coinbase})
    mocked_wbtc = MockedTokens_WBTC.deploy(10 * 10**8, {"from": multisig})

    TheRanchBullsMintAndReward.setUsdcTokenAddress(mocked_usdc,{"from": multisig})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_wbtc,{"from": multisig})
    TheRanchBullsMintAndReward.setBaseURI("ipfs://aldkfjasdpofe", {"from": multisig})
    TheRanchBullsMintAndReward.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})


 
    #########################################################
    ####       Transfer USDC  each person                ####
    #########################################################
    

    mocked_usdc.transfer(person_1, 20_000 * 10**6, {"from": coinbase})




    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(False, {"from": multisig})
  
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": multisig})




   
    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')






    raffleEntryBool = True

    amt = 11
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    amt = 10
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})
    print(tx1.info())
    assert TheRanchBullsMintAndReward.addressMintCount(person_1) == 10

    amt = 10
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})
    assert TheRanchBullsMintAndReward.addressMintCount(person_1) == 20

    amt = 10
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})
    assert TheRanchBullsMintAndReward.addressMintCount(person_1) == 30

    amt = 10
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})
    assert TheRanchBullsMintAndReward.addressMintCount(person_1) == 40


    amt = 10
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})
    assert TheRanchBullsMintAndReward.addressMintCount(person_1) == 50


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

   
    assert TheRanchBullsMintAndReward.addressMintCount(person_1) == 50