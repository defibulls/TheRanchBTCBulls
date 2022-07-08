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






def test_balances_withdraw():

  

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


    owner_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(multisig)
    person_1_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(person_1)
    person_2_mocked_usdc_before_tx1= mocked_usdc.balanceOf(person_2)
    person_3_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(person_3)
    coreTeam1_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(coreTeam1)
    coreTeam2_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(coreTeam2)



    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((5 * 350) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   ((5 * 350) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == ((5 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((5 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == ((5 * 350) * (10 ** 6)) * 0.05
    
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 5
    assert TheRanchBullsMintAndReward.totalSupply() == 5
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1


    #### get baseline balance of what should be here before any withdraw ####

    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":coreTeam1}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":coreTeam2}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_1}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_4}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_5}) == 0


    ###################################################################
    #### WITHDRAW BTC MINERS FUND AND ASSERT NOTHING ELSE CHANGES  ####
    ###################################################################

    starting_safe_balance = mocked_usdc.balanceOf(btcMinersSafe)

    tx_withdraw_btc_miner_fund = TheRanchBullsMintAndReward.withdrawBtcMinersSafeBalance({"from": multisig})
    print(tx_withdraw_btc_miner_fund.info())
    btc_miner_fund = tx_withdraw_btc_miner_fund.events["Transfer"]["value"]

    
    assert mocked_usdc.balanceOf(btcMinersSafe) == starting_safe_balance + btc_miner_fund
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((5 * 350) * (10 ** 6)) - btc_miner_fund
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   0
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == ((5 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((5 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == ((5 * 350) * (10 ** 6)) * 0.05



    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":coreTeam1}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":coreTeam2}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_1}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_4}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_5}) == 0

    




    ###################################################################
    #### WITHDRAW WAR CHEST FUND AND ASSERT NOTHING ELSE CHANGES  ####
    ###################################################################


    tx_withdraw_hosting_safe = TheRanchBullsMintAndReward.withdrawHostingSafeBalance({"from": multisig})

    hosting_safe_amt = tx_withdraw_hosting_safe.events["Transfer"]["value"]

    assert hosting_safe_amt == ((5 * 350) * (10 ** 6)) * 0.05


    assert mocked_usdc.balanceOf(hostingSafe) == hosting_safe_amt
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((5 * 350) * (10 ** 6)) - (btc_miner_fund + hosting_safe_amt)
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   0
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((5 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == 0 
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == ((5 * 350) * (10 ** 6)) * 0.05



    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":coreTeam1}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":coreTeam2}) == ((5 * 350) * (10 ** 6)) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_1}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_2}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_4}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from":person_5}) == 0













