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






def test_withdraw():

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


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    print(tx1.info())
    ## return

    # if raffleEntryBool:
    #     assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    #     assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == 300 * 10 ** 6
    #     assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() == (300 * 10 ** 6) * .95
    #     assert TheRanchBullsMintAndReward.USDCRewardsBalanceTotal.call() == (300 * 10 ** 6) * .05
    #     assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() == (300 * 10 ** 6) * .03
    #     assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 1
    #     assert TheRanchBullsMintAndReward.totalSupply() == 2
    #     assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1
    #     assert TheRanchBullsMintAndReward.checkUpkeep('0x')[0] == True
       
   


    TheRanchBullsMintAndReward.setPartnerAddress(person_1,{"from": person_2})
    assert TheRanchBullsMintAndReward.myPartner(person_2) == person_1


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    tx2 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})





    owner_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(owner)
    person_1_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(person_1)
    person_2_mocked_usdc_before_tx1= mocked_usdc.balanceOf(person_2)
    person_3_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(person_3)
    coreTeam1_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(coreTeam1)
    coreTeam2_mocked_usdc_before_tx1 = mocked_usdc.balanceOf(coreTeam2)








    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == 300 * 10 ** 6
    assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() == (300 * 10 ** 6) * .95
    assert TheRanchBullsMintAndReward.USDCRewardsBalanceTotal.call() == (300 * 10 ** 6) * .05
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() == (300 * 10 ** 6) * .03
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 2
    assert TheRanchBullsMintAndReward.totalSupply() == 2
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1


    tax_collector_usdc = TheRanchBullsMintAndReward.usdcTaxWinner.call()
    print(f' tax_collector_usdc {tax_collector_usdc}')

    assert tax_collector_usdc != person_1
    assert tax_collector_usdc != person_2
    assert tax_collector_usdc != coreTeam1
    assert tax_collector_usdc != coreTeam2


    #### get baseline balance of what should be here before any withdraw ####

    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(tax_collector_usdc) == 0

    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(coreTeam1) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(coreTeam2) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_1) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_2) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_3) == 0
    



    ### assert what should happen

    # when person 1 withdraws, they should be subject to the tax 
    # when a coreteam member withdraws, they should NOT  

    withdraw_tx = TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": person_1})

    tax1 = withdraw_tx.events['withdrawUSDCRewardsForAddressEvent']['taxCollectedAmt']
    amount_withdrawn_from_user = withdraw_tx.events['withdrawUSDCRewardsForAddressEvent']['totalAmountTransferred']

    assert tax1 == ((150*10**6) * .01) * 0.005
    assert amount_withdrawn_from_user == ((150*10**6) * .01) - tax1 
    print(withdraw_tx.info())


    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(tax_collector_usdc) == tax1

    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(coreTeam1) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(coreTeam2) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_1) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_2) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_3) == 0


    assert mocked_usdc.balanceOf(person_1) == person_1_mocked_usdc_before_tx1 + amount_withdrawn_from_user
    assert mocked_usdc.balanceOf(person_2) == person_2_mocked_usdc_before_tx1 
    assert mocked_usdc.balanceOf(person_3) == person_3_mocked_usdc_before_tx1 
    assert mocked_usdc.balanceOf(coreTeam1) == coreTeam1_mocked_usdc_before_tx1
    assert mocked_usdc.balanceOf(coreTeam2) == coreTeam2_mocked_usdc_before_tx1 
    assert mocked_usdc.balanceOf(owner) == owner_mocked_usdc_before_tx1 






    assert TheRanchBullsMintAndReward.coreTeam_1.call() == coreTeam1

    withdraw_tx2 = TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": coreTeam1})

    tax2 = withdraw_tx2.events['withdrawUSDCRewardsForAddressEvent']['taxCollectedAmt']
    amount_withdrawn_from_coreTeamMember = withdraw_tx2.events['withdrawUSDCRewardsForAddressEvent']['totalAmountTransferred']

    assert tax2 == 0 
    assert amount_withdrawn_from_coreTeamMember == ((150*10**6) * .01)
    print(withdraw_tx2.info())


    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(tax_collector_usdc) == tax1

    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(coreTeam1) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(coreTeam2) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_1) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_2) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_3) == 0


    assert mocked_usdc.balanceOf(person_1) == person_1_mocked_usdc_before_tx1 + amount_withdrawn_from_user
    assert mocked_usdc.balanceOf(person_2) == person_2_mocked_usdc_before_tx1 
    assert mocked_usdc.balanceOf(person_3) == person_3_mocked_usdc_before_tx1 
    assert mocked_usdc.balanceOf(coreTeam1) == coreTeam1_mocked_usdc_before_tx1 + amount_withdrawn_from_coreTeamMember
    assert mocked_usdc.balanceOf(coreTeam2) == coreTeam2_mocked_usdc_before_tx1 
    assert mocked_usdc.balanceOf(owner) == owner_mocked_usdc_before_tx1 





    assert TheRanchBullsMintAndReward.coreTeam_2.call() == coreTeam2

    withdraw_tx3 = TheRanchBullsMintAndReward.withdrawUsdcRewardBalance({"from": coreTeam2})

    tax3 = withdraw_tx3.events['withdrawUSDCRewardsForAddressEvent']['taxCollectedAmt']
    amount_withdrawn_from_coreTeamMember = withdraw_tx3.events['withdrawUSDCRewardsForAddressEvent']['totalAmountTransferred']

    assert tax3 == 0 
    assert amount_withdrawn_from_coreTeamMember == ((150*10**6) * .01)
    print(withdraw_tx3.info())


    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(tax_collector_usdc) == tax1

    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(coreTeam1) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(coreTeam2) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_1) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_2) == (150*10**6) * .01
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress(person_3) == 0


    assert mocked_usdc.balanceOf(person_1) == person_1_mocked_usdc_before_tx1 + amount_withdrawn_from_user
    assert mocked_usdc.balanceOf(person_2) == person_2_mocked_usdc_before_tx1 
    assert mocked_usdc.balanceOf(person_3) == person_3_mocked_usdc_before_tx1 
    assert mocked_usdc.balanceOf(coreTeam1) == coreTeam1_mocked_usdc_before_tx1 + amount_withdrawn_from_coreTeamMember
    assert mocked_usdc.balanceOf(coreTeam2) == coreTeam2_mocked_usdc_before_tx1 + amount_withdrawn_from_coreTeamMember
    assert mocked_usdc.balanceOf(owner) == owner_mocked_usdc_before_tx1 



