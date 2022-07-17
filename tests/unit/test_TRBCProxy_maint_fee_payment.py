
import pprint
import math
from urllib.request import proxy_bypass
import pytest


from brownie import (
    TheRanchBTCBullsCommunity,
    TheRanchBTCBullsCommunityV2,
    TRBCProxy,
    Contract,
    network,
    config,
    accounts,
    exceptions,
    MockedTokens_USDC,
    MockedTokens_WBTC
)
from scripts.helpful_scripts import get_account, encode_function_data, upgrade, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_TRBCProxy_maint_fee_payment():



    deployer = accounts[0]

    account = get_account()
    TRBC = TheRanchBTCBullsCommunity.deploy(
        {"from": deployer},
    )

   
    # proxy_admin = ProxyAdmin.deploy(
    #     {"from": owner},
    # )
    box_encoded_initializer_function = encode_function_data()
    proxy = TRBCProxy.deploy(
        TRBC.address,
        # proxy_admin.address,
        box_encoded_initializer_function,
        {"from": deployer, "gas_limit": 2000000},
    )
    TRBCV2 = TheRanchBTCBullsCommunityV2.deploy(
        {"from": deployer},
    )


    proxy_TRBC = Contract.from_abi("TheRanchBTCBullsCommunity", proxy.address, TRBC.abi)


    coinbase = accounts[10001]
    defender_wallet = accounts[10002]
    multisig = accounts[10003]

    btcMinersSafe = accounts[10006]
    hostingSafe = accounts[10007]
    coreTeam1 = accounts[10004]
    coreTeam2 = accounts[10005]



    mocked_usdc = MockedTokens_USDC.deploy(1_000_000_000 * 10**6, {"from": coinbase})
    mocked_wbtc = MockedTokens_WBTC.deploy(10 * 10**8, {"from": multisig})






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



    proxy_TRBC.initialize({"from": multisig })
    TRBC.initialize({"from": multisig })



    print(f'deployer: {deployer}')
    print(f'multisig : {multisig}')
    print(f'owner of proxy_TRBC  : {proxy_TRBC.owner.call()}')
    print(f'owner of TRBC  : {TRBC.owner.call()}')


    DEFAULT_ADMIN_ROLE = proxy.DEFAULT_ADMIN_ROLE.call()

    proxy.hasRole(DEFAULT_ADMIN_ROLE, deployer) == True
    proxy.hasRole(DEFAULT_ADMIN_ROLE, multisig) == False

    proxy.grantRole(DEFAULT_ADMIN_ROLE,multisig,{"from": deployer})
    proxy.revokeRole(DEFAULT_ADMIN_ROLE,deployer,{"from": multisig})

    print(proxy.hasRole(DEFAULT_ADMIN_ROLE, deployer))
    print(proxy.hasRole(DEFAULT_ADMIN_ROLE, multisig))

    proxy.hasRole(DEFAULT_ADMIN_ROLE, deployer) == False
    proxy.hasRole(DEFAULT_ADMIN_ROLE, multisig) == True


    proxy_TRBC.setUsdcTokenAddress(mocked_usdc,{"from": multisig})
    proxy_TRBC.setWbtcTokenAddress(mocked_wbtc,{"from": multisig})
    proxy_TRBC.setBaseURI("ipfs://aldkfjasdpofe", {"from": multisig})
    proxy_TRBC.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})
    proxy_TRBC.setCoreTeamAddresses(coreTeam1,coreTeam2,{"from": multisig})



    print("Things needed to unpause the contract")
    print("--------------------------------------")

    print(f' coreTeam1: {proxy_TRBC.coreTeam_1.call()}')
    print(f' coreTeam2: {proxy_TRBC.coreTeam_2.call()}')
    print(f' usdc contract : {proxy_TRBC.usdcTokenContract.call()}')
    print(f' wbtc contract : {proxy_TRBC.wbtcTokenContract.call()}')
    print(f' hosting safe address  : {proxy_TRBC.hostingSafe.call()}')
    print(f' btcMinersSafe address  : {proxy_TRBC.btcMinersSafe.call()}')
    print(f'nftPerAddressLimit: {proxy_TRBC.nftPerAddressLimit.call()}')
    print(f'mintingCost: {proxy_TRBC.mintingCost.call()}')




    print("Things needed to unpause the contract")
    print("--------------------------------------")

    print(f' coreTeam1: {TRBC.coreTeam_1.call()}')
    print(f' coreTeam2: {TRBC.coreTeam_2.call()}')
    print(f' usdc contract : {TRBC.usdcTokenContract.call()}')
    print(f' wbtc contract : {TRBC.wbtcTokenContract.call()}')
    print(f' hosting safe address  : {TRBC.hostingSafe.call()}')
    print(f' btcMinersSafe address  : {TRBC.btcMinersSafe.call()}')
    print(f'nftPerAddressLimit: {TRBC.nftPerAddressLimit.call()}')
    print(f'mintingCost: {TRBC.mintingCost.call()}')




 
    assert proxy_TRBC.nftPerAddressLimit.call() == 50
    assert proxy_TRBC.wbtcTokenDecimals.call() == 8
    assert proxy_TRBC.usdcTokenDecimals.call() == 6

    assert proxy_TRBC.mintingCost.call() == 350
    assert proxy_TRBC.publicSaleLive.call() == False
    assert proxy_TRBC.paused.call() == True

    assert proxy_TRBC.coreTeam_1.call() == coreTeam1
    assert proxy_TRBC.coreTeam_2.call() == coreTeam2




    assert proxy_TRBC.paused.call() == True
    assert TRBC.paused.call() == True


    assert proxy_TRBC.publicSaleLive.call() == False
    assert TRBC.publicSaleLive.call() == False



    proxy_TRBC.setPauseStatus(False, {"from": multisig})
 
    #owner starts the public sale
    proxy_TRBC.togglePublicSaleStatus({"from": multisig})




    assert proxy_TRBC.paused.call() == False
    assert TRBC.paused.call() == True


    assert proxy_TRBC.publicSaleLive.call() == True
    assert TRBC.publicSaleLive.call() == False


    def price_needed(count):
        return (count * proxy_TRBC.mintingCost() * 10 ** 6)



    ######################################################
    ###       CHECK BEFORE ANYONE PARTNERS ARE SET   #####
    ######################################################


    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_1, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_2, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_1}) == False

    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_1, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_2, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_2}) == False
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == False



    raffleEntryBool = True

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_1})
    tx1 = proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})


    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_2})
    tx2 = proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    amt = 2
    proxy_TRBC.setPartnerAddress(person_1, {"from": person_3})

    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == True
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_3})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    amt = 2
    proxy_TRBC.setPartnerAddress(person_2, {"from": person_4})
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == True
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_4})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    amt = 2
    proxy_TRBC.setPartnerAddress(person_1, {"from": person_5})
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == True
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_5})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    amt = 2
    proxy_TRBC.setPartnerAddress(person_2, {"from": person_6})
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == True
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_6})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})


    amt = 2
    proxy_TRBC.setPartnerAddress(person_1, {"from": person_7})
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == True
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_7})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    amt = 2
    proxy_TRBC.setPartnerAddress(person_2, {"from": person_8})
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == True
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_8})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    amt = 2
    proxy_TRBC.setPartnerAddress(person_1, {"from": person_9})
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == True
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_9})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    amt = 2
    proxy_TRBC.setPartnerAddress(person_3, {"from": person_10})
    assert proxy_TRBC.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_3}) == True
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_10})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
 


  
    assert proxy_TRBC.balanceOf(proxy_TRBC) == 0
    assert mocked_usdc.balanceOf(proxy_TRBC) == ((20 * 350) * (10 ** 6))
    assert proxy_TRBC.btcMinersSafeBalance.call() ==   ((20 * 350) * (10 ** 6)) * .90
    assert proxy_TRBC.hostingSafeBalance.call() == ((20* 350) * (10 ** 6)) * 0.05
    assert proxy_TRBC.dailyRaffleBalance.call() ==  ((20 * 350) * (10 ** 6)) * 0.03
    assert proxy_TRBC.USDCRewardsBalance.call() == ((20 * 350) * (10 ** 6)) * 0.05
    
    assert proxy_TRBC.getNumberOfRafflePlayers() == 10
    assert proxy_TRBC.totalSupply() == 20
    assert proxy_TRBC.getRafflePlayer(0,{"from": multisig}) == person_1
    assert proxy_TRBC.getRafflePlayer(1,{"from": multisig}) == person_2



    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_1) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_2) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_3) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_4) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_5) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_6) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_7) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_8) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_9) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_10) == True
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_11) == False
    assert proxy_TRBC.getUserAlreadyInDailyRaffleStatus(person_12) == False





    ### Assert Totaly Supply Minted and How many NFTs each person should have ###
    assert proxy_TRBC.totalSupply() == 20
    assert len(proxy_TRBC.walletOfOwner(person_1)) == 2
    assert len(proxy_TRBC.walletOfOwner(person_2)) == 2 
    assert len(proxy_TRBC.walletOfOwner(person_3)) == 2
    assert len(proxy_TRBC.walletOfOwner(person_4)) == 2
    assert len(proxy_TRBC.walletOfOwner(person_5)) == 2
    assert len(proxy_TRBC.walletOfOwner(person_6)) == 2
    assert len(proxy_TRBC.walletOfOwner(person_7)) == 2
    assert len(proxy_TRBC.walletOfOwner(person_8)) == 2
    assert len(proxy_TRBC.walletOfOwner(person_9)) == 2
    assert len(proxy_TRBC.walletOfOwner(person_10)) == 2



    ####### Person 10 has a change of heart and changes their partner to person_1 ########


    assert  proxy_TRBC.getPartnerNetworkTeamCount({"from":person_1}) == 4
    assert  proxy_TRBC.getPartnerNetworkTeamCount({"from": person_2}) == 3
    assert  proxy_TRBC.getPartnerNetworkTeamCount({"from":person_3}) == 1



    ######################################################################################
    ### Check if the partner that they person set has minted from the contract before  ###
    ######################################################################################


    assert proxy_TRBC.getHaveTheyMintedBefore(person_1) == True
    assert proxy_TRBC.getHaveTheyMintedBefore(person_2) == True
    assert proxy_TRBC.getHaveTheyMintedBefore(person_3) == True

    assert proxy_TRBC.getHaveTheyMintedBefore(person_11) == False
    assert proxy_TRBC.getHaveTheyMintedBefore(person_12) == False
 


    print(f'team count person_1 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_1})}')
    print(f'team count person_2 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_2})}')
    print(f'team count person_3 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_3})}')
    print(f'team count person_4 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_4})}')
    print(f'team count person_5 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_5})}')
    print(f'team count person_6 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_6})}')
    print(f'team count person_7 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_7})}')
    print(f'team count person_8 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_8})}')
    print(f'team count person_9 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_9})}')
    print(f'team count person_10 : {proxy_TRBC.getPartnerNetworkTeamCount({"from":person_10})}')













    #######################################################
    #######                                         #######
    #######                REWARD                   #######     
    #######                                         #######
    #######################################################



    #################################################################
    ######### owner needs to set the stockyard information  #########
    #################################################################

    tx_set_stockyard = proxy_TRBC.setStockYardInfo(1,1,20, {"from": multisig})


    #### set the defender wallet up to allow this ###
    proxy_TRBC.setDefenderRole(defender_wallet, True, {"from": multisig})


    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 0
    assert proxy_TRBC.payPerNftForTheMonth.call() == 0



    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(18*10**6, {"from": multisig})   # 14 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 18*10**6



    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

   


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0622',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    print(proxy_TRBC.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / proxy_TRBC.totalSupply())
    assert proxy_TRBC.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

  
  

    ### call the readyToReward function to begin the rewarding process ###
    proxy_TRBC.setReadyToReward({"from": multisig})


    
    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    proxy_TRBC.setPauseStatus(True, {"from": defender_wallet})

   
    assert proxy_TRBC.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################


    reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())


    ####################################
    ### UPDATE MAINTENANCE STANDING  ###
    ####################################

    update_maint_standing = proxy_TRBC.updateMaintenanceStanding({"from":defender_wallet})

    print(update_maint_standing.info())











    print("\n\n")



    print(f'Maint Fee Due person_1 : {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1})}')
    print(f'USDC balance person_1 : {proxy_TRBC.getUsdcBalanceForAddress({"from": person_1})}')
  

    print("\n\n")


    print(f'Maint Fee Due person_3 : {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3})}')
    print(f'USDC balance person_3 : {proxy_TRBC.getUsdcBalanceForAddress({"from": person_3})}')


    print("\n\n")

    print(f'Maint Fee Due person_5 : {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_5})}')
    print(f'USDC balance person_5 : {proxy_TRBC.getUsdcBalanceForAddress({"from": person_5})}')
   





                                # Maint Fee Due person_1 : 36000000
                                #  USDC balance person_1 : 56000000



                             

    pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_1})
    print(pay_maintenance_fees_event.info())

    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithCurrentRewards"] == 36000000
    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithoutCurrentRewards"] == 0


    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1})  == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_1}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_1}) == 56000000 - 36000000







                                # Maint Fee Due person_3 : 36000000
                                #  USDC balance person_3 : 14000000





    usdc_balance =  proxy_TRBC.getUsdcBalanceForAddress({"from": person_3})
    fees_due = proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3})
    if usdc_balance >= fees_due: 
        pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_3})
    else:
        amount_to_approve = fees_due - usdc_balance
        mocked_usdc.approve(proxy_TRBC,amount_to_approve, {"from": person_3})
        pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_3})


    print(pay_maintenance_fees_event.info())

    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithCurrentRewards"] == 14000000
    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithoutCurrentRewards"] == 36000000 - 14000000


    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3})  == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_3}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_3}) == 0







                                # Maint Fee Due person_5 : 36000000
                                #  USDC balance person_5 : 0





    usdc_balance =  proxy_TRBC.getUsdcBalanceForAddress({"from": person_5})
    fees_due = proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_5})
    if usdc_balance >= fees_due: 
        pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_5})
    else:
        amount_to_approve = fees_due - usdc_balance
        mocked_usdc.approve(proxy_TRBC,amount_to_approve, {"from": person_5})
        pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_5})


    print(pay_maintenance_fees_event.info())

    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithCurrentRewards"] == 0
    assert pay_maintenance_fees_event.events["payMaintanenceFeesEvent"]["totalAmountPayedWithoutCurrentRewards"] == 36000000


    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3})  == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_3}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_3}) == 0



    with pytest.raises(exceptions.VirtualMachineError): 
        proxy_TRBC.payMaintanenceFees({"from": person_12})
























    # assert mocked_wbtc.balanceOf(person_1) == 0

    # # usdc_balance =  proxy_TRBC.getUsdcBalanceForAddress({"from": person_1})
    # # fees_due = proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1})
    # # if usdc_balance >= fees_due: 
    # #     pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_1})
    # # else:
    # #     amount_to_approve = fees_due - usdc_balance
    # #     mocked_usdc.approve(proxy_TRBC,amount_to_approve, {"from": person_1})
    # #     pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_1})


    # # print(pay_maintenance_fees_event.info())
    # # assert pay_maintenance_fees_event.events["Transfer"]["value"] == fees_due
