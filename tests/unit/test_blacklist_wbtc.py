from curses import use_env
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintAndReward, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_blacklist_wbtc():

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
    person_31 = accounts[34]


    coinbase = accounts[31]
    coreTeam1 = accounts[32]
    coreTeam2 = accounts[33]


    people = {
        person_1: 'person_1',
        person_2: 'person_2',
        person_3: 'person_3',
        person_4: 'person_4',
        person_5: 'person_5',
        person_6: 'person_6',
        person_7: 'person_7',
        person_8: 'person_8',
        person_9: 'person_9',
        person_10: 'person_10',
        person_11: 'person_11',
        person_12: 'person_12',
        person_13: 'person_13',
        person_14: 'person_14',
        person_15: 'person_15',
        person_16: 'person_16',
        person_17: 'person_17',
        person_18: 'person_18',
        person_19: 'person_19',
        person_20: 'person_20',
        person_21: 'person_21',
        person_22: 'person_22',
        person_23: 'person_23',
        person_24: 'person_24',
        person_25: 'person_25',
        person_26: 'person_26',
        person_27: 'person_27',
        person_28: 'person_28',
        person_29: 'person_29',
        person_30: 'person_30',
        person_31: 'person_31',
    }



  
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

    amt = 4
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_11})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_11, "value":  price_needed(amt)})
    

    ###################################################################################
    ####   Owner withdraws BTC Miners Fund and invests funds into Compass Mining   ####
    ###################################################################################
    assert mocked_usdc.balanceOf(owner) / 10**6 == 0

    #### withdraw btcMinerAmt
    btcminer_withdraw_tx = TheRanchBullsMintAndReward.withdrawBtcMinerBalance({"from": owner})
    print(btcminer_withdraw_tx.info())

    assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() == 0



    ##################################################################
    ### Set the Reward Token for the contract after deploying WBTC ###
    ##################################################################

    ## deploy the wbtc contract so the owner now has wbtc in their wallet
    wbtc_decimals = 10 ** 8
    wbtc_to_start = 10
    mocked_wbtc = MockedTokens_WBTC.deploy(wbtc_to_start * wbtc_decimals, {"from": owner})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_wbtc, {"from": owner})


    starting_owner_balance_wbtc = mocked_wbtc.balanceOf(owner)
    assert starting_owner_balance_wbtc == wbtc_to_start * wbtc_decimals
    assert mocked_wbtc.balanceOf(TheRanchBullsMintAndReward) == 0

    #### send satoshi values to all 5 stockyards ###

    amount_to_send = 1 * wbtc_decimals
  
 

    print(f'money to approve : {amount_to_send}')


    mocked_wbtc.approve(TheRanchBullsMintAndReward,amount_to_send, {"from":owner})

    fund_stockyards_tx = TheRanchBullsMintAndReward.fundAndRewardBulls(1,15,amount_to_send,{"from": owner})
    ##print(fund_stockyards_tx.info())
    assert mocked_wbtc.balanceOf(TheRanchBullsMintAndReward) == amount_to_send 




    ##############################################
    ### TEST WITHDRAW FOR WBTC FROM PERSON 2 #####
    ##############################################




    ##########################################################################
    #####      Let person_2 claim their rewards and check balances       #####
    ##########################################################################
    reward_contract_balance_wbtc_before_tx = mocked_wbtc.balanceOf(TheRanchBullsMintAndReward)





    # make sure person_2 currently has zero wbtc in their own wallet
    assert mocked_wbtc.balanceOf(person_2) == 0 

    person_1_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1})
    person_2_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2})
    person_3_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3})
    person_4_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4})
    person_5_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5})
    person_6_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6})
    person_7_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7})
    person_8_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8})
    person_9_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9})
    person_10_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10})
    person_11_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11})
    person_12_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12})
    person_13_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13})
    person_14_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14})
    person_15_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15})
    person_16_award_balance_before_tx = TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16})
   
 
   #####################################
    ####  Person 5 withdraws their WBTC balance #####
    #################################################

    assert TheRanchBullsMintAndReward.paused.call() == False
    TheRanchBullsMintAndReward.togglePauseStatus()
    assert TheRanchBullsMintAndReward.paused.call() == True
     
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMintAndReward.withdrawWbtcForWalletAddress({"from": person_2})
    
    TheRanchBullsMintAndReward.togglePauseStatus()
    assert TheRanchBullsMintAndReward.paused.call() == False
    
    
    assert TheRanchBullsMintAndReward.getBlacklistedStatus(person_2) == False

    TheRanchBullsMintAndReward.blacklistMalicious(person_2, True)   ## blacklist person_2

    assert TheRanchBullsMintAndReward.getBlacklistedStatus(person_2) == True
    
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMintAndReward.withdrawWbtcForWalletAddress({"from": person_2})



    TheRanchBullsMintAndReward.blacklistMalicious(person_2, False)
    assert TheRanchBullsMintAndReward.getBlacklistedStatus(person_2) == False

    withdraw_person_2 = TheRanchBullsMintAndReward.withdrawWbtcForWalletAddress({"from": person_2})


