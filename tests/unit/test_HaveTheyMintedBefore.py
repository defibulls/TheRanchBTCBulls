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
    person_5 = accounts[5]
    person_6 = accounts[6]
    person_7 = accounts[7]
    person_8 = accounts[8]
    person_9 = accounts[9]
    person_10 = accounts[10]
    person_11 = accounts[11]
    person_12 = accounts[12]
    person_13 = accounts[13]
    person_14 = accounts[14]
    person_15 = accounts[15]
    person_16 = accounts[16]
    person_17 = accounts[17]
    person_18 = accounts[18]
    person_19 = accounts[19]
    person_20 = accounts[20]
    person_21 = accounts[21]
    person_22 = accounts[22]
    person_23 = accounts[23]
    person_24 = accounts[24]
    person_25 = accounts[25]
    person_26 = accounts[26]
    person_27 = accounts[27]
    person_28 = accounts[28]
    person_29 = accounts[29]
    person_30 = accounts[30]
    
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
    

    mocked_usdc.transfer(person_1, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_2, 10_000 * 10**6, {"from": coinbase})
   
    mocked_usdc.transfer(person_3, 10_000 * 10**6, {"from": coinbase})
   
    mocked_usdc.transfer(person_4, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_5, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_6, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_7, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_8, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_9, 10_000 * 10**6, {"from": coinbase})
  
    mocked_usdc.transfer(person_10, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_11, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_12, 10_000 * 10**6, {"from": coinbase})



    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(False, {"from": multisig})
  
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": multisig})




   
    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')






    raffleEntryBool = True

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})


    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    tx2 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_3})

    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_3})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_4})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_5})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_6})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_6})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})


    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_7})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_7})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_8})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_8})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_9})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_9})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_10})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_10})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
 






    ######################################################################################
    ### Check if the partner that they person set has minted from the contract before  ###
    ######################################################################################


    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_1) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_2) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_3) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_4) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_5) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_6) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_7) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_8) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_9) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_10) == True


    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_11) == False
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_12) == False
