
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


def test_TRBCProxy_blacklist_wbtc():



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

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')


    raffleEntryBool = True


    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_1})
    tx1 = proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_2})
    tx2 = proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_3})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_4})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_5})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_6})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_7})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_8})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_9})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_10})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
    amt = 2
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_2})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    amt = 4
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_11})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_11, "value":  price_needed(amt)})
    





    #################################################################
    ######### owner needs to set the stockyard information  ###########
    #################################################################

    tx_set_stockyard = proxy_TRBC.setStockYardInfo(1,1,15, {"from": multisig})
   


    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert proxy_TRBC.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0322',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


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





    # make sure person_2 currently has zero wbtc in their own wallet
    assert mocked_wbtc.balanceOf(person_2) == 0 

    person_1_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_1})
    person_2_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_2})
    person_3_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_3})
    person_4_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_4})
    person_5_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_5})
    person_6_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_6})
    person_7_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_7})
    person_8_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_8})
    person_9_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_9})
    person_10_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_10})
    person_11_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_11})
    person_12_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_12})
    person_13_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_13})
    person_14_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_14})
    person_15_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_15})
    person_16_award_balance_before_tx = proxy_TRBC.getWbtcBalanceForAddress({"from": person_16})
   
    
   
    ################################################
    ####  Person 5 withdraws their WBTC balance #####
    #################################################



    assert proxy_TRBC.paused.call() == True
     
    with pytest.raises(exceptions.VirtualMachineError):
        rewards_withdraw_event = proxy_TRBC.withdrawWbtcBalance({"from": person_5})



    change_pause_status = proxy_TRBC.setPauseStatus(False, {"from": multisig})
    assert proxy_TRBC.paused.call() == False

    assert proxy_TRBC.getBlacklistedStatus(person_5) == False
    

    proxy_TRBC.blacklistMalicious(person_5, True, {"from": multisig})   ## blacklist person_5


    assert proxy_TRBC.getBlacklistedStatus(person_5) == True
    
    with pytest.raises(exceptions.VirtualMachineError):
        rewards_withdraw_event = proxy_TRBC.withdrawWbtcBalance({"from": person_5})
    
    
    
    proxy_TRBC.blacklistMalicious(person_5, False, {"from": multisig})
    assert proxy_TRBC.getBlacklistedStatus(person_5) == False




    



    usdc_balance =  proxy_TRBC.getUsdcBalanceForAddress({"from": person_5})
    fees_due = proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from": person_5})
    if usdc_balance >= fees_due: 
        pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_5})
    else:
        amount_to_approve = fees_due - usdc_balance
        mocked_usdc.approve(proxy_TRBC,amount_to_approve, {"from": person_5})
        pay_maintenance_fees_event = proxy_TRBC.payMaintanenceFees({"from": person_5})


    print(pay_maintenance_fees_event.info())

    rewards_withdraw_event = proxy_TRBC.withdrawWbtcBalance({"from": person_5})

    print(rewards_withdraw_event.info())




    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_5}) == 0

