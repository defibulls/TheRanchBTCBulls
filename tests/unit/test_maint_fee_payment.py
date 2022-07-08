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






def test_PartnerNetworkTeam():


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



    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(False, {"from": multisig})
  
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": multisig})


    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)



    ######################################################
    ###       CHECK BEFORE ANYONE PARTNERS ARE SET   #####
    ######################################################


    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_1, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_2, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_1}) == False

    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_1, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_2, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == False



    raffleEntryBool = True

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})


    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    tx2 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_3})

    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_3})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_4})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_5})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_6})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_6})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})


    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_7})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_7})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_8})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_8})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_9})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_9})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_3, {"from": person_10})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_3}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_10})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
 


  
    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((20 * 350) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersSafeBalance.call() ==   ((20 * 350) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.hostingSafeBalance.call() == ((20* 350) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((20 * 350) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.USDCRewardsBalance.call() == ((20 * 350) * (10 ** 6)) * 0.05
    
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 10
    assert TheRanchBullsMintAndReward.totalSupply() == 20
    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1
    assert TheRanchBullsMintAndReward.getRafflePlayer(1) == person_2



    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_1) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_2) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_3) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_4) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_5) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_6) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_7) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_8) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_9) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_10) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_11) == False
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_12) == False





    ### Assert Totaly Supply Minted and How many NFTs each person should have ###
    assert TheRanchBullsMintAndReward.totalSupply() == 20
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_1)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_2)) == 2 
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_3)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_4)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_5)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_6)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_7)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_8)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_9)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_10)) == 2



    ####### Person 10 has a change of heart and changes their partner to person_1 ########


    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_1) == 4
    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_2) == 3
    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_3) == 1



    ######################################################################################
    ### Check if the partner that they person set has minted from the contract before  ###
    ######################################################################################


    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_1) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_2) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_3) == True

    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_11) == False
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_12) == False
 


    print(f'team count person_1 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_1)}')
    print(f'team count person_2 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_2)}')
    print(f'team count person_3 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_3)}')
    print(f'team count person_4 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_4)}')
    print(f'team count person_5 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_5)}')
    print(f'team count person_6 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_6)}')
    print(f'team count person_7 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_7)}')
    print(f'team count person_8 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_8)}')
    print(f'team count person_9 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_9)}')
    print(f'team count person_10 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_10)}')













    #######################################################
    #######                                         #######
    #######                REWARD                   #######     
    #######                                         #######
    #######################################################



    #################################################################
    ######### owner needs to set the stockyard information  #########
    #################################################################

    tx_set_stockyard = TheRanchBullsMintAndReward.setStockYardInfo(1,1,20, {"from": multisig})


    #### set the defender wallet up to allow this ###
    TheRanchBullsMintAndReward.setDefenderRole(defender_wallet, True, {"from": multisig})


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


    ####################################
    ### UPDATE MAINTENANCE STANDING  ###
    ####################################

    update_maint_standing = TheRanchBullsMintAndReward.updateMaintenanceStanding({"from":defender_wallet})

    print(update_maint_standing.info())











    print("\n\n")



    print(f'Maint Fee Due person_1 : {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1})}')
    print(f'USDC balance person_1 : {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_1})}')
  

    print("\n\n")


    print(f'Maint Fee Due person_3 : {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3})}')
    print(f'USDC balance person_3 : {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3})}')


    print("\n\n")

    print(f'Maint Fee Due person_5 : {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_5})}')
    print(f'USDC balance person_5 : {TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_5})}')
   





                                # Maint Fee Due person_1 : 36000000
                                #  USDC balance person_1 : 56000000



                             

    pay_maintenance_fees_event = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_1})
    print(pay_maintenance_fees_event.info())

    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithCurrentRewards"] == 36000000
    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithoutCurrentRewards"] == 0


    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1})  == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_1}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_1}) == 56000000 - 36000000







                                # Maint Fee Due person_3 : 36000000
                                #  USDC balance person_3 : 14000000





    usdc_balance =  TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3})
    fees_due = TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3})
    if usdc_balance >= fees_due: 
        pay_maintenance_fees_event = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_3})
    else:
        amount_to_approve = fees_due - usdc_balance
        mocked_usdc.approve(TheRanchBullsMintAndReward,amount_to_approve, {"from": person_3})
        pay_maintenance_fees_event = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_3})


    print(pay_maintenance_fees_event.info())

    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithCurrentRewards"] == 14000000
    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithoutCurrentRewards"] == 36000000 - 14000000


    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3})  == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3}) == 0







                                # Maint Fee Due person_5 : 36000000
                                #  USDC balance person_5 : 0





    usdc_balance =  TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_5})
    fees_due = TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_5})
    if usdc_balance >= fees_due: 
        pay_maintenance_fees_event = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_5})
    else:
        amount_to_approve = fees_due - usdc_balance
        mocked_usdc.approve(TheRanchBullsMintAndReward,amount_to_approve, {"from": person_5})
        pay_maintenance_fees_event = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_5})


    print(pay_maintenance_fees_event.info())

    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithCurrentRewards"] == 0
    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithoutCurrentRewards"] == 36000000


    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_3})  == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from": person_3}) == 0
    assert TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_3}) == 0



    with pytest.raises(exceptions.VirtualMachineError): 
        TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_12})
























    # assert mocked_wbtc.balanceOf(person_1) == 0

    # # usdc_balance =  TheRanchBullsMintAndReward.getUsdcRewardBalanceForTheOwner({"from": person_1})
    # # fees_due = TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from": person_1})
    # # if usdc_balance >= fees_due: 
    # #     pay_maintenance_fees_event = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_1})
    # # else:
    # #     amount_to_approve = fees_due - usdc_balance
    # #     mocked_usdc.approve(TheRanchBullsMintAndReward,amount_to_approve, {"from": person_1})
    # #     pay_maintenance_fees_event = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_1})


    # # print(pay_maintenance_fees_event.info())
    # # assert pay_maintenance_fees_event.events["Transfer"]["value"] == fees_due
