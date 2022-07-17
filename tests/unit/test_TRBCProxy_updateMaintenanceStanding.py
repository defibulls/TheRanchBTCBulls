
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


def test_maintenance_fees():



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



    proxy_TRBC.setUsdcTokenAddress(mocked_usdc,{"from": multisig})
    proxy_TRBC.setWbtcTokenAddress(mocked_wbtc,{"from": multisig})
    proxy_TRBC.setBaseURI("ipfs://aldkfjasdpofe", {"from": multisig})
    proxy_TRBC.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})
    proxy_TRBC.setCoreTeamAddresses(coreTeam1,coreTeam2,{"from": multisig})


    TRBC.setUsdcTokenAddress(mocked_usdc,{"from": multisig})
    TRBC.setWbtcTokenAddress(mocked_wbtc,{"from": multisig})
    TRBC.setBaseURI("ipfs://aldkfjasdpofe", {"from": multisig})
    TRBC.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})
    TRBC.setCoreTeamAddresses(coreTeam1,coreTeam2,{"from": multisig})



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

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')


    raffleEntryBool = True


    amt = 1
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_1})
    tx1 = proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_2})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(3),{"from":person_3})
    proxy_TRBC.mint(3,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_4})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_5})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})



    assert proxy_TRBC.balanceOf(proxy_TRBC) == 0
    assert mocked_usdc.balanceOf(proxy_TRBC) == ((7 * 350) * (10 ** 6))
    assert proxy_TRBC.btcMinersSafeBalance.call() ==   ((7 * 350) * (10 ** 6)) * .90
    assert proxy_TRBC.hostingSafeBalance.call() == ((7 * 350) * (10 ** 6)) * 0.05
    assert proxy_TRBC.dailyRaffleBalance.call() ==  ((7 * 350) * (10 ** 6)) * 0.03
    assert proxy_TRBC.USDCRewardsBalance.call() == ((7 * 350) * (10 ** 6)) * 0.05
    
    assert proxy_TRBC.getNumberOfRafflePlayers() == 5
    assert proxy_TRBC.totalSupply() == 7
    assert proxy_TRBC.getRafflePlayer(0,{"from": multisig}) == person_1



    ##################################################################
    ### Set the Reward Token for the contract after deploying WBTC ###
    ##################################################################

    ## deploy the wbtc contract so the owner now has wbtc in their wallet
    wbtc_decimals = 10 ** 8
    wbtc_to_start = 10
    mocked_wbtc = MockedTokens_WBTC.deploy(wbtc_to_start * wbtc_decimals, {"from": multisig})
    proxy_TRBC.setWbtcTokenAddress(mocked_wbtc, {"from": multisig})


    starting_owner_balance_wbtc = mocked_wbtc.balanceOf(multisig)
    assert starting_owner_balance_wbtc == wbtc_to_start * wbtc_decimals
    assert mocked_wbtc.balanceOf(proxy_TRBC) == 0




    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 0

    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3}) ==0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_4}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_5}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_7}) == 0

    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_2}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_3}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_4}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_5}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_7}) == 0


    
    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 12*10**6



    #################################################################
    ######### owner needs to set the stockyard information  ###########
    #################################################################

    tx_set_stockyard = proxy_TRBC.setStockYardInfo(1,1,7, {"from": multisig})

    print("\n")
    print(f'stockyard_0: {proxy_TRBC.stockyardInfo(0)}')
    print(f'stockyard_1: {proxy_TRBC.stockyardInfo(1)}')
    print(f'stockyard_2: {proxy_TRBC.stockyardInfo(2)}')
    print(f'stockyard_3: {proxy_TRBC.stockyardInfo(3)}')

    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert proxy_TRBC.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0322',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    # mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    # with pytest.raises(exceptions.VirtualMachineError):
    #     fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0323',{"from": multisig})




    print(proxy_TRBC.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / proxy_TRBC.totalSupply())
    assert proxy_TRBC.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 12*10**6

    #### set the defender wallet up to allow this ###
    proxy_TRBC.setDefenderRole(defender_wallet, True, {"from": multisig})


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


    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1}) == 12*10**6
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_2}) == 12*10**6
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3}) == (12*10**6) * 3
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_4}) == 12*10**6
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_5}) == 12*10**6
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_7}) == 0

    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_1}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_2}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_3}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_4}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_5}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_7}) == 0



    assert proxy_TRBC.getRewardAddressesLength() == 5







    ##############################################################################
    ####                               ROUND 2                                ####
    ##############################################################################

    tx_reset = proxy_TRBC.resetReadyToRewardChecks({"from": multisig})
    print(tx_reset.info())


    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 0
    assert proxy_TRBC.payPerNftForTheMonth.call() == 0



    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(14*10**6, {"from": multisig})   # 14 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 14*10**6



    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

   


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0422',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    print(proxy_TRBC.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / proxy_TRBC.totalSupply())
    assert proxy_TRBC.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(14*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 14*10**6

  

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



    print("#######################################################################################")
    print(f'\t\t\t\t\t ROUND 2')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam1})}')
    print(f'coreTeam_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam2})}')
    print(f'person_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1})}')
    print(f'person_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_2})}')
    print(f'person_3 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3})}')





    



    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1}) == (12*10**6) + (14*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_2}) == (12*10**6) + (14*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3}) == ((12*10**6) * 3) + ((14*10**6) * 3)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_4}) == (12*10**6) + (14*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_5}) == (12*10**6) + (14*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_7}) == 0

    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_1}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_2}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_3}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_4}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_5}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_7}) == 0







    ##############################################################################
    ####                               ROUND 3                                ####
    ##############################################################################

    tx_reset = proxy_TRBC.resetReadyToRewardChecks({"from": multisig})
    print(tx_reset.info())


    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 0
    assert proxy_TRBC.payPerNftForTheMonth.call() == 0



    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(16*10**6, {"from": multisig})   # 14 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 16*10**6



    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

   


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0522',{"from": multisig})
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


    print("#######################################################################################")
    print(f'\t\t\t\t\t ROUND 3')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam1})}')
    print(f'coreTeam_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam2})}')
    print(f'person_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1})}')
    print(f'person_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_2})}')
    print(f'person_3 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3})}')


    print(reward_tx.info())


    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_2}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3}) == ((12*10**6) * 3) + ((14*10**6) * 3) + ((16*10**6)*3)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_4}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_5}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_7}) == 0

    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_1}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_2}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_3}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_4}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_5}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_7}) == 0







    #####################################################################################
    ################    person 5 sells their NFT to person 7  ###########################
    #####################################################################################

    assert proxy_TRBC.ownerOf(7) == person_5
    assert proxy_TRBC.ownerOf(7) != person_7

    proxy_TRBC.transferFrom(person_5, person_7, 7, {"from": person_5})    
    assert proxy_TRBC.ownerOf(7) != person_5
    assert proxy_TRBC.ownerOf(7) == person_7







    ##############################################################################
    ####                               ROUND 4                                ####
    ##############################################################################

    tx_reset = proxy_TRBC.resetReadyToRewardChecks({"from": multisig})
    print(tx_reset.info())


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


    print("#######################################################################################")
    print(f'\t\t\t\t\t ROUND 4')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam1})}')
    print(f'coreTeam_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam2})}')
    print(f'person_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1})}')
    print(f'person_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_2})}')
    print(f'person_3 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3})}')


    print(reward_tx.info())



    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_1}) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_2}) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_3}) == ((12*10**6) * 3) + ((14*10**6) * 3) + ((16*10**6)*3) + ((18*10**6) * 3)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_4}) == (12*10**6) + (14*10**6) + (16*10**6) + (18*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_5}) == (12*10**6) + (14*10**6) + (16*10**6)
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_7}) == (18*10**6)

    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_1}) == 4
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_2}) == 4
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_3}) == 4
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_4}) == 4
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_5}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from": person_7}) == 1




















