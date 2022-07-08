from curses import use_env
from curses.ascii import FF
from distutils import core
from unittest import mock
from attr import mutable
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintReward, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_maintenance_fees():


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


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

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
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   ((7 * 350) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == ((7 * 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((7 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == ((7 * 350) * (10 ** 6)) * 0.05
    
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 5
    assert TheRanchBullsMintAndReward.totalSupply() == 7
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1



    ##################################################################
    ### Set the Reward Token for the contract after deploying WBTC ###
    ##################################################################

    ## deploy the wbtc contract so the owner now has wbtc in their wallet
    wbtc_decimals = 10 ** 8
    wbtc_to_start = 10
    mocked_wbtc = MockedTokens_WBTC.deploy(wbtc_to_start * wbtc_decimals, {"from": multisig})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_wbtc, {"from": multisig})


    starting_owner_balance_wbtc = mocked_wbtc.balanceOf(multisig)
    assert starting_owner_balance_wbtc == wbtc_to_start * wbtc_decimals
    assert mocked_wbtc.balanceOf(TheRanchBullsMintAndReward) == 0




    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 0

    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3}) ==0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_4}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_5}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_7}) == 0

    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_3}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_4}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_5}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_7}) == 0


    
    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6



    #################################################################
    ######### owner needs to set the stockyard information  ###########
    #################################################################

    tx_set_stockyard = TheRanchBullsMintAndReward.setStockYardInfo(1,1,7, {"from": multisig})

    print("\n")
    print(f'stockyard_0: {TheRanchBullsMintAndReward.stockyardInfo(0)}')
    print(f'stockyard_1: {TheRanchBullsMintAndReward.stockyardInfo(1)}')
    print(f'stockyard_2: {TheRanchBullsMintAndReward.stockyardInfo(2)}')
    print(f'stockyard_3: {TheRanchBullsMintAndReward.stockyardInfo(3)}')

    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = TheRanchBullsMintAndReward.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0322',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    # mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    # with pytest.raises(exceptions.VirtualMachineError):
    #     fundAndSetPayPerNFT = TheRanchBullsMintAndReward.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0323',{"from": multisig})




    print(TheRanchBullsMintAndReward.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / TheRanchBullsMintAndReward.totalSupply())
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6

    #### set the defender wallet up to allow this ###
    TheRanchBullsMintAndReward.setDefenderRole(defender_wallet, True, {"from": multisig})


    ### call the readyToReward function to begin the rewarding process ###
    TheRanchBullsMintAndReward.setReadyToReward({"from": multisig})


    
    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    TheRanchBullsMintAndReward.setPauseStatus(True, {"from": defender_wallet})

   



    assert TheRanchBullsMintAndReward.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################


    reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())



    ####################################
    ### UPDATE MAINTENANCE STANDING  ###
    ####################################

    update_maint_standing = TheRanchBullsMintAndReward.updateMaintenanceStanding({"from":defender_wallet})

    print(update_maint_standing.info())


    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1}) == 12*10**6
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_2}) == 12*10**6
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3}) == (12*10**6) * 3
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_4}) == 12*10**6
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_5}) == 12*10**6
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_7}) == 0

    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_1}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_2}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_3}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_4}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_5}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_7}) == 0



    assert TheRanchBullsMintAndReward.getRewardAddressesLength() == 5







    ##############################################################################
    ####                               ROUND 2                                ####
    ##############################################################################

    tx_reset = TheRanchBullsMintAndReward.resetReadyToRewardChecks({"from": multisig})
    print(tx_reset.info())


    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 0
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == 0



    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(14*10**6, {"from": multisig})   # 14 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 14*10**6



    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

   


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = TheRanchBullsMintAndReward.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0422',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    print(TheRanchBullsMintAndReward.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / TheRanchBullsMintAndReward.totalSupply())
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(14*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 14*10**6

  

    ### call the readyToReward function to begin the rewarding process ###
    TheRanchBullsMintAndReward.setReadyToReward({"from": multisig})


    
    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    TheRanchBullsMintAndReward.setPauseStatus(True, {"from": defender_wallet})

   
    assert TheRanchBullsMintAndReward.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################


    reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())



    print("#######################################################################################")
    print(f'\t\t\t\t\t ROUND 2')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam1})}')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam2})}')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1})}')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_2})}')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3})}')





    



    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1}) == (12*10**6) + (14*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_2}) == (12*10**6) + (14*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3}) == ((12*10**6) * 3) + ((14*10**6) * 3)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_4}) == (12*10**6) + (14*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_5}) == (12*10**6) + (14*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_7}) == 0

    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_1}) == 2
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_2}) == 2
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_3}) == 2
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_4}) == 2
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_5}) == 2
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_7}) == 0







    ##############################################################################
    ####                               ROUND 3                                ####
    ##############################################################################

    tx_reset = TheRanchBullsMintAndReward.resetReadyToRewardChecks({"from": multisig})
    print(tx_reset.info())


    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 0
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == 0



    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(16*10**6, {"from": multisig})   # 14 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 16*10**6



    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

   


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = TheRanchBullsMintAndReward.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0522',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    print(TheRanchBullsMintAndReward.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / TheRanchBullsMintAndReward.totalSupply())
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

  
  

    ### call the readyToReward function to begin the rewarding process ###
    TheRanchBullsMintAndReward.setReadyToReward({"from": multisig})


    
    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    TheRanchBullsMintAndReward.setPauseStatus(True, {"from": defender_wallet})

   
    assert TheRanchBullsMintAndReward.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################


    reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())


    print("#######################################################################################")
    print(f'\t\t\t\t\t ROUND 3')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam1})}')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam2})}')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1})}')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_2})}')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3})}')


    print(reward_tx.info())


    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_2}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3}) == ((12*10**6) * 3) + ((14*10**6) * 3) + ((16*10**6)*3)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_4}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_5}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_7}) == 0

    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_1}) == 3
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_2}) == 3
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_3}) == 3
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_4}) == 3
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_5}) == 3
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_7}) == 0







    #####################################################################################
    ################    person 5 sells their NFT to person 7  ###########################
    #####################################################################################

    assert TheRanchBullsMintAndReward.ownerOf(7) == person_5
    assert TheRanchBullsMintAndReward.ownerOf(7) != person_7

    TheRanchBullsMintAndReward.transferFrom(person_5, person_7, 7, {"from": person_5})    
    assert TheRanchBullsMintAndReward.ownerOf(7) != person_5
    assert TheRanchBullsMintAndReward.ownerOf(7) == person_7







    ##############################################################################
    ####                               ROUND 4                                ####
    ##############################################################################

    tx_reset = TheRanchBullsMintAndReward.resetReadyToRewardChecks({"from": multisig})
    print(tx_reset.info())


    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 0
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == 0



    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(18*10**6, {"from": multisig})   # 14 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 18*10**6



    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

   


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = TheRanchBullsMintAndReward.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0622',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    print(TheRanchBullsMintAndReward.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / TheRanchBullsMintAndReward.totalSupply())
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

  
  

    ### call the readyToReward function to begin the rewarding process ###
    TheRanchBullsMintAndReward.setReadyToReward({"from": multisig})


    
    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    TheRanchBullsMintAndReward.setPauseStatus(True, {"from": defender_wallet})

   
    assert TheRanchBullsMintAndReward.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################


    reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())


    print("#######################################################################################")
    print(f'\t\t\t\t\t ROUND 4')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam1})}')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam2})}')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1})}')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_2})}')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3})}')


    print(reward_tx.info())



    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1}) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_2}) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3}) == ((12*10**6) * 3) + ((14*10**6) * 3) + ((16*10**6)*3) + ((18*10**6) * 3)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_4}) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_5}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_7}) == (18*10**6)

    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_1}) == 4
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_2}) == 4
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_3}) == 4
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_4}) == 4
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_5}) == 4
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_7}) == 1



    return





































    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(18*10**6, {"from": owner})   # 16 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 18*10**6

    mocked_wbtc.approve(TheRanchBullsMintAndReward, (amount_to_award * 2), {"from": owner})
    fund_stockyards_tx = TheRanchBullsMintAndReward.fundAndRewardBulls(1,8,amount_to_award,{"from": owner})
   
    assert mocked_wbtc.balanceOf(TheRanchBullsMintAndReward) == amount_to_award + amount_to_award + amount_to_award + amount_to_award

    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": owner})
    print(tx_update_fees.info())


    tx_update_months_behind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": owner})
    print(tx_update_months_behind.info())






    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam1) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam2) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == ((12*10**6) * 3) + ((14*10**6) * 3) + ((16*10**6) * 3) + ((18*10**6) * 3) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == (16*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == (16*10**6) + + (18*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == + (18*10**6) 

    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam1) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam2) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 4
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 4
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 4
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 4
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 1


    
    print("#######################################################################################")
    print(f'\t\t\t\t\t ROUND 4')
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
    print(f'person_6 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7)}')


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




    ############## LIQUIDATION #############
    liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": owner})

    print(liquidation_event.info())



    print("#######################################################################################")
    print(f'\t\t\t\t\t AFTER LIQUIDATION')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam1)}')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(coreTeam2)}')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1)}')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2)}')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3)}')
    print(f'person_4 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4)}')
    print(f'person_5 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5)}')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6)}')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7)}')


    print('\n')
    

    print(f'coreTeam_1 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam1)}')
    print(f'coreTeam_2 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(coreTeam2)}')
    print(f'person_1 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1)}')
    print(f'person_2 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2)}')
    print(f'person_3 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3)}')
    print(f'person_4 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4)}')
    print(f'person_5 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5)}')
    print(f'person_6 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6)}')
    print(f'person_6 months behind maintenance maint fees: {TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7)}')


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







    




    with pytest.raises(exceptions.VirtualMachineError):
        withdraw_person_6_tx = TheRanchBullsMintAndReward.withdrawWbtcForWalletAddress({"from": person_6})

    

    ##### Person 7 withdraw, no USDC rewards for them #####
    
    usdc_rewards_7 = TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_7})
    maint_fees_7 = TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7)

    print(f'usdc person_7: {usdc_rewards_7}')
    print(f'maint_fees_person_7 {maint_fees_7}')

    if usdc_rewards_7 < maint_fees_7:
        amt_to_approve = maint_fees_7 - usdc_rewards_7
        mocked_usdc.approve(TheRanchBullsMintAndReward.address, amt_to_approve ,{"from":person_7})


    pay_maint_fees_person_7 = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_7})
    print(pay_maint_fees_person_7.info())

    assert pay_maint_fees_person_7.events["Transfer"]["value"] == maint_fees_7 - usdc_rewards_7







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







    






    
    
    

   

































