from cmath import exp
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






def test_USDC_rewards_covery_maintenance_fees():

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

  

    TheRanchBullsMintAndReward.setPartnerAddress(person_1,{"from": person_2})
    assert TheRanchBullsMintAndReward.myPartner(person_2) == person_1

    TheRanchBullsMintAndReward.setPartnerAddress(person_1,{"from": person_3})
    assert TheRanchBullsMintAndReward.myPartner(person_3) == person_1

    TheRanchBullsMintAndReward.setPartnerAddress(person_1,{"from": person_4})
    assert TheRanchBullsMintAndReward.myPartner(person_4) == person_1

    TheRanchBullsMintAndReward.setPartnerAddress(person_1,{"from": person_5})
    assert TheRanchBullsMintAndReward.myPartner(person_5) == person_1

       

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(3),{"from":person_3})
    TheRanchBullsMintAndReward.mint(3,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})






    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((7 * 150) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() ==   ((7 * 150) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((7 * 150) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.warChestBalance.call() ==  ((7 * 150) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.USDCRewardsBalanceTotal.call() == ((7 * 150) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 5
    assert TheRanchBullsMintAndReward.totalSupply() == 7
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1




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





    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 0

    ## no one shoud have any maintenance fees due right now. 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam1)== 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam2) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == 0

    ## everyone should be 0 months behind on the maintenance fees
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam1) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam2) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 0

    
    
    
    
    
    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(6*10**6)   # 6 dollars in USDC.e
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 6*10**6









    amount_to_award = 1 * wbtc_decimals

    print(f'money to approve : {amount_to_award}')

    mocked_wbtc.approve(TheRanchBullsMintAndReward, amount_to_award, {"from": owner})
    fund_stockyards_tx = TheRanchBullsMintAndReward.fundAndRewardBulls(1,7,amount_to_award,{"from": owner})
    print(fund_stockyards_tx.info())
    assert mocked_wbtc.balanceOf(TheRanchBullsMintAndReward) == amount_to_award 



    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth()
    print(tx_update_fees.info())

    tx_update_months_behind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate()
    print(tx_update_months_behind.info())






    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam1) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam2) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == 6*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == 6*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == (6*10**6) * 3
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == 6*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == 6*10**6
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == 0

    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam1) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam2) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 0



    
    print("#######################################################################################")
    print(f'\t\t\t\t\t ROUND 1')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam1)}')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam2)}')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1)}')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2)}')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3)}')
    print(f'person_4 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4)}')
    print(f'person_5 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5)}')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6)}')
    print(f'person_7 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7)}')


    print('\n')
    

    print(f'coreTeam_1 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam1)}')
    print(f'coreTeam_2 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam2)}')
    print(f'person_1 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1)}')
    print(f'person_2 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2)}')
    print(f'person_3 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3)}')
    print(f'person_4 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4)}')
    print(f'person_5 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5)}')
    print(f'person_6 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6)}')
    print(f'person_7 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7)}')

    print('\n')

    print(f'liquidation list: {TheRanchBullsMintAndReward.getLiquidatedArray()}')

    print('\n')

    print(f'coreTeam1 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": coreTeam1})}')
    print(f'coreTeam2 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": coreTeam2})}')
    print(f'person_1 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1})}')
    print(f'person_2 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2})}')
    print(f'person_3 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3})}')
    print(f'person_4 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4})}')
    print(f'person_5 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5})}')
    print(f'person_6 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6})}')
    print(f'person_7 WBTC rewards on contract: {TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7})}')








    person_1_usdc_rewards = TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_1})
    person_1_maint_fee_due = TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1)

    print(f'\n######### before paying maint fees ############\n')
    print(f'person_1_usdc_rewards: {person_1_usdc_rewards}')
    print(f'person_1_maint_fee_due: {person_1_maint_fee_due}')




    if person_1_usdc_rewards < person_1_maint_fee_due:
        amt_to_approve = person_1_maint_fee_due - person_1_usdc_rewards
        mocked_usdc.approve(TheRanchBullsMintAndReward.address, amt_to_approve ,{"from":person_1})


    pay_maint_fees_person_1 = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_1})
    print(pay_maint_fees_person_1.info())
  
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_1}) == person_1_usdc_rewards - person_1_maint_fee_due


    person_1_usdc_rewards = TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_1})
    person_1_maint_fee_due = TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1)
    print(f'\n######### after paying maint fees ############\n')
    print(f'person_1_usdc_rewards: {person_1_usdc_rewards}')
    print(f'person_1_maint_fee_due: {person_1_maint_fee_due}')


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == 0



