from cmath import exp
from curses import use_env
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintAndReward, TheRanchBullsFeeding, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_bullsFeeding import deploy_feeding_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_feedingContract():

    fund_deposited = 80_000

    #owner = accounts[0]
    owner = get_account()
    TheRanchBullsMintAndReward = deploy_contract()

    ### set the address on each contract for to reference other contract ####

 
    # assert contract_balance == 0
    
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


    coinbase = accounts[31]
    coreTeam1 = accounts[32]
    coreTeam2 = accounts[33]




  
    starting_balance_of_each_account = 50_000 * 10**18


    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": coinbase})


    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

   
    TheRanchBullsMintAndReward.setUsdcTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_usdc,{"from": owner})
    
    # print(f'usdc address : {mocked_usdc.address}')
    # print(f'dai address :  {mocked_dai.address}')
    # print(f'TotalSupplyOfTokens: {mocked_tokens_usdc.totalSupply()/10**18}')
    print(f'CoinbaseMock USDC Balance: {mocked_usdc.balanceOf(coinbase) / 10**6}')
 
    print(f'TheRanchBullsMintAndReward_ETH_balance: {TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) /10**18}')
  
    assert (mocked_usdc.balanceOf(coinbase) / 10**6) == 500_000



 
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






    ### set coreTeam wallets ###
    TheRanchBullsMintAndReward.setCoreTeam_1_Address(coreTeam1,{"from": owner})
    TheRanchBullsMintAndReward.setCoreTeam_2_Address(coreTeam2,{"from": owner})

    # Owner unpauses contracts
    TheRanchBullsMintAndReward.togglePauseStatus({"from": owner})
    
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": owner})


   
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

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})






    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((7 * 350) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() ==   ((7 * 350) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((7 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.warChestBalance.call() ==  ((7 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.USDCRewardsBalanceTotal.call() == ((7 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 5
    assert TheRanchBullsMintAndReward.totalSupply() == 7
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1





    print(f'B coreTeam1 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": coreTeam1})}')
    print(f'B person_1 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_1})}')
    print(f'B person_2 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_2})}')
    print(f'B person_3 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_3})}')
    print(f'B person_4 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_4})}')
    print(f'B person_5 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_5})}')
    print(f'B person_6 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_6})}')
    print(f'B person_7 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_7})}')



    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_1}) == ((1 * 350) * (10 ** 6)) * 0.02
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_4}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_5}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_7}) == 0



    ###################################
    ### DEPLOY THE FEEDING CONTRACT ###
    ###################################

    TheRanchBullsFeedingContract = deploy_feeding_contract()


    TheRanchBullsFeedingContract.setUsdcTokenAddress(mocked_usdc,{"from": owner})




    #### let person 4,5,6,7 mint from the feeding contract ###



    def price_needed(count):
        return (count * TheRanchBullsFeedingContract.mintingCost() * 10 ** 6)

 


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


    TheRanchBullsMintAndReward.setAllowedContractsToAwardTheBulls(TheRanchBullsFeedingContract,True)

    mocked_usdc.approve(TheRanchBullsFeedingContract, 400 ,{"from":owner})
    TheRanchBullsFeedingContract.setTheRanchBullsMintandRewardAddress(TheRanchBullsMintAndReward, {"from": owner})  


    TheRanchBullsFeedingContract.feedTheBulls(1,4, 1000)


    print(f'A coreTeam1 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": coreTeam1})}')
    print(f'A person_1 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_1})}')
    print(f'A person_2 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_2})}')
    print(f'A person_3 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_3})}')
    print(f'A person_4 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_4})}')
    print(f'A person_5 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_5})}')
    print(f'A person_6 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_6})}')
    print(f'A person_7 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_7})}')
    print(f'A person_8 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_8})}')
    print(f'A person_9 USDC rewards on contract: {TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_9})}')








