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






def test_double_raffle_entry():

 
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
    ####       Transfer USDC and DAI to each person      ####
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

    mocked_usdc.transfer(person_13, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_14, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_15, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_16, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_17, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_18, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_19, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_20, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_21, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_22, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_23, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_24, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_25, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_26, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_27, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_28, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_29, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_30, 10_000 * 10**6, {"from": coinbase})







    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(False, {"from": multisig})
  
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": multisig})






    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)



    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == 0
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   0
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == 0
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  0
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == 0    
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 0
    assert TheRanchBullsMintAndReward.totalSupply() == 0
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_1) == False
  




    raffleEntryBool = True

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})
    #print(tx1.info())
    
    

    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((2 * 350) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   ((2 * 350) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == ((2 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((2 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == ((2 * 350) * (10 ** 6)) * 0.05
    
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 1
    assert TheRanchBullsMintAndReward.totalSupply() == 2
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_1) == True




    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx2 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})



 

    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((4 * 350) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   ((4 * 350) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == ((4 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((4 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == ((4 * 350) * (10 ** 6)) * 0.05
    
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 1
    assert TheRanchBullsMintAndReward.totalSupply() == 4
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_1) == True
    







