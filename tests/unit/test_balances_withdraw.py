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






def test_balances_withdraw():

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



    print(f'CoinbaseMock USDC Balance: {mocked_usdc.balanceOf(coinbase) / 10**6}')
    print(f'TheRanchBullsMintAndReward_ETH_balance: {TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) /10**18}')
  
    assert (mocked_usdc.balanceOf(coinbase) / 10**6) == 500_000
    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0



 
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

 

    raffleEntryBool = True


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})


    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_3})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})


    owner_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(owner)
    person_1_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(person_1)
    person_2_mocked_usdc_before_tx1= mocked_usdc.balanceOf(person_2)
    person_3_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(person_3)
    coreTeam1_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(coreTeam1)
    coreTeam2_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(coreTeam2)



    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((5 * 350) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() ==   ((5 * 350) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((5 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.warChestBalance.call() ==  ((5 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.USDCRewardsBalanceTotal.call() == ((5 * 350) * (10 ** 6)) * 0.05
    
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 5
    assert TheRanchBullsMintAndReward.totalSupply() == 5
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1




    #### get baseline balance of what should be here before any withdraw ####

    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":coreTeam1}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":coreTeam2}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_1}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_4}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_5}) == 0
    

    ###################################################################
    #### WITHDRAW BTC MINERS FUND AND ASSERT NOTHING ELSE CHANGES  ####
    ###################################################################

    starting_owner_balance = mocked_usdc.balanceOf(owner)

    tx_withdraw_btc_miner_fund = TheRanchBullsMintAndReward.withdrawBtcMinerBalance({"from": owner})
    print(tx_withdraw_btc_miner_fund.info())
    btc_miner_fund = tx_withdraw_btc_miner_fund.events["Transfer"]["value"]


    assert mocked_usdc.balanceOf(owner) == starting_owner_balance + btc_miner_fund
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((5 * 350) * (10 ** 6)) - btc_miner_fund
    assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() ==   0
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((5 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.warChestBalance.call() ==  ((5 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.USDCRewardsBalanceTotal.call() == ((5 * 350) * (10 ** 6)) * 0.05



    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":coreTeam1}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":coreTeam2}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_1}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_4}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_5}) == 0




    ###################################################################
    #### WITHDRAW WAR CHEST FUND AND ASSERT NOTHING ELSE CHANGES  ####
    ###################################################################


    tx_withdraw_war_chest_fund = TheRanchBullsMintAndReward.withdrawWarChestBalance({"from": owner})

    war_chest_fund = tx_withdraw_war_chest_fund.events["Transfer"]["value"]

    assert war_chest_fund == ((5 * 350) * (10 ** 6)) * 0.05


    assert mocked_usdc.balanceOf(owner) == starting_owner_balance + btc_miner_fund + war_chest_fund
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((5 * 350) * (10 ** 6)) - (btc_miner_fund + war_chest_fund)
    assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() ==   0
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((5 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.warChestBalance.call() ==  0 
    assert TheRanchBullsMintAndReward.USDCRewardsBalanceTotal.call() == ((5 * 350) * (10 ** 6)) * 0.05



    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":coreTeam1}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":coreTeam2}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_1}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_4}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from":person_5}) == 0













