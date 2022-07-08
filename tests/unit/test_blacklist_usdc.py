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






def test_blacklist_usdc():


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
    defender_wallet  = accounts[34]


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
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_3})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})


    TheRanchBullsMintAndReward.setPartnerAddress(person_5,{"from": person_6})
    assert TheRanchBullsMintAndReward.myPartner(person_6) == person_5


    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_6})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})


    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_7})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_8})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_9})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_10})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})


    
 
    #################################################
    ####  Person 5 withdraws their USDC balance #####
    #################################################

    assert TheRanchBullsMintAndReward.paused.call() == False
    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(True, {"from": multisig})


    assert TheRanchBullsMintAndReward.paused.call() == True
     
    with pytest.raises(exceptions.VirtualMachineError):
        rewards_withdraw_event = TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": person_5})
    
    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(False, {"from": multisig})
    assert TheRanchBullsMintAndReward.paused.call() == False

    assert TheRanchBullsMintAndReward.getBlacklistedStatus(person_5) == False
    

    TheRanchBullsMintAndReward.blacklistMalicious(person_5, True, {"from": multisig})   ## blacklist person_5


    assert TheRanchBullsMintAndReward.getBlacklistedStatus(person_5) == True
    
    with pytest.raises(exceptions.VirtualMachineError):
        rewards_withdraw_event = TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": person_5})
    
    
    
    TheRanchBullsMintAndReward.blacklistMalicious(person_5, False, {"from": multisig})
    assert TheRanchBullsMintAndReward.getBlacklistedStatus(person_5) == False


    rewards_withdraw_event = TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": person_5})



    print(rewards_withdraw_event.info())

    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_5}) == 0


   

    














