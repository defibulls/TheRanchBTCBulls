from curses import use_env
from curses.ascii import FF
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintReward, TheRanchBullsFeeding, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_bullsFeeding import deploy_feeding_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_feedingContract_works_with_partner_set():


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



    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(False, {"from": multisig})
  
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": multisig})



   
    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')


    raffleEntryBool = True


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    TheRanchBullsMintAndReward.setPartnerAddress(person_1,{"from": person_2})
    assert TheRanchBullsMintAndReward.myPartner(person_2) == person_1


    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(3),{"from":person_3})
    TheRanchBullsMintAndReward.mint(3,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})


    TheRanchBullsMintAndReward.setPartnerAddress(person_3,{"from": person_4})
    assert TheRanchBullsMintAndReward.myPartner(person_4) == person_3

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})





    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((7 * 350) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   ((7 * 350) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == ((7 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((7 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == ((7 * 350) * (10 ** 6)) * 0.05
    
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 5
    assert TheRanchBullsMintAndReward.totalSupply() == 7
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1



    print(f'B coreTeam1 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": coreTeam1})}')
    print(f'B coreTeam2 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": coreTeam2})}')
    print(f'B person_1 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_1})}')
    print(f'B person_2 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_2})}')
    print(f'B person_3 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3})}')
    print(f'B person_4 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_4})}')
    print(f'B person_5 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_5})}')
    print(f'B person_6 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_6})}')
    print(f'B person_7 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_7})}')



    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_1}) == ((1 * 350) * (10 ** 6)) * 0.02
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3}) == ((1 * 350) * (10 ** 6)) * 0.02
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_4}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_5}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_7}) == 0




    ## let core team withdraw so their starting balance for the test is back at 0


    TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": coreTeam1})
    TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": coreTeam2})
    TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": person_3})





    ###################################
    ### DEPLOY THE FEEDING CONTRACT ###
    ###################################

    TheRanchBullsFeedingContract = deploy_feeding_contract(multisig)


    TheRanchBullsFeedingContract.setUsdcTokenAddress(mocked_usdc,{"from": multisig})




    #### let person 4,5,6,7 mint from the feeding contract ###



    def price_needed(count):
        return (count * TheRanchBullsFeedingContract.mintingCost() * 10 ** 6)

 

    amt = 1
    mocked_usdc.approve(TheRanchBullsFeedingContract.address, price_needed(amt),{"from":person_4})
    TheRanchBullsFeedingContract.mint(amt,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsFeedingContract.address, price_needed(amt),{"from":person_5})
    TheRanchBullsFeedingContract.mint(amt,{"from": person_5, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsFeedingContract.address, price_needed(amt),{"from":person_6})
    TheRanchBullsFeedingContract.mint(amt,{"from": person_6, "value":  price_needed(amt)})


    mocked_usdc.approve(TheRanchBullsFeedingContract.address, price_needed(amt),{"from":person_7})
    TheRanchBullsFeedingContract.mint(amt,{"from": person_7, "value":  price_needed(amt)})



    print('\n\n')
    print(f'person_4 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_4)}')
    print(f'person_5 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_5)}')
    print(f'person_6 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_6)}')
    print(f'person_7 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_7)}')
    print(f'person_8 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_8)}')


    print(f'\nReward the Bulls for owning the HayBales \n')  


    TheRanchBullsMintAndReward.setEcosystemRole(TheRanchBullsFeedingContract, True, {"from": multisig})


    TheRanchBullsFeedingContract.setTheRanchBullsMintRewardAddress(TheRanchBullsMintAndReward, {"from": multisig})  


    #mocked_usdc.approve(TheRanchBullsFeedingContract, 4000 ,{"from":multisig})



    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3}) == 0

    pre_hostingSafe_balance = TheRanchBullsMintAndReward.hostingSafeBalance.call()


    TheRanchBullsFeedingContract.feedTheBulls(1,4, 4000)



    # expected cuts for coreteam1 0,50,50,50 = 150
    # expected cuts for coreteam2 0,50,50,50 = 150
    # hosting safe should get 20% of the last two people at 200,200 so that would be 400 


    print(f'A coreTeam1 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": coreTeam1})}')
    print(f'A coreTeam2 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": coreTeam2})}') 
    print(f'A person_1 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_1})}')
    print(f'A person_2 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_2})}')
    print(f'A person_3 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3})}')
    print(f'A person_4 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_4})}')
    print(f'A person_5 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_5})}')
    print(f'A person_6 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_6})}')
    print(f'A person_7 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_7})}')
    print(f'A person_8 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_8})}')
    print(f'A person_9 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_9})}')



    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": coreTeam1}) == 150
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": coreTeam2}) == 150
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == pre_hostingSafe_balance + 400




    ### persons 4,5 have nfts on both contracts and should get 90% since they don't have a partner set each, 6,7 don't own a BTC bull and should only get 70% of the 1000


    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_1}) == ((1 * 350) * (10 ** 6)) * 0.02
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3}) == 50
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_4}) == 950
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_5}) == 900
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_6}) == 700
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_7}) == 700
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_8}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_9}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_10}) == 0







